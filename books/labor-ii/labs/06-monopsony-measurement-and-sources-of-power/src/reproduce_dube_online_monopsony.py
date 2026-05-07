#!/usr/bin/env python3
"""Synthetic Week 6 reproduction anchored to Dube et al. (2020)."""
from __future__ import annotations

import argparse
import math
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_synthetic_panel(seed: int = 20260505) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    categories = ["data-tagging", "translation", "web-research", "image-labeling"]
    requesters = ["Aster", "Beacon", "Cobalt", "Delta", "Elm", "Foundry"]
    quality = {"data-tagging": 0.05, "translation": 0.16, "web-research": 0.09, "image-labeling": 0.02}

    rows = []
    posting_id = 0
    for category in categories:
        for requester in requesters:
            base_log_wage = math.log(rng.uniform(9.5, 16.0))
            for week in range(1, 21):
                posting_id += 1
                wage_shock = rng.normal(0.0, 0.14)
                log_wage = base_log_wage + wage_shock
                wage = math.exp(log_wage)
                latent = 1.25 + 1.45 * log_wage + quality[category] + rng.normal(0.0, 0.16)
                applicants = max(3, int(round(math.exp(latent))))
                fill_prob = min(0.985, max(0.12, 0.36 + 0.11 * log_wage + 0.08 * quality[category] + rng.normal(0.0, 0.05)))
                filled = int(rng.random() < fill_prob)
                rows.append(
                    {
                        "posting_id": posting_id,
                        "category": category,
                        "requester": requester,
                        "week": week,
                        "wage": wage,
                        "log_wage": log_wage,
                        "applicants": applicants,
                        "fill_prob": fill_prob,
                        "filled": filled,
                    }
                )
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    elasticity = np.polyfit(df["log_wage"], np.log(df["applicants"]), deg=1)[0]
    fill_slope = np.polyfit(df["log_wage"], df["fill_prob"], deg=1)[0]
    summary = pd.DataFrame(
        [
            {"metric": "num_postings", "value": len(df)},
            {"metric": "mean_wage", "value": df["wage"].mean()},
            {"metric": "mean_applicants", "value": df["applicants"].mean()},
            {"metric": "mean_fill_probability", "value": df["fill_prob"].mean()},
            {"metric": "application_elasticity_loglog", "value": elasticity},
            {"metric": "fill_probability_slope", "value": fill_slope},
        ]
    )

    quartiles = (
        df.assign(wage_quartile=pd.qcut(df["wage"], 4, labels=["Q1 low", "Q2", "Q3", "Q4 high"]))
        .groupby("wage_quartile", observed=False)
        .agg(
            mean_wage=("wage", "mean"),
            mean_applicants=("applicants", "mean"),
            mean_fill_probability=("fill_prob", "mean"),
            fill_rate=("filled", "mean"),
            postings=("posting_id", "count"),
        )
        .reset_index()
    )
    return summary, quartiles


def make_figure(df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8))

    axes[0].scatter(df["log_wage"], np.log(df["applicants"]), s=28, alpha=0.65, color="#3B6EA8", edgecolors="none")
    slope, intercept = np.polyfit(df["log_wage"], np.log(df["applicants"]), deg=1)
    xgrid = np.linspace(df["log_wage"].min(), df["log_wage"].max(), 100)
    axes[0].plot(xgrid, intercept + slope * xgrid, linewidth=2.5, color="#B55D4C")
    axes[0].set_title("Recruiting elasticity")
    axes[0].set_xlabel("Log posted wage")
    axes[0].set_ylabel("Log applicants")
    axes[0].grid(alpha=0.2)
    axes[0].text(
        xgrid.min() + 0.02,
        np.log(df["applicants"]).max() - 0.12,
        f"Elasticity ≈ {slope:.2f}",
        fontsize=10.5,
        color="#B55D4C",
    )

    axes[1].scatter(df["wage"], df["fill_prob"], s=28, alpha=0.65, color="#4E9A8E", edgecolors="none")
    slope_fill, intercept_fill = np.polyfit(df["wage"], df["fill_prob"], deg=1)
    wage_grid = np.linspace(df["wage"].min(), df["wage"].max(), 100)
    axes[1].plot(wage_grid, intercept_fill + slope_fill * wage_grid, linewidth=2.5, color="#C79A35")
    axes[1].set_title("Staffing probability")
    axes[1].set_xlabel("Posted wage")
    axes[1].set_ylabel("Fill probability")
    axes[1].grid(alpha=0.2)

    fig.suptitle("Synthetic Dube-style task panel: wage variation reveals recruiting responses")
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

    df = build_synthetic_panel()
    summary, quartiles = summarize(df)

    df.to_csv(args.outdir / "dube_online_monopsony_postings.csv", index=False)
    summary.to_csv(args.outdir / "dube_online_monopsony_summary.csv", index=False)
    quartiles.to_csv(args.outdir / "dube_online_monopsony_by_quartile.csv", index=False)
    make_figure(df, args.outdir / "dube_online_monopsony_elasticity.png")

    print(f"Wrote Week 6 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
