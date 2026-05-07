#!/usr/bin/env python3
"""Bounded Week 5 reproduction path inspired by Lachowska et al. (2022)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd


def slope(x: pd.Series, y: pd.Series) -> float:
    centered_x = x - x.mean()
    denom = (centered_x**2).sum()
    if denom == 0:
        return 0.0
    return float((centered_x * (y - y.mean())).sum() / denom)


def build_outputs(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    work = df.copy().sort_values("secondary_wage_shock")
    work["shock_bin"] = pd.qcut(work["secondary_wage_shock"], q=4, labels=["low", "mid-low", "mid-high", "high"])

    by_bin = (
        work.groupby("shock_bin", as_index=False, observed=False)
        .agg(
            secondary_wage_shock=("secondary_wage_shock", "mean"),
            primary_wage_change=("primary_wage_change", "mean"),
            separation=("separation", "mean"),
        )
    )
    by_bin["primary_pass_through"] = by_bin["primary_wage_change"] / by_bin["secondary_wage_shock"].where(by_bin["secondary_wage_shock"] != 0, 1)

    wage_pass_through = slope(work["secondary_wage_shock"], work["primary_wage_change"])
    separation_gradient = slope(work["secondary_wage_shock"], work["separation"])

    summary = pd.DataFrame(
        [
            {"metric": "mean_secondary_wage_shock", "value": work["secondary_wage_shock"].mean()},
            {"metric": "mean_primary_wage_change", "value": work["primary_wage_change"].mean()},
            {"metric": "mean_separation_rate", "value": work["separation"].mean()},
            {"metric": "wage_pass_through_slope", "value": wage_pass_through},
            {"metric": "separation_gradient", "value": separation_gradient},
            {
                "metric": "protocol_signal",
                "value": "posting-leaning" if abs(separation_gradient) > abs(wage_pass_through) else "bargaining-leaning",
            },
        ]
    )

    by_bin.to_csv(outdir / "lachowska_wage_setting_by_bin.csv", index=False)
    summary.to_csv(outdir / "lachowska_wage_setting_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    axes[0].plot(
        by_bin["secondary_wage_shock"],
        by_bin["primary_wage_change"],
        marker="o",
        linewidth=2.4,
        color="#3B6EA8",
    )
    axes[0].axhline(0.0, color="#9AA4AF", linestyle=":", linewidth=1.1)
    axes[0].axvline(0.0, color="#9AA4AF", linestyle=":", linewidth=1.1)
    axes[0].set_title("Incumbent wage response")
    axes[0].set_xlabel("Secondary-job wage shock")
    axes[0].set_ylabel("Primary-job wage change")

    axes[1].plot(
        by_bin["secondary_wage_shock"],
        by_bin["separation"],
        marker="o",
        linewidth=2.4,
        color="#B55D4C",
    )
    axes[1].axhline(work["separation"].mean(), color="#9AA4AF", linestyle=":", linewidth=1.1)
    axes[1].set_title("Incumbent separation response")
    axes[1].set_xlabel("Secondary-job wage shock")
    axes[1].set_ylabel("Primary-job separation rate")

    fig.suptitle("Bounded Week 5 dual-jobholder tradeoff: wage response versus turnover response")
    fig.tight_layout()
    fig.savefig(outdir / "lachowska_wage_setting_tradeoff.png", dpi=220)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    build_outputs(df, args.outdir)
    print(f"Saved bounded Lachowska-style outputs to {args.outdir}")


if __name__ == "__main__":
    main()
