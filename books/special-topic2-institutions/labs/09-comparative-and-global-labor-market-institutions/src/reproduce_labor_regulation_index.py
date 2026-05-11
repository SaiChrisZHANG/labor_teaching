from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


NUMERIC_FIELDS = [
    "employment_law_index",
    "collective_relations_index",
    "social_security_index",
    "legal_coverage_rate",
    "union_membership_rate",
    "bargaining_coverage_rate",
    "enforcement_capacity_index",
    "informality_rate",
    "unemployment_rate",
    "formal_employment_share",
]


def read_rows(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows: list[dict[str, object]] = list(csv.DictReader(handle))
    for row in rows:
        for field in NUMERIC_FIELDS:
            row[field] = float(row[field])
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def mean(rows: list[dict[str, object]], field: str) -> float:
    if not rows:
        return 0.0
    return round(fmean(float(row[field]) for row in rows), 4)


def enrich_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for row in rows:
        rules_index = fmean(
            [
                float(row["employment_law_index"]),
                float(row["collective_relations_index"]),
                float(row["social_security_index"]),
            ]
        )
        effective_index = rules_index * float(row["legal_coverage_rate"]) * float(row["enforcement_capacity_index"])
        coverage_membership_gap = float(row["legal_coverage_rate"]) - float(row["union_membership_rate"])
        bargaining_extension_gap = float(row["bargaining_coverage_rate"]) - float(row["union_membership_rate"])
        text_implementation_gap = rules_index - effective_index
        output.append(
            {
                "country_id": row["country_id"],
                "region": row["region"],
                "income_group": row["income_group"],
                "regime_type": row["regime_type"],
                "legal_origin": row["legal_origin"],
                "rules_on_paper_index": round(rules_index, 4),
                "effective_protection_index": round(effective_index, 4),
                "text_implementation_gap": round(text_implementation_gap, 4),
                "legal_coverage_rate": round(float(row["legal_coverage_rate"]), 4),
                "union_membership_rate": round(float(row["union_membership_rate"]), 4),
                "bargaining_coverage_rate": round(float(row["bargaining_coverage_rate"]), 4),
                "coverage_membership_gap": round(coverage_membership_gap, 4),
                "bargaining_extension_gap": round(bargaining_extension_gap, 4),
                "enforcement_capacity_index": round(float(row["enforcement_capacity_index"]), 4),
                "informality_rate": round(float(row["informality_rate"]), 4),
                "unemployment_rate": round(float(row["unemployment_rate"]), 4),
                "formal_employment_share": round(float(row["formal_employment_share"]), 4),
            }
        )
    return output


def summarize(rows: list[dict[str, object]], group_field: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[group_field])].append(row)
    output: list[dict[str, object]] = []
    for group, group_rows in sorted(grouped.items()):
        output.append(
            {
                group_field: group,
                "countries": len(group_rows),
                "rules_on_paper_index": mean(group_rows, "rules_on_paper_index"),
                "effective_protection_index": mean(group_rows, "effective_protection_index"),
                "text_implementation_gap": mean(group_rows, "text_implementation_gap"),
                "bargaining_coverage_rate": mean(group_rows, "bargaining_coverage_rate"),
                "union_membership_rate": mean(group_rows, "union_membership_rate"),
                "enforcement_capacity_index": mean(group_rows, "enforcement_capacity_index"),
                "informality_rate": mean(group_rows, "informality_rate"),
                "formal_employment_share": mean(group_rows, "formal_employment_share"),
            }
        )
    return output


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 9 synthetic labor-regulation index reproduction note",
                "",
                "This is a pedagogical exercise inspired by Botero et al. 2004.",
                "The rules-on-paper index averages employment law, collective relations law, and social-security law components.",
                "The effective-protection index multiplies that legal index by legal coverage and enforcement capacity.",
                "The gap between the two indices is the teaching object: legal text is not implementation.",
                "Do not interpret these synthetic values as country data or an official replication.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    rows = enrich_rows(read_rows(args.input))
    write_csv(
        args.outdir / "regulation_by_country.csv",
        [
            "country_id",
            "region",
            "income_group",
            "regime_type",
            "legal_origin",
            "rules_on_paper_index",
            "effective_protection_index",
            "text_implementation_gap",
            "legal_coverage_rate",
            "union_membership_rate",
            "bargaining_coverage_rate",
            "coverage_membership_gap",
            "bargaining_extension_gap",
            "enforcement_capacity_index",
            "informality_rate",
            "unemployment_rate",
            "formal_employment_share",
        ],
        rows,
    )
    write_csv(
        args.outdir / "regulation_summary_by_income.csv",
        [
            "income_group",
            "countries",
            "rules_on_paper_index",
            "effective_protection_index",
            "text_implementation_gap",
            "bargaining_coverage_rate",
            "union_membership_rate",
            "enforcement_capacity_index",
            "informality_rate",
            "formal_employment_share",
        ],
        summarize(rows, "income_group"),
    )
    write_csv(
        args.outdir / "regulation_gap_by_regime.csv",
        [
            "regime_type",
            "countries",
            "rules_on_paper_index",
            "effective_protection_index",
            "text_implementation_gap",
            "bargaining_coverage_rate",
            "union_membership_rate",
            "enforcement_capacity_index",
            "informality_rate",
            "formal_employment_share",
        ],
        summarize(rows, "regime_type"),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 9 regulation-index outputs to {args.outdir}")


if __name__ == "__main__":
    main()
