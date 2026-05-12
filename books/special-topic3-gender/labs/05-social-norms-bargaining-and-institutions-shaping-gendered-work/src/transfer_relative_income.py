#!/usr/bin/env python3
"""Transfer the Week 5 workflow to a bounded relative-income exercise."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["wife_earning_share", "wife_weekly_hours", "husband_weekly_hours", "wife_home_hours"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic relative-income CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for transfer outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def share_bin(value: float) -> str:
    if value < 0.40:
        return "below_40"
    if value < 0.50:
        return "40_to_50"
    if value < 0.60:
        return "50_to_60"
    return "above_60"


def near_threshold_group(value: float) -> str:
    if 0.46 <= value < 0.50:
        return "near_below_50"
    if 0.50 <= value <= 0.54:
        return "near_above_50"
    return "outside_window"


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def group_summary(rows: list[dict[str, str]], keys: list[str], outcomes: list[str]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["households"] = len(group)
        for outcome in outcomes:
            summary[f"mean_{outcome}"] = f"{mean([float(row[outcome]) for row in group]):.4f}"
        summaries.append(summary)
    return summaries


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    required = {"wife_earning_share", "wife_potential_share", "wife_earns_more", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    for row in rows:
        share = float(row["wife_earning_share"])
        row["share_bin"] = share_bin(share)
        row["threshold_window"] = near_threshold_group(share)

    distribution_rows = group_summary(rows, ["share_bin"], OUTCOMES)
    write_dicts(outdir / "relative_income_distribution.csv", distribution_rows)

    window_rows = [row for row in rows if row["threshold_window"] != "outside_window"]
    threshold_rows = group_summary(window_rows, ["threshold_window"], OUTCOMES)
    write_dicts(outdir / "threshold_window_summary.csv", threshold_rows)

    lookup = {row["threshold_window"]: row for row in threshold_rows}
    below = lookup["near_below_50"]
    above = lookup["near_above_50"]
    diagnostics = [
        {
            "comparison": "near_above_50_minus_near_below_50",
            "wife_earning_share_difference": f"{float(above['mean_wife_earning_share']) - float(below['mean_wife_earning_share']):.4f}",
            "wife_hours_difference": f"{float(above['mean_wife_weekly_hours']) - float(below['mean_wife_weekly_hours']):.4f}",
            "wife_home_hours_difference": f"{float(above['mean_wife_home_hours']) - float(below['mean_wife_home_hours']):.4f}",
            "observed_margin": "relative earnings, market hours, and home production near the 50 percent threshold",
            "interpretation": "threshold exercise for identity, bargaining, or selection diagnosis; not a randomized norm intervention",
        }
    ]
    write_dicts(outdir / "threshold_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This transfer exercise summarizes a synthetic relative-income threshold pattern.",
            "The observed margins are wife earnings share, market hours, and home production near equal earnings.",
            "Use it to compare threshold evidence with a norm-misperception intervention and to name what data would separate identity, bargaining, and selection.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved relative-income transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
