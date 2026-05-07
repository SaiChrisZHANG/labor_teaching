#!/usr/bin/env python3
"""Synthetic Week 8 reproduction anchored to Farber et al. (2021)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_state_panel(seed: int = 20260508) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    states = {
        "Midwest": {"coverage_1984": 0.37, "membership_gap": 0.05, "trend": -0.0050},
        "Northeast": {"coverage_1984": 0.34, "membership_gap": 0.04, "trend": -0.0036},
        "South": {"coverage_1984": 0.24, "membership_gap": 0.03, "trend": -0.0028},
        "Pacific": {"coverage_1984": 0.29, "membership_gap": 0.04, "trend": -0.0026},
        "Mountain": {"coverage_1984": 0.19, "membership_gap": 0.03, "trend": -0.0020},
    }

    rows = []
    for state, params in states.items():
        for year in range(1984, 2025):
            t = year - 1984
            coverage = max(0.065, params["coverage_1984"] + params["trend"] * t + rng.normal(0.0, 0.007))
            membership = max(0.04, coverage - params["membership_gap"] + rng.normal(0.0, 0.005))
            direct_compression = 0.28 + 18.5 * coverage + rng.normal(0.0, 0.08)
            spillover_compression = 0.12 + 7.5 * coverage + rng.normal(0.0, 0.06)
            no_union_gap = 1.58 + 0.017 * t + rng.normal(0.0, 0.03)
            observed_gap = no_union_gap - direct_compression / 10.0 - spillover_compression / 10.0
            rows.append(
                {
                    "state": state,
                    "year": year,
                    "membership_rate": membership,
                    "coverage_rate": coverage,
                    "covered_nonmember_rate": coverage - membership,
                    "direct_compression_points": direct_compression,
                    "spillover_compression_points": spillover_compression,
                    "p90_p10_gap_no_union_counterfactual": no_union_gap,
                    "p90_p10_gap_observed": observed_gap,
                }
            )
    df = pd.DataFrame(rows)
    df["union_presence_rate"] = 0.6 * df["membership_rate"] + 0.4 * df["coverage_rate"]
    return df


def add_era_labels(df: pd.DataFrame) -> pd.DataFrame:
    era_bins = [1983, 1991, 2001, 2012, 2025]
    era_labels = ["1984-1991", "1992-2001", "2002-2012", "2013-2024"]
    return df.assign(era=pd.cut(df["year"], bins=era_bins, labels=era_labels))


def summarize(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary = pd.DataFrame(
        [
            {"metric": "mean_membership_rate", "value": df["membership_rate"].mean()},
            {"metric": "mean_coverage_rate", "value": df["coverage_rate"].mean()},
            {"metric": "mean_covered_nonmember_rate", "value": df["covered_nonmember_rate"].mean()},
            {"metric": "mean_direct_compression_points", "value": df["direct_compression_points"].mean()},
            {"metric": "mean_spillover_compression_points", "value": df["spillover_compression_points"].mean()},
            {"metric": "mean_observed_p90_p10_gap", "value": df["p90_p10_gap_observed"].mean()},
            {
                "metric": "share_of_total_compression_from_spillovers",
                "value": df["spillover_compression_points"].sum()
                / (df["direct_compression_points"].sum() + df["spillover_compression_points"].sum()),
            },
        ]
    )

    era_summary = (
        add_era_labels(df)
        .groupby("era", observed=False)
        .agg(
            mean_membership_rate=("membership_rate", "mean"),
            mean_coverage_rate=("coverage_rate", "mean"),
            mean_direct_compression_points=("direct_compression_points", "mean"),
            mean_spillover_compression_points=("spillover_compression_points", "mean"),
            mean_p90_p10_gap_observed=("p90_p10_gap_observed", "mean"),
            mean_p90_p10_gap_no_union_counterfactual=("p90_p10_gap_no_union_counterfactual", "mean"),
        )
        .reset_index()
    )
    return summary, era_summary


def make_figure(df: pd.DataFrame, outpath: Path) -> None:
    national = (
        df.groupby("year", as_index=False)
        .agg(
            membership_rate=("membership_rate", "mean"),
            coverage_rate=("coverage_rate", "mean"),
            direct_compression_points=("direct_compression_points", "mean"),
            spillover_compression_points=("spillover_compression_points", "mean"),
            observed_gap=("p90_p10_gap_observed", "mean"),
            counterfactual_gap=("p90_p10_gap_no_union_counterfactual", "mean"),
        )
    )

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))

    axes[0].plot(national["year"], national["membership_rate"], linewidth=2.5, color="#3B6EA8", label="Membership")
    axes[0].plot(national["year"], national["coverage_rate"], linewidth=2.5, color="#4E9A8E", label="Coverage")
    axes[0].fill_between(
        national["year"],
        national["membership_rate"],
        national["coverage_rate"],
        color="#F0C36B",
        alpha=0.35,
        label="Covered nonmembers",
    )
    axes[0].set_title("Membership versus coverage")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Share of workers")
    axes[0].grid(alpha=0.2)
    axes[0].legend(fontsize=8.5, loc="upper right")

    axes[1].plot(national["year"], national["counterfactual_gap"], linewidth=2.5, color="#B55D4C", label="No-union counterfactual")
    axes[1].plot(national["year"], national["observed_gap"], linewidth=2.5, color="#5C7A29", label="Observed 90/10 gap")
    axes[1].fill_between(
        national["year"],
        national["observed_gap"],
        national["observed_gap"] + national["direct_compression_points"] / 10.0,
        color="#8FB7D6",
        alpha=0.35,
        label="Direct compression",
    )
    axes[1].fill_between(
        national["year"],
        national["observed_gap"] + national["direct_compression_points"] / 10.0,
        national["counterfactual_gap"],
        color="#E8D19A",
        alpha=0.45,
        label="Spillover compression",
    )
    axes[1].set_title("Synthetic inequality decomposition")
    axes[1].set_xlabel("Year")
    axes[1].set_ylabel("90/10 wage gap")
    axes[1].grid(alpha=0.2)
    axes[1].legend(fontsize=8.0, loc="upper left")

    fig.suptitle("Synthetic Week 8 reproduction: coverage, direct compression, and spillovers")
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

    df = build_state_panel()
    summary, era_summary = summarize(df)

    df.to_csv(args.outdir / "farber_union_inequality_panel.csv", index=False)
    summary.to_csv(args.outdir / "farber_union_inequality_summary.csv", index=False)
    era_summary.to_csv(args.outdir / "farber_union_inequality_by_era.csv", index=False)
    make_figure(df, args.outdir / "farber_union_inequality_decomposition.png")

    print(f"Wrote Week 8 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
