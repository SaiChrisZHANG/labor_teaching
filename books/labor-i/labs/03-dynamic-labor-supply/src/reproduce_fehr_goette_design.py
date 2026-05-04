#!/usr/bin/env python3
"""Bounded Week 3 reproduction in the spirit of temporary wage variation."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic shift CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for figure and summary files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {"high_bonus", "hours", "deliveries", "earnings"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary = (
        df.groupby("high_bonus", as_index=False)
        .agg(
            mean_hours=("hours", "mean"),
            mean_deliveries=("deliveries", "mean"),
            mean_earnings=("earnings", "mean"),
            shifts=("worker_id", "size"),
        )
        .sort_values("high_bonus")
    )
    summary["bonus_label"] = summary["high_bonus"].map({0: "Baseline pay", 1: "Temporary high pay"})
    summary["hours_gap_from_baseline"] = summary["mean_hours"] - summary.loc[summary["high_bonus"] == 0, "mean_hours"].iloc[0]
    summary["deliveries_gap_from_baseline"] = (
        summary["mean_deliveries"] - summary.loc[summary["high_bonus"] == 0, "mean_deliveries"].iloc[0]
    )

    summary.to_csv(outdir / "reproduction_summary.csv", index=False)

    plt.figure(figsize=(9, 5))
    positions = range(len(summary))
    width = 0.36
    plt.bar([p - width / 2 for p in positions], summary["mean_hours"], width=width, label="Mean hours")
    plt.bar([p + width / 2 for p in positions], summary["mean_deliveries"], width=width, label="Mean deliveries")
    plt.xticks(list(positions), summary["bonus_label"])
    plt.ylabel("Shift outcome level")
    plt.title("Bounded temporary-wage response in synthetic Week 3 data")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "reproduction_response.png", dpi=200)
    plt.close()

    note_lines = [
        "This bounded output is closest to a temporary intertemporal-substitution object.",
        "It should not be read as a permanent wage-change elasticity.",
        "Observed gaps can still be muted by persistence, scheduling rigidities, or adjustment costs.",
    ]
    (outdir / "reproduction_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
