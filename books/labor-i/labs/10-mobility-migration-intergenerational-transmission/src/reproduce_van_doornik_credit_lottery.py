#!/usr/bin/env python3
"""Build a bounded Week 10 mobility factbook from synthetic lottery data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def outcome_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("lottery_label", as_index=False)
        .agg(
            move_rate=("move_any", "mean"),
            far_move_rate=("move_far", "mean"),
            employer_switch_rate=("employer_switch", "mean"),
            occupation_upgrade_rate=("occupation_upgrade", "mean"),
            mean_wage_growth=("wage_growth", "mean"),
            mean_unemployment_days=("unemployment_days", "mean"),
        )
        .sort_values("lottery_label")
        .reset_index(drop=True)
    )

    winner = summary.loc[summary["lottery_label"] == "winner"].iloc[0]
    control = summary.loc[summary["lottery_label"] == "control"].iloc[0]
    summary["winner_minus_control_move_rate"] = float(winner["move_rate"] - control["move_rate"])
    summary["winner_minus_control_wage_growth"] = float(winner["mean_wage_growth"] - control["mean_wage_growth"])
    return summary


def heterogeneity_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["gap_quartile", "lottery_label"], as_index=False)
        .agg(
            move_rate=("move_any", "mean"),
            far_move_rate=("move_far", "mean"),
            employer_switch_rate=("employer_switch", "mean"),
            mean_wage_growth=("wage_growth", "mean"),
        )
    )
    pivot = summary.pivot(index="gap_quartile", columns="lottery_label", values=["move_rate", "far_move_rate", "mean_wage_growth"])
    pivot.columns = [f"{left}_{right}" for left, right in pivot.columns]
    pivot = pivot.reset_index()
    pivot["move_rate_gap"] = pivot["move_rate_winner"] - pivot["move_rate_control"]
    pivot["far_move_rate_gap"] = pivot["far_move_rate_winner"] - pivot["far_move_rate_control"]
    pivot["wage_growth_gap"] = pivot["mean_wage_growth_winner"] - pivot["mean_wage_growth_control"]
    return pivot


def mover_type_summary(df: pd.DataFrame) -> pd.DataFrame:
    mover_type = pd.Series("stayer", index=df.index)
    mover_type.loc[df["move_any"] == 1] = "local_mover"
    mover_type.loc[df["move_far"] == 1] = "far_mover"
    mover_type.loc[df["employer_switch"] == 1] = mover_type.loc[df["employer_switch"] == 1] + "_switch"
    temp = df.assign(mover_type=mover_type)
    return (
        temp.groupby("mover_type", as_index=False)
        .agg(
            observations=("worker_id", "count"),
            mean_wage_growth=("wage_growth", "mean"),
            mean_unemployment_days=("unemployment_days", "mean"),
        )
        .sort_values("mean_wage_growth")
        .reset_index(drop=True)
    )


def make_figure(
    outcome_df: pd.DataFrame,
    heterogeneity_df: pd.DataFrame,
    mover_df: pd.DataFrame,
    outdir: Path,
) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.4))

    width = 0.34
    x = range(3)
    control = outcome_df.loc[outcome_df["lottery_label"] == "control"].iloc[0]
    winner = outcome_df.loc[outcome_df["lottery_label"] == "winner"].iloc[0]
    control_vals = [control["move_rate"], control["employer_switch_rate"], control["mean_wage_growth"]]
    winner_vals = [winner["move_rate"], winner["employer_switch_rate"], winner["mean_wage_growth"]]
    axes[0].bar([item - width / 2 for item in x], control_vals, width=width, color="#1f5c99", label="control")
    axes[0].bar([item + width / 2 for item in x], winner_vals, width=width, color="#c25b2a", label="winner")
    axes[0].set_xticks(list(x), ["Move rate", "Employer switch", "Wage growth"])
    axes[0].set_title("Lottery winners versus controls")
    axes[0].legend(frameon=False)

    axes[1].plot(heterogeneity_df["gap_quartile"], heterogeneity_df["move_rate_gap"], marker="o", color="#2a7f62", label="Move gap")
    axes[1].plot(heterogeneity_df["gap_quartile"], heterogeneity_df["far_move_rate_gap"], marker="o", color="#7d5ba6", label="Far-move gap")
    axes[1].set_title("Treatment effects by local opportunity gap")
    axes[1].set_ylabel("Winner minus control")
    axes[1].legend(frameon=False)

    display = mover_df.tail(5)
    axes[2].barh(display["mover_type"], display["mean_wage_growth"], color="#d8a25b")
    axes[2].set_title("Wage growth by mover type")
    axes[2].set_xlabel("Mean wage growth")

    fig.tight_layout()
    fig.savefig(outdir / "reproduction_credit_lottery.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    outcome_df = outcome_summary(df)
    heterogeneity_df = heterogeneity_summary(df)
    mover_df = mover_type_summary(df)

    outcome_df.to_csv(args.outdir / "lottery_mobility_summary.csv", index=False)
    heterogeneity_df.to_csv(args.outdir / "lottery_heterogeneity_summary.csv", index=False)
    mover_df.to_csv(args.outdir / "mover_type_summary.csv", index=False)
    make_figure(outcome_df, heterogeneity_df, mover_df, args.outdir)

    note = (
        "This bounded reproduction estimates how randomized credit access changes mobility-related outcomes. "
        "It identifies the effect of relaxing one mobility friction, not the unconditional return to moving."
    )
    (args.outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
