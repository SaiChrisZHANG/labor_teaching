#!/usr/bin/env python3
"""Estimate bounded employer discrimination report cards for the Week 9 transfer lab."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def firm_level_gaps(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["firm_id", "firm_name", "segment", "signal_label"], as_index=False)
        .agg(
            callback_rate=("callback", "mean"),
            n=("callback", "count"),
        )
    )
    pivot = grouped.pivot(index=["firm_id", "firm_name", "segment"], columns="signal_label", values=["callback_rate", "n"])
    pivot.columns = [f"{left}_{right}" for left, right in pivot.columns]
    pivot = pivot.reset_index()
    pivot["raw_gap_group1_minus_group0"] = pivot["callback_rate_group_1"] - pivot["callback_rate_group_0"]

    p1 = pivot["callback_rate_group_1"]
    p0 = pivot["callback_rate_group_0"]
    n1 = pivot["n_group_1"]
    n0 = pivot["n_group_0"]
    pivot["gap_se"] = np.sqrt((p1 * (1 - p1) / n1) + (p0 * (1 - p0) / n0))
    return pivot.sort_values("raw_gap_group1_minus_group0").reset_index(drop=True)


def shrink_report_cards(report_df: pd.DataFrame) -> pd.DataFrame:
    overall_gap = float(report_df["raw_gap_group1_minus_group0"].mean())
    se2 = np.square(report_df["gap_se"])
    signal_var = max(float(report_df["raw_gap_group1_minus_group0"].var(ddof=0) - se2.mean()), 1e-4)
    weights = signal_var / (signal_var + se2)
    report_df = report_df.copy()
    report_df["shrinkage_weight"] = weights
    report_df["shrunken_gap"] = weights * report_df["raw_gap_group1_minus_group0"] + (1 - weights) * overall_gap
    report_df["overall_gap"] = overall_gap
    return report_df.sort_values("shrunken_gap").reset_index(drop=True)


def ranking_table(report_df: pd.DataFrame) -> pd.DataFrame:
    ranking = report_df[["firm_id", "firm_name", "segment", "raw_gap_group1_minus_group0", "gap_se", "shrunken_gap"]].copy()
    ranking["raw_rank"] = ranking["raw_gap_group1_minus_group0"].rank(method="first")
    ranking["shrunken_rank"] = ranking["shrunken_gap"].rank(method="first")
    return ranking.sort_values("shrunken_gap").reset_index(drop=True)


def make_figure(report_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.8))

    axes[0].scatter(report_df["raw_gap_group1_minus_group0"], report_df["shrunken_gap"], color="#1f5c99", s=45)
    limits = [
        min(report_df["raw_gap_group1_minus_group0"].min(), report_df["shrunken_gap"].min()) - 0.02,
        max(report_df["raw_gap_group1_minus_group0"].max(), report_df["shrunken_gap"].max()) + 0.02,
    ]
    axes[0].plot(limits, limits, linestyle="--", color="#555555", linewidth=1.4)
    axes[0].set_xlim(limits)
    axes[0].set_ylim(limits)
    axes[0].set_xlabel("Raw employer gap")
    axes[0].set_ylabel("Shrunken report-card gap")
    axes[0].set_title("Noise-aware firm report cards")

    display = report_df.nsmallest(8, "shrunken_gap")
    axes[1].barh(display["firm_name"], display["shrunken_gap"], color="#c25b2a")
    axes[1].errorbar(
        display["shrunken_gap"],
        display["firm_name"],
        xerr=1.96 * display["gap_se"],
        fmt="none",
        ecolor="#374151",
        elinewidth=1.2,
        capsize=3,
    )
    axes[1].axvline(report_df["overall_gap"].iloc[0], color="#2a7f62", linestyle="--", linewidth=1.4)
    axes[1].set_title("Most negative report-card estimates")
    axes[1].set_xlabel("group_1 minus group_0 callback gap")

    fig.tight_layout()
    fig.savefig(outdir / "transfer_report_cards.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    report_df = shrink_report_cards(firm_level_gaps(df))
    ranking_df = ranking_table(report_df)

    report_df.to_csv(args.outdir / "report_card_summary.csv", index=False)
    ranking_df.to_csv(args.outdir / "firm_rankings.csv", index=False)
    make_figure(report_df, args.outdir)

    note = (
        "This bounded transfer exercise estimates employer-level callback gaps and then shrinks them toward the "
        "overall mean to reflect ranking uncertainty. The goal is to teach why firm heterogeneity and noise matter "
        "once the class moves beyond one pooled average treatment effect."
    )
    (args.outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
