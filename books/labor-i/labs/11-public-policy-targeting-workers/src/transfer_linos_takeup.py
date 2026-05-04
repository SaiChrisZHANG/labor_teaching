#!/usr/bin/env python3
"""Estimate bounded Week 11 take-up effects from a synthetic EITC nudge experiment."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def arm_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("treatment_arm", as_index=False)
        .agg(
            take_up_rate=("take_up", "mean"),
            completed_filing_rate=("completed_filing", "mean"),
            mean_benefit_received_k=("benefit_received_k", "mean"),
            n=("claimant_id", "count"),
        )
        .sort_values("treatment_arm")
        .reset_index(drop=True)
    )
    control = summary.loc[summary["treatment_arm"] == "control"].iloc[0]
    summary["take_up_gain_vs_control"] = summary["take_up_rate"] - float(control["take_up_rate"])
    summary["filing_gain_vs_control"] = summary["completed_filing_rate"] - float(control["completed_filing_rate"])
    return summary


def burden_heterogeneity(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["burden_group", "treatment_arm"], as_index=False)
        .agg(
            take_up_rate=("take_up", "mean"),
            completed_filing_rate=("completed_filing", "mean"),
        )
    )
    pivot = grouped.pivot(index="burden_group", columns="treatment_arm")
    pivot.columns = [f"{name}_{arm}" for name, arm in pivot.columns]
    pivot = pivot.reset_index()
    pivot["reminder_gain"] = pivot["take_up_rate_reminder_letter"] - pivot["take_up_rate_control"]
    pivot["simplified_gain"] = pivot["take_up_rate_simplified_notice"] - pivot["take_up_rate_control"]
    return pivot.sort_values("burden_group").reset_index(drop=True)


def make_figure(arm_df: pd.DataFrame, burden_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5))

    axes[0].bar(
        arm_df["treatment_arm"],
        arm_df["take_up_rate"],
        color=["#1f5c99", "#d8a25b", "#2a7f62"],
        width=0.64,
    )
    axes[0].set_title("Average take-up by treatment arm")
    axes[0].set_ylabel("Take-up rate")
    axes[0].tick_params(axis="x", rotation=18)

    axes[1].plot(burden_df["burden_group"], burden_df["reminder_gain"], marker="o", color="#c25b2a", label="Reminder gain")
    axes[1].plot(
        burden_df["burden_group"],
        burden_df["simplified_gain"],
        marker="o",
        color="#2a7f62",
        label="Simplified notice gain",
    )
    axes[1].axhline(0.0, color="#555555", linewidth=1.2)
    axes[1].set_title("Delivery gains are larger under high burden")
    axes[1].set_ylabel("Take-up gain versus control")
    axes[1].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(outdir / "transfer_takeup_nudges.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    arm_df = arm_summary(df)
    burden_df = burden_heterogeneity(df)

    arm_df.to_csv(args.outdir / "takeup_arm_summary.csv", index=False)
    burden_df.to_csv(args.outdir / "takeup_burden_heterogeneity.csv", index=False)
    make_figure(arm_df, burden_df, args.outdir)

    note = (
        "This bounded transfer exercise estimates how reminders and simplified notices raise EITC take-up in a "
        "synthetic field experiment. It teaches that policy delivery changes effective treatment intensity, "
        "especially when administrative burden is high."
    )
    (args.outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote Week 11 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
