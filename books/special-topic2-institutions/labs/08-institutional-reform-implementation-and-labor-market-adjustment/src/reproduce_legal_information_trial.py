from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


NUMERIC_FIELDS = [
    "treated_information",
    "low_baseline_knowledge",
    "local_capacity_index",
    "firm_visibility_index",
    "baseline_knowledge_index",
    "followup_knowledge_index",
    "perceived_enforcement_index",
    "claim_intention_index",
    "formal_contract",
    "employment_at_followup",
    "wage_index",
]

OUTCOME_FIELDS = [
    "baseline_knowledge_index",
    "followup_knowledge_index",
    "perceived_enforcement_index",
    "claim_intention_index",
    "formal_contract",
    "employment_at_followup",
    "wage_index",
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


def summarize_by_treatment(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[int(float(row["treated_information"]))].append(row)
    output: list[dict[str, object]] = []
    for treated in [0, 1]:
        group_rows = grouped[treated]
        summary: dict[str, object] = {
            "treated_information": treated,
            "workers": len(group_rows),
        }
        for field in OUTCOME_FIELDS:
            summary[field] = mean(group_rows, field)
        output.append(summary)
    return output


def difference_rows(rows: list[dict[str, object]], label: str) -> list[dict[str, object]]:
    treated = [row for row in rows if int(float(row["treated_information"])) == 1]
    control = [row for row in rows if int(float(row["treated_information"])) == 0]
    output: list[dict[str, object]] = []
    for field in OUTCOME_FIELDS:
        treated_mean = mean(treated, field)
        control_mean = mean(control, field)
        output.append(
            {
                "sample": label,
                "variable": field,
                "treated_mean": treated_mean,
                "control_mean": control_mean,
                "treated_minus_control": round(treated_mean - control_mean, 4),
                "interpretation": interpretation(field),
            }
        )
    return output


def heterogeneity_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for low_baseline, label in [(0, "higher_baseline_knowledge"), (1, "lower_baseline_knowledge")]:
        subset = [row for row in rows if int(float(row["low_baseline_knowledge"])) == low_baseline]
        for diff in difference_rows(subset, label):
            if diff["variable"] in ["followup_knowledge_index", "claim_intention_index", "formal_contract", "wage_index"]:
                output.append(diff)
    return output


def interpretation(field: str) -> str:
    labels = {
        "baseline_knowledge_index": "pre-treatment balance check",
        "followup_knowledge_index": "legal-knowledge margin",
        "perceived_enforcement_index": "belief about implementation credibility",
        "claim_intention_index": "take-up and bargaining intention",
        "formal_contract": "contract-form labor margin",
        "employment_at_followup": "employment labor margin",
        "wage_index": "wage labor margin",
    }
    return labels[field]


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 8 synthetic legal-information reproduction note",
                "",
                "This is a pedagogical exercise inspired by Bertrand-Crepon 2021.",
                "The output separates knowledge and belief margins from realized labor-market outcomes.",
                "Large knowledge differences with smaller employment or wage differences are a feature of the teaching design.",
                "Do not interpret these synthetic differences as an official replication.",
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
    rows = read_rows(args.input)
    write_csv(
        args.outdir / "legal_information_summary.csv",
        ["treated_information", "workers", *OUTCOME_FIELDS],
        summarize_by_treatment(rows),
    )
    write_csv(
        args.outdir / "treatment_differences.csv",
        ["sample", "variable", "treated_mean", "control_mean", "treated_minus_control", "interpretation"],
        difference_rows(rows, "all_workers"),
    )
    write_csv(
        args.outdir / "heterogeneity_by_baseline_knowledge.csv",
        ["sample", "variable", "treated_mean", "control_mean", "treated_minus_control", "interpretation"],
        heterogeneity_rows(rows),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 8 legal-information outputs to {args.outdir}")


if __name__ == "__main__":
    main()
