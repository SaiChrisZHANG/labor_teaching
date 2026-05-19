"""Run the Week 4 shift-share transfer teaching workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week4_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week4_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ols_beta(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return beta


def homoskedastic_se(y: np.ndarray, x: np.ndarray, beta: np.ndarray) -> np.ndarray:
    residual = y - x @ beta
    n, k = x.shape
    sigma2 = float(residual @ residual / max(n - k, 1))
    cov = sigma2 * np.linalg.pinv(x.T @ x)
    return np.sqrt(np.maximum(np.diag(cov), 0.0))


def controls_matrix(df: pd.DataFrame) -> np.ndarray:
    region_dummies = pd.get_dummies(df["region"], prefix="region", drop_first=True, dtype=float)
    controls = pd.concat(
        [
            pd.Series(1.0, index=df.index, name="intercept"),
            df[["baseline_growth"]].astype(float),
            region_dummies,
        ],
        axis=1,
    )
    return controls.to_numpy(dtype=float)


def two_stage_least_squares(
    y: np.ndarray,
    d: np.ndarray,
    z: np.ndarray,
    controls: np.ndarray,
) -> tuple[float, float]:
    x = np.column_stack([d, controls])
    w = np.column_stack([z, controls])
    pz = w @ np.linalg.pinv(w.T @ w) @ w.T
    beta = np.linalg.pinv(x.T @ pz @ x) @ (x.T @ pz @ y)
    residual = y - x @ beta
    n, k = x.shape
    sigma2 = float(residual @ residual / max(n - k, 1))
    cov = sigma2 * np.linalg.pinv(x.T @ pz @ x)
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    return float(beta[0]), float(se[0])


def first_stage_f(d: np.ndarray, z: np.ndarray, controls: np.ndarray) -> float:
    restricted = controls
    unrestricted = np.column_stack([z, controls])
    beta_r = ols_beta(d, restricted)
    beta_u = ols_beta(d, unrestricted)
    rss_r = float(np.sum((d - restricted @ beta_r) ** 2))
    rss_u = float(np.sum((d - unrestricted @ beta_u) ** 2))
    n, k_u = unrestricted.shape
    return float(((rss_r - rss_u) / 1) / (rss_u / max(n - k_u, 1)))


def analyze(places: pd.DataFrame, shocks: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    sectors = shocks["sector"].tolist()
    share_cols = [f"share_{sector}" for sector in sectors]
    shock_lookup = shocks.set_index("sector")["shock"].to_dict()
    shock_vector = np.array([shock_lookup[sector] for sector in sectors], dtype=float)

    shares = places[share_cols].to_numpy(dtype=float)
    places = places.copy()
    places["shift_share_instrument"] = shares @ shock_vector
    places["dominant_share"] = shares.max(axis=1)
    places["exposure_herfindahl"] = (shares**2).sum(axis=1)

    contribution_rows = []
    for _, row in places.iterrows():
        for sector in sectors:
            contribution = float(row[f"share_{sector}"] * shock_lookup[sector])
            contribution_rows.append(
                {
                    "place_id": int(row["place_id"]),
                    "sector": sector,
                    "share": float(row[f"share_{sector}"]),
                    "shock": float(shock_lookup[sector]),
                    "contribution": contribution,
                    "abs_contribution": abs(contribution),
                }
            )
    contributions = pd.DataFrame(contribution_rows)
    contributions.to_csv(outdir / "shift_share_components.csv", index=False)

    dominant = (
        contributions.sort_values(["place_id", "abs_contribution"], ascending=[True, False])
        .groupby("place_id", as_index=False)
        .first()[["place_id", "sector", "share", "shock", "contribution"]]
        .rename(columns={"sector": "dominant_contribution_sector"})
    )
    dominant.to_csv(outdir / "dominant_contributions.csv", index=False)

    y = places["outcome_growth"].to_numpy(dtype=float)
    d = places["treatment_intensity"].to_numpy(dtype=float)
    z = places["shift_share_instrument"].to_numpy(dtype=float)
    controls = controls_matrix(places)

    ols_x = np.column_stack([d, controls])
    ols = ols_beta(y, ols_x)
    ols_se = homoskedastic_se(y, ols_x, ols)

    fs_x = np.column_stack([z, controls])
    fs = ols_beta(d, fs_x)
    fs_se = homoskedastic_se(d, fs_x, fs)
    rf = ols_beta(y, fs_x)
    rf_se = homoskedastic_se(y, fs_x, rf)
    tsls, tsls_se = two_stage_least_squares(y, d, z, controls)
    partial_f = first_stage_f(d, z, controls)

    estimates = pd.DataFrame(
        [
            {
                "object": "OLS treatment coefficient",
                "estimate": float(ols[0]),
                "standard_error": float(ols_se[0]),
                "interpretation": "association between treatment intensity and outcome growth",
            },
            {
                "object": "first stage: shift-share -> treatment",
                "estimate": float(fs[0]),
                "standard_error": float(fs_se[0]),
                "interpretation": "effect of predicted shock exposure on treatment intensity",
            },
            {
                "object": "reduced form: shift-share -> outcome",
                "estimate": float(rf[0]),
                "standard_error": float(rf_se[0]),
                "interpretation": "effect of predicted shock exposure on outcome growth",
            },
            {
                "object": "2SLS treatment coefficient",
                "estimate": tsls,
                "standard_error": tsls_se,
                "interpretation": "effect identified by shift-share exposure under IV assumptions",
            },
        ]
    )
    estimates.to_csv(outdir / "shift_share_iv_estimates.csv", index=False)

    exposure_by_sector = contributions.groupby("sector", as_index=False).agg(
        mean_share=("share", "mean"),
        total_abs_contribution=("abs_contribution", "sum"),
        mean_contribution=("contribution", "mean"),
    )
    shock_summary = shocks.merge(exposure_by_sector, on="sector", how="left")
    shock_summary["inference_note"] = "independent variation is at the sector-shock level in this synthetic design"
    shock_summary.to_csv(outdir / "shock_level_summary.csv", index=False)

    corr_exposure_baseline = float(np.corrcoef(places["shift_share_instrument"], places["baseline_growth"])[0, 1])
    corr_shares_baseline = float(np.corrcoef(places["share_manufacturing"], places["baseline_growth"])[0, 1])
    diagnostics = pd.DataFrame(
        [
            {
                "diagnostic": "number_of_places",
                "value": float(len(places)),
                "interpretation": "place observations in the transfer path",
            },
            {
                "diagnostic": "number_of_sector_shocks",
                "value": float(len(sectors)),
                "interpretation": "shock-level independent variation is limited by the number of shocks",
            },
            {
                "diagnostic": "partial_first_stage_F",
                "value": partial_f,
                "interpretation": "excluded shift-share instrument strength conditional on controls",
            },
            {
                "diagnostic": "mean_dominant_share",
                "value": float(places["dominant_share"].mean()),
                "interpretation": "high values mean places are concentrated in one sector",
            },
            {
                "diagnostic": "mean_exposure_herfindahl",
                "value": float(places["exposure_herfindahl"].mean()),
                "interpretation": "summary of exposure concentration across sectors",
            },
            {
                "diagnostic": "correlation_shift_share_baseline_growth",
                "value": corr_exposure_baseline,
                "interpretation": "pre-period imbalance warning for exposure-based designs",
            },
            {
                "diagnostic": "correlation_manufacturing_share_baseline_growth",
                "value": corr_shares_baseline,
                "interpretation": "endogenous-share warning",
            },
        ]
    )
    diagnostics.to_csv(outdir / "shift_share_diagnostics.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "Does identification come from shocks or shares?",
                "student_note": "Use shock_level_summary.csv and the exposure construction.",
            },
            {
                "prompt": "Which sectors dominate predicted exposure?",
                "student_note": "Use dominant_contributions.csv and shift_share_components.csv.",
            },
            {
                "prompt": "Why might geographic clustering be insufficient?",
                "student_note": "Places share the same sector shocks, so independent variation may be shock-level.",
            },
            {
                "prompt": "How would this differ from judge leniency?",
                "student_note": "Leniency requires quasi-random assignment to decision-makers and leave-out construction.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)

    sector_plot = shock_summary.sort_values("total_abs_contribution", ascending=False)
    plt.figure(figsize=(7.4, 4.2))
    plt.bar(sector_plot["sector"], sector_plot["total_abs_contribution"], color="#54A24B")
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Total absolute contribution")
    plt.xlabel("Sector shock")
    plt.tight_layout()
    plt.savefig(outdir / "shock_contribution_by_sector.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--places", required=True, type=Path)
    parser.add_argument("--shocks", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    places = pd.read_csv(args.places)
    shocks = pd.read_csv(args.shocks)
    analyze(places, shocks, args.outdir)
    print(f"Wrote shift-share diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
