#!/usr/bin/env python3
"""Synthetic Week 7 reproduction anchored to Cengiz et al. (2019)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_grouped_panel(seed: int = 20260507) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    regions = {
        "Metro North": {"median_wage": 18.4, "new_floor": 14.0, "policy_month": 7},
        "River South": {"median_wage": 16.3, "new_floor": 13.5, "policy_month": 7},
        "Lake East": {"median_wage": 15.7, "new_floor": 13.0, "policy_month": 8},
        "Valley West": {"median_wage": 17.8, "new_floor": 13.0, "policy_month": 8},
    }
    bins = np.array([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0])
    rows = []
    for region, params in regions.items():
        median = params["median_wage"]
        floor = params["new_floor"]
        policy_month = params["policy_month"]
        bite = floor / median
        for month in range(1, 13):
            post = int(month >= policy_month)
            for wage_bin in bins:
                baseline = 140 - 12 * abs(wage_bin - 13.0) + rng.normal(0.0, 5.5)
                shock = 0.0
                if post and wage_bin < floor:
                    shock -= 28 + 36 * bite
                if post and floor <= wage_bin <= floor + 1.0:
                    shock += 18 + 26 * bite
                avg_wage = wage_bin + 0.25 + 0.65 * post * (wage_bin <= floor + 0.5) + rng.normal(0.0, 0.08)
                jobs = max(8, int(round(baseline + shock + rng.normal(0.0, 4.2))))
                rows.append(
                    {
                        "region": region,
                        "month": month,
                        "policy_month": policy_month,
                        "post": post,
                        "median_wage": median,
                        "new_floor": floor,
                        "bite": bite,
                        "wage_bin": wage_bin,
                        "avg_wage": avg_wage,
                        "jobs": jobs,
                        "below_floor": int(wage_bin < floor),
                        "near_floor": int(floor <= wage_bin <= floor + 1.0),
                    }
                )
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    grouped = (
        df.groupby(["post", "below_floor", "near_floor"], as_index=False)
        .agg(
            mean_jobs=("jobs", "mean"),
            mean_avg_wage=("avg_wage", "mean"),
            mean_bite=("bite", "mean"),
        )
    )

    below_pre = df[(df["post"] == 0) & (df["below_floor"] == 1)]["jobs"].mean()
    below_post = df[(df["post"] == 1) & (df["below_floor"] == 1)]["jobs"].mean()
    near_pre = df[(df["post"] == 0) & (df["near_floor"] == 1)]["jobs"].mean()
    near_post = df[(df["post"] == 1) & (df["near_floor"] == 1)]["jobs"].mean()
    summary = pd.DataFrame(
        [
            {"metric": "rows", "value": len(df)},
            {"metric": "mean_bite", "value": df["bite"].mean()},
            {"metric": "below_floor_job_change", "value": below_post - below_pre},
            {"metric": "near_floor_job_change", "value": near_post - near_pre},
            {"metric": "mean_avg_wage_change_post", "value": df[df["post"] == 1]["avg_wage"].mean() - df[df["post"] == 0]["avg_wage"].mean()},
        ]
    )

    bins = (
        df.groupby(["post", "wage_bin"], as_index=False)
        .agg(mean_jobs=("jobs", "mean"), mean_avg_wage=("avg_wage", "mean"))
        .assign(period=lambda x: np.where(x["post"] == 1, "Post", "Pre"))
        .drop(columns="post")
    )
    return summary, grouped, bins


def make_figure(bin_df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    for period, color in [("Pre", "#3B6EA8"), ("Post", "#B55D4C")]:
        sub = bin_df[bin_df["period"] == period]
        axes[0].plot(sub["wage_bin"], sub["mean_jobs"], marker="o", linewidth=2.3, color=color, label=period)
        axes[1].plot(sub["wage_bin"], sub["mean_avg_wage"], marker="o", linewidth=2.3, color=color, label=period)

    axes[0].set_title("Jobs by wage bin")
    axes[0].set_xlabel("Wage bin midpoint")
    axes[0].set_ylabel("Mean jobs")
    axes[0].grid(alpha=0.2)
    axes[0].legend(fontsize=9)

    axes[1].set_title("Average wage by bin")
    axes[1].set_xlabel("Wage bin midpoint")
    axes[1].set_ylabel("Observed wage")
    axes[1].grid(alpha=0.2)
    axes[1].legend(fontsize=9)

    fig.suptitle("Synthetic Cengiz-style grouped panel: low-wage jobs shift upward around the new floor")
    fig.tight_layout()
    fig.savefig(outpath, dpi=220)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    df = build_grouped_panel()
    summary, grouped, bins = summarize(df)

    df.to_csv(args.outdir / "cengiz_low_wage_panel.csv", index=False)
    summary.to_csv(args.outdir / "cengiz_low_wage_summary.csv", index=False)
    grouped.to_csv(args.outdir / "cengiz_low_wage_grouped_summary.csv", index=False)
    bins.to_csv(args.outdir / "cengiz_low_wage_bins.csv", index=False)
    make_figure(bins, args.outdir / "cengiz_low_wage_bins.png")

    print(f"Wrote Week 7 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
