#!/usr/bin/env python3
"""Synthetic Week 9 reproduction anchored to Almeida and Carneiro (2012)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_panel(seed: int = 20260509) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    localities = {
        "Metro North": {"base_inspection": 0.58, "wage_rigidity": 0.18, "base_formal": 0.69},
        "Industrial Belt": {"base_inspection": 0.64, "wage_rigidity": 0.15, "base_formal": 0.73},
        "Interior Services": {"base_inspection": 0.46, "wage_rigidity": 0.21, "base_formal": 0.61},
        "Coastal Trade": {"base_inspection": 0.51, "wage_rigidity": 0.19, "base_formal": 0.66},
        "Agrarian South": {"base_inspection": 0.34, "wage_rigidity": 0.24, "base_formal": 0.54},
        "Frontier West": {"base_inspection": 0.29, "wage_rigidity": 0.27, "base_formal": 0.48},
    }

    rows = []
    for locality, params in localities.items():
        for year in range(2006, 2025):
            t = year - 2006
            inspection_rate = np.clip(
                params["base_inspection"] + 0.006 * np.sin(t / 2.0) + rng.normal(0.0, 0.02),
                0.16,
                0.88,
            )
            compliance_index = np.clip(0.28 + 0.76 * inspection_rate + rng.normal(0.0, 0.04), 0.15, 0.97)
            mandated_benefit_value = np.clip(0.09 + 0.22 * compliance_index + rng.normal(0.0, 0.015), 0.05, 0.34)
            formal_wage_index = 1.02 - 0.19 * inspection_rate + 0.08 * mandated_benefit_value + rng.normal(0.0, 0.03)
            low_wage_formalization_gain = (
                0.04 + 0.18 * compliance_index + 0.12 * params["wage_rigidity"] + rng.normal(0.0, 0.015)
            )
            formal_share = np.clip(
                params["base_formal"] + 0.16 * compliance_index - 0.05 * inspection_rate + 0.10 * params["wage_rigidity"]
                + rng.normal(0.0, 0.02),
                0.35,
                0.92,
            )
            informal_share = 1.0 - formal_share
            rows.append(
                {
                    "locality": locality,
                    "year": year,
                    "inspection_rate": inspection_rate,
                    "compliance_index": compliance_index,
                    "mandated_benefit_value": mandated_benefit_value,
                    "formal_wage_index": formal_wage_index,
                    "formal_share": formal_share,
                    "informal_share": informal_share,
                    "low_wage_formalization_gain": low_wage_formalization_gain,
                    "wage_rigidity_index": params["wage_rigidity"],
                }
            )
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary = pd.DataFrame(
        [
            {"metric": "mean_inspection_rate", "value": df["inspection_rate"].mean()},
            {"metric": "mean_compliance_index", "value": df["compliance_index"].mean()},
            {"metric": "mean_formal_share", "value": df["formal_share"].mean()},
            {"metric": "mean_formal_wage_index", "value": df["formal_wage_index"].mean()},
            {
                "metric": "corr_inspection_formal_share",
                "value": df[["inspection_rate", "formal_share"]].corr().iloc[0, 1],
            },
            {
                "metric": "corr_inspection_formal_wage_index",
                "value": df[["inspection_rate", "formal_wage_index"]].corr().iloc[0, 1],
            },
        ]
    )

    tiered = (
        df.assign(
            enforcement_tier=pd.qcut(
                df["inspection_rate"],
                q=3,
                labels=["lower enforcement", "middle enforcement", "higher enforcement"],
            )
        )
        .groupby("enforcement_tier", observed=False)
        .agg(
            mean_inspection_rate=("inspection_rate", "mean"),
            mean_compliance_index=("compliance_index", "mean"),
            mean_formal_share=("formal_share", "mean"),
            mean_formal_wage_index=("formal_wage_index", "mean"),
            mean_low_wage_formalization_gain=("low_wage_formalization_gain", "mean"),
        )
        .reset_index()
    )
    return summary, tiered


def make_figure(df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9))

    grouped = (
        df.groupby("locality", as_index=False)
        .agg(
            inspection_rate=("inspection_rate", "mean"),
            compliance_index=("compliance_index", "mean"),
            formal_share=("formal_share", "mean"),
            formal_wage_index=("formal_wage_index", "mean"),
        )
    )
    scatter = axes[0].scatter(
        grouped["inspection_rate"],
        grouped["formal_share"],
        s=180,
        c=grouped["compliance_index"],
        cmap="YlGnBu",
        edgecolor="#35536B",
        linewidth=0.8,
    )
    for _, row in grouped.iterrows():
        axes[0].annotate(row["locality"], (row["inspection_rate"], row["formal_share"]), xytext=(4, 4), textcoords="offset points", fontsize=8)
    axes[0].set_title("Inspection intensity and formality")
    axes[0].set_xlabel("Inspection rate")
    axes[0].set_ylabel("Formal employment share")
    axes[0].grid(alpha=0.2)
    cbar = fig.colorbar(scatter, ax=axes[0], shrink=0.86)
    cbar.set_label("Compliance index")

    tiered = (
        df.assign(
            enforcement_tier=pd.qcut(
                df["inspection_rate"],
                q=3,
                labels=["Lower enforcement", "Middle enforcement", "Higher enforcement"],
            )
        )
        .groupby("enforcement_tier", observed=False)
        .agg(
            low_wage_formalization_gain=("low_wage_formalization_gain", "mean"),
            formal_wage_index=("formal_wage_index", "mean"),
        )
        .reset_index()
    )
    x = np.arange(len(tiered))
    axes[1].bar(x - 0.17, tiered["low_wage_formalization_gain"], width=0.34, color="#4E9A8E", label="Low-wage formalization gain")
    axes[1].bar(x + 0.17, tiered["formal_wage_index"], width=0.34, color="#C79A35", label="Formal wage index")
    axes[1].set_xticks(x, tiered["enforcement_tier"], rotation=8)
    axes[1].set_title("Adjustment across enforcement tiers")
    axes[1].set_ylabel("Synthetic index / share")
    axes[1].grid(axis="y", alpha=0.2)
    axes[1].legend(fontsize=8.5, loc="upper left")

    fig.suptitle("Synthetic Week 9 reproduction: enforcement, compliance, and formality")
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

    df = build_panel()
    summary, tiered = summarize(df)

    df.to_csv(args.outdir / "almeida_enforcement_panel.csv", index=False)
    summary.to_csv(args.outdir / "almeida_enforcement_summary.csv", index=False)
    tiered.to_csv(args.outdir / "almeida_enforcement_by_enforcement_tier.csv", index=False)
    make_figure(df, args.outdir / "almeida_enforcement_framework.png")

    print(f"Wrote Week 9 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
