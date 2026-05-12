#!/usr/bin/env python3
"""Transfer the Week 2 workflow to a bounded IVF-style fertility design."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


OUTCOMES = ["employment_after", "hours_after", "earnings_after_index"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic IVF-style CSV.")
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
    required = {"ivf_success", "birth_within_two_years", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    by_success = {0: [], 1: []}
    for row in rows:
        by_success[int(row["ivf_success"])].append(row)

    summary_rows: list[dict[str, object]] = []
    for success in (0, 1):
        group = by_success[success]
        summary = {
            "ivf_success": success,
            "people": len(group),
            "birth_rate": f"{mean([float(row['birth_within_two_years']) for row in group]):.4f}",
        }
        for outcome in OUTCOMES:
            summary[f"mean_{outcome}"] = f"{mean([float(row[outcome]) for row in group]):.4f}"
        summary_rows.append(summary)
    write_dicts(outdir / "fertility_design_summary.csv", summary_rows)

    no_success, success = summary_rows
    first_stage = float(success["birth_rate"]) - float(no_success["birth_rate"])
    estimate_rows: list[dict[str, object]] = []
    for outcome in OUTCOMES:
        reduced_form = float(success[f"mean_{outcome}"]) - float(no_success[f"mean_{outcome}"])
        estimate_rows.append(
            {
                "outcome": outcome,
                "first_stage_birth_rate": f"{first_stage:.4f}",
                "reduced_form": f"{reduced_form:.4f}",
                "wald_effect_of_birth": f"{reduced_form / first_stage:.4f}",
                "interpretation": "local fertility effect for the IVF-shifted margin",
            }
        )
    write_dicts(outdir / "wald_estimates.csv", estimate_rows)

    note = "\n".join(
        [
            "This transfer exercise uses IVF success as a fertility shifter.",
            "The first stage is the induced change in birth probability.",
            "The Wald ratio is a local causal fertility object, not a dynamic child-penalty path.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved fertility-design transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
