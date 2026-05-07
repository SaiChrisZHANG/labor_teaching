#!/usr/bin/env python3
"""Synthetic Week 9 transfer comparing UI spillovers and uncovered margins."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_ui_market_panel(seed: int = 20260510) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    regions = {
        "treated-north": {"treated": 1, "base_duration": 22},
        "treated-west": {"treated": 1, "base_duration": 23},
        "control-east": {"treated": 0, "base_duration": 20},
        "control-south": {"treated": 0, "base_duration": 19},
    }

    rows = []
    for region, params in regions.items():
        for year in range(2010, 2025):
            post = int(year >= 2017)
            benefit_duration = params["base_duration"] + 6 * params["treated"] * post
            eligible_jobfinding = 0.47 - 0.010 * benefit_duration + rng.normal(0.0, 0.01)
            noneligible_jobfinding = 0.44 + 0.004 * params["treated"] * post + rng.normal(0.0, 0.01)
            vacancy_rate = 0.032 + 0.001 * params["treated"] * post + rng.normal(0.0, 0.0015)
            rows.append(
                {
                    "region": region,
                    "year": year,
                    "treated_region": params["treated"],
                    "post_period": post,
                    "benefit_duration_weeks": benefit_duration,
                    "eligible_jobfinding_rate": max(0.18, eligible_jobfinding),
                    "noneligible_jobfinding_rate": max(0.18, noneligible_jobfinding),
                    "vacancy_rate": max(0.005, vacancy_rate),
                }
            )
    return pd.DataFrame(rows)


def build_ui_informality_panel(seed: int = 20260511) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    municipalities = ["Capital", "Industrial", "Logistics", "Services", "Periphery"]
    rows = []
    for municipality in municipalities:
        base_informality = {
            "Capital": 0.19,
            "Industrial": 0.24,
            "Logistics": 0.27,
            "Services": 0.31,
            "Periphery": 0.38,
        }[municipality]
        for spell in range(1, 81):
            eligible = int(spell % 2 == 0)
            formal_layoff_rate = 0.082 + 0.013 * eligible + 0.035 * base_informality + rng.normal(0.0, 0.006)
            informal_transition_share = 0.21 + 0.07 * eligible + 0.42 * base_informality + rng.normal(0.0, 0.02)
            recall_rate = 0.28 + 0.04 * eligible - 0.06 * base_informality + rng.normal(0.0, 0.015)
            rows.append(
                {
                    "municipality": municipality,
                    "spell_id": f"{municipality[:3]}-{spell:03d}",
                    "ui_eligible": eligible,
                    "baseline_informality": base_informality,
                    "formal_layoff_rate": max(0.01, formal_layoff_rate),
                    "informal_transition_share": min(0.95, max(0.05, informal_transition_share)),
                    "recall_rate": min(0.92, max(0.05, recall_rate)),
                }
            )
    return pd.DataFrame(rows)


def summarize(ui_df: pd.DataFrame, informal_df: pd.DataFrame) -> pd.DataFrame:
    ui_post = ui_df[(ui_df["treated_region"] == 1) & (ui_df["post_period"] == 1)]
    ui_pre = ui_df[(ui_df["treated_region"] == 1) & (ui_df["post_period"] == 0)]

    summary = pd.DataFrame(
        [
            {
                "object": "eligible_jobfinding_change_treated_regions",
                "value": ui_post["eligible_jobfinding_rate"].mean() - ui_pre["eligible_jobfinding_rate"].mean(),
            },
            {
                "object": "noneligible_jobfinding_change_treated_regions",
                "value": ui_post["noneligible_jobfinding_rate"].mean() - ui_pre["noneligible_jobfinding_rate"].mean(),
            },
            {
                "object": "vacancy_rate_change_treated_regions",
                "value": ui_post["vacancy_rate"].mean() - ui_pre["vacancy_rate"].mean(),
            },
            {
                "object": "formal_layoff_gap_eligible_minus_ineligible",
                "value": informal_df.loc[informal_df["ui_eligible"] == 1, "formal_layoff_rate"].mean()
                - informal_df.loc[informal_df["ui_eligible"] == 0, "formal_layoff_rate"].mean(),
            },
            {
                "object": "informal_transition_gap_eligible_minus_ineligible",
                "value": informal_df.loc[informal_df["ui_eligible"] == 1, "informal_transition_share"].mean()
                - informal_df.loc[informal_df["ui_eligible"] == 0, "informal_transition_share"].mean(),
            },
        ]
    )
    return summary


def make_figure(ui_df: pd.DataFrame, informal_df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9))

    grouped = ui_df.groupby(["year", "treated_region"], as_index=False).agg(
        eligible_jobfinding_rate=("eligible_jobfinding_rate", "mean"),
        noneligible_jobfinding_rate=("noneligible_jobfinding_rate", "mean"),
    )
    treated = grouped[grouped["treated_region"] == 1]
    control = grouped[grouped["treated_region"] == 0]
    axes[0].plot(treated["year"], treated["eligible_jobfinding_rate"], color="#B55D4C", linewidth=2.5, label="Eligible, treated regions")
    axes[0].plot(treated["year"], treated["noneligible_jobfinding_rate"], color="#4E9A8E", linewidth=2.5, label="Noneligible, treated regions")
    axes[0].plot(control["year"], control["eligible_jobfinding_rate"], color="#B55D4C", linestyle="--", linewidth=1.8, label="Eligible, control regions")
    axes[0].axvline(2017, color="#77838F", linestyle=":", linewidth=1.2)
    axes[0].set_title("Equilibrium UI spillover object")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Job-finding rate")
    axes[0].grid(alpha=0.2)
    axes[0].legend(fontsize=7.8, loc="lower left")

    binned = (
        informal_df.assign(informality_bucket=pd.qcut(informal_df["baseline_informality"], q=3, labels=["Low", "Middle", "High"]))
        .groupby(["informality_bucket", "ui_eligible"], observed=False)
        .agg(
            formal_layoff_rate=("formal_layoff_rate", "mean"),
            informal_transition_share=("informal_transition_share", "mean"),
        )
        .reset_index()
    )
    for eligible, color in [(0, "#8FB7D6"), (1, "#C79A35")]:
        subset = binned[binned["ui_eligible"] == eligible]
        axes[1].plot(
            subset["informality_bucket"],
            subset["informal_transition_share"],
            marker="o",
            linewidth=2.3,
            color=color,
            label=f"Eligible={eligible}",
        )
    axes[1].set_title("Covered UI with an uncovered informal margin")
    axes[1].set_xlabel("Baseline informality bucket")
    axes[1].set_ylabel("Informal transition share")
    axes[1].grid(alpha=0.2)
    axes[1].legend(fontsize=8.5, loc="upper left")

    fig.suptitle("Synthetic Week 9 transfer: equilibrium UI and informal-margin adjustment")
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

    ui_df = build_ui_market_panel()
    informal_df = build_ui_informality_panel()
    summary = summarize(ui_df, informal_df)

    ui_df.to_csv(args.outdir / "synthetic_ui_market_panel.csv", index=False)
    informal_df.to_csv(args.outdir / "synthetic_ui_informality_panel.csv", index=False)
    summary.to_csv(args.outdir / "regulation_transfer_summary.csv", index=False)
    make_figure(ui_df, informal_df, args.outdir / "regulation_transfer_designs.png")

    print(f"Wrote Week 9 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
