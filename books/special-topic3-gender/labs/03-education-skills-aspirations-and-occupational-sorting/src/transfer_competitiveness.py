#!/usr/bin/env python3
"""Transfer the Week 3 workflow to a bounded competitiveness and track-choice exercise."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["competition_choice", "confidence_index", "high_variance_track"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic competitiveness CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for transfer outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    required = {"female", "math_score", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["female"], row["competition_choice"])].append(row)

    summary_rows: list[dict[str, object]] = []
    for (female, competition_choice), group in sorted(grouped.items()):
        summary_rows.append(
            {
                "female": female,
                "competition_choice": competition_choice,
                "students": len(group),
                "mean_math_score": f"{mean([float(row['math_score']) for row in group]):.4f}",
                "mean_confidence_index": f"{mean([float(row['confidence_index']) for row in group]):.4f}",
                "mean_high_variance_track": f"{mean([float(row['high_variance_track']) for row in group]):.4f}",
            }
        )
    write_dicts(outdir / "competitiveness_summary.csv", summary_rows)

    by_gender: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_gender[row["female"]].append(row)

    diagnostics: list[dict[str, object]] = []
    for female, group in sorted(by_gender.items()):
        competitors = [row for row in group if row["competition_choice"] == "1"]
        noncompetitors = [row for row in group if row["competition_choice"] == "0"]
        diagnostics.append(
            {
                "female": female,
                "competition_rate": f"{mean([float(row['competition_choice']) for row in group]):.4f}",
                "track_gap_competitors_minus_noncompetitors": f"{mean([float(row['high_variance_track']) for row in competitors]) - mean([float(row['high_variance_track']) for row in noncompetitors]):.4f}",
                "interpretation": "behavioral measure linked to track choice, not a randomized role-model intervention",
            }
        )
    write_dicts(outdir / "track_choice_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This transfer exercise links a synthetic competitiveness measure to later track choice.",
            "The object differs from a role-model intervention because the competitiveness margin is observed, not randomly assigned here.",
            "Interpret the track-choice association as a diagnostic sorting exercise unless a design supplies exogenous variation.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved competitiveness transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
