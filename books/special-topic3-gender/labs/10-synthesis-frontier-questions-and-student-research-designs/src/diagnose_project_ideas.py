#!/usr/bin/env python3
"""Diagnose candidate gender-and-labor research designs."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


METHOD_KEYWORDS = {
    "randomized": 2,
    "audit": 2,
    "regression discontinuity": 2,
    "difference-in-differences": 2,
    "event study": 2,
    "mover": 2,
    "threshold": 2,
    "staggered": 2,
}

DATA_FIT_KEYWORDS = {
    "applications": ["application", "job-board", "audit", "resume"],
    "callbacks": ["audit", "resume", "correspondence"],
    "retention": ["panel", "payroll", "worker-firm", "administrative"],
    "promotion": ["personnel", "manager", "evaluation"],
    "hours": ["payroll", "schedules", "administrative"],
    "safety": ["route", "safety", "survey", "job-board"],
    "enforcement": ["election", "enforcement", "inspection", "complaint"],
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def score_text(value: str, generic_terms: set[str] | None = None) -> int:
    generic_terms = generic_terms or set()
    tokens = [token for token in value.lower().replace("-", " ").split() if token]
    if len(tokens) >= 5 and not generic_terms.intersection(tokens):
        return 2
    if len(tokens) >= 3:
        return 1
    return 0


def score_identification(method: str, comparison: str) -> int:
    text = f"{method} {comparison}".lower()
    if any(keyword in text for keyword in METHOD_KEYWORDS):
        return 2
    if any(word in text for word in ["compare", "linked", "variation", "vs"]):
        return 1
    return 0


def score_data_fit(row: dict[str, str]) -> int:
    margin = row["key_margin"].lower()
    data = row["data_source"].lower()
    method = row["method"].lower()
    for margin_key, keywords in DATA_FIT_KEYWORDS.items():
        if margin_key in margin and any(keyword in data or keyword in method for keyword in keywords):
            return 2
    return 1 if data else 0


def recommendation(total: int) -> str:
    if total >= 12:
        return "proposal-ready after threat paragraph"
    if total >= 9:
        return "promising but needs sharper variation"
    return "revise object, comparison, or data fit"


def threat_row(row: dict[str, str]) -> dict[str, str]:
    method = row["method"].lower()
    threat = row["main_threat"]
    if "audit" in method:
        strengthening = "Clarify that the estimand is treatment of a visible signal at the screening margin."
    elif "regression discontinuity" in method:
        strengthening = "Show balance and density checks around the cutoff or close-election threshold."
    elif "threshold" in method:
        strengthening = "Test manipulation around the reporting threshold and track firm adjustment margins."
    elif "event study" in method or "difference-in-differences" in method:
        strengthening = "Document pre-trends, anticipation windows, and untreated comparison-group logic."
    else:
        strengthening = "Specify the source of variation before choosing the estimator."
    return {
        "project_id": row["project_id"],
        "title": row["title"],
        "primary_threat": threat,
        "strengthening_move": strengthening,
    }


def method_fit_row(row: dict[str, str]) -> dict[str, str]:
    data_fit = score_data_fit(row)
    if data_fit == 2:
        fit_comment = "Data source observes the proposed labor margin directly enough for a bounded design."
    else:
        fit_comment = "Data source may observe a proxy; add linkage or narrow the claim."
    return {
        "project_id": row["project_id"],
        "key_margin": row["key_margin"],
        "data_source": row["data_source"],
        "method": row["method"],
        "fit_score": data_fit,
        "fit_comment": fit_comment,
    }


def score_row(row: dict[str, str]) -> dict[str, object]:
    labor_focus = score_text(row["labor_object"], {"gender"})
    mechanism_clarity = score_text(row["mechanism"], {"gender"})
    counterfactual_clarity = score_text(row["comparison_group"])
    data_fit = score_data_fit(row)
    identification_credibility = score_identification(row["method"], row["comparison_group"])
    welfare_relevance = score_text(row["welfare_object"], {"gap"})
    portability = score_text(row["portability_claim"])
    total = (
        labor_focus
        + mechanism_clarity
        + counterfactual_clarity
        + data_fit
        + identification_credibility
        + welfare_relevance
        + portability
    )
    return {
        "project_id": row["project_id"],
        "title": row["title"],
        "labor_focus": labor_focus,
        "mechanism_clarity": mechanism_clarity,
        "counterfactual_clarity": counterfactual_clarity,
        "data_fit": data_fit,
        "identification_credibility": identification_credibility,
        "welfare_relevance": welfare_relevance,
        "portability": portability,
        "total_score": total,
        "recommendation": recommendation(total),
    }


def write_note(path: Path, scores: list[dict[str, object]]) -> None:
    ranked = sorted(scores, key=lambda row: (-int(row["total_score"]), str(row["project_id"])))
    best = ranked[0]
    weakest = ranked[-1]
    text = [
        "Week 10 diagnosis note",
        "======================",
        "",
        f"Highest-scoring idea: {best['project_id']} -- {best['title']} ({best['total_score']}/14).",
        f"Lowest-scoring idea: {weakest['project_id']} -- {weakest['title']} ({weakest['total_score']}/14).",
        "",
        "Scores are pedagogical diagnostics, not quality rankings. The goal is to force explicit discussion of labor focus, mechanism clarity, counterfactuals, data fit, identification, welfare, and portability.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(text) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = read_rows(args.input)
    scores = [score_row(row) for row in rows]
    threats = [threat_row(row) for row in rows]
    method_fit = [method_fit_row(row) for row in rows]
    write_csv(args.outdir / "project_scores.csv", scores)
    write_csv(args.outdir / "identification_threats.csv", threats)
    write_csv(args.outdir / "method_fit_diagnostics.csv", method_fit)
    write_note(args.outdir / "diagnosis_note.txt", scores)
    print(f"Saved Week 10 project diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
