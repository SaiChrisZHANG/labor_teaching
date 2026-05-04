#!/usr/bin/env python3
"""
Transfer the Week 2 bunching workflow to one bounded subgroup comparison.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV.")
    parser.add_argument("--earnings-col", required=True)
    parser.add_argument("--group-col", required=True)
    parser.add_argument("--kink", type=float, required=True)
    parser.add_argument("--bin-width", type=float, default=2.0)
    parser.add_argument("--window", type=float, default=12.0)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def prepare_bins(
    df: pd.DataFrame,
    earnings_col: str,
    group_col: str,
    kink: float,
    bin_width: float,
    window: float,
) -> pd.DataFrame:
    temp = df[[earnings_col, group_col]].dropna().copy()
    temp["distance_from_kink"] = temp[earnings_col].astype(float) - kink
    temp = temp.loc[temp["distance_from_kink"].abs() <= window].copy()

    edges = np.arange(-window, window + bin_width, bin_width)
    temp["bin"] = pd.cut(
        temp["distance_from_kink"],
        bins=edges,
        include_lowest=True,
        right=False,
    )

    grouped = (
        temp.groupby([group_col, "bin"], observed=False)
        .size()
        .reset_index(name="count")
    )
    grouped["bin_left"] = grouped["bin"].map(lambda x: float(x.left)).astype(float)
    grouped["bin_right"] = grouped["bin"].map(lambda x: float(x.right)).astype(float)
    grouped["bin_midpoint"] = (grouped["bin_left"] + grouped["bin_right"]) / 2
    grouped["near_kink"] = grouped["bin_left"].between(-bin_width, 0, inclusive="left")
    return grouped[[group_col, "bin_left", "bin_right", "bin_midpoint", "count", "near_kink"]]


def save_outputs(bins: pd.DataFrame, group_col: str, outdir: Path, kink: float) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    bins.to_csv(outdir / "transfer_bunching_bins.csv", index=False)

    summary = (
        bins.groupby(group_col, as_index=False)
        .agg(
            total_count=("count", "sum"),
            count_in_kink_bin=("count", lambda s: int(s[bins.loc[s.index, "near_kink"]].sum())),
        )
    )
    summary.to_csv(outdir / "transfer_bunching_summary.csv", index=False)

    plt.figure(figsize=(9, 5))
    for group_value, group_df in bins.groupby(group_col):
        plt.plot(group_df["bin_midpoint"], group_df["count"], marker="o", label=str(group_value))
    plt.axvline(0, color="black", linestyle="--", linewidth=1)
    plt.xlabel("Distance from kink")
    plt.ylabel("Count")
    plt.title(f"Bounded subgroup bunching comparison around kink at {kink:g}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "transfer_bunching_by_group.png", dpi=200)
    plt.close()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    missing = {args.earnings_col, args.group_col} - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    bins = prepare_bins(
        df=df,
        earnings_col=args.earnings_col,
        group_col=args.group_col,
        kink=args.kink,
        bin_width=args.bin_width,
        window=args.window,
    )
    save_outputs(bins, args.group_col, outdir, args.kink)
    print(f"Saved transfer bunching outputs to {outdir}")


if __name__ == "__main__":
    main()
