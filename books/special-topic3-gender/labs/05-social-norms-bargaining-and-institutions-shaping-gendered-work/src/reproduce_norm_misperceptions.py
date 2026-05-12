#!/usr/bin/env python3
"""Reproduce bounded norm-misperception and job-search summaries."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


BALANCE_OUTCOMES = [
    "private_support",
    "perceived_peer_support",
    "true_peer_support",
    "baseline_misperception",
    "wife_interested_work",
]
SEARCH_OUTCOMES = [
    "posterior_peer_support",
    "job_matching_signup",
    "followup_job_search",
    "followup_employment",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic norm-misperception CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def add_misperception_group(rows: list[dict[str, str]]) -> None:
    values = sorted(float(row["baseline_misperception"]) for row in rows)
    median = values[len(values) // 2]
    for row in rows:
        row["high_misperception"] = str(int(float(row["baseline_misperception"]) >= median))


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
        summary["respondents"] = len(group)
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
    required = {"information_treatment", *BALANCE_OUTCOMES, *SEARCH_OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    add_misperception_group(rows)

    balance_rows = group_summary(rows, ["information_treatment"], BALANCE_OUTCOMES)
    write_dicts(outdir / "norm_information_balance.csv", balance_rows)

    effect_rows = group_summary(rows, ["high_misperception", "information_treatment"], SEARCH_OUTCOMES)
    write_dicts(outdir / "job_search_effects.csv", effect_rows)

    lookup = {(row["high_misperception"], row["information_treatment"]): row for row in effect_rows}
    diagnostics: list[dict[str, object]] = []
    for high_misperception in ("0", "1"):
        control = lookup[(high_misperception, "0")]
        treated = lookup[(high_misperception, "1")]
        diagnostics.append(
            {
                "high_misperception": high_misperception,
                "posterior_belief_difference": f"{float(treated['mean_posterior_peer_support']) - float(control['mean_posterior_peer_support']):.4f}",
                "signup_difference": f"{float(treated['mean_job_matching_signup']) - float(control['mean_job_matching_signup']):.4f}",
                "job_search_difference": f"{float(treated['mean_followup_job_search']) - float(control['mean_followup_job_search']):.4f}",
                "employment_difference": f"{float(treated['mean_followup_employment']) - float(control['mean_followup_employment']):.4f}",
                "interpretation": "information-induced belief and job-search exercise, not a wage or legal-rights effect",
            }
        )
    write_dicts(outdir / "mechanism_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This reproduction summarizes a synthetic norm-misperception information exercise.",
            "The observed margins are posterior perceived support, job-matching sign-up, follow-up job search, and follow-up employment.",
            "The design is a teaching analog for a belief-about-acceptability channel; it does not estimate wage effects, legal rights, or long-run household bargaining.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved norm-misperception reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
