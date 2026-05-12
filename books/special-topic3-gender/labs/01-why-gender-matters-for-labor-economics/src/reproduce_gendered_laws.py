from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


ORDER = ["low_legal_access", "middle_legal_access", "high_legal_access"]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(rows: list[dict[str, str]], column: str) -> float:
    return fmean(float(row[column]) for row in rows)


def tier(row: dict[str, str]) -> str:
    score = float(row["legal_access_score"])
    if score < 0.50:
        return "low_legal_access"
    if score < 0.70:
        return "middle_legal_access"
    return "high_legal_access"


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tier(row)].append(row)

    summary: list[dict[str, object]] = []
    for group in ORDER:
        group_rows = grouped[group]
        female_lfp = mean(group_rows, "female_lfp_rate")
        male_lfp = mean(group_rows, "male_lfp_rate")
        female_employment = mean(group_rows, "female_employment_rate")
        male_employment = mean(group_rows, "male_employment_rate")
        female_hours = mean(group_rows, "female_weekly_hours")
        male_hours = mean(group_rows, "male_weekly_hours")
        summary.append(
            {
                "legal_access_tier": group,
                "country_years": len(group_rows),
                "legal_access_score": round(mean(group_rows, "legal_access_score"), 3),
                "workplace_protection_score": round(mean(group_rows, "workplace_protection_score"), 3),
                "family_law_score": round(mean(group_rows, "family_law_score"), 3),
                "paid_leave_weeks": round(mean(group_rows, "paid_leave_weeks"), 2),
                "female_lfp_rate": round(female_lfp, 3),
                "male_lfp_rate": round(male_lfp, 3),
                "lfp_gap_female_minus_male": round(female_lfp - male_lfp, 3),
                "employment_gap_female_minus_male": round(female_employment - male_employment, 3),
                "hours_gap_female_minus_male": round(female_hours - male_hours, 2),
                "female_authority_share": round(mean(group_rows, "female_authority_share"), 3),
            }
        )
    return summary


def gap_table(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    low = summary[0]
    high = summary[-1]
    fields = [
        "legal_access_score",
        "female_lfp_rate",
        "lfp_gap_female_minus_male",
        "employment_gap_female_minus_male",
        "hours_gap_female_minus_male",
        "female_authority_share",
    ]
    row: dict[str, object] = {"comparison": "high_minus_low_legal_access"}
    for field in fields:
        row[field] = round(float(high[field]) - float(low[field]), 3)
    return [row]


def design_map() -> list[dict[str, str]]:
    return [
        {
            "question": "What outcome is measured?",
            "answer": "Female labor-force participation, employment, hours, and authority share.",
        },
        {
            "question": "What is the comparison group?",
            "answer": "Country-years grouped by legal-access tier, with male outcomes used for gap construction.",
        },
        {
            "question": "What mechanism is claimed?",
            "answer": "Legal access and workplace protection may change feasible work, retention, and authority.",
        },
        {
            "question": "What level does the mechanism operate on?",
            "answer": "Institutional country-year variation, not worker-level preferences or firm-level pay-setting.",
        },
        {
            "question": "What is the design type?",
            "answer": "Descriptive factbook for teaching; a causal paper would need stronger identifying variation.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    rows = read_rows(Path(args.input))
    summary = summarize(rows)
    gaps = gap_table(summary)

    write_csv(
        outdir / "legal_access_tier_summary.csv",
        summary,
        [
            "legal_access_tier",
            "country_years",
            "legal_access_score",
            "workplace_protection_score",
            "family_law_score",
            "paid_leave_weeks",
            "female_lfp_rate",
            "male_lfp_rate",
            "lfp_gap_female_minus_male",
            "employment_gap_female_minus_male",
            "hours_gap_female_minus_male",
            "female_authority_share",
        ],
    )
    write_csv(
        outdir / "high_low_gap_diagnostics.csv",
        gaps,
        [
            "comparison",
            "legal_access_score",
            "female_lfp_rate",
            "lfp_gap_female_minus_male",
            "employment_gap_female_minus_male",
            "hours_gap_female_minus_male",
            "female_authority_share",
        ],
    )
    write_csv(outdir / "design_diagnosis_map.csv", design_map(), ["question", "answer"])

    note = (
        "This synthetic factbook is inspired by gendered-law research. It is useful for "
        "classifying outcomes, comparison groups, mechanisms, and design types, but it is "
        "not an official replication and not a causal estimate.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
