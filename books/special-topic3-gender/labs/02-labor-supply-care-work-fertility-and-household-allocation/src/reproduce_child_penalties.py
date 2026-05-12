#!/usr/bin/env python3
"""Reproduce bounded child-penalty event-time summaries."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["earnings_index", "hours", "employment_rate", "job_quality_index", "weekly_care_hours"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic child-penalty CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def write_dicts(path: Path, rows: list[dict[str, object]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames or list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    required = {"parent", "event_time", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    grouped: dict[tuple[str, int], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        key = (row["parent"], int(row["event_time"]))
        for outcome in OUTCOMES:
            grouped[key][outcome].append(float(row[outcome]))

    profile_rows: list[dict[str, object]] = []
    for parent, event_time in sorted(grouped):
        profile = {"parent": parent, "event_time": event_time}
        for outcome in OUTCOMES:
            profile[f"mean_{outcome}"] = f"{mean(grouped[(parent, event_time)][outcome]):.4f}"
        profile_rows.append(profile)
    write_dicts(outdir / "event_time_profiles.csv", profile_rows)

    baseline = {
        row["parent"]: {outcome: float(row[f"mean_{outcome}"]) for outcome in OUTCOMES}
        for row in profile_rows
        if int(row["event_time"]) == -1
    }
    summary_rows: list[dict[str, object]] = []
    for row in profile_rows:
        event_time = int(row["event_time"])
        if event_time not in (0, 2, 5, 8):
            continue
        parent = row["parent"]
        summary = {"parent": parent, "event_time": event_time}
        for outcome in OUTCOMES:
            value = float(row[f"mean_{outcome}"])
            summary[f"{outcome}_relative_to_year_minus_1"] = f"{value - baseline[parent][outcome]:.4f}"
        summary_rows.append(summary)
    write_dicts(outdir / "child_penalty_summary.csv", summary_rows)

    lookup = {(row["parent"], int(row["event_time"])): row for row in summary_rows}
    diagnostics: list[dict[str, object]] = []
    for event_time in (0, 2, 5, 8):
        mother = lookup[("mother", event_time)]
        father = lookup[("father", event_time)]
        diagnostics.append(
            {
                "event_time": event_time,
                "earnings_mother_minus_father": f"{float(mother['earnings_index_relative_to_year_minus_1']) - float(father['earnings_index_relative_to_year_minus_1']):.4f}",
                "hours_mother_minus_father": f"{float(mother['hours_relative_to_year_minus_1']) - float(father['hours_relative_to_year_minus_1']):.4f}",
                "care_hours_mother_minus_father": f"{float(mother['weekly_care_hours_relative_to_year_minus_1']) - float(father['weekly_care_hours_relative_to_year_minus_1']):.4f}",
                "interpretation": "dynamic child penalty, not a stand-alone causal fertility estimate",
            }
        )
    write_dicts(outdir / "margin_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This reproduction traces event-time paths around first birth.",
            "The outputs separate labor-market reallocation from care-time reallocation.",
            "The event-study path is descriptive unless paired with a separate causal design or policy counterfactual.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved child-penalty reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
