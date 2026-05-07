#!/usr/bin/env python3
"""Synthetic Week 8 transfer comparing certification and spillover objects."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_certification_panel(seed: int = 20260509) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    industries = ["manufacturing", "logistics", "retail", "hospitality"]
    rows = []
    for industry in industries:
        for election_id in range(1, 81):
            margin = rng.uniform(-0.18, 0.18)
            win = int(margin >= 0)
            payroll_effect = 0.012 + 0.052 * win + rng.normal(0.0, 0.018)
            employment_effect = -0.004 + 0.006 * win + rng.normal(0.0, 0.016)
            survival_prob = 0.84 - 0.03 * abs(margin) + 0.015 * win + rng.normal(0.0, 0.015)
            rows.append(
                {
                    "industry": industry,
                    "election_id": f"{industry[:3]}-{election_id:03d}",
                    "vote_margin": margin,
                    "union_win": win,
                    "post_log_payroll_change": payroll_effect,
                    "post_log_employment_change": employment_effect,
                    "post_survival_probability": max(0.35, min(0.98, survival_prob)),
                }
            )
    return pd.DataFrame(rows)


def build_spillover_panel(seed: int = 20260510) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    regions = ["Great Lakes", "Mid-Atlantic", "South Atlantic", "Pacific"]
    rows = []
    for region in regions:
        base_presence = {"Great Lakes": 0.29, "Mid-Atlantic": 0.25, "South Atlantic": 0.16, "Pacific": 0.22}[region]
        for year in range(2000, 2025):
            union_presence = max(0.06, base_presence - 0.004 * (year - 2000) + rng.normal(0.0, 0.01))
            nonunion_wage = 18.0 + 0.38 * (year - 2000) + 4.2 * union_presence + rng.normal(0.0, 0.45)
            threat_index = 0.18 + 1.7 * union_presence + rng.normal(0.0, 0.05)
            rows.append(
                {
                    "region": region,
                    "year": year,
                    "union_presence_rate": union_presence,
                    "nonunion_hourly_wage": nonunion_wage,
                    "threat_effect_index": threat_index,
                }
            )
    return pd.DataFrame(rows)


def summarize(cert_df: pd.DataFrame, spill_df: pd.DataFrame) -> pd.DataFrame:
    close = cert_df[cert_df["vote_margin"].abs() <= 0.05]
    close_win_payroll = close.loc[close["union_win"] == 1, "post_log_payroll_change"].mean()
    close_loss_payroll = close.loc[close["union_win"] == 0, "post_log_payroll_change"].mean()
    close_win_employment = close.loc[close["union_win"] == 1, "post_log_employment_change"].mean()
    close_loss_employment = close.loc[close["union_win"] == 0, "post_log_employment_change"].mean()

    summary = pd.DataFrame(
        [
            {"object": "close_election_payroll_gap", "value": close_win_payroll - close_loss_payroll},
            {"object": "close_election_employment_gap", "value": close_win_employment - close_loss_employment},
            {"object": "mean_close_election_survival_win", "value": close.loc[close["union_win"] == 1, "post_survival_probability"].mean()},
            {"object": "mean_close_election_survival_loss", "value": close.loc[close["union_win"] == 0, "post_survival_probability"].mean()},
            {
                "object": "corr_nonunion_wage_union_presence",
                "value": spill_df[["nonunion_hourly_wage", "union_presence_rate"]].corr().iloc[0, 1],
            },
            {"object": "mean_threat_effect_index", "value": spill_df["threat_effect_index"].mean()},
        ]
    )
    return summary


def make_figure(cert_df: pd.DataFrame, spill_df: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    bins = np.linspace(-0.18, 0.18, 13)
    binned = (
        cert_df.assign(bin=pd.cut(cert_df["vote_margin"], bins=bins, include_lowest=True))
        .groupby("bin", observed=False)
        .agg(
            vote_margin=("vote_margin", "mean"),
            payroll_change=("post_log_payroll_change", "mean"),
        )
        .dropna()
        .reset_index(drop=True)
    )
    axes[0].scatter(cert_df["vote_margin"], cert_df["post_log_payroll_change"], s=18, alpha=0.2, color="#9BB6D1", edgecolors="none")
    axes[0].plot(binned["vote_margin"], binned["payroll_change"], color="#B55D4C", linewidth=2.5, marker="o")
    axes[0].axvline(0.0, color="#77838F", linestyle=":", linewidth=1.2)
    axes[0].set_title("Certification RD object")
    axes[0].set_xlabel("Union vote margin")
    axes[0].set_ylabel("Post log payroll change")
    axes[0].grid(alpha=0.2)

    grouped = spill_df.groupby("year", as_index=False).agg(
        union_presence_rate=("union_presence_rate", "mean"),
        nonunion_hourly_wage=("nonunion_hourly_wage", "mean"),
    )
    axes[1].plot(grouped["year"], grouped["nonunion_hourly_wage"], color="#4E9A8E", linewidth=2.5, label="Nonunion wage")
    ax2 = axes[1].twinx()
    ax2.plot(grouped["year"], grouped["union_presence_rate"], color="#C79A35", linewidth=2.5, label="Union presence")
    axes[1].set_title("Spillover object")
    axes[1].set_xlabel("Year")
    axes[1].set_ylabel("Nonunion hourly wage")
    ax2.set_ylabel("Union presence rate")
    axes[1].grid(alpha=0.2)

    left_lines, left_labels = axes[1].get_legend_handles_labels()
    right_lines, right_labels = ax2.get_legend_handles_labels()
    axes[1].legend(left_lines + right_lines, left_labels + right_labels, fontsize=8.5, loc="upper left")

    fig.suptitle("Synthetic Week 8 transfer: organizing RD versus nonunion spillovers")
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

    cert_df = build_certification_panel()
    spill_df = build_spillover_panel()
    summary = summarize(cert_df, spill_df)

    cert_df.to_csv(args.outdir / "synthetic_certification_elections.csv", index=False)
    spill_df.to_csv(args.outdir / "synthetic_spillover_panel.csv", index=False)
    summary.to_csv(args.outdir / "union_transfer_summary.csv", index=False)
    make_figure(cert_df, spill_df, args.outdir / "union_transfer_designs.png")

    print(f"Wrote Week 8 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
