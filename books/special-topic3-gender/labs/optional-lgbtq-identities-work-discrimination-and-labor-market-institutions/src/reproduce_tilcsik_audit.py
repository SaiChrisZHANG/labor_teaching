#!/usr/bin/env python3
"""Reproduce bounded callback-gap summaries for the Week 10 audit lab."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


REQUIRED_COLUMNS = {
    "pair_id",
    "identity_signal",
    "occupation",
    "employer_climate",
    "state_protection",
    "employer_size",
    "resume_quality",
    "local_unemployment",
    "callback",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthetic Tilcsik-style audit CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    missing = REQUIRED_COLUMNS - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def f4(value: float) -> str:
    return f"{value:.4f}"


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def group(rows: list[dict[str, str]], key: str) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row[key]].append(row)
    return grouped


def callback_gap_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_signal = group(rows, "identity_signal")
    control = by_signal.get("control", [])
    gay_signal = by_signal.get("gay_signal", [])
    control_rate = mean([float(row["callback"]) for row in control])
    gay_rate = mean([float(row["callback"]) for row in gay_signal])
    return [
        {
            "identity_signal": "control",
            "applications": len(control),
            "callback_rate": f4(control_rate),
            "gap_vs_control": f4(0.0),
            "observed_margin": "callback",
        },
        {
            "identity_signal": "gay_signal",
            "applications": len(gay_signal),
            "callback_rate": f4(gay_rate),
            "gap_vs_control": f4(gay_rate - control_rate),
            "observed_margin": "callback",
        },
    ]


def callback_gap_by_occupation(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for occupation, occ_rows in sorted(group(rows, "occupation").items()):
        by_signal = group(occ_rows, "identity_signal")
        control_rate = mean([float(row["callback"]) for row in by_signal.get("control", [])])
        gay_rate = mean([float(row["callback"]) for row in by_signal.get("gay_signal", [])])
        output.append(
            {
                "occupation": occupation,
                "applications": len(occ_rows),
                "control_callback_rate": f4(control_rate),
                "gay_signal_callback_rate": f4(gay_rate),
                "gay_minus_control_gap": f4(gay_rate - control_rate),
                "interpretation": "randomized signal gap at the callback margin within occupation",
            }
        )
    return output


def employer_climate_gradient(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    climate_order = ["low", "middle", "high"]
    for climate in climate_order:
        climate_rows = [row for row in rows if row["employer_climate"] == climate]
        by_signal = group(climate_rows, "identity_signal")
        control_rate = mean([float(row["callback"]) for row in by_signal.get("control", [])])
        gay_rate = mean([float(row["callback"]) for row in by_signal.get("gay_signal", [])])
        output.append(
            {
                "employer_climate": climate,
                "applications": len(climate_rows),
                "control_callback_rate": f4(control_rate),
                "gay_signal_callback_rate": f4(gay_rate),
                "gay_minus_control_gap": f4(gay_rate - control_rate),
                "state_protection_share": f4(mean([float(row["state_protection"]) for row in climate_rows])),
            }
        )
    return output


def design_balance(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_signal = group(rows, "identity_signal")
    output: list[dict[str, object]] = []
    for signal in ["control", "gay_signal"]:
        signal_rows = by_signal.get(signal, [])
        output.append(
            {
                "identity_signal": signal,
                "applications": len(signal_rows),
                "mean_resume_quality": f4(mean([float(row["resume_quality"]) for row in signal_rows])),
                "mean_local_unemployment": f4(mean([float(row["local_unemployment"]) for row in signal_rows])),
                "state_protection_share": f4(mean([float(row["state_protection"]) for row in signal_rows])),
                "large_employer_share": f4(mean([row["employer_size"] == "large" for row in signal_rows])),
            }
        )
    return output


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "callback_gap_summary.csv", callback_gap_summary(rows))
    write_dicts(outdir / "callback_gap_by_occupation.csv", callback_gap_by_occupation(rows))
    write_dicts(outdir / "employer_climate_gradient.csv", employer_climate_gradient(rows))
    write_dicts(outdir / "design_balance.csv", design_balance(rows))

    note = "\n".join(
        [
            "This reproduction summarizes deterministic synthetic correspondence-audit data.",
            "The exercise is inspired by Tilcsik's Pride and Prejudice design, not an official replication.",
            "The randomized object is an identity signal in otherwise comparable resumes.",
            "The observed margin is callback; the design does not observe applications avoided, post-hire treatment, or hidden welfare costs.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved Week 10 audit reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
