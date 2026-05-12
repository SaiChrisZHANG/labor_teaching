#!/usr/bin/env python3
"""Reproduce bounded role-model intervention summaries."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["economics_major", "belonging_index", "expected_returns_index"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic role-model CSV.")
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
        summary["students"] = len(group)
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
    required = {"female", "role_model_exposure", "baseline_gpa", "prior_quant_index", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    balance_rows = group_summary(rows, ["female", "role_model_exposure"], ["baseline_gpa", "prior_quant_index"])
    write_dicts(outdir / "role_model_balance.csv", balance_rows)

    effect_rows = group_summary(rows, ["female", "role_model_exposure"], OUTCOMES)
    write_dicts(outdir / "major_choice_effects.csv", effect_rows)

    lookup = {(row["female"], row["role_model_exposure"]): row for row in effect_rows}
    diagnostics: list[dict[str, object]] = []
    for female in ("0", "1"):
        untreated = lookup[(female, "0")]
        treated = lookup[(female, "1")]
        diagnostics.append(
            {
                "female": female,
                "major_choice_treatment_difference": f"{float(treated['mean_economics_major']) - float(untreated['mean_economics_major']):.4f}",
                "belonging_treatment_difference": f"{float(treated['mean_belonging_index']) - float(untreated['mean_belonging_index']):.4f}",
                "expected_returns_treatment_difference": f"{float(treated['mean_expected_returns_index']) - float(untreated['mean_expected_returns_index']):.4f}",
                "interpretation": "reduced-form early-choice intervention, not a later-career estimate",
            }
        )
    write_dicts(outdir / "mechanism_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This reproduction summarizes a synthetic role-model intervention.",
            "The observed margin is economics major choice, with beliefs and belonging as diagnostic intermediates.",
            "The reduced form speaks to early choices; it does not estimate later wages, promotion, or occupational persistence.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved role-model reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
