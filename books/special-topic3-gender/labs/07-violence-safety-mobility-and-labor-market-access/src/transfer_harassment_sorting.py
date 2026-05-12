#!/usr/bin/env python3
"""Transfer Week 7 logic to a bounded harassment-risk sorting exercise."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = [
    "survey_harassment_risk",
    "reported_harassment",
    "wage",
    "quit_next_year",
    "moves_to_safer_job",
    "job_quality_score",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic harassment-sorting CSV.")
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


def make_tradeoff(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {(row["female"], row["high_risk_job"]): row for row in summary_rows}
    rows: list[dict[str, object]] = []
    for female in ("0", "1"):
        low = lookup[(female, "0")]
        high = lookup[(female, "1")]
        rows.append(
            {
                "female": female,
                "high_minus_low_wage": f"{float(high['mean_wage']) - float(low['mean_wage']):.4f}",
                "high_minus_low_quit_rate": f"{float(high['mean_quit_next_year']) - float(low['mean_quit_next_year']):.4f}",
                "high_minus_low_safer_move": f"{float(high['mean_moves_to_safer_job']) - float(low['mean_moves_to_safer_job']):.4f}",
                "high_minus_low_job_quality": f"{float(high['mean_job_quality_score']) - float(low['mean_job_quality_score']):.4f}",
                "welfare_warning": "wage premium does not price hidden harm without welfare data",
            }
        )
    return rows


def make_diagnostics(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    overall_report_rate = mean([float(row["reported_harassment"]) for row in rows])
    overall_survey_risk = mean([float(row["survey_harassment_risk"]) for row in rows])
    female_quit = mean([float(row["quit_next_year"]) for row in rows if row["female"] == "1"])
    male_quit = mean([float(row["quit_next_year"]) for row in rows if row["female"] == "0"])
    return [
        {
            "diagnostic": "reporting_gap",
            "value": f"{overall_survey_risk - overall_report_rate:.4f}",
            "interpretation": "survey risk exceeds reports; reports are selected measures of exposure",
        },
        {
            "diagnostic": "female_minus_male_quit_rate",
            "value": f"{female_quit - male_quit:.4f}",
            "interpretation": "quit margin may reveal harassment-risk sorting and hidden welfare costs",
        },
        {
            "diagnostic": "observed_margin",
            "value": "quit_next_year; moves_to_safer_job; wage; job_quality_score",
            "interpretation": "labor response and welfare proxies, not full utility",
        },
    ]


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    required = {"female", "high_risk_job", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary_rows = group_summary(rows, ["female", "high_risk_job"], OUTCOMES)
    write_dicts(outdir / "harassment_risk_summary.csv", summary_rows)

    tradeoff_rows = make_tradeoff(summary_rows)
    write_dicts(outdir / "risk_wage_tradeoff.csv", tradeoff_rows)

    diagnostic_rows = make_diagnostics(rows)
    write_dicts(outdir / "transfer_diagnostics.csv", diagnostic_rows)

    note = "\n".join(
        [
            "This transfer exercise summarizes a synthetic harassment-risk sorting setting.",
            "The observed margins are wage, quit risk, moves to safer jobs, reporting, and job quality.",
            "Use the wage-risk comparison to explain why higher wages need not imply higher welfare.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved harassment-sorting transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
