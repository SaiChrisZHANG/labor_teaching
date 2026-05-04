#!/usr/bin/env python3
"""
Build a compact labor-market factbook from a small micro-level dataset.

Required inputs:
- date column
- employment status column with values in {employed, unemployed, nilf}
- weight column
- hours column
- weekly earnings column

Optional:
- group column for subgroup summaries
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


VALID_STATUSES = {"employed", "unemployed", "nilf"}


def coerce_dates(series: pd.Series) -> pd.Series:
    try:
        return pd.PeriodIndex(series.astype(str), freq="Q").to_timestamp()
    except Exception:
        return pd.to_datetime(series)


def weighted_mean(values: pd.Series, weights: pd.Series) -> float:
    mask = values.notna() & weights.notna()
    if mask.sum() == 0:
        return float("nan")
    values = values[mask].astype(float)
    weights = weights[mask].astype(float)
    return float(np.average(values, weights=weights))


def weighted_median(values: pd.Series, weights: pd.Series) -> float:
    mask = values.notna() & weights.notna()
    if mask.sum() == 0:
        return float("nan")
    values = values[mask].astype(float)
    weights = weights[mask].astype(float)
    order = np.argsort(values.to_numpy())
    values_sorted = values.to_numpy()[order]
    weights_sorted = weights.to_numpy()[order]
    cumulative = np.cumsum(weights_sorted) / weights_sorted.sum()
    return float(values_sorted[np.searchsorted(cumulative, 0.5)])


def validate_statuses(df: pd.DataFrame, status_col: str) -> None:
    observed = set(df[status_col].dropna().astype(str).str.lower().unique())
    if not observed.issubset(VALID_STATUSES):
        raise ValueError(
            f"Employment status must be a subset of {sorted(VALID_STATUSES)}. "
            f"Observed unexpected values: {sorted(observed - VALID_STATUSES)}"
        )


def summarize_group(
    df: pd.DataFrame,
    date_col: str,
    status_col: str,
    weight_col: str,
    hours_col: str,
    earnings_col: str,
    group_cols: Iterable[str],
) -> pd.DataFrame:
    records = []
    group_cols = list(group_cols)
    for keys, g in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        key_map = dict(zip(group_cols, keys))
        total_pop = g[weight_col].sum()
        labor_force = g.loc[g[status_col].isin(["employed", "unemployed"]), weight_col].sum()
        employed = g.loc[g[status_col] == "employed", weight_col].sum()
        unemployed = g.loc[g[status_col] == "unemployed", weight_col].sum()
        g_emp = g.loc[g[status_col] == "employed"].copy()
        records.append(
            {
                **key_map,
                "population_weight": total_pop,
                "labor_force_weight": labor_force,
                "employment_rate": employed / total_pop if total_pop else np.nan,
                "labor_force_participation_rate": labor_force / total_pop if total_pop else np.nan,
                "unemployment_rate": unemployed / labor_force if labor_force else np.nan,
                "mean_hours_employed": weighted_mean(g_emp[hours_col], g_emp[weight_col]),
                "median_weekly_earnings_employed": weighted_median(
                    g_emp[earnings_col], g_emp[weight_col]
                ),
            }
        )
    return pd.DataFrame.from_records(records)


def make_plots(summary: pd.DataFrame, date_col: str, outdir: Path, group_col: str | None) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    plot_df = summary.copy()
    plot_df[date_col] = coerce_dates(plot_df[date_col])

    if group_col:
        for metric, filename, ylabel in [
            ("employment_rate", "employment_rate_by_group.png", "Employment rate"),
            (
                "labor_force_participation_rate",
                "lfpr_by_group.png",
                "Labor force participation rate",
            ),
            (
                "median_weekly_earnings_employed",
                "median_weekly_earnings_by_group.png",
                "Median weekly earnings",
            ),
        ]:
            plt.figure(figsize=(9, 5))
            for group_value, g in plot_df.groupby(group_col):
                plt.plot(g[date_col], g[metric], label=str(group_value))
            plt.title(metric.replace("_", " ").title())
            plt.xlabel("Date")
            plt.ylabel(ylabel)
            plt.legend()
            plt.tight_layout()
            plt.savefig(outdir / filename, dpi=200)
            plt.close()
    else:
        for metric, filename, ylabel in [
            ("employment_rate", "employment_rate.png", "Employment rate"),
            (
                "labor_force_participation_rate",
                "lfpr.png",
                "Labor force participation rate",
            ),
            (
                "median_weekly_earnings_employed",
                "median_weekly_earnings.png",
                "Median weekly earnings",
            ),
        ]:
            plt.figure(figsize=(9, 5))
            plt.plot(plot_df[date_col], plot_df[metric])
            plt.title(metric.replace("_", " ").title())
            plt.xlabel("Date")
            plt.ylabel(ylabel)
            plt.tight_layout()
            plt.savefig(outdir / filename, dpi=200)
            plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to a CSV dataset.")
    parser.add_argument("--date-col", required=True)
    parser.add_argument("--status-col", required=True)
    parser.add_argument("--weight-col", required=True)
    parser.add_argument("--hours-col", required=True)
    parser.add_argument("--earnings-col", required=True)
    parser.add_argument("--group-col", default=None)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    df[args.status_col] = df[args.status_col].astype(str).str.lower()
    validate_statuses(df, args.status_col)

    grouping = [args.date_col]
    if args.group_col:
        grouping.append(args.group_col)

    summary = summarize_group(
        df=df,
        date_col=args.date_col,
        status_col=args.status_col,
        weight_col=args.weight_col,
        hours_col=args.hours_col,
        earnings_col=args.earnings_col,
        group_cols=grouping,
    )
    outdir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(outdir / "labor_factbook_summary.csv", index=False)
    make_plots(summary, args.date_col, outdir, args.group_col)
    print(f"Saved summary and plots to {outdir}")


if __name__ == "__main__":
    main()
