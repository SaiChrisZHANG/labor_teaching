#!/usr/bin/env python3
"""Build a bounded Week 9 callback-gap factbook from synthetic teaching data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def callback_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("signal_label", as_index=False)
        .agg(
            callback_rate=("callback", "mean"),
            applications=("application_id", "count"),
        )
        .sort_values("signal_label")
        .reset_index(drop=True)
    )
    rate_map = dict(zip(summary["signal_label"], summary["callback_rate"]))
    gap = rate_map["group_1"] - rate_map["group_0"]
    summary["overall_gap_group1_minus_group0"] = gap
    return summary


def quality_gap_summary(df: pd.DataFrame) -> pd.DataFrame:
    pivot = (
        df.groupby(["quality_label", "signal_label"])["callback"]
        .mean()
        .unstack("signal_label")
        .reset_index()
        .rename_axis(columns=None)
    )
    pivot["gap_group1_minus_group0"] = pivot["group_1"] - pivot["group_0"]
    return pivot


def segment_gap_summary(df: pd.DataFrame) -> pd.DataFrame:
    pivot = (
        df.groupby(["firm_segment", "signal_label"])["callback"]
        .mean()
        .unstack("signal_label")
        .reset_index()
        .rename_axis(columns=None)
    )
    pivot["gap_group1_minus_group0"] = pivot["group_1"] - pivot["group_0"]
    return pivot.sort_values("gap_group1_minus_group0")


def make_figure(
    callback_df: pd.DataFrame,
    quality_df: pd.DataFrame,
    segment_df: pd.DataFrame,
    outdir: Path,
) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 3, figsize=(12.2, 4.3))

    axes[0].bar(callback_df["signal_label"], callback_df["callback_rate"], color=["#1f5c99", "#c25b2a"], width=0.65)
    axes[0].set_title("Average callback rates")
    axes[0].set_ylabel("Callback rate")
    for idx, value in enumerate(callback_df["callback_rate"]):
        axes[0].text(idx, value + 0.004, f"{value:.1%}", ha="center", va="bottom", fontsize=9)

    x = range(len(quality_df))
    width = 0.34
    axes[1].bar([item - width / 2 for item in x], quality_df["group_0"], width=width, color="#1f5c99", label="group_0")
    axes[1].bar([item + width / 2 for item in x], quality_df["group_1"], width=width, color="#c25b2a", label="group_1")
    axes[1].set_xticks(list(x), quality_df["quality_label"])
    axes[1].set_title("Callback rates by resume quality")
    axes[1].legend(frameon=False)

    axes[2].barh(segment_df["firm_segment"], segment_df["gap_group1_minus_group0"], color="#5b8c5a")
    axes[2].axvline(0, color="#555555", linewidth=1.2)
    axes[2].set_title("Segment-specific callback gaps")
    axes[2].set_xlabel("group_1 minus group_0")

    fig.tight_layout()
    fig.savefig(outdir / "reproduction_callback_gap.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    callback_df = callback_summary(df)
    quality_df = quality_gap_summary(df)
    segment_df = segment_gap_summary(df)

    callback_df.to_csv(args.outdir / "callback_summary.csv", index=False)
    quality_df.to_csv(args.outdir / "quality_gap_summary.csv", index=False)
    segment_df.to_csv(args.outdir / "segment_gap_summary.csv", index=False)
    make_figure(callback_df, quality_df, segment_df, args.outdir)

    note = (
        "This bounded reproduction estimates a callback-gap object from a synthetic correspondence-study dataset. "
        "It shows one direct treatment effect at the screening stage, but it does not recover the full wage, "
        "task, or sorting consequences of discrimination."
    )
    (args.outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
