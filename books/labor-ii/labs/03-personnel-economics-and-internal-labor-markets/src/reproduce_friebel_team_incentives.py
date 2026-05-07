#!/usr/bin/env python3
"""
Reduced pedagogical team-incentive pipeline for Labor II, Week 3.

Required input columns:
- team_id
- store_id
- event_time
- incentive_group
- complementarity_group
- sales_index
- profit_index
- attendance_rate
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "team_id",
    "store_id",
    "event_time",
    "incentive_group",
    "complementarity_group",
    "sales_index",
    "profit_index",
    "attendance_rate",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    for col in ["sales_index", "profit_index", "attendance_rate"]:
        if (df[col] <= 0).any():
            raise ValueError(f"Column {col} must be strictly positive.")


def prepare_panel(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    temp = df.copy().sort_values(["team_id", "event_time"])
    temp["post"] = (temp["event_time"] >= 0).astype(int)
    return temp


def make_event_path(panel: pd.DataFrame) -> pd.DataFrame:
    return (
        panel.groupby(["event_time", "incentive_group"])
        .agg(
            mean_sales_index=("sales_index", "mean"),
            mean_profit_index=("profit_index", "mean"),
            mean_attendance_rate=("attendance_rate", "mean"),
        )
        .reset_index()
        .sort_values(["incentive_group", "event_time"])
    )


def make_summary(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for outcome in ["sales_index", "profit_index", "attendance_rate"]:
        grouped = (
            panel.groupby(["incentive_group", "post"])[outcome]
            .mean()
            .unstack("post")
            .rename(columns={0: "pre_mean", 1: "post_mean"})
        )
        control_pre = float(grouped.loc["control", "pre_mean"])
        control_post = float(grouped.loc["control", "post_mean"])
        treated_pre = float(grouped.loc["treated", "pre_mean"])
        treated_post = float(grouped.loc["treated", "post_mean"])
        did = (treated_post - treated_pre) - (control_post - control_pre)
        rows.append(
            {
                "outcome": outcome,
                "control_pre_mean": control_pre,
                "control_post_mean": control_post,
                "treated_pre_mean": treated_pre,
                "treated_post_mean": treated_post,
                "difference_in_differences": did,
            }
        )
    return pd.DataFrame(rows)


def make_heterogeneity(panel: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        panel.groupby(["incentive_group", "complementarity_group", "post"])[
            ["sales_index", "profit_index"]
        ]
        .mean()
        .reset_index()
    )
    rows = []
    for incentive_group in ["control", "treated"]:
        for complementarity_group in ["high", "low"]:
            subset = grouped[
                (grouped["incentive_group"] == incentive_group)
                & (grouped["complementarity_group"] == complementarity_group)
            ].set_index("post")
            rows.append(
                {
                    "incentive_group": incentive_group,
                    "complementarity_group": complementarity_group,
                    "sales_gain": float(subset.loc[1, "sales_index"] - subset.loc[0, "sales_index"]),
                    "profit_gain": float(subset.loc[1, "profit_index"] - subset.loc[0, "profit_index"]),
                }
            )
    return pd.DataFrame(rows)


def make_plot(event_path: pd.DataFrame, heterogeneity: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "friebel_team_incentives_effects.png"
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))

    for group, color in [("control", "#4c78a8"), ("treated", "#f58518")]:
        subset = event_path[event_path["incentive_group"] == group]
        axes[0].plot(
            subset["event_time"],
            subset["mean_sales_index"],
            marker="o",
            linewidth=2.2,
            color=color,
            label=group.title(),
        )
    axes[0].axvline(0, color="gray", linestyle="--", linewidth=1.0)
    axes[0].set_title("Synthetic Week 3 team-incentive event path")
    axes[0].set_xlabel("Event time")
    axes[0].set_ylabel("Mean sales index")
    axes[0].legend()

    x = np.arange(len(heterogeneity))
    axes[1].bar(x, heterogeneity["sales_gain"], color=["#4c78a8", "#72b7b2", "#f58518", "#e45756"])
    axes[1].axhline(0.0, color="gray", linewidth=0.8)
    axes[1].set_title("Sales gains by team complementarity")
    axes[1].set_ylabel("Post minus pre sales index")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(
        [
            f"{row.incentive_group}\n{row.complementarity_group}"
            for row in heterogeneity.itertuples(index=False)
        ]
    )

    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic Week 3 team panel.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    panel = prepare_panel(df)
    event_path = make_event_path(panel)
    summary = make_summary(panel)
    heterogeneity = make_heterogeneity(panel)
    outdir.mkdir(parents=True, exist_ok=True)
    panel.to_csv(outdir / "friebel_team_incentives_panel.csv", index=False)
    event_path.to_csv(outdir / "friebel_team_incentives_event_path.csv", index=False)
    summary.to_csv(outdir / "friebel_team_incentives_summary.csv", index=False)
    heterogeneity.to_csv(outdir / "friebel_team_incentives_heterogeneity.csv", index=False)
    make_plot(event_path, heterogeneity, outdir)
    print(f"Saved reduced Week 3 reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
