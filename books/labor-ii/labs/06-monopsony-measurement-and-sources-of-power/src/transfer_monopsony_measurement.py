#!/usr/bin/env python3
"""Synthetic Week 6 transfer comparing markdown and merger objects."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_plant_panel(seed: int = 20260506) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    markets = ["North", "South", "Metro", "Rural"]
    for market in markets:
        concentration_level = {"North": 0.18, "South": 0.26, "Metro": 0.14, "Rural": 0.34}[market]
        for plant in range(1, 31):
            for year in range(1, 6):
                mrpl = rng.normal(42 + 3 * year, 3.2)
                markdown = 1.08 + 0.55 * concentration_level + rng.normal(0.0, 0.05)
                wage = mrpl / markdown
                rows.append(
                    {
                        "market": market,
                        "plant_id": f"{market[:2]}-{plant:02d}",
                        "year": 2018 + year,
                        "concentration": concentration_level + rng.normal(0.0, 0.015),
                        "mrpl": mrpl,
                        "wage": wage,
                        "markdown": mrpl / wage,
                    }
                )
    return pd.DataFrame(rows)


def build_merger_panel(seed: int = 20260507) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    treated_markets = {"RuralCare", "NorthMed"}
    rows = []
    for market in ["RuralCare", "NorthMed", "MetroHealth", "SouthGeneral"]:
        base_wage = rng.uniform(24, 32)
        for rel_year in range(-2, 3):
            treated = int(market in treated_markets)
            post = int(rel_year >= 0)
            delta = -1.15 * treated * post + rng.normal(0.0, 0.18)
            rows.append(
                {
                    "market": market,
                    "relative_year": rel_year,
                    "treated": treated,
                    "post": post,
                    "wage": base_wage + 0.35 * rel_year + delta,
                    "concentration": 0.22 + 0.07 * treated + 0.08 * treated * post + rng.normal(0.0, 0.01),
                }
            )
    return pd.DataFrame(rows)


def summarize(plant_df: pd.DataFrame, merger_df: pd.DataFrame) -> pd.DataFrame:
    plant_summary = plant_df.groupby("market", as_index=False).agg(
        mean_concentration=("concentration", "mean"),
        mean_markdown=("markdown", "mean"),
        mean_wage=("wage", "mean"),
    )
    treated = merger_df[(merger_df["treated"] == 1) & (merger_df["post"] == 1)]["wage"].mean()
    treated_pre = merger_df[(merger_df["treated"] == 1) & (merger_df["post"] == 0)]["wage"].mean()
    control = merger_df[(merger_df["treated"] == 0) & (merger_df["post"] == 1)]["wage"].mean()
    control_pre = merger_df[(merger_df["treated"] == 0) & (merger_df["post"] == 0)]["wage"].mean()
    did = (treated - treated_pre) - (control - control_pre)

    summary_rows = [
        {"object": "plant_panel_mean_markdown", "value": plant_df["markdown"].mean()},
        {"object": "corr_markdown_concentration", "value": plant_df[["markdown", "concentration"]].corr().iloc[0, 1]},
        {"object": "merger_diff_in_diff_wage_effect", "value": did},
        {"object": "treated_post_mean_concentration", "value": merger_df[(merger_df["treated"] == 1) & (merger_df["post"] == 1)]["concentration"].mean()},
    ]
    summary = pd.DataFrame(summary_rows)
    return plant_summary, summary


def make_figure(plant_df: pd.DataFrame, merger_df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    axes[0].scatter(plant_df["concentration"], plant_df["markdown"], s=28, alpha=0.65, color="#3B6EA8", edgecolors="none")
    slope, intercept = np.polyfit(plant_df["concentration"], plant_df["markdown"], deg=1)
    xgrid = np.linspace(plant_df["concentration"].min(), plant_df["concentration"].max(), 100)
    axes[0].plot(xgrid, intercept + slope * xgrid, linewidth=2.5, color="#B55D4C")
    axes[0].set_title("Synthetic markdown panel")
    axes[0].set_xlabel("Concentration proxy")
    axes[0].set_ylabel("Markdown (MRPL / wage)")
    axes[0].grid(alpha=0.2)

    grouped = merger_df.groupby(["treated", "relative_year"], as_index=False)["wage"].mean()
    for treated, label, color in [(1, "Treated markets", "#4E9A8E"), (0, "Control markets", "#C79A35")]:
        sub = grouped[grouped["treated"] == treated]
        axes[1].plot(sub["relative_year"], sub["wage"], marker="o", linewidth=2.4, color=color, label=label)
    axes[1].axvline(0, color="#9AA4AF", linestyle=":", linewidth=1.2)
    axes[1].set_title("Synthetic merger event study")
    axes[1].set_xlabel("Years relative to merger")
    axes[1].set_ylabel("Average wage")
    axes[1].grid(alpha=0.2)
    axes[1].legend(fontsize=9)

    fig.suptitle("Transfer comparison: markdown measurement versus merger-based wage effects")
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

    plant_df = build_plant_panel()
    merger_df = build_merger_panel()
    plant_summary, summary = summarize(plant_df, merger_df)

    plant_df.to_csv(args.outdir / "synthetic_markdown_panel.csv", index=False)
    merger_df.to_csv(args.outdir / "synthetic_merger_panel.csv", index=False)
    plant_summary.to_csv(args.outdir / "monopsony_transfer_by_market.csv", index=False)
    summary.to_csv(args.outdir / "monopsony_transfer_summary.csv", index=False)
    make_figure(plant_df, merger_df, args.outdir / "monopsony_transfer_comparison.png")

    print(f"Wrote Week 6 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
