#!/usr/bin/env python3
"""Transfer the Week 3 temporary-shock design to different persistence environments."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic transfer CSV.")
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
    required = {"friction_group", "high_bonus", "lag_high_bonus", "hours", "deliveries"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    grouped = (
        df.groupby(["friction_group", "high_bonus"], as_index=False)
        .agg(
            mean_hours=("hours", "mean"),
            mean_deliveries=("deliveries", "mean"),
            mean_lag_high_bonus=("lag_high_bonus", "mean"),
            shifts=("worker_id", "size"),
        )
        .sort_values(["friction_group", "high_bonus"])
    )
    grouped.to_csv(outdir / "transfer_response_summary.csv", index=False)

    pivot = grouped.pivot(index="high_bonus", columns="friction_group", values="mean_hours")
    response_gap = (
        pivot.loc[1] - pivot.loc[0]
    ).rename("hours_gap").reset_index().rename(columns={"friction_group": "group"})
    response_gap.to_csv(outdir / "transfer_hours_gap.csv", index=False)

    plt.figure(figsize=(9, 5))
    for group_name, group_df in grouped.groupby("friction_group"):
        ordered = group_df.sort_values("high_bonus")
        plt.plot(
            ordered["high_bonus"],
            ordered["mean_hours"],
            marker="o",
            linewidth=2.4,
            label=group_name.replace("_", " "),
        )
    plt.xticks([0, 1], ["Baseline pay", "Temporary high pay"])
    plt.ylabel("Mean hours")
    plt.title("Temporary bonus response by adjustment-cost environment")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "transfer_response_by_group.png", dpi=200)
    plt.close()

    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
