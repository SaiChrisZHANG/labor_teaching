"""Run a bounded selection-on-observables teaching workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week1_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week1_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


TRAINING_COVARIATES = [
    "age",
    "education",
    "black",
    "hispanic",
    "married",
    "nodegree",
    "earnings_1974",
    "earnings_1975",
]


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35, 35)))


def standardize(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std[std == 0] = 1.0
    return (x - mean) / std, mean, std


def fit_logit_propensity(x: np.ndarray, d: np.ndarray) -> np.ndarray:
    z, _, _ = standardize(x)
    z = np.column_stack([np.ones(len(z)), z])
    beta = np.zeros(z.shape[1])
    learning_rate = 0.08

    for _ in range(5000):
        p = sigmoid(z @ beta)
        gradient = z.T @ (p - d) / len(d)
        beta -= learning_rate * gradient

    return np.clip(sigmoid(z @ beta), 0.03, 0.97)


def ols_coef(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return beta


def regression_adjustment(y: np.ndarray, d: np.ndarray, x: np.ndarray) -> float:
    design = np.column_stack([np.ones(len(y)), d, x])
    return float(ols_coef(y, design)[1])


def outcome_model_predictions(y: np.ndarray, d: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    design = np.column_stack([np.ones(len(y)), x])
    beta0 = ols_coef(y[d == 0], design[d == 0])
    beta1 = ols_coef(y[d == 1], design[d == 1])
    return design @ beta0, design @ beta1


def nearest_neighbor_att(y: np.ndarray, d: np.ndarray, pscore: np.ndarray) -> tuple[float, pd.DataFrame]:
    treated_idx = np.where(d == 1)[0]
    control_idx = np.where(d == 0)[0]
    rows = []
    effects = []

    for idx in treated_idx:
        match_position = np.argmin(np.abs(pscore[control_idx] - pscore[idx]))
        matched_idx = control_idx[match_position]
        effects.append(y[idx] - y[matched_idx])
        rows.append(
            {
                "treated_row": int(idx),
                "matched_control_row": int(matched_idx),
                "treated_pscore": float(pscore[idx]),
                "control_pscore": float(pscore[matched_idx]),
                "distance": float(abs(pscore[idx] - pscore[matched_idx])),
            }
        )

    return float(np.mean(effects)), pd.DataFrame(rows)


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.sum(values * weights) / np.sum(weights))


def weighted_var(values: np.ndarray, weights: np.ndarray) -> float:
    mu = weighted_mean(values, weights)
    return float(np.sum(weights * (values - mu) ** 2) / np.sum(weights))


def standardized_difference(values: np.ndarray, d: np.ndarray, weights: np.ndarray) -> float:
    treated = d == 1
    control = d == 0
    mt = weighted_mean(values[treated], weights[treated])
    mc = weighted_mean(values[control], weights[control])
    vt = weighted_var(values[treated], weights[treated])
    vc = weighted_var(values[control], weights[control])
    pooled = np.sqrt((vt + vc) / 2.0)
    if pooled == 0:
        return 0.0
    return float((mt - mc) / pooled)


def balance_table(df: pd.DataFrame, covariates: list[str], d: np.ndarray, pscore: np.ndarray) -> pd.DataFrame:
    raw_weights = np.ones(len(df))
    att_weights = np.where(d == 1, 1.0, pscore / (1.0 - pscore))
    ate_weights = np.where(d == 1, 1.0 / pscore, 1.0 / (1.0 - pscore))

    rows = []
    for covariate in covariates:
        values = df[covariate].to_numpy(dtype=float)
        rows.append(
            {
                "covariate": covariate,
                "smd_raw": standardized_difference(values, d, raw_weights),
                "smd_weighted_att": standardized_difference(values, d, att_weights),
                "smd_weighted_ate": standardized_difference(values, d, ate_weights),
            }
        )

    return pd.DataFrame(rows)


def make_plots(
    outdir: Path,
    balance: pd.DataFrame,
    d: np.ndarray,
    pscore: np.ndarray,
) -> None:
    plt.figure(figsize=(7.5, 4.4))
    plt.hist(pscore[d == 1], bins=18, alpha=0.65, label="treated", density=True)
    plt.hist(pscore[d == 0], bins=18, alpha=0.65, label="untreated", density=True)
    plt.xlabel("Estimated propensity score")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "propensity_overlap.png", dpi=160)
    plt.close()

    plot_data = balance.copy()
    plot_data["abs_raw"] = plot_data["smd_raw"].abs()
    plot_data["abs_weighted_att"] = plot_data["smd_weighted_att"].abs()
    positions = np.arange(len(plot_data))
    width = 0.38

    plt.figure(figsize=(8.2, 4.8))
    plt.bar(positions - width / 2, plot_data["abs_raw"], width, label="raw")
    plt.bar(positions + width / 2, plot_data["abs_weighted_att"], width, label="ATT weighted")
    plt.axhline(0.10, color="black", linestyle="--", linewidth=1)
    plt.xticks(positions, plot_data["covariate"], rotation=35, ha="right")
    plt.ylabel("Absolute standardized difference")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "balance_smd.png", dpi=160)
    plt.close()


def analyze_design(
    df: pd.DataFrame,
    treatment_col: str,
    outcome_col: str,
    covariates: list[str],
    outdir: Path,
) -> dict[str, pd.DataFrame]:
    outdir.mkdir(parents=True, exist_ok=True)

    d = df[treatment_col].to_numpy(dtype=int)
    y = df[outcome_col].to_numpy(dtype=float)
    x = df[covariates].to_numpy(dtype=float)
    pscore = fit_logit_propensity(x, d)

    naive = float(y[d == 1].mean() - y[d == 0].mean())
    reg = regression_adjustment(y, d, x)
    match_att, matches = nearest_neighbor_att(y, d, pscore)
    ipw_ate = float(np.mean(d * y / pscore - (1 - d) * y / (1 - pscore)))
    control_att_weights = pscore[d == 0] / (1.0 - pscore[d == 0])
    ipw_att = float(y[d == 1].mean() - weighted_mean(y[d == 0], control_att_weights))
    m0, m1 = outcome_model_predictions(y, d, x)
    aipw_ate = float(np.mean(m1 - m0 + d * (y - m1) / pscore - (1 - d) * (y - m0) / (1 - pscore)))

    estimates = pd.DataFrame(
        [
            {"estimand": "raw difference", "method": "naive means", "estimate": naive},
            {"estimand": "adjusted comparison", "method": "linear regression adjustment", "estimate": reg},
            {"estimand": "ATT", "method": "nearest-neighbor propensity match", "estimate": match_att},
            {"estimand": "ATE", "method": "inverse-probability weighting", "estimate": ipw_ate},
            {"estimand": "ATT", "method": "odds-weighted controls", "estimate": ipw_att},
            {"estimand": "ATE", "method": "augmented IPW / doubly robust", "estimate": aipw_ate},
        ]
    )

    balance = balance_table(df, covariates, d, pscore)
    propensity = df.copy()
    propensity["propensity_score"] = pscore
    propensity["att_weight"] = np.where(d == 1, 1.0, pscore / (1.0 - pscore))
    propensity["ate_weight"] = np.where(d == 1, 1.0 / pscore, 1.0 / (1.0 - pscore))

    overlap = pd.DataFrame(
        [
            {
                "group": "treated",
                "n": int(d.sum()),
                "pscore_min": float(pscore[d == 1].min()),
                "pscore_p10": float(np.quantile(pscore[d == 1], 0.10)),
                "pscore_median": float(np.median(pscore[d == 1])),
                "pscore_p90": float(np.quantile(pscore[d == 1], 0.90)),
                "pscore_max": float(pscore[d == 1].max()),
            },
            {
                "group": "untreated",
                "n": int((1 - d).sum()),
                "pscore_min": float(pscore[d == 0].min()),
                "pscore_p10": float(np.quantile(pscore[d == 0], 0.10)),
                "pscore_median": float(np.median(pscore[d == 0])),
                "pscore_p90": float(np.quantile(pscore[d == 0], 0.90)),
                "pscore_max": float(pscore[d == 0].max()),
            },
        ]
    )

    estimates.to_csv(outdir / "estimates.csv", index=False)
    balance.to_csv(outdir / "balance_diagnostics.csv", index=False)
    propensity.to_csv(outdir / "propensity_scores.csv", index=False)
    overlap.to_csv(outdir / "overlap_summary.csv", index=False)
    matches.to_csv(outdir / "matching_pairs.csv", index=False)
    make_plots(outdir, balance, d, pscore)

    return {
        "estimates": estimates,
        "balance": balance,
        "propensity": propensity,
        "overlap": overlap,
        "matches": matches,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze_design(df, "treat", "earnings_1978", TRAINING_COVARIATES, args.outdir)
    print(f"Wrote reproduce outputs to {args.outdir}")


if __name__ == "__main__":
    main()
