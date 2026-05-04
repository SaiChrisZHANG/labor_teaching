#!/usr/bin/env python3
"""Estimate bounded Week 10 reform-exposure effects from synthetic migration data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def estimate_exposure_effect(df: pd.DataFrame, outcome: str) -> dict[str, float | str]:
    region_dummies = pd.get_dummies(df["region_name"], drop_first=True, dtype=float)
    year_dummies = pd.get_dummies(df["year"].astype(str), drop_first=True, dtype=float)
    treatment = df["exposure_share"] * df["post"]

    X = np.column_stack(
        [
            np.ones(len(df)),
            treatment.to_numpy(),
            df["manufacturing_share"].to_numpy(),
            region_dummies.to_numpy(),
            year_dummies.to_numpy(),
        ]
    )
    y = df[outcome].to_numpy()
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    dof = X.shape[0] - X.shape[1]
    sigma2 = float((resid @ resid) / dof)
    vcov = sigma2 * np.linalg.inv(X.T @ X)
    beta = float(coef[1])
    se = float(np.sqrt(vcov[1, 1]))
    return {"outcome": outcome, "beta_exposure_post": beta, "se": se}


def estimate_table(df: pd.DataFrame) -> pd.DataFrame:
    outcomes = ["ee_reallocation_rate", "log_firm_employment", "native_wage_growth"]
    return pd.DataFrame([estimate_exposure_effect(df, outcome) for outcome in outcomes])


def exposure_series(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["year", "exposure_group"], as_index=False)
        .agg(
            ee_reallocation_rate=("ee_reallocation_rate", "mean"),
            log_firm_employment=("log_firm_employment", "mean"),
            native_wage_growth=("native_wage_growth", "mean"),
        )
        .sort_values(["exposure_group", "year"])
        .reset_index(drop=True)
    )


def make_figure(estimate_df: pd.DataFrame, series_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.7))

    high = series_df[series_df["exposure_group"] == "high_exposure"]
    low = series_df[series_df["exposure_group"] == "low_exposure"]
    axes[0].plot(high["year"], high["ee_reallocation_rate"], marker="o", color="#c25b2a", label="High exposure")
    axes[0].plot(low["year"], low["ee_reallocation_rate"], marker="o", color="#1f5c99", label="Low exposure")
    axes[0].axvline(2018, color="#555555", linestyle="--", linewidth=1.2)
    axes[0].set_title("EE reallocation by exposure group")
    axes[0].set_ylabel("Mean reallocation rate")
    axes[0].legend(frameon=False)

    axes[1].bar(
        estimate_df["outcome"],
        estimate_df["beta_exposure_post"],
        color=["#2a7f62", "#d8a25b", "#7d5ba6"],
    )
    axes[1].errorbar(
        estimate_df["outcome"],
        estimate_df["beta_exposure_post"],
        yerr=1.96 * estimate_df["se"],
        fmt="none",
        ecolor="#374151",
        elinewidth=1.2,
        capsize=4,
    )
    axes[1].set_title("Exposure-design estimates")
    axes[1].set_ylabel("Exposure x post coefficient")
    axes[1].tick_params(axis="x", rotation=20)

    fig.tight_layout()
    fig.savefig(outdir / "transfer_reallocation_effects.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    estimate_df = estimate_table(df)
    series_df = exposure_series(df)

    estimate_df.to_csv(args.outdir / "diff_in_diff_estimates.csv", index=False)
    series_df.to_csv(args.outdir / "exposure_group_series.csv", index=False)
    make_figure(estimate_df, series_df, args.outdir)

    note = (
        "This bounded transfer exercise estimates reduced-form labor-market responses to a migration reform "
        "using differential pre-reform exposure. It identifies market-level reallocation effects, not one "
        "single structural mechanism."
    )
    (args.outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
