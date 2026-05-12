#!/usr/bin/env python3
"""Diagnose what the Week 9 application-data design observes and misses."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthetic application choice-set CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for diagnosis outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    required = {
        "worker_id",
        "gender",
        "occupation",
        "posted_wage",
        "commute_minutes",
        "firm_premium",
        "gendered_language_score",
        "applied",
        "callback",
    }
    missing = required - set(rows[0])
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


def observed_vs_missing_margins() -> list[dict[str, object]]:
    return [
        {
            "design_object": "application choice set",
            "observed_margin": "worker-job rows and application decisions",
            "what_it_identifies_well": "descriptive search and sorting patterns conditional on observed choice sets",
            "what_it_misses": "jobs never shown, informal search, identity disclosure, climate after hiring",
            "stronger_linkage": "platform exposure logs or survey modules on beliefs and constraints",
        },
        {
            "design_object": "callback among applications",
            "observed_margin": "employer response conditional on applying",
            "what_it_identifies_well": "screening gap among applicants in the observed pool",
            "what_it_misses": "workers deterred from applying and later treatment after hire",
            "stronger_linkage": "audit randomization or employer-side personnel data",
        },
        {
            "design_object": "job attributes",
            "observed_margin": "posted wage, commute, flexibility, language, firm premium",
            "what_it_identifies_well": "which posted attributes correlate with application behavior",
            "what_it_misses": "true amenities, supervisor behavior, promotion ladders, harassment risk",
            "stronger_linkage": "matched worker-firm data, climate surveys, and internal vacancy records",
        },
        {
            "design_object": "gender variable",
            "observed_margin": "binary synthetic gender category",
            "what_it_identifies_well": "teaching contrast for application behavior",
            "what_it_misses": "legal sex versus self-identified gender versus perceived workplace treatment",
            "stronger_linkage": "privacy-safe identity and climate measurement",
        },
    ]


def nonapplication_diagnostics(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["gender"]].append(row)

    output: list[dict[str, object]] = []
    for gender, group in sorted(grouped.items()):
        nonapps = [row for row in group if int(row["applied"]) == 0]
        apps = [row for row in group if int(row["applied"]) == 1]
        callbacks = [row for row in apps if int(row["callback"]) == 1]
        output.append(
            {
                "gender": gender,
                "choice_set_rows": len(group),
                "nonapplication_rows": len(nonapps),
                "nonapplication_rate": f4(len(nonapps) / len(group)),
                "callback_rate_among_applications": f4(len(callbacks) / len(apps) if apps else 0.0),
                "share_nonapplications_high_wage": f4(
                    mean([float(row["posted_wage"]) >= 40.0 for row in nonapps])
                ),
                "share_nonapplications_high_premium": f4(
                    mean([float(row["firm_premium"]) >= 0.50 for row in nonapps])
                ),
                "mean_nonapplied_commute": f4(mean([float(row["commute_minutes"]) for row in nonapps])),
                "mean_nonapplied_gendered_language": f4(
                    mean([float(row["gendered_language_score"]) for row in nonapps])
                ),
                "interpretation": "nonapplications are visible here because the synthetic data include choice sets; many real datasets do not",
            }
        )
    return output


def identification_shortfalls() -> list[dict[str, object]]:
    return [
        {
            "shortfall": "selection into observed choice set",
            "why_it_matters": "workers may not see the same vacancies or may avoid platforms entirely",
            "diagnosis": "application gaps are conditional on observed jobs",
            "possible_fix": "observe vacancy exposure or randomize information about jobs",
        },
        {
            "shortfall": "sorting versus firm treatment",
            "why_it_matters": "application data reveal where workers apply, not how firms treat hired workers over time",
            "diagnosis": "callbacks are a screening margin, not a promotion or wage-setting margin",
            "possible_fix": "link applications to matched employer-employee or personnel records",
        },
        {
            "shortfall": "posted attributes versus lived job quality",
            "why_it_matters": "flexibility, climate, safety, and authority may differ from posted language",
            "diagnosis": "text and postings proxy job design but do not observe workplace treatment",
            "possible_fix": "link postings to worker surveys, retention, reviews, or internal records",
        },
        {
            "shortfall": "hidden harms and welfare",
            "why_it_matters": "wages and callbacks miss fear, harassment, retaliation, dignity, and identity concealment",
            "diagnosis": "standard outcomes are direct outcomes, not complete welfare objects",
            "possible_fix": "add climate, safety, disclosure, and retention measures",
        },
        {
            "shortfall": "gender measurement",
            "why_it_matters": "legal category, self-identity, perceived gender, and workplace treatment can differ",
            "diagnosis": "binary categories can be useful for teaching but incomplete for frontier research",
            "possible_fix": "design privacy-safe identity measurement and pre-specify aggregation rules",
        },
    ]


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "observed_vs_missing_margins.csv", observed_vs_missing_margins())
    write_dicts(outdir / "nonapplication_diagnostics.csv", nonapplication_diagnostics(rows))
    write_dicts(outdir / "identification_shortfalls.csv", identification_shortfalls())

    note = "\n".join(
        [
            "This diagnosis separates observed application behavior from causal firm treatment and welfare.",
            "The synthetic choice set lets students see nonapplications, but many real administrative data do not.",
            "Use the shortfalls as Week 10 research openings rather than as reasons to abandon the question.",
        ]
    )
    (outdir / "diagnosis_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved design-diagnosis outputs to {outdir}")


if __name__ == "__main__":
    main()
