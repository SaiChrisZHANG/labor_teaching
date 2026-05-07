#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "output" / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / "output" / ".cache"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_exposure_panel(firm_panel: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        firm_panel.groupby(["market", "occupation_group"], as_index=False)
        .agg(
            adoption_share=("adopted", "mean"),
            ai_intensity=("ai_intensity", "mean"),
            vacancy_ai_skill_share=("vacancy_ai_skill_share", "mean"),
            routine_share=("routine_share", "mean"),
            employment_growth=("employment_growth", "mean"),
            wagebill_growth=("wagebill_growth", "mean"),
        )
    )

    market_effect = grouped["market"].str.extract(r"(\d+)").astype(int)[0] / 100.0
    occupation_effect = grouped["occupation_group"].str.extract(r"(\d+)").astype(int)[0] / 90.0
    grouped["baseline_ai_exposure"] = np.clip(
        0.35 * grouped["routine_share"]
        + 0.30 * grouped["vacancy_ai_skill_share"]
        + 0.20 * grouped["ai_intensity"]
        + market_effect
        + occupation_effect,
        0.02,
        1.20,
    )
    grouped["alternative_routine_exposure"] = np.clip(
        0.70 * grouped["routine_share"] + 0.10 * grouped["vacancy_ai_skill_share"] + market_effect,
        0.02,
        1.20,
    )
    grouped["wage_growth"] = grouped["wagebill_growth"] - 0.18 * grouped["routine_share"]
    grouped["employment_change"] = grouped["employment_growth"]
    return grouped.round(4)


def build_summary(panel: pd.DataFrame) -> pd.DataFrame:
    bins = pd.qcut(panel["baseline_ai_exposure"], q=3, labels=["low", "middle", "high"])
    out = (
        panel.assign(exposure_bucket=bins)
        .groupby("exposure_bucket", as_index=False, observed=False)[
            [
                "baseline_ai_exposure",
                "adoption_share",
                "employment_change",
                "wage_growth",
                "vacancy_ai_skill_share",
            ]
        ]
        .mean()
        .round(4)
    )
    return out


def build_alt_results(panel: pd.DataFrame) -> pd.DataFrame:
    result = panel[
        [
            "market",
            "occupation_group",
            "baseline_ai_exposure",
            "alternative_routine_exposure",
            "adoption_share",
            "employment_change",
            "wage_growth",
        ]
    ].copy()
    result["baseline_minus_alternative"] = (
        result["baseline_ai_exposure"] - result["alternative_routine_exposure"]
    ).round(4)
    return result.round(4)


def build_robot_challenge(panel: pd.DataFrame) -> pd.DataFrame:
    zones = [f"cz-{idx}" for idx in range(1, 9)]
    years = np.arange(2015, 2021)
    rows: list[dict[str, float | str | int]] = []
    for z_idx, zone in enumerate(zones, start=1):
        base = panel.iloc[(z_idx - 1) % len(panel)]
        for year in years:
            robot_exposure = float(
                np.clip(0.10 + 0.08 * z_idx + 0.015 * (year - 2015) + 0.45 * base["routine_share"], 0.05, 1.4)
            )
            employment_change = 0.018 - 0.022 * robot_exposure + 0.002 * (year - 2015)
            wage_change = 0.012 - 0.010 * robot_exposure + 0.0015 * (year - 2015)
            rows.append(
                {
                    "commuting_zone": zone,
                    "year": year,
                    "robot_exposure": round(robot_exposure, 4),
                    "employment_change": round(employment_change, 4),
                    "wage_change": round(wage_change, 4),
                }
            )
    return pd.DataFrame(rows)


def plot_outputs(panel: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    axes[0].scatter(
        panel["baseline_ai_exposure"],
        panel["employment_change"],
        color="#4c78a8",
        alpha=0.85,
    )
    axes[0].set_title("Exposure versus employment change")
    axes[0].set_xlabel("Baseline AI exposure")
    axes[0].set_ylabel("Employment change")

    axes[1].scatter(
        panel["adoption_share"],
        panel["wage_growth"],
        color="#e45756",
        alpha=0.85,
    )
    axes[1].set_title("Adoption versus wage growth")
    axes[1].set_xlabel("Adoption share")
    axes[1].set_ylabel("Wage growth")

    fig.tight_layout()
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reproduced", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    firm_panel = pd.read_csv(args.reproduced)
    exposure_panel = build_exposure_panel(firm_panel)
    exposure_summary = build_summary(exposure_panel)
    alt_results = build_alt_results(exposure_panel)
    robot_challenge = build_robot_challenge(exposure_panel)

    exposure_panel.to_csv(args.outdir / "exposure_vs_adoption_panel.csv", index=False)
    exposure_summary.to_csv(args.outdir / "exposure_vs_adoption_summary.csv", index=False)
    alt_results.to_csv(args.outdir / "alternative_exposure_results.csv", index=False)
    robot_challenge.to_csv(args.outdir / "robot_market_challenge.csv", index=False)
    plot_outputs(exposure_panel, args.outdir / "exposure_vs_adoption.png")


if __name__ == "__main__":
    main()
