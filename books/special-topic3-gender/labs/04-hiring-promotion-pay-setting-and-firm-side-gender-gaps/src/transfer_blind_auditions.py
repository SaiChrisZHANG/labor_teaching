#!/usr/bin/env python3
"""Transfer the Week 4 workflow to a bounded blind-screening exercise."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


BALANCE_OUTCOMES = ["baseline_score", "audition_score"]
SCREEN_OUTCOMES = ["advanced"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic blind-screening CSV.")
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


def group_summary(rows: list[dict[str, str]], keys: list[str], outcomes: list[str]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["candidates"] = len(group)
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
    required = {"female", "blind_screen", *BALANCE_OUTCOMES, *SCREEN_OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    balance_rows = group_summary(rows, ["female", "blind_screen"], BALANCE_OUTCOMES)
    write_dicts(outdir / "screening_balance.csv", balance_rows)

    advancement_rows = group_summary(rows, ["female", "blind_screen"], SCREEN_OUTCOMES)
    write_dicts(outdir / "blind_screen_advancement.csv", advancement_rows)

    lookup = {(row["female"], row["blind_screen"]): row for row in advancement_rows}
    diagnostics: list[dict[str, object]] = []
    for female in ("0", "1"):
        nonblind = lookup[(female, "0")]
        blind = lookup[(female, "1")]
        diagnostics.append(
            {
                "female": female,
                "blind_minus_nonblind_advancement": f"{float(blind['mean_advanced']) - float(nonblind['mean_advanced']):.4f}",
                "observed_margin": "entry-stage advancement",
                "interpretation": "screening design, not downstream promotion or wage-setting",
            }
        )

    nonblind_gender_gap = float(lookup[("1", "0")]["mean_advanced"]) - float(lookup[("0", "0")]["mean_advanced"])
    blind_gender_gap = float(lookup[("1", "1")]["mean_advanced"]) - float(lookup[("0", "1")]["mean_advanced"])
    diagnostics.append(
        {
            "female": "gap_female_minus_male",
            "blind_minus_nonblind_advancement": f"{blind_gender_gap - nonblind_gender_gap:.4f}",
            "observed_margin": "change in gender advancement gap",
            "interpretation": "procedure changes entry screen; later outcomes remain unobserved",
        }
    )
    write_dicts(outdir / "transfer_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This transfer exercise summarizes a synthetic blind-screening design.",
            "The observed margin is advancement at entry, not promotion, authority, wage growth, or retention.",
            "Use it to compare a clean hiring screen with a within-firm personnel mechanism.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved blind-screening transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
