#!/usr/bin/env python3
"""Transfer the Week 8 comparative framework to norms and development settings."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


NUMERIC_COLUMNS = [
    "care_index",
    "service_share",
    "norm_restrictiveness",
    "mobility_cost",
    "informality_rate",
    "legal_access_index",
    "demand_opportunity",
    "supply_feasibility",
    "female_lfp",
    "acceptable_service_jobs",
    "transportability_score",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthetic norms-transfer CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for transfer outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


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


def setting_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["setting"]].append(row)

    output: list[dict[str, object]] = []
    for setting, group in sorted(grouped.items()):
        summary: dict[str, object] = {"setting": setting, "cells": len(group)}
        for column in NUMERIC_COLUMNS:
            summary[f"mean_{column}"] = f"{mean([float(row[column]) for row in group]):.4f}"
        output.append(summary)
    return output


def classify_binding_constraint(row: dict[str, object]) -> tuple[str, str]:
    care = float(row["mean_care_index"])
    service = float(row["mean_service_share"])
    norms = float(row["mean_norm_restrictiveness"])
    mobility = float(row["mean_mobility_cost"])
    informality = float(row["mean_informality_rate"])
    legal = float(row["mean_legal_access_index"])

    candidates = {
        "care infrastructure": 1.0 - care,
        "service-sector demand": 1.0 - service,
        "norms": norms,
        "mobility": mobility,
        "informality": informality,
        "legal regime": 1.0 - legal,
    }
    mechanism = max(candidates, key=candidates.get)
    if mechanism == "norms":
        warning = "transport norm mechanism only after naming norm content and enforcement"
    elif mechanism == "mobility":
        warning = "employment effects may be muted until search radius or commute safety changes"
    elif mechanism == "informality":
        warning = "formal policy transfer may miss uncovered workers"
    elif mechanism == "care infrastructure":
        warning = "service demand may not translate into work while care binds"
    elif mechanism == "legal regime":
        warning = "formal rights require credible enforcement"
    else:
        warning = "demand-side mechanism depends on sector task mix and job quality"
    return mechanism, warning


def portable_vs_setting_specific(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for row in summary_rows:
        mechanism, warning = classify_binding_constraint(row)
        output.append(
            {
                "setting": row["setting"],
                "binding_constraint": mechanism,
                "portable_mechanism": "constraint changes feasible labor supply or labor demand",
                "setting_specific_detail": warning,
                "what_should_generalize": "the mechanism under similar context variables",
                "what_should_not_generalize": "the policy label or synthetic effect size",
            }
        )
    return output


def country_pitch_rows(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in summary_rows:
        mechanism, warning = classify_binding_constraint(row)
        rows.append(
            {
                "setting": row["setting"],
                "labor_object": "female employment, acceptable service jobs, and transportability",
                "mechanism_to_lead_with": mechanism,
                "comparative_taxonomy": "map care, services, norms, mobility, informality, and law",
                "leverage_sentence": f"Setting is informative because {mechanism} is plausibly first-order.",
                "transportability_sentence": warning,
            }
        )
    return rows


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    required = {"setting", "local_cell", *NUMERIC_COLUMNS}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    summaries = setting_summary(rows)
    write_dicts(outdir / "transfer_setting_summary.csv", summaries)
    write_dicts(outdir / "portable_vs_setting_specific.csv", portable_vs_setting_specific(summaries))
    write_dicts(outdir / "country_pitch_template.csv", country_pitch_rows(summaries))

    note = "\n".join(
        [
            "This transfer exercise is inspired by norms-and-development evidence.",
            "The synthetic settings vary care infrastructure, service demand, norms, mobility, informality, and legal access.",
            "Use the outputs to pitch country-specific evidence through mechanism, taxonomy, leverage, and transportability limits.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved norms-transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
