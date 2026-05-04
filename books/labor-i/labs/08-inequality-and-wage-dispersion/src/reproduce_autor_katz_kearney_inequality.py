#!/usr/bin/env python3
"""Build a bounded inequality factbook from synthetic Week 8 teaching data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def weighted_quantile(values: pd.Series, quantile: float, weights: pd.Series) -> float:
    order = np.argsort(values.to_numpy())
    values_sorted = values.to_numpy()[order]
    weights_sorted = weights.to_numpy()[order]
    cumulative = np.cumsum(weights_sorted) / np.sum(weights_sorted)
    return float(np.interp(quantile, cumulative, values_sorted))


def weighted_mean(values: pd.Series, weights: pd.Series) -> float:
    return float(np.average(values.to_numpy(), weights=weights.to_numpy()))


def weighted_var(values: pd.Series, weights: pd.Series) -> float:
    mean = weighted_mean(values, weights)
    return float(np.average(np.square(values.to_numpy() - mean), weights=weights.to_numpy()))


def percentile_gap_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year, year_df in df.groupby("year", sort=True):
        log_wage = year_df["log_hourly_wage"]
        weights = year_df["weight"]
        q10 = weighted_quantile(log_wage, 0.10, weights)
        q50 = weighted_quantile(log_wage, 0.50, weights)
        q90 = weighted_quantile(log_wage, 0.90, weights)
        rows.append(
            {
                "year": year,
                "p10": q10,
                "p50": q50,
                "p90": q90,
                "p90_p10": q90 - q10,
                "p90_p50": q90 - q50,
                "p50_p10": q50 - q10,
            }
        )
    return pd.DataFrame(rows)


def college_premium_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year, year_df in df.groupby("year", sort=True):
        for college_value, label in [(0, "noncollege"), (1, "college")]:
            sub = year_df[year_df["college"] == college_value]
            rows.append(
                {
                    "year": year,
                    "group": label,
                    "mean_log_hourly_wage": weighted_mean(sub["log_hourly_wage"], sub["weight"]),
                }
            )
    summary = pd.DataFrame(rows)
    pivot = summary.pivot(index="year", columns="group", values="mean_log_hourly_wage").reset_index()
    pivot["college_premium"] = pivot["college"] - pivot["noncollege"]
    return pivot


def decomposition_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year, year_df in df.groupby("year", sort=True):
        total_var = weighted_var(year_df["log_hourly_wage"], year_df["weight"])
        group_means = {
            group_value: weighted_mean(sub["log_hourly_wage"], sub["weight"])
            for group_value, sub in year_df.groupby("college")
        }
        mapped_means = year_df["college"].map(group_means)
        between_var = weighted_var(mapped_means, year_df["weight"])

        within_var = 0.0
        for _, sub in year_df.groupby("college"):
            share = float(sub["weight"].sum() / year_df["weight"].sum())
            within_var += share * weighted_var(sub["log_hourly_wage"], sub["weight"])

        rows.append(
            {
                "year": year,
                "total_variance": total_var,
                "between_variance": between_var,
                "within_variance": within_var,
            }
        )
    return pd.DataFrame(rows)


def residual_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year, year_df in df.groupby("year", sort=True):
        design = pd.get_dummies(
            year_df[["college", "female", "experience", "region", "occupation_group"]],
            columns=["region", "occupation_group"],
            drop_first=True,
            dtype=float,
        )
        design["experience_sq"] = np.square(design["experience"])
        X = np.column_stack([np.ones(len(design)), design.to_numpy()])
        y = year_df["log_hourly_wage"].to_numpy()
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        residual = y - X @ coef
        rows.append(
            {
                "year": year,
                "residual_variance": float(np.var(residual)),
                "residual_sd": float(np.std(residual)),
            }
        )
    return pd.DataFrame(rows)


def make_figure(
    percentile_df: pd.DataFrame,
    college_df: pd.DataFrame,
    decomposition_df: pd.DataFrame,
    residual_df: pd.DataFrame,
    outdir: Path,
) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(2, 2, figsize=(11.2, 8.4))

    axes[0, 0].plot(percentile_df["year"], percentile_df["p90_p10"], marker="o", color="#1f5c99", label="p90-p10")
    axes[0, 0].plot(percentile_df["year"], percentile_df["p90_p50"], marker="o", color="#2a7f62", label="p90-p50")
    axes[0, 0].plot(percentile_df["year"], percentile_df["p50_p10"], marker="o", color="#c25b2a", label="p50-p10")
    axes[0, 0].set_title("Percentile-gap series")
    axes[0, 0].set_ylabel("Log wage gap")
    axes[0, 0].legend(frameon=False)

    axes[0, 1].plot(college_df["year"], college_df["college_premium"], marker="o", color="#5b8c5a")
    axes[0, 1].set_title("College premium")
    axes[0, 1].set_ylabel("Difference in mean log wages")

    width = 3.5
    axes[1, 0].bar(
        decomposition_df["year"] - width / 2,
        decomposition_df["between_variance"],
        width=width,
        color="#d8a25b",
        label="Between",
    )
    axes[1, 0].bar(
        decomposition_df["year"] - width / 2,
        decomposition_df["within_variance"],
        width=width,
        bottom=decomposition_df["between_variance"],
        color="#8b9dc3",
        label="Within",
    )
    axes[1, 0].set_title("Between-versus-within variance")
    axes[1, 0].set_ylabel("Variance")
    axes[1, 0].legend(frameon=False)

    axes[1, 1].plot(residual_df["year"], residual_df["residual_variance"], marker="o", color="#7d5ba6")
    axes[1, 1].set_title("Residual inequality")
    axes[1, 1].set_ylabel("Residual variance")

    for ax in axes.flat:
        ax.set_xlabel("Year")

    fig.tight_layout()
    fig.savefig(outdir / "reproduction_inequality_factbook.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    percentile_df = percentile_gap_table(df)
    college_df = college_premium_table(df)
    decomposition_df = decomposition_table(df)
    residual_df = residual_table(df)
    merged = decomposition_df.merge(residual_df, on="year", how="left")

    percentile_df.to_csv(args.outdir / "percentile_gap_series.csv", index=False)
    college_df.to_csv(args.outdir / "college_premium_summary.csv", index=False)
    merged.to_csv(args.outdir / "decomposition_summary.csv", index=False)

    make_figure(percentile_df, college_df, decomposition_df, residual_df, args.outdir)

    note = (
        "This bounded reproduction builds a synthetic inequality factbook in the spirit of "
        "Autor, Katz, and Kearney. It distinguishes upper-tail from lower-tail inequality, "
        "shows a rising college premium, and separates between-group, within-group, and residual dispersion."
    )
    (args.outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
