#!/usr/bin/env python3
"""
Reduced pedagogical dynamic-adjustment pipeline for Labor II, Week 2.

Required input columns:
- firm_id
- uncertainty_group
- period
- event_time
- target_employment
- actual_employment
- hours_index
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
    "firm_id",
    "uncertainty_group",
    "period",
    "event_time",
    "target_employment",
    "actual_employment",
    "hours_index",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    for col in ["target_employment", "actual_employment", "hours_index"]:
        if (df[col] <= 0).any():
            raise ValueError(f"Column {col} must be strictly positive.")


def prepare_panel(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    temp = df.copy().sort_values(["firm_id", "period"])
    temp["next_actual_employment"] = temp.groupby("firm_id")["actual_employment"].shift(-1)
    temp["next_hours_index"] = temp.groupby("firm_id")["hours_index"].shift(-1)
    temp["employment_gap"] = temp["target_employment"] - temp["actual_employment"]
    temp["headcount_change_next"] = temp["next_actual_employment"] - temp["actual_employment"]
    temp["hours_change_next"] = temp["next_hours_index"] - temp["hours_index"]
    valid_gap = temp["employment_gap"].abs() > 1e-9
    temp["gap_closure_share"] = np.where(
        valid_gap,
        temp["headcount_change_next"] / temp["employment_gap"],
        np.nan,
    )
    return temp


def make_summary(panel: pd.DataFrame) -> pd.DataFrame:
    use = panel.dropna(subset=["gap_closure_share"]).copy()
    grouped = (
        use.groupby("uncertainty_group")
        .agg(
            observations=("firm_id", "size"),
            mean_gap=("employment_gap", "mean"),
            mean_gap_closure_share=("gap_closure_share", "mean"),
            mean_headcount_change_next=("headcount_change_next", "mean"),
            mean_hours_change_next=("hours_change_next", "mean"),
        )
        .reset_index()
    )
    return grouped


def make_event_path(panel: pd.DataFrame) -> pd.DataFrame:
    return (
        panel.groupby("event_time")
        .agg(
            mean_target_employment=("target_employment", "mean"),
            mean_actual_employment=("actual_employment", "mean"),
            mean_hours_index=("hours_index", "mean"),
        )
        .reset_index()
        .sort_values("event_time")
    )


def make_plot(event_path: pd.DataFrame, summary: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "dibiasi_adjustment_paths.png"
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))

    axes[0].plot(
        event_path["event_time"],
        event_path["mean_target_employment"],
        linewidth=2.3,
        label="Target employment",
    )
    axes[0].plot(
        event_path["event_time"],
        event_path["mean_actual_employment"],
        linewidth=2.3,
        label="Actual employment",
    )
    axes[0].plot(
        event_path["event_time"],
        event_path["mean_hours_index"],
        linewidth=2.3,
        label="Hours index",
    )
    axes[0].set_title("Synthetic Week 2 event path")
    axes[0].set_xlabel("Event time")
    axes[0].set_ylabel("Index")
    axes[0].legend()

    x = np.arange(len(summary))
    width = 0.35
    axes[1].bar(
        x - width / 2,
        summary["mean_gap_closure_share"],
        width,
        label="Gap closure share",
    )
    axes[1].bar(
        x + width / 2,
        summary["mean_hours_change_next"],
        width,
        label="Next-period hours change",
    )
    axes[1].axhline(0.0, color="gray", linewidth=0.8)
    axes[1].set_title("Adjustment by uncertainty group")
    axes[1].set_ylabel("Share or index points")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(summary["uncertainty_group"])
    axes[1].legend()

    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic dynamic-adjustment CSV.")
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
    summary = make_summary(panel)
    event_path = make_event_path(panel)
    outdir.mkdir(parents=True, exist_ok=True)
    panel.to_csv(outdir / "dibiasi_adjustment_panel.csv", index=False)
    summary.to_csv(outdir / "dibiasi_adjustment_summary.csv", index=False)
    event_path.to_csv(outdir / "dibiasi_adjustment_event_path.csv", index=False)
    make_plot(event_path, summary, outdir)
    print(f"Saved reduced Week 2 outputs to {outdir}")


if __name__ == "__main__":
    main()
