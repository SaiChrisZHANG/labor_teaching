#!/usr/bin/env python3
"""
Reduced pedagogical bunching workflow for Labor I, Week 2.

The script bins earnings around a user-supplied kink, saves the binned counts,
and writes a stylized histogram that makes the local-density logic visible.
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
    parser.add_argument("--earnings-col", required=True, help="Column holding earnings values.")
    parser.add_argument("--kink", type=float, required=True, help="Kink location in earnings units.")
    parser.add_argument("--bin-width", type=float, default=1.0)
    parser.add_argument("--window", type=float, default=10.0)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def build_bins(df: pd.DataFrame, earnings_col: str, kink: float, bin_width: float, window: float) -> pd.DataFrame:
    temp = df[[earnings_col]].copy()
    temp = temp.dropna()
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
        temp.groupby("bin", observed=False)
        .size()
        .reset_index(name="count")
    )
    grouped["bin_left"] = grouped["bin"].map(lambda x: float(x.left)).astype(float)
    grouped["bin_right"] = grouped["bin"].map(lambda x: float(x.right)).astype(float)
    grouped["bin_midpoint"] = (grouped["bin_left"] + grouped["bin_right"]) / 2
    grouped["near_kink"] = grouped["bin_left"].between(-bin_width, 0, inclusive="left")
    return grouped[["bin_left", "bin_right", "bin_midpoint", "count", "near_kink"]]


def save_outputs(bins: pd.DataFrame, outdir: Path, kink: float, bin_width: float) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    bins.to_csv(outdir / "bunching_bins.csv", index=False)

    plt.figure(figsize=(9, 5))
    colors = np.where(bins["near_kink"], "#c44e52", "#4c72b0")
    plt.bar(bins["bin_midpoint"], bins["count"], width=bin_width * 0.9, color=colors)
    plt.axvline(0, color="black", linestyle="--", linewidth=1)
    plt.xlabel("Distance from kink")
    plt.ylabel("Count")
    plt.title(f"Stylized bunching around kink at earnings = {kink:g}")
    plt.tight_layout()
    plt.savefig(outdir / "bunching_histogram.png", dpi=200)
    plt.close()

    summary = {
        "total_count_in_window": int(bins["count"].sum()),
        "count_in_kink_bin": int(bins.loc[bins["near_kink"], "count"].sum()),
        "number_of_bins": int(len(bins)),
    }
    pd.Series(summary).to_csv(outdir / "bunching_summary.csv", header=["value"])


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    if args.earnings_col not in df.columns:
        raise ValueError(f"Missing earnings column: {args.earnings_col}")

    bins = build_bins(df, args.earnings_col, args.kink, args.bin_width, args.window)
    save_outputs(bins, outdir, args.kink, args.bin_width)
    print(f"Saved reduced bunching outputs to {outdir}")


if __name__ == "__main__":
    main()
