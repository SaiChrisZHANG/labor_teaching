"""Run the Week 10 DML teaching reproduction on synthetic online labor data."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTCOME = "log_hourly_wage"
TREATMENT = "high_client_concentration"


@dataclass
class FeatureSpec:
    feature_names: list[str]
    means: np.ndarray
    scales: np.ndarray
    occupation_levels: list[str]
    region_levels: list[str]


def raw_controls(df: pd.DataFrame, occupation_levels: list[str], region_levels: list[str]) -> tuple[np.ndarray, list[str]]:
    parts: list[np.ndarray] = []
    names: list[str] = []
    numeric = pd.DataFrame(index=df.index)
    numeric["experience_years"] = df["experience_years"].astype(float)
    numeric["experience_years_sq"] = df["experience_years"].astype(float) ** 2
    numeric["log_completed_tasks"] = np.log1p(df["completed_tasks"].astype(float))
    numeric["rating"] = df["rating"].astype(float)
    numeric["prior_log_wage"] = df["prior_log_wage"].astype(float)
    numeric["market_thickness"] = df["market_thickness"].astype(float)
    numeric["local_unemployment"] = df["local_unemployment"].astype(float)
    numeric["skill_score"] = df["skill_score"].astype(float)
    numeric["repeat_client_share"] = df["repeat_client_share"].astype(float)
    numeric["skill_x_thickness"] = numeric["skill_score"] * numeric["market_thickness"]
    numeric["prior_wage_x_skill"] = numeric["prior_log_wage"] * numeric["skill_score"]
    parts.append(numeric.to_numpy(dtype=float))
    names.extend(list(numeric.columns))

    for occupation in occupation_levels:
        parts.append((df["occupation"] == occupation).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"occupation:{occupation}")
    for region in region_levels:
        parts.append((df["region"] == region).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"region:{region}")

    return np.column_stack(parts), names


def make_spec(train_df: pd.DataFrame, occupation_levels: list[str], region_levels: list[str]) -> FeatureSpec:
    x_raw, names = raw_controls(train_df, occupation_levels, region_levels)
    means = x_raw.mean(axis=0)
    scales = x_raw.std(axis=0)
    scales[scales < 1e-8] = 1.0
    return FeatureSpec(names, means, scales, occupation_levels, region_levels)


def transform(df: pd.DataFrame, spec: FeatureSpec) -> np.ndarray:
    x_raw, names = raw_controls(df, spec.occupation_levels, spec.region_levels)
    if names != spec.feature_names:
        raise ValueError("Control feature names changed.")
    return (x_raw - spec.means) / spec.scales


def add_intercept(x: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(x.shape[0]), x])


def ols_fit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.linalg.pinv(x.T @ x) @ x.T @ y


def ols_treatment_effect(y: np.ndarray, d: np.ndarray, controls: np.ndarray) -> tuple[float, float]:
    x = add_intercept(np.column_stack([d, controls]))
    beta = ols_fit(x, y)
    residuals = y - x @ beta
    bread = np.linalg.pinv(x.T @ x)
    meat = x.T @ (x * residuals.reshape(-1, 1) ** 2)
    variance = bread @ meat @ bread
    se = float(np.sqrt(max(variance[1, 1], 0.0)))
    return float(beta[1]), se


def ridge_fit(x: np.ndarray, y: np.ndarray, penalty: float) -> tuple[float, np.ndarray]:
    y_mean = float(y.mean())
    y_centered = y - y_mean
    gram = (x.T @ x) / x.shape[0]
    rhs = (x.T @ y_centered) / x.shape[0]
    beta = np.linalg.solve(gram + penalty * np.eye(x.shape[1]), rhs)
    return y_mean, beta


def ridge_predict(intercept: float, beta: np.ndarray, x: np.ndarray) -> np.ndarray:
    return intercept + x @ beta


def soft_threshold(value: float, threshold: float) -> float:
    if value > threshold:
        return value - threshold
    if value < -threshold:
        return value + threshold
    return 0.0


def lasso_fit(x: np.ndarray, y: np.ndarray, penalty: float, max_iter: int = 3500) -> np.ndarray:
    y_centered = y - y.mean()
    beta = np.zeros(x.shape[1])
    column_norms = (x**2).mean(axis=0)
    column_norms[column_norms < 1e-10] = 1.0
    fitted = x @ beta
    for _ in range(max_iter):
        old = beta.copy()
        for j in range(x.shape[1]):
            residual = y_centered - fitted + x[:, j] * beta[j]
            rho = float(np.mean(x[:, j] * residual))
            updated = soft_threshold(rho, penalty / 2.0) / column_norms[j]
            fitted += x[:, j] * (updated - beta[j])
            beta[j] = updated
        if float(np.max(np.abs(beta - old))) < 1e-7:
            break
    return beta


def make_folds(df: pd.DataFrame, k: int = 5) -> np.ndarray:
    rng = np.random.default_rng(10201)
    folds = np.zeros(len(df), dtype=int)
    for label in [0, 1]:
        positions = np.where(df[TREATMENT].to_numpy() == label)[0]
        shuffled = rng.permutation(positions)
        for idx, position in enumerate(shuffled):
            folds[position] = idx % k
    return folds


def r2_score(y: np.ndarray, y_hat: np.ndarray) -> float:
    denom = float(np.sum((y - y.mean()) ** 2))
    if denom <= 1e-12:
        return 0.0
    return float(1.0 - np.sum((y - y_hat) ** 2) / denom)


def dml_estimate(df: pd.DataFrame, penalty: float) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, float]]:
    occupation_levels = sorted(df["occupation"].unique().tolist())
    region_levels = sorted(df["region"].unique().tolist())
    folds = make_folds(df)
    y = df[OUTCOME].to_numpy(dtype=float)
    d = df[TREATMENT].to_numpy(dtype=float)
    y_resid = np.zeros(len(df))
    d_resid = np.zeros(len(df))
    y_hat = np.zeros(len(df))
    d_hat = np.zeros(len(df))
    rows: list[dict[str, float | int]] = []

    for fold in sorted(set(folds)):
        train_df = df.iloc[folds != fold]
        holdout_df = df.iloc[folds == fold]
        spec = make_spec(train_df, occupation_levels, region_levels)
        x_train = transform(train_df, spec)
        x_holdout = transform(holdout_df, spec)
        y_train = train_df[OUTCOME].to_numpy(dtype=float)
        d_train = train_df[TREATMENT].to_numpy(dtype=float)
        y_intercept, y_beta = ridge_fit(x_train, y_train, penalty)
        d_intercept, d_beta = ridge_fit(x_train, d_train, penalty)
        holdout_idx = np.where(folds == fold)[0]
        y_hat[holdout_idx] = ridge_predict(y_intercept, y_beta, x_holdout)
        d_hat[holdout_idx] = ridge_predict(d_intercept, d_beta, x_holdout)
        y_resid[holdout_idx] = y[holdout_idx] - y_hat[holdout_idx]
        d_resid[holdout_idx] = d[holdout_idx] - d_hat[holdout_idx]
        rows.append(
            {
                "fold": int(fold),
                "n_holdout": int(len(holdout_df)),
                "treated_share_holdout": float(holdout_df[TREATMENT].mean()),
                "outcome_nuisance_r2_holdout": r2_score(y[holdout_idx], y_hat[holdout_idx]),
                "treatment_nuisance_r2_holdout": r2_score(d[holdout_idx], d_hat[holdout_idx]),
                "mean_predicted_treatment_holdout": float(np.mean(d_hat[holdout_idx])),
                "sd_treatment_residual_holdout": float(np.std(d_resid[holdout_idx], ddof=1)),
            }
        )

    theta = float(np.sum(d_resid * y_resid) / np.sum(d_resid**2))
    psi = d_resid * (y_resid - theta * d_resid)
    jacobian = -float(np.mean(d_resid**2))
    se = float(np.sqrt(np.mean(psi**2) / (jacobian**2 * len(df))))
    residuals = pd.DataFrame(
        {
            "worker_id": df["worker_id"],
            "fold": folds,
            "log_hourly_wage": y,
            "high_client_concentration": d,
            "predicted_outcome_nuisance": y_hat,
            "predicted_treatment_nuisance": d_hat,
            "outcome_residual": y_resid,
            "treatment_residual": d_resid,
        }
    )
    estimate = {"theta": theta, "se": se, "penalty": float(penalty)}
    return residuals, pd.DataFrame(rows), estimate


def post_double_selection(df: pd.DataFrame, penalty: float = 0.018) -> tuple[pd.DataFrame, pd.DataFrame]:
    occupation_levels = sorted(df["occupation"].unique().tolist())
    region_levels = sorted(df["region"].unique().tolist())
    spec = make_spec(df, occupation_levels, region_levels)
    x = transform(df, spec)
    y = df[OUTCOME].to_numpy(dtype=float)
    d = df[TREATMENT].to_numpy(dtype=float)
    beta_y = lasso_fit(x, y, penalty)
    beta_d = lasso_fit(x, d, penalty)
    selected = (np.abs(beta_y) > 1e-6) | (np.abs(beta_d) > 1e-6)
    selected_x = x[:, selected] if np.any(selected) else np.empty((len(df), 0))
    theta, se = ols_treatment_effect(y, d, selected_x)
    selected_table = pd.DataFrame(
        {
            "feature": spec.feature_names,
            "selected_outcome_equation": np.abs(beta_y) > 1e-6,
            "selected_treatment_equation": np.abs(beta_d) > 1e-6,
            "selected_union": selected,
            "outcome_lasso_coefficient": beta_y,
            "treatment_lasso_coefficient": beta_d,
        }
    ).sort_values(["selected_union", "feature"], ascending=[False, True])
    estimate = pd.DataFrame(
        [
            {
                "method": "post_double_selection",
                "theta": theta,
                "se": se,
                "penalty": penalty,
                "selected_controls": int(selected.sum()),
            }
        ]
    )
    return estimate, selected_table


def selection_stability(df: pd.DataFrame, penalty: float = 0.018) -> pd.DataFrame:
    occupation_levels = sorted(df["occupation"].unique().tolist())
    region_levels = sorted(df["region"].unique().tolist())
    folds = make_folds(df)
    counts: dict[str, int] = {}
    for fold in sorted(set(folds)):
        train_df = df.iloc[folds != fold]
        spec = make_spec(train_df, occupation_levels, region_levels)
        x_train = transform(train_df, spec)
        y_train = train_df[OUTCOME].to_numpy(dtype=float)
        d_train = train_df[TREATMENT].to_numpy(dtype=float)
        selected = (np.abs(lasso_fit(x_train, y_train, penalty)) > 1e-6) | (
            np.abs(lasso_fit(x_train, d_train, penalty)) > 1e-6
        )
        for name, is_selected in zip(spec.feature_names, selected):
            if is_selected:
                counts[name] = counts.get(name, 0) + 1
    rows = [
        {"feature": name, "selected_folds": count, "selection_rate": count / len(set(folds))}
        for name, count in counts.items()
    ]
    return pd.DataFrame(rows).sort_values(["selection_rate", "feature"], ascending=[False, True])


def write_overlap_plot(residuals: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    treated = residuals[residuals["high_client_concentration"] == 1]["predicted_treatment_nuisance"]
    untreated = residuals[residuals["high_client_concentration"] == 0]["predicted_treatment_nuisance"]
    ax.hist(untreated, bins=18, alpha=0.62, label="untreated", color="#7a7a7a", density=True)
    ax.hist(treated, bins=18, alpha=0.62, label="treated", color="#2b6cb0", density=True)
    ax.set_xlabel("Cross-fitted predicted treatment probability")
    ax.set_ylabel("Density")
    ax.set_title("Overlap diagnostic")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def run(input_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_path)
    occupation_levels = sorted(df["occupation"].unique().tolist())
    region_levels = sorted(df["region"].unique().tolist())
    full_spec = make_spec(df, occupation_levels, region_levels)
    x_full = transform(df, full_spec)
    y = df[OUTCOME].to_numpy(dtype=float)
    d = df[TREATMENT].to_numpy(dtype=float)

    low_controls = df[
        [
            "experience_years",
            "rating",
            "prior_log_wage",
            "market_thickness",
            "local_unemployment",
            "skill_score",
        ]
    ].to_numpy(dtype=float)
    low_controls = (low_controls - low_controls.mean(axis=0)) / low_controls.std(axis=0)
    baseline_theta, baseline_se = ols_treatment_effect(y, d, low_controls)
    highdim_theta, highdim_se = ols_treatment_effect(y, d, x_full)
    baseline_estimates = pd.DataFrame(
        [
            {
                "method": "low_dimensional_ols",
                "theta": baseline_theta,
                "se": baseline_se,
                "controls": "experience, rating, prior wage, thickness, unemployment, skill",
            },
            {
                "method": "naive_high_dimensional_ols",
                "theta": highdim_theta,
                "se": highdim_se,
                "controls": "all pre-treatment engineered controls",
            },
        ]
    )
    baseline_estimates.to_csv(outdir / "baseline_estimates.csv", index=False)

    residuals, fold_diagnostics, dml = dml_estimate(df, penalty=1.0)
    pd.DataFrame(
        [
            {
                "method": "cross_fitted_dml_ridge",
                "theta": dml["theta"],
                "se": dml["se"],
                "ridge_penalty": dml["penalty"],
                "target": "effect of high client concentration on log hourly wage",
            }
        ]
    ).to_csv(outdir / "dml_estimates.csv", index=False)
    residuals.to_csv(outdir / "residualized_scores.csv", index=False)
    fold_diagnostics.to_csv(outdir / "fold_diagnostics.csv", index=False)

    sensitivity_rows = []
    for penalty in [0.05, 0.25, 1.0, 5.0]:
        _, fold_rows, estimate = dml_estimate(df, penalty=penalty)
        sensitivity_rows.append(
            {
                "ridge_penalty": penalty,
                "theta": estimate["theta"],
                "se": estimate["se"],
                "mean_outcome_nuisance_r2": float(fold_rows["outcome_nuisance_r2_holdout"].mean()),
                "mean_treatment_nuisance_r2": float(fold_rows["treatment_nuisance_r2_holdout"].mean()),
            }
        )
    pd.DataFrame(sensitivity_rows).to_csv(outdir / "learner_sensitivity.csv", index=False)

    p_hat = np.clip(residuals["predicted_treatment_nuisance"].to_numpy(dtype=float), 0.0, 1.0)
    overlap = pd.DataFrame(
        [
            {
                "n": len(df),
                "treated_share": float(df[TREATMENT].mean()),
                "p_hat_min": float(np.min(p_hat)),
                "p_hat_p05": float(np.quantile(p_hat, 0.05)),
                "p_hat_p50": float(np.quantile(p_hat, 0.50)),
                "p_hat_p95": float(np.quantile(p_hat, 0.95)),
                "p_hat_max": float(np.max(p_hat)),
                "share_below_0_10": float(np.mean(p_hat < 0.10)),
                "share_above_0_90": float(np.mean(p_hat > 0.90)),
            }
        ]
    )
    overlap.to_csv(outdir / "overlap_summary.csv", index=False)
    write_overlap_plot(residuals, outdir / "overlap_plot.png")

    pds_estimate, selected_controls = post_double_selection(df)
    pds_estimate.to_csv(outdir / "post_double_selection_estimate.csv", index=False)
    selected_controls.to_csv(outdir / "post_double_selection_controls.csv", index=False)
    selection_stability(df).to_csv(outdir / "selection_stability.csv", index=False)

    leakage = pd.DataFrame(
        [
            {
                "feature": "future_client_rating",
                "status": "excluded",
                "reason": "Post-treatment platform rating can be affected by client concentration and wage outcomes.",
                "diagnostic": "Draw timing before feature construction; exclude variables realized after treatment.",
            },
            {
                "feature": "prior_log_wage",
                "status": "included",
                "reason": "Pre-treatment earnings history is a plausible confounder and nuisance predictor.",
                "diagnostic": "Check whether it is measured before the concentration exposure.",
            },
            {
                "feature": "repeat_client_share",
                "status": "included",
                "reason": "Pre-treatment market relationship measure that predicts treatment assignment.",
                "diagnostic": "Inspect overlap because strong treatment prediction can create thin support.",
            },
        ]
    )
    leakage.to_csv(outdir / "leakage_audit.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "step": "reproduce",
                "prompt": "Compare low-dimensional OLS, high-dimensional OLS, post-double selection, and cross-fitted DML.",
            },
            {
                "step": "diagnose",
                "prompt": "Use overlap, nuisance R2, leakage, and fold-stability outputs to decide whether DML sharpens the design.",
            },
            {
                "step": "report",
                "prompt": "State what the concentration effect identifies under the selection-on-observables design and what it does not identify.",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)
    print(f"DML theta: {dml['theta']:.4f} (se {dml['se']:.4f})")
    print(f"Wrote outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.input, args.outdir)


if __name__ == "__main__":
    main()
