#!/usr/bin/env python3
"""
Reduced pedagogical composition-adjustment pipeline for Labor I, Week 1.

This script expects a cell-level panel with columns:
- date
- cell
- employment_share
- mean_log_wage
- base_weight

It computes:
- raw average log wage = sum_t employment_share * mean_log_wage
- composition-adjusted average log wage = sum_t base_weight * mean_log_wage
- composition gap = raw - adjusted
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


REQUIRED_COLUMNS = {
    "date",
    "cell",
    "employment_share",
    "mean_log_wage",
    "base_weight",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def compute_series(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    temp = df.copy()
    temp["raw_component"] = temp["employment_share"] * temp["mean_log_wage"]
    temp["adjusted_component"] = temp["base_weight"] * temp["mean_log_wage"]
    grouped = (
        temp.groupby("date", as_index=False)[["raw_component", "adjusted_component"]]
        .sum()
        .rename(
            columns={
                "raw_component": "raw_log_wage",
                "adjusted_component": "adjusted_log_wage",
            }
        )
    )
    grouped["composition_gap"] = grouped["raw_log_wage"] - grouped["adjusted_log_wage"]
    return grouped.sort_values("date")


def save_outputs(series: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    csv_path = outdir / "composition_adjusted_series.csv"
    fig_path = outdir / "composition_adjusted_series.png"
    series.to_csv(csv_path, index=False)

    plot_df = series.copy()
    try:
        plot_df["date"] = pd.PeriodIndex(plot_df["date"], freq="Q").to_timestamp()
    except Exception:
        plot_df["date"] = pd.to_datetime(plot_df["date"])

    plt.figure(figsize=(9, 5))
    plt.plot(plot_df["date"], plot_df["raw_log_wage"], label="Raw average log wage")
    plt.plot(plot_df["date"], plot_df["adjusted_log_wage"], label="Composition-adjusted log wage")
    plt.plot(plot_df["date"], plot_df["composition_gap"], label="Composition gap")
    plt.title("Week 1 pedagogical composition-adjustment series")
    plt.xlabel("Date")
    plt.ylabel("Log wage units")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the reduced panel CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    series = compute_series(df)
    save_outputs(series, outdir)
    print(f"Saved outputs to {outdir}")


if __name__ == "__main__":
    main()
