#!/usr/bin/env python3
"""Estimate bounded Week 12 gift-exchange contrasts from synthetic data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def arm_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("treatment_arm", as_index=False)
        .agg(
            extra_work_units=("extra_work_units", "mean"),
            productivity_index=("productivity_index", "mean"),
            n=("shift_id", "count"),
        )
        .sort_values("treatment_arm")
        .reset_index(drop=True)
    )
    baseline = summary.loc[summary["treatment_arm"] == "baseline"].iloc[0]
    summary["extra_work_gain_vs_baseline"] = summary["extra_work_units"] - float(baseline["extra_work_units"])
    summary["productivity_gain_vs_baseline"] = summary["productivity_index"] - float(baseline["productivity_index"])
    return summary


def employer_return_heterogeneity(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["employer_return_high", "treatment_arm"], as_index=False)
        .agg(
            extra_work_units=("extra_work_units", "mean"),
            productivity_index=("productivity_index", "mean"),
        )
    )
    pivot = grouped.pivot(index="employer_return_high", columns="treatment_arm")
    pivot.columns = [f"{name}_{arm}" for name, arm in pivot.columns]
    pivot = pivot.reset_index()
    pivot["gift_extra_work_gain"] = pivot["extra_work_units_gift"] - pivot["extra_work_units_baseline"]
    pivot["piece_rate_extra_work_gain"] = pivot["extra_work_units_high_piece_rate"] - pivot["extra_work_units_baseline"]
    return pivot.sort_values("employer_return_high").reset_index(drop=True)


def make_figure(arm_df: pd.DataFrame, hetero_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))

    axes[0].bar(
        arm_df["treatment_arm"],
        arm_df["extra_work_units"],
        color=["#1f5c99", "#2a7f62", "#d8a25b"],
        width=0.64,
    )
    axes[0].set_title("Extra work by treatment arm")
    axes[0].set_ylabel("Average extra work units")
    axes[0].tick_params(axis="x", rotation=18)

    axes[1].plot(
        hetero_df["employer_return_high"],
        hetero_df["gift_extra_work_gain"],
        marker="o",
        linewidth=2.0,
        color="#2a7f62",
        label="Gift gain",
    )
    axes[1].plot(
        hetero_df["employer_return_high"],
        hetero_df["piece_rate_extra_work_gain"],
        marker="o",
        linewidth=2.0,
        color="#c25b2a",
        label="Piece-rate gain",
    )
    axes[1].set_title("Gains barely depend on employer return")
    axes[1].set_ylabel("Gain versus baseline")
    axes[1].set_xticks([0, 1], ["low return", "high return"])
    axes[1].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(outdir / "transfer_gift_exchange.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    arm_df = arm_summary(df)
    hetero_df = employer_return_heterogeneity(df)

    arm_df.to_csv(args.outdir / "gift_exchange_arm_summary.csv", index=False)
    hetero_df.to_csv(args.outdir / "gift_exchange_employer_return_heterogeneity.csv", index=False)
    make_figure(arm_df, hetero_df, args.outdir)

    note = (
        "This bounded transfer exercise contrasts baseline, gift, and high piece-rate conditions. "
        "It teaches that extra work can respond to reciprocity differently than to the employer's return."
    )
    (args.outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote Week 12 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
