#!/usr/bin/env python3
"""
Reduced pedagogical promotion-assignment pipeline for Labor II, Week 3.

Required input columns:
- rule
- employee_id
- frontline_performance
- collaboration_signal
- managerial_potential
- promoted
- post_promotion_output
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd


REQUIRED_COLUMNS = {
    "rule",
    "employee_id",
    "frontline_performance",
    "collaboration_signal",
    "managerial_potential",
    "promoted",
    "post_promotion_output",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if not set(df["promoted"].unique()).issubset({0, 1}):
        raise ValueError("Column promoted must contain only 0/1 indicators.")


def make_summary(df: pd.DataFrame) -> pd.DataFrame:
    promoted = df[df["promoted"] == 1].copy()
    return (
        promoted.groupby("rule")
        .agg(
            promotion_count=("employee_id", "size"),
            mean_frontline_performance=("frontline_performance", "mean"),
            mean_collaboration_signal=("collaboration_signal", "mean"),
            mean_managerial_potential=("managerial_potential", "mean"),
            mean_post_promotion_output=("post_promotion_output", "mean"),
        )
        .reset_index()
    )


def make_plot(summary: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "personnel_assignment_tradeoff.png"
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8))
    colors = {
        "performance_first": "#f58518",
        "balanced": "#54a24b",
        "potential_first": "#4c78a8",
    }

    for row in summary.itertuples(index=False):
        axes[0].scatter(
            row.mean_frontline_performance,
            row.mean_post_promotion_output,
            s=120,
            color=colors[row.rule],
        )
        axes[0].annotate(row.rule, (row.mean_frontline_performance + 0.2, row.mean_post_promotion_output + 0.2))
    axes[0].set_title("Current performance versus next-role output")
    axes[0].set_xlabel("Mean frontline performance among promoted")
    axes[0].set_ylabel("Mean post-promotion output")

    axes[1].bar(
        summary["rule"],
        summary["mean_managerial_potential"],
        color=[colors[rule] for rule in summary["rule"]],
    )
    axes[1].set_title("Managerial potential among promoted")
    axes[1].set_ylabel("Mean managerial potential")
    axes[1].tick_params(axis="x", rotation=20)

    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic Week 3 transfer CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    validate_columns(df)
    summary = make_summary(df)
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir / "personnel_assignment_candidates.csv", index=False)
    summary.to_csv(outdir / "personnel_assignment_summary.csv", index=False)
    make_plot(summary, outdir)
    print(f"Saved reduced Week 3 transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
