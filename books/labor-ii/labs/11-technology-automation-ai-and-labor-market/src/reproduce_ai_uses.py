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


def build_panel() -> pd.DataFrame:
    rng = np.random.default_rng(11)
    firms = np.arange(1, 121)
    quarters = pd.period_range("2021Q1", "2024Q4", freq="Q")
    use_types = np.array(["automation", "augmentation", "reorganization", "screening"])
    use_probs = np.array([0.26, 0.34, 0.22, 0.18])

    adoption_quarter = {firm: int(rng.integers(4, 13)) for firm in firms}
    ai_use = {firm: str(rng.choice(use_types, p=use_probs)) for firm in firms}
    market = {firm: f"market-{(firm - 1) % 8 + 1}" for firm in firms}
    occupation = {firm: f"occupation-{(firm - 1) % 6 + 1}" for firm in firms}
    sector = {firm: ["services", "manufacturing", "business-tech", "retail"][(firm - 1) % 4] for firm in firms}

    effect_map = {
        "automation": {"employment": -0.030, "vacancy": -0.012, "routine": -0.050, "wagebill": 0.004},
        "augmentation": {"employment": 0.028, "vacancy": 0.020, "routine": -0.010, "wagebill": 0.021},
        "reorganization": {"employment": 0.010, "vacancy": 0.015, "routine": -0.022, "wagebill": 0.014},
        "screening": {"employment": -0.004, "vacancy": 0.006, "routine": -0.015, "wagebill": 0.010},
    }

    rows: list[dict[str, float | int | str]] = []
    for firm in firms:
        base_employment = int(rng.integers(120, 420))
        base_wagebill = float(rng.uniform(2.4, 6.8))
        base_vacancy = float(rng.uniform(0.015, 0.065))
        base_routine = float(rng.uniform(0.28, 0.62))

        for q_idx, quarter in enumerate(quarters):
            adopted = int(q_idx >= adoption_quarter[firm])
            post = max(q_idx - adoption_quarter[firm] + 1, 0)
            use = ai_use[firm]
            intensity = adopted * min(0.25 + 0.09 * post + rng.normal(0.0, 0.03), 1.0)
            intensity = float(np.clip(intensity, 0.0, 1.0))
            effects = effect_map[use]

            time_trend = 0.004 * q_idx
            employment_growth = (
                0.006
                + time_trend
                + adopted * effects["employment"] * intensity
                + rng.normal(0.0, 0.010)
            )
            vacancy_growth = (
                0.004
                + 0.5 * time_trend
                + adopted * effects["vacancy"] * intensity
                + rng.normal(0.0, 0.008)
            )
            wagebill_growth = (
                0.009
                + 0.3 * time_trend
                + adopted * effects["wagebill"] * intensity
                + rng.normal(0.0, 0.008)
            )
            routine_share = (
                base_routine
                - 0.01 * q_idx
                + adopted * effects["routine"] * intensity
                + rng.normal(0.0, 0.015)
            )
            routine_share = float(np.clip(routine_share, 0.05, 0.85))

            employment = base_employment * (1.0 + employment_growth)
            wagebill = base_wagebill * (1.0 + wagebill_growth)
            vacancy_rate = base_vacancy * (1.0 + vacancy_growth)
            vacancy_ai_skill_share = float(
                np.clip(0.12 + 0.22 * intensity + rng.normal(0.0, 0.03), 0.02, 0.70)
            )

            rows.append(
                {
                    "firm_id": firm,
                    "quarter": str(quarter),
                    "quarter_index": q_idx,
                    "market": market[firm],
                    "occupation_group": occupation[firm],
                    "sector": sector[firm],
                    "ai_use_type": use,
                    "adoption_quarter_index": adoption_quarter[firm],
                    "adopted": adopted,
                    "ai_intensity": round(intensity, 4),
                    "employment": round(employment, 2),
                    "employment_growth": round(employment_growth, 4),
                    "vacancy_rate": round(vacancy_rate, 4),
                    "vacancy_growth": round(vacancy_growth, 4),
                    "routine_share": round(routine_share, 4),
                    "wagebill_millions": round(wagebill, 4),
                    "wagebill_growth": round(wagebill_growth, 4),
                    "vacancy_ai_skill_share": round(vacancy_ai_skill_share, 4),
                }
            )

    return pd.DataFrame(rows)


def build_summary(panel: pd.DataFrame) -> pd.DataFrame:
    return (
        panel.groupby("ai_use_type", sort=True)[
            [
                "employment_growth",
                "vacancy_growth",
                "routine_share",
                "wagebill_growth",
                "vacancy_ai_skill_share",
                "ai_intensity",
            ]
        ]
        .mean()
        .reset_index()
        .round(4)
    )


def build_effects(panel: pd.DataFrame) -> pd.DataFrame:
    grouped = panel.assign(post=panel["adopted"] == 1).groupby(["firm_id", "ai_use_type", "post"])[
        ["employment_growth", "vacancy_growth", "routine_share", "wagebill_growth"]
    ].mean()
    wide = grouped.unstack("post")
    wide.columns = [
        f"{metric}_{'post' if post else 'pre'}"
        for metric, post in wide.columns.to_flat_index()
    ]
    wide = wide.reset_index()
    for metric in ["employment_growth", "vacancy_growth", "routine_share", "wagebill_growth"]:
        wide[f"{metric}_post_minus_pre"] = wide[f"{metric}_post"] - wide[f"{metric}_pre"]
    return wide.round(4)


def plot_outputs(summary: pd.DataFrame, outpath: Path) -> None:
    summary = summary.sort_values("employment_growth")
    x = np.arange(len(summary))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    axes[0].bar(x, summary["employment_growth"], color="#4c78a8", alpha=0.9, label="Employment growth")
    axes[0].bar(x, summary["vacancy_growth"], color="#54a24b", alpha=0.8, label="Vacancy growth")
    axes[0].axhline(0.0, color="#2f2f2f", linewidth=1.0)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(summary["ai_use_type"], rotation=18)
    axes[0].set_title("Labor-demand responses by AI use")
    axes[0].set_ylabel("Average growth rate")
    axes[0].legend(frameon=False, fontsize=8)

    axes[1].scatter(
        summary["routine_share"],
        summary["wagebill_growth"],
        s=120,
        c=["#e45756", "#4c78a8", "#72b7b2", "#f58518"],
    )
    for _, row in summary.iterrows():
        axes[1].annotate(
            row["ai_use_type"],
            (row["routine_share"], row["wagebill_growth"]),
            textcoords="offset points",
            xytext=(4, 5),
            fontsize=8,
        )
    axes[1].set_title("Routine exposure versus wage-bill growth")
    axes[1].set_xlabel("Average routine-task share")
    axes[1].set_ylabel("Average wage-bill growth")

    fig.tight_layout()
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    panel = build_panel()
    summary = build_summary(panel)
    effects = build_effects(panel)

    panel.to_csv(args.outdir / "firm_ai_panel.csv", index=False)
    summary.to_csv(args.outdir / "ai_use_summary.csv", index=False)
    effects.to_csv(args.outdir / "ai_use_effects.csv", index=False)
    plot_outputs(summary, args.outdir / "ai_use_labor_demand.png")


if __name__ == "__main__":
    main()
