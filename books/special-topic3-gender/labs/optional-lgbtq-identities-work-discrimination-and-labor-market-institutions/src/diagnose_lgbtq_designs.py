#!/usr/bin/env python3
"""Diagnose observed and hidden margins in the Week 10 LGBTQ+ labor lab."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", required=True, help="Path to synthetic Tilcsik-style audit CSV.")
    parser.add_argument("--trans", required=True, help="Path to synthetic transgender hiring audit CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for diagnosis outputs.")
    return parser.parse_args()


def read_rows(path: Path, required: set[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns in {path}: {sorted(missing)}")
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


def observed_vs_hidden_margins() -> list[dict[str, object]]:
    return [
        {
            "design_object": "correspondence audit",
            "observed_margin": "callback response to randomized identity signal",
            "what_it_identifies_well": "screening-stage differential treatment of visible signals",
            "what_it_misses": "workers who do not apply, post-hire treatment, disclosure costs, retention, promotion",
            "stronger_linkage": "link audit or application data to later employer records, worker surveys, or accepted jobs",
        },
        {
            "design_object": "identity signal",
            "observed_margin": "employer response to disclosed or implied identity",
            "what_it_identifies_well": "treatment of a signal held constant across resumes",
            "what_it_misses": "underlying LGBTQ+ population membership and workers who conceal identity",
            "stronger_linkage": "survey modules distinguishing identity, disclosure, perception, and workplace treatment",
        },
        {
            "design_object": "transgender hiring audit",
            "observed_margin": "callback response to transgender signal",
            "what_it_identifies_well": "access to jobs at screening margin for signaled trans applicants",
            "what_it_misses": "documentation issues, benefit access, safety, within-job climate, transition timing",
            "stronger_linkage": "audit plus administrative earnings or personnel data with privacy protections",
        },
        {
            "design_object": "legal protection",
            "observed_margin": "formal policy or law exposure",
            "what_it_identifies_well": "changes around legal timing when outcomes are observed",
            "what_it_misses": "employer compliance, worker beliefs, reporting behavior, actual climate",
            "stronger_linkage": "policy timing linked to applications, employer practices, benefits, and climate surveys",
        },
    ]


def trans_hiring_diagnostics(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for occupation, occ_rows in sorted(group(rows, "occupation").items()):
        by_signal = group(occ_rows, "identity_signal")
        cis_rate = mean([float(row["callback"]) for row in by_signal.get("cis_signal", [])])
        trans_rate = mean([float(row["callback"]) for row in by_signal.get("trans_signal", [])])
        output.append(
            {
                "occupation": occupation,
                "applications": len(occ_rows),
                "customer_facing_share": f4(mean([float(row["customer_facing"]) for row in occ_rows])),
                "cis_signal_callback_rate": f4(cis_rate),
                "trans_signal_callback_rate": f4(trans_rate),
                "trans_minus_cis_gap": f4(trans_rate - cis_rate),
                "interpretation": "challenge audit margin; not evidence on within-job treatment after hire",
            }
        )
    return output


def identification_shortfalls(audit_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    climate_rows = group(audit_rows, "employer_climate")
    low_gap = mean([float(row["callback"]) for row in climate_rows["low"] if row["identity_signal"] == "gay_signal"]) - mean(
        [float(row["callback"]) for row in climate_rows["low"] if row["identity_signal"] == "control"]
    )
    high_gap = mean([float(row["callback"]) for row in climate_rows["high"] if row["identity_signal"] == "gay_signal"]) - mean(
        [float(row["callback"]) for row in climate_rows["high"] if row["identity_signal"] == "control"]
    )
    return [
        {
            "shortfall": "underlying membership versus disclosed signal",
            "why_it_matters": "audit estimates treatment of visible signals, not outcomes for everyone in the population",
            "diagnosis": "identity_signal is randomized; LGBTQ+ identity itself is not",
            "possible_fix": "combine audits with privacy-safe worker identity and disclosure surveys",
        },
        {
            "shortfall": "hiring versus within-job treatment",
            "why_it_matters": "callback gaps may coexist with different pay, promotion, benefits, climate, or exits after hire",
            "diagnosis": "callback is the only direct employer outcome in the audit path",
            "possible_fix": "link applications to accepted jobs, payroll, benefit records, and climate measures",
        },
        {
            "shortfall": "firm heterogeneity",
            "why_it_matters": "discrimination may be concentrated in low-climate employers rather than spread evenly",
            "diagnosis": f"synthetic low-climate gap is {f4(low_gap)} and high-climate gap is {f4(high_gap)}",
            "possible_fix": "use large-employer audit platforms or repeated applications by firm",
        },
        {
            "shortfall": "legal protection versus workplace treatment",
            "why_it_matters": "formal protection can change law without changing climate or worker beliefs",
            "diagnosis": "state_protection is observed but not randomly assigned in this synthetic path",
            "possible_fix": "use policy timing plus outcomes that separately measure employer and worker response",
        },
        {
            "shortfall": "hidden harms",
            "why_it_matters": "wages and callbacks miss concealment, harassment, safety, dignity, and stress",
            "diagnosis": "the audit observes callback only",
            "possible_fix": "add survey/list experiments, climate modules, retention, and wellbeing measures",
        },
    ]


def main() -> None:
    args = parse_args()
    audit_rows = read_rows(
        Path(args.audit),
        {"identity_signal", "employer_climate", "state_protection", "callback"},
    )
    trans_rows = read_rows(
        Path(args.trans),
        {"identity_signal", "occupation", "customer_facing", "callback"},
    )
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "observed_vs_hidden_margins.csv", observed_vs_hidden_margins())
    write_dicts(outdir / "trans_hiring_diagnostics.csv", trans_hiring_diagnostics(trans_rows))
    write_dicts(outdir / "identification_shortfalls.csv", identification_shortfalls(audit_rows))

    note = "\n".join(
        [
            "This diagnosis separates randomized identity signals from underlying population membership.",
            "The audit margin is callback; it is not within-job treatment, disclosure cost, benefit access, or worker welfare.",
            "Use the shortfalls to design stronger links between hiring, firm behavior, climate, law, and careers.",
        ]
    )
    (outdir / "diagnosis_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved Week 10 design-diagnosis outputs to {outdir}")


if __name__ == "__main__":
    main()
