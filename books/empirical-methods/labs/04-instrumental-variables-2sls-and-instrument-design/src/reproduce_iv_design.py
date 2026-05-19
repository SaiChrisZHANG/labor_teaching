"""Run the Week 4 compulsory-schooling IV teaching workflow."""

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


def controls_matrix(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    state_dummies = pd.get_dummies(df["state"], prefix="state", drop_first=True, dtype=float)
    cohort_dummies = pd.get_dummies(df["birth_year"], prefix="cohort", drop_first=True, dtype=float)
    continuous = pd.DataFrame(
        {
            "intercept": 1.0,
            "female": df["female"].astype(float),
            "parent_education": (df["parent_education"] - df["parent_education"].mean())
            / df["parent_education"].std(ddof=0),
            "family_income": (df["family_income"] - df["family_income"].mean())
            / df["family_income"].std(ddof=0),
        },
        index=df.index,
    )
    controls = pd.concat([continuous, state_dummies, cohort_dummies], axis=1)
    return controls.to_numpy(dtype=float), list(controls.columns)


def first_stage_f(d: np.ndarray, z: np.ndarray, controls: np.ndarray) -> tuple[float, float, float]:
    restricted = controls
    unrestricted = np.column_stack([z, controls])
    beta_r = ols_beta(d, restricted)
    beta_u = ols_beta(d, unrestricted)
    rss_r = float(np.sum((d - restricted @ beta_r) ** 2))
    rss_u = float(np.sum((d - unrestricted @ beta_u) ** 2))
    q = 1
    n, k_u = unrestricted.shape
    f_stat = ((rss_r - rss_u) / q) / (rss_u / max(n - k_u, 1))
    partial_r2 = max((rss_r - rss_u) / rss_r, 0.0)
    return float(f_stat), float(partial_r2), float(beta_u[0])


def two_stage_least_squares(
    y: np.ndarray,
    d: np.ndarray,
    z: np.ndarray,
    controls: np.ndarray,
) -> tuple[float, float]:
    x = np.column_stack([d, controls])
    w = np.column_stack([z, controls])
    pz = w @ np.linalg.pinv(w.T @ w) @ w.T
    xpzx = x.T @ pz @ x
    beta = np.linalg.pinv(xpzx) @ (x.T @ pz @ y)
    residual = y - x @ beta
    n, k = x.shape
    sigma2 = float(residual @ residual / max(n - k, 1))
    cov = sigma2 * np.linalg.pinv(xpzx)
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    return float(beta[0]), float(se[0])


def standardized_balance(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in ["female", "parent_education", "family_income", "birth_year"]:
        z0 = df.loc[df["compulsory_exposure"] == 0, col].astype(float)
        z1 = df.loc[df["compulsory_exposure"] == 1, col].astype(float)
        pooled_sd = np.sqrt((z0.var(ddof=1) + z1.var(ddof=1)) / 2)
        rows.append(
            {
                "covariate": col,
                "mean_z0": float(z0.mean()),
                "mean_z1": float(z1.mean()),
                "difference_z1_minus_z0": float(z1.mean() - z0.mean()),
                "standardized_difference": float((z1.mean() - z0.mean()) / pooled_sd),
            }
        )
    return pd.DataFrame(rows)


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    y = df["log_earnings"].to_numpy(dtype=float)
    d = df["stayed_in_school"].to_numpy(dtype=float)
    z = df["compulsory_exposure"].to_numpy(dtype=float)
    controls, control_names = controls_matrix(df)

    ols_x = np.column_stack([d, controls])
    ols = ols_beta(y, ols_x)
    ols_se = homoskedastic_se(y, ols_x, ols)

    fs_x = np.column_stack([z, controls])
    fs_beta = ols_beta(d, fs_x)
    fs_se = homoskedastic_se(d, fs_x, fs_beta)

    rf_beta = ols_beta(y, fs_x)
    rf_se = homoskedastic_se(y, fs_x, rf_beta)

    simple_first_stage = float(df.loc[z == 1, "stayed_in_school"].mean() - df.loc[z == 0, "stayed_in_school"].mean())
    simple_reduced_form = float(df.loc[z == 1, "log_earnings"].mean() - df.loc[z == 0, "log_earnings"].mean())
    simple_wald = simple_reduced_form / simple_first_stage
    adjusted_wald = float(rf_beta[0] / fs_beta[0])
    f_stat, partial_r2, _ = first_stage_f(d, z, controls)
    tsls_beta, tsls_se = two_stage_least_squares(y, d, z, controls)
    true_complier_late = float(
        df.loc[df["synthetic_compliance_type"] == "complier", "synthetic_true_effect"].mean()
    )

    estimates = pd.DataFrame(
        [
            {
                "object": "naive OLS coefficient on stayed_in_school",
                "estimate": float(ols[0]),
                "standard_error": float(ols_se[0]),
                "interpretation": "observational association adjusted for controls; still confounded by synthetic ability",
            },
            {
                "object": "first stage: compulsory_exposure -> stayed_in_school",
                "estimate": float(fs_beta[0]),
                "standard_error": float(fs_se[0]),
                "interpretation": "rule exposure effect on the probability of staying in school",
            },
            {
                "object": "reduced form: compulsory_exposure -> log_earnings",
                "estimate": float(rf_beta[0]),
                "standard_error": float(rf_se[0]),
                "interpretation": "effect of instrument exposure on earnings",
            },
            {
                "object": "unadjusted Wald ratio",
                "estimate": float(simple_wald),
                "standard_error": np.nan,
                "interpretation": "raw reduced form divided by raw first stage",
            },
            {
                "object": "adjusted Wald ratio",
                "estimate": adjusted_wald,
                "standard_error": np.nan,
                "interpretation": "control-adjusted reduced form divided by control-adjusted first stage",
            },
            {
                "object": "2SLS coefficient on stayed_in_school",
                "estimate": tsls_beta,
                "standard_error": tsls_se,
                "interpretation": "complier effect under IV assumptions",
            },
            {
                "object": "synthetic true complier LATE",
                "estimate": true_complier_late,
                "standard_error": np.nan,
                "interpretation": "known only because this is synthetic teaching data",
            },
        ]
    )
    estimates.to_csv(outdir / "iv_estimates.csv", index=False)

    diagnostics = pd.DataFrame(
        [
            {
                "diagnostic": "observations",
                "value": float(len(df)),
                "interpretation": "synthetic sample size",
            },
            {
                "diagnostic": "simple_first_stage",
                "value": simple_first_stage,
                "interpretation": "difference in treatment rates by instrument status",
            },
            {
                "diagnostic": "control_adjusted_first_stage",
                "value": float(fs_beta[0]),
                "interpretation": "coefficient on instrument in first-stage regression",
            },
            {
                "diagnostic": "partial_first_stage_F",
                "value": f_stat,
                "interpretation": "excluded-instrument F statistic conditional on controls",
            },
            {
                "diagnostic": "partial_R2",
                "value": partial_r2,
                "interpretation": "incremental first-stage fit from the excluded instrument",
            },
            {
                "diagnostic": "controls",
                "value": float(len(control_names)),
                "interpretation": "number of included control columns, including intercept and fixed effects",
            },
        ]
    )
    diagnostics.to_csv(outdir / "first_stage_diagnostics.csv", index=False)

    standardized_balance(df).to_csv(outdir / "balance_by_instrument.csv", index=False)

    complier_profile = (
        df.groupby("synthetic_compliance_type", as_index=False)
        .agg(
            observations=("person_id", "size"),
            share=("person_id", lambda x: len(x) / len(df)),
            treatment_rate=("stayed_in_school", "mean"),
            instrument_rate=("compulsory_exposure", "mean"),
            mean_log_earnings=("log_earnings", "mean"),
            mean_true_effect=("synthetic_true_effect", "mean"),
        )
        .sort_values("synthetic_compliance_type")
    )
    complier_profile.to_csv(outdir / "complier_profile.csv", index=False)

    first_stage_by_cell = (
        df.groupby(["birth_quarter", "compulsory_exposure"], as_index=False)
        .agg(
            observations=("person_id", "size"),
            treatment_rate=("stayed_in_school", "mean"),
            mean_log_earnings=("log_earnings", "mean"),
        )
        .sort_values(["birth_quarter", "compulsory_exposure"])
    )
    first_stage_by_cell.to_csv(outdir / "first_stage_by_cell.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "What treatment margin does compulsory_exposure move?",
                "student_note": "Use first_stage_diagnostics.csv and complier_profile.csv.",
            },
            {
                "prompt": "What is the leading exclusion threat?",
                "student_note": "Think about birth timing, cohort, and schooling-entry channels.",
            },
            {
                "prompt": "Why does OLS differ from 2SLS?",
                "student_note": "Treatment is correlated with synthetic ability, which is omitted from the estimating equations.",
            },
            {
                "prompt": "What does the IV estimate not identify?",
                "student_note": "It does not identify the ATE for always-takers or never-takers.",
            },
            {
                "prompt": "How would the diagnosis change for a leave-out leniency instrument?",
                "student_note": "Check assignment-cell balance, leave-one-out construction, and direct decision-maker channels.",
            },
        ]
    )
    prompts.to_csv(outdir / "design_prompts.csv", index=False)

    plot_data = (
        df.groupby("compulsory_exposure", as_index=False)
        .agg(treatment_rate=("stayed_in_school", "mean"))
        .sort_values("compulsory_exposure")
    )
    plt.figure(figsize=(6.6, 4.0))
    plt.bar(plot_data["compulsory_exposure"].astype(str), plot_data["treatment_rate"], color=["#4C78A8", "#F58518"])
    plt.ylim(0.0, 1.0)
    plt.xlabel("Compulsory-schooling exposure")
    plt.ylabel("Share staying in school")
    plt.tight_layout()
    plt.savefig(outdir / "treatment_by_instrument.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote IV diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
