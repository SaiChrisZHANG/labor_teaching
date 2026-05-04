#!/usr/bin/env python3
"""Transfer the Week 6 workflow to a bounded child-penalty event study."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic child-penalty panel CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for transfer files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {"parent", "event_time", "log_earnings", "hours", "participation_rate"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    profiles = (
        df.groupby(["parent", "event_time"], as_index=False)
        .agg(
            mean_log_earnings=("log_earnings", "mean"),
            mean_hours=("hours", "mean"),
            mean_participation=("participation_rate", "mean"),
        )
        .sort_values(["parent", "event_time"])
    )
    profiles.to_csv(outdir / "event_time_profiles.csv", index=False)

    baseline = (
        profiles.loc[profiles["event_time"] == -1, ["parent", "mean_log_earnings", "mean_hours", "mean_participation"]]
        .rename(
            columns={
                "mean_log_earnings": "baseline_log_earnings",
                "mean_hours": "baseline_hours",
                "mean_participation": "baseline_participation",
            }
        )
    )
    merged = profiles.merge(baseline, on="parent", how="left")
    merged["earnings_penalty"] = merged["mean_log_earnings"] - merged["baseline_log_earnings"]
    merged["hours_penalty"] = merged["mean_hours"] - merged["baseline_hours"]
    merged["participation_penalty"] = merged["mean_participation"] - merged["baseline_participation"]

    penalty_summary = (
        merged.loc[merged["event_time"].isin([0, 2, 5, 10])]
        .pivot_table(
            index="event_time",
            columns="parent",
            values=["earnings_penalty", "hours_penalty", "participation_penalty"],
        )
    )
    penalty_summary.to_csv(outdir / "penalty_summary.csv")

    mothers = merged.loc[merged["parent"] == "mother"]
    fathers = merged.loc[merged["parent"] == "father"]

    plt.figure(figsize=(9.0, 5.5))
    plt.plot(mothers["event_time"], mothers["earnings_penalty"], color="#c44e52", linewidth=3, marker="o", label="Mothers")
    plt.plot(fathers["event_time"], fathers["earnings_penalty"], color="#4c78a8", linewidth=3, marker="o", label="Fathers")
    plt.axhline(0.0, color="#666666", linewidth=1)
    plt.axvline(0.0, color="#666666", linewidth=1, linestyle="--")
    plt.xlabel("Years relative to first birth")
    plt.ylabel("Log earnings relative to year -1")
    plt.title("Bounded Week 6 child-penalty event study")
    plt.legend(frameon=False, loc="lower left")
    plt.tight_layout()
    plt.savefig(outdir / "transfer_child_penalty_event_study.png", dpi=200)
    plt.close()

    note_lines = [
        "The event-study object traces relative earnings paths rather than one average treatment effect.",
        "Stable pre-birth profiles help students focus on dynamic divergence after childbirth.",
        "The resulting path is useful for persistence and decomposition questions even when it is not itself a policy counterfactual.",
    ]
    (outdir / "transfer_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
