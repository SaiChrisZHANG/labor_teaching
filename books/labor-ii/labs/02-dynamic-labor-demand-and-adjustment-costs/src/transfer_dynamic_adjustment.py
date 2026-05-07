#!/usr/bin/env python3
"""
Transfer Week 2 adjustment-cost logic to a small scenario file.

Required input columns:
- scenario
- target_change_pct
- hours_speed
- headcount_speed
- inaction_band
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
    "scenario",
    "target_change_pct",
    "hours_speed",
    "headcount_speed",
    "inaction_band",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def simulate_paths(df: pd.DataFrame, horizons: int = 6) -> pd.DataFrame:
    validate_columns(df)
    rows = []

    for row in df.to_dict(orient="records"):
        target_level = 100 * (1 + row["target_change_pct"])
        hours_level = 100.0
        headcount_level = 100.0

        rows.append(
            {
                "scenario": row["scenario"],
                "horizon": 0,
                "target_level": 100.0,
                "hours_level": hours_level,
                "headcount_level": headcount_level,
            }
        )

        for horizon in range(1, horizons + 1):
            hours_gap = target_level - hours_level
            hours_level = hours_level + row["hours_speed"] * hours_gap

            headcount_gap = target_level - headcount_level
            if abs(headcount_gap) <= row["inaction_band"]:
                new_headcount = headcount_level
            else:
                adjustment_speed = row["headcount_speed"]
                if row["inaction_band"] > 0:
                    adjustment_speed = max(adjustment_speed, 0.75)
                new_headcount = headcount_level + adjustment_speed * headcount_gap
                if headcount_gap > 0:
                    new_headcount = min(new_headcount, target_level)
                else:
                    new_headcount = max(new_headcount, target_level)
            headcount_level = new_headcount

            rows.append(
                {
                    "scenario": row["scenario"],
                    "horizon": horizon,
                    "target_level": target_level,
                    "hours_level": hours_level,
                    "headcount_level": headcount_level,
                }
            )

    return pd.DataFrame(rows)


def make_summary(paths: pd.DataFrame) -> pd.DataFrame:
    terminal = paths.sort_values("horizon").groupby("scenario").tail(1).copy()
    terminal["terminal_headcount_gap"] = terminal["target_level"] - terminal["headcount_level"]
    terminal["terminal_hours_gap"] = terminal["target_level"] - terminal["hours_level"]
    return terminal[
        [
            "scenario",
            "target_level",
            "hours_level",
            "headcount_level",
            "terminal_hours_gap",
            "terminal_headcount_gap",
        ]
    ].reset_index(drop=True)


def make_plot(paths: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "dynamic_adjustment_transfer.png"
    scenarios = list(paths["scenario"].drop_duplicates())
    fig, axes = plt.subplots(1, len(scenarios), figsize=(4.6 * len(scenarios), 4.4), sharey=True)

    if len(scenarios) == 1:
        axes = [axes]

    for ax, scenario in zip(axes, scenarios):
        temp = paths.loc[paths["scenario"] == scenario]
        ax.plot(temp["horizon"], temp["target_level"], linewidth=2.1, linestyle="--", label="Target")
        ax.plot(temp["horizon"], temp["hours_level"], linewidth=2.1, label="Hours")
        ax.plot(temp["horizon"], temp["headcount_level"], linewidth=2.1, label="Headcount")
        ax.set_title(scenario.replace("-", " "))
        ax.set_xlabel("Horizon")
        ax.set_ylabel("Index")
        ax.legend()

    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the dynamic-adjustment scenario CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    paths = simulate_paths(df)
    summary = make_summary(paths)
    outdir.mkdir(parents=True, exist_ok=True)
    paths.to_csv(outdir / "dynamic_adjustment_paths.csv", index=False)
    summary.to_csv(outdir / "dynamic_adjustment_summary.csv", index=False)
    make_plot(paths, outdir)
    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
