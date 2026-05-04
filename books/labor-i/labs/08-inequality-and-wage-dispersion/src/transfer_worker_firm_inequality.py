#!/usr/bin/env python3
"""Run a bounded worker-firm decomposition for the Week 8 inequality lab."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def residualize_controls(df: pd.DataFrame) -> np.ndarray:
    X = np.column_stack(
        [
            np.ones(len(df)),
            df["college"].to_numpy(),
            df["female"].to_numpy(),
            df["experience"].to_numpy(),
        ]
    )
    y = df["log_wage"].to_numpy()
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ coef


def component_summary(df: pd.DataFrame) -> pd.DataFrame:
    wage_net = residualize_controls(df)
    alpha = df["worker_effect_true"].to_numpy()
    psi = df["firm_premium_true"].to_numpy()
    alpha_centered = alpha - alpha.mean()
    psi_centered = psi - psi.mean()
    residual = wage_net - alpha_centered - psi_centered

    total = float(np.var(wage_net))
    worker = float(np.var(alpha_centered))
    firm = float(np.var(psi_centered))
    sorting = float(2.0 * np.cov(alpha_centered, psi_centered, bias=True)[0, 1])
    residual_var = float(np.var(residual))

    return pd.DataFrame(
        [
            {"component": "worker_effect", "value": worker, "share_of_total": worker / total},
            {"component": "firm_premium", "value": firm, "share_of_total": firm / total},
            {"component": "sorting_covariance", "value": sorting, "share_of_total": sorting / total},
            {"component": "residual", "value": residual_var, "share_of_total": residual_var / total},
            {"component": "total_residualized_variance", "value": total, "share_of_total": 1.0},
        ]
    )


def firm_quartile_summary(df: pd.DataFrame) -> pd.DataFrame:
    firm_df = (
        df.groupby("firm_id", as_index=False)
        .agg(
            mean_log_wage=("log_wage", "mean"),
            mean_total_job_value=("total_job_value", "mean"),
            mean_firm_premium=("firm_premium_true", "mean"),
            mean_amenity_value=("amenity_value", "mean"),
        )
        .sort_values("mean_firm_premium")
        .reset_index(drop=True)
    )
    firm_df["firm_quartile"] = pd.qcut(firm_df["mean_firm_premium"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
    return (
        firm_df.groupby("firm_quartile", as_index=False, observed=False)
        .agg(
            average_log_wage=("mean_log_wage", "mean"),
            average_total_job_value=("mean_total_job_value", "mean"),
            average_amenity_value=("mean_amenity_value", "mean"),
        )
    )


def make_figure(component_df: pd.DataFrame, quartile_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    display_df = component_df[component_df["component"] != "total_residualized_variance"].copy()
    axes[0].bar(
        display_df["component"],
        display_df["share_of_total"],
        color=["#1f5c99", "#2a7f62", "#7d5ba6", "#c25b2a"],
    )
    axes[0].set_title("AKM-style component shares")
    axes[0].set_ylabel("Share of residualized wage variance")
    axes[0].tick_params(axis="x", rotation=25)

    axes[1].plot(quartile_df["firm_quartile"], quartile_df["average_log_wage"], marker="o", color="#d8a25b", label="Mean log wage")
    axes[1].plot(
        quartile_df["firm_quartile"],
        quartile_df["average_total_job_value"],
        marker="o",
        color="#1f5c99",
        label="Mean total job value",
    )
    axes[1].set_title("Firm quartiles: wages versus total value")
    axes[1].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(outdir / "transfer_worker_firm_bridge.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    component_df = component_summary(df)
    quartile_df = firm_quartile_summary(df)

    component_df.to_csv(args.outdir / "akm_component_summary.csv", index=False)
    quartile_df.to_csv(args.outdir / "firm_quartile_summary.csv", index=False)
    make_figure(component_df, quartile_df, args.outdir)

    note = (
        "This bounded transfer exercise uses a synthetic worker-firm panel to separate worker effects, "
        "firm premia, sorting covariance, and residual dispersion. It also compares wage rankings with "
        "total job-value rankings across firm-premium quartiles."
    )
    (args.outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
