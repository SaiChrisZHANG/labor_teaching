"""Run a bounded randomized encouragement teaching workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week2_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week2_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASELINE_COVARIATES = ["baseline_enrolled", "salary", "tenure", "age"]


def mean_difference(df: pd.DataFrame, outcome: str, assignment: str) -> float:
    observed = df.dropna(subset=[outcome])
    treated = observed[observed[assignment] == 1][outcome]
    control = observed[observed[assignment] == 0][outcome]
    return float(treated.mean() - control.mean())


def ols_coef(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return beta


def standardized_difference(values: np.ndarray, z: np.ndarray) -> float:
    treated = values[z == 1]
    control = values[z == 0]
    pooled = np.sqrt((treated.var(ddof=0) + control.var(ddof=0)) / 2.0)
    if pooled == 0:
        return 0.0
    return float((treated.mean() - control.mean()) / pooled)


def clustered_se(df: pd.DataFrame, y_col: str, x_cols: list[str], cluster_col: str) -> tuple[pd.Series, pd.Series]:
    observed = df.dropna(subset=[y_col]).copy()
    y = observed[y_col].to_numpy(dtype=float)
    x = np.column_stack([np.ones(len(observed))] + [observed[col].to_numpy(dtype=float) for col in x_cols])
    beta = ols_coef(y, x)
    residual = y - x @ beta
    xtx_inv = np.linalg.inv(x.T @ x)
    meat = np.zeros((x.shape[1], x.shape[1]))
    for _, group in observed.assign(_resid=residual).groupby(cluster_col):
        idx = group.index.to_numpy()
        positions = observed.index.get_indexer(idx)
        xg = x[positions, :]
        ug = residual[positions]
        score = xg.T @ ug
        meat += np.outer(score, score)
    cov = xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.diag(cov))
    names = ["intercept"] + x_cols
    return pd.Series(beta, index=names), pd.Series(se, index=names)


def balance_table(df: pd.DataFrame) -> pd.DataFrame:
    z = df["assigned_encouragement"].to_numpy(dtype=int)
    rows = []
    for covariate in BASELINE_COVARIATES:
        values = df[covariate].to_numpy(dtype=float)
        rows.append(
            {
                "covariate": covariate,
                "assigned_mean": float(values[z == 1].mean()),
                "control_mean": float(values[z == 0].mean()),
                "standardized_difference": standardized_difference(values, z),
            }
        )
    return pd.DataFrame(rows)


def exposure_table(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("assigned_encouragement")
        .agg(
            n=("worker_id", "size"),
            mean_peer_assignment_share=("peer_assignment_share", "mean"),
            mean_attendance=("attended_seminar", "mean"),
            mean_outcome_observed=("outcome_observed", "mean"),
        )
        .reset_index()
    )
    grouped["assignment_group"] = grouped["assigned_encouragement"].map({0: "control", 1: "encouraged"})
    return grouped[
        [
            "assignment_group",
            "n",
            "mean_peer_assignment_share",
            "mean_attendance",
            "mean_outcome_observed",
        ]
    ]


def make_plots(outdir: Path, balance: pd.DataFrame, df: pd.DataFrame) -> None:
    plot_data = balance.copy()
    plot_data["abs_smd"] = plot_data["standardized_difference"].abs()
    positions = np.arange(len(plot_data))

    plt.figure(figsize=(7.8, 4.3))
    plt.bar(positions, plot_data["abs_smd"])
    plt.axhline(0.10, color="black", linestyle="--", linewidth=1)
    plt.xticks(positions, plot_data["covariate"], rotation=30, ha="right")
    plt.ylabel("Absolute standardized difference")
    plt.tight_layout()
    plt.savefig(outdir / "balance_by_assignment.png", dpi=160)
    plt.close()

    plt.figure(figsize=(7.2, 4.2))
    plt.hist(
        df.loc[df["assigned_encouragement"] == 1, "peer_assignment_share"],
        bins=12,
        alpha=0.65,
        label="encouraged",
        density=True,
    )
    plt.hist(
        df.loc[df["assigned_encouragement"] == 0, "peer_assignment_share"],
        bins=12,
        alpha=0.65,
        label="control",
        density=True,
    )
    plt.xlabel("Peer assignment share")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "peer_exposure_distribution.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    itt_attendance = mean_difference(df, "attended_seminar", "assigned_encouragement")
    itt_enrollment = mean_difference(df, "enrolled_after", "assigned_encouragement")
    first_stage = itt_attendance
    wald_late = itt_enrollment / first_stage if abs(first_stage) > 1e-9 else np.nan
    naive_receipt = mean_difference(df, "enrolled_after", "attended_seminar")

    beta_enroll, se_enroll = clustered_se(
        df,
        "enrolled_after",
        ["assigned_encouragement", "peer_assignment_share"],
        "department_id",
    )
    beta_attend, se_attend = clustered_se(
        df,
        "attended_seminar",
        ["assigned_encouragement", "peer_assignment_share"],
        "department_id",
    )

    estimates = pd.DataFrame(
        [
            {
                "estimand": "ITT attendance",
                "method": "mean difference by randomized encouragement",
                "estimate": itt_attendance,
                "interpretation": "effect of encouragement on seminar attendance",
            },
            {
                "estimand": "ITT enrollment",
                "method": "mean difference by randomized encouragement",
                "estimate": itt_enrollment,
                "interpretation": "effect of encouragement on retirement-plan participation",
            },
            {
                "estimand": "first stage",
                "method": "attendance difference by assignment",
                "estimate": first_stage,
                "interpretation": "take-up response to randomized encouragement",
            },
            {
                "estimand": "Wald/LATE-style ratio",
                "method": "ITT enrollment divided by first stage",
                "estimate": wald_late,
                "interpretation": "local effect for attendance compliers under additional assumptions",
            },
            {
                "estimand": "naive receipt contrast",
                "method": "enrollment difference by attendance",
                "estimate": naive_receipt,
                "interpretation": "not randomized; useful as a warning comparison",
            },
            {
                "estimand": "direct assignment with exposure control",
                "method": "OLS with department-clustered standard error",
                "estimate": float(beta_enroll["assigned_encouragement"]),
                "clustered_se": float(se_enroll["assigned_encouragement"]),
                "interpretation": "assignment contrast holding measured peer exposure fixed",
            },
            {
                "estimand": "peer exposure association",
                "method": "OLS with department-clustered standard error",
                "estimate": float(beta_enroll["peer_assignment_share"]),
                "clustered_se": float(se_enroll["peer_assignment_share"]),
                "interpretation": "exposure contrast; causal only under exposure-design assumptions",
            },
            {
                "estimand": "attendance exposure first stage",
                "method": "OLS with department-clustered standard error",
                "estimate": float(beta_attend["peer_assignment_share"]),
                "clustered_se": float(se_attend["peer_assignment_share"]),
                "interpretation": "peer exposure association for seminar attendance",
            },
        ]
    )

    takeup = (
        df.groupby("assigned_encouragement")
        .agg(
            n=("worker_id", "size"),
            attendance_rate=("attended_seminar", "mean"),
            enrollment_rate_observed=("enrolled_after", "mean"),
        )
        .reset_index()
    )
    takeup["assignment_group"] = takeup["assigned_encouragement"].map({0: "control", 1: "encouraged"})

    attrition = (
        df.groupby("assigned_encouragement")
        .agg(n=("worker_id", "size"), outcome_observed_rate=("outcome_observed", "mean"))
        .reset_index()
    )
    attrition["assignment_group"] = attrition["assigned_encouragement"].map({0: "control", 1: "encouraged"})

    balance = balance_table(df)
    exposure = exposure_table(df)

    estimates.to_csv(outdir / "experimental_estimates.csv", index=False)
    balance.to_csv(outdir / "balance_by_assignment.csv", index=False)
    takeup[["assignment_group", "n", "attendance_rate", "enrollment_rate_observed"]].to_csv(
        outdir / "takeup_by_assignment.csv",
        index=False,
    )
    attrition[["assignment_group", "n", "outcome_observed_rate"]].to_csv(
        outdir / "attrition_by_assignment.csv",
        index=False,
    )
    exposure.to_csv(outdir / "exposure_summary.csv", index=False)
    df.to_csv(outdir / "analysis_dataset.csv", index=False)
    make_plots(outdir, balance, df)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote reproduce outputs to {args.outdir}")


if __name__ == "__main__":
    main()
