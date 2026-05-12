#!/usr/bin/env python3
"""Reproduce bounded manager-access and promotion summaries."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


BALANCE_OUTCOMES = ["baseline_performance", "pre_level", "prior_wage"]
CAREER_OUTCOMES = ["informal_interaction", "mentoring_score", "promoted", "wage_growth", "retained"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic personnel CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
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


def group_summary(rows: list[dict[str, str]], keys: list[str], outcomes: list[str]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["workers"] = len(group)
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
    required = {"female", "manager_overlap", *BALANCE_OUTCOMES, *CAREER_OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    balance_rows = group_summary(rows, ["female", "manager_overlap"], BALANCE_OUTCOMES)
    write_dicts(outdir / "manager_access_balance.csv", balance_rows)

    effect_rows = group_summary(rows, ["female", "manager_overlap"], CAREER_OUTCOMES)
    write_dicts(outdir / "promotion_effects.csv", effect_rows)

    lookup = {(row["female"], row["manager_overlap"]): row for row in effect_rows}
    diagnostics: list[dict[str, object]] = []
    for female in ("0", "1"):
        low_access = lookup[(female, "0")]
        high_access = lookup[(female, "1")]
        diagnostics.append(
            {
                "female": female,
                "interaction_difference": f"{float(high_access['mean_informal_interaction']) - float(low_access['mean_informal_interaction']):.4f}",
                "promotion_difference": f"{float(high_access['mean_promoted']) - float(low_access['mean_promoted']):.4f}",
                "wage_growth_difference": f"{float(high_access['mean_wage_growth']) - float(low_access['mean_wage_growth']):.4f}",
                "retention_difference": f"{float(high_access['mean_retained']) - float(low_access['mean_retained']):.4f}",
                "interpretation": "within-firm manager-access exercise, not between-firm sorting",
            }
        )
    write_dicts(outdir / "mechanism_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This reproduction summarizes a synthetic within-firm manager-access exercise.",
            "The observed margins are informal interaction, mentoring, promotion, wage growth, and retention.",
            "The design is a teaching analog for personnel-data evidence; it does not estimate sorting into firms.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved manager-access reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
