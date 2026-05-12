#!/usr/bin/env python3
"""Reproduce a compact research-design table from Week 10 candidate ideas."""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = [
    "project_id",
    "title",
    "labor_object",
    "mechanism",
    "comparison_group",
    "key_margin",
    "data_source",
    "method",
    "welfare_object",
    "portability_claim",
    "main_threat",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    missing = [col for col in REQUIRED_COLUMNS if col not in rows[0]]
    if missing:
        raise ValueError(f"Missing required columns in {path}: {missing}")
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_design_table(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    design_rows: list[dict[str, str]] = []
    for row in rows:
        design_sentence = (
            f"Use {row['method']} with {row['data_source']} to study how "
            f"{row['mechanism']} changes {row['labor_object']}."
        )
        design_rows.append(
            {
                "project_id": row["project_id"],
                "title": row["title"],
                "labor_object": row["labor_object"],
                "mechanism": row["mechanism"],
                "comparison_group": row["comparison_group"],
                "key_margin": row["key_margin"],
                "data_source": row["data_source"],
                "method": row["method"],
                "welfare_object": row["welfare_object"],
                "portability_claim": row["portability_claim"],
                "design_sentence": design_sentence,
            }
        )
    return design_rows


def build_counts(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    counts = Counter((row.get("domain", "unknown"), row["method"]) for row in rows)
    return [
        {"domain": domain, "method": method, "candidate_ideas": count}
        for (domain, method), count in sorted(counts.items())
    ]


def write_note(path: Path, rows: list[dict[str, str]]) -> None:
    methods = sorted({row["method"] for row in rows})
    objects = sorted({row["labor_object"] for row in rows})
    text = [
        "Week 10 reproduction note",
        "==========================",
        "",
        f"Candidate ideas: {len(rows)}",
        f"Distinct methods: {len(methods)}",
        f"Distinct labor objects: {len(objects)}",
        "",
        "The reproduction step does not estimate causal effects. It verifies that each idea is represented as a labor object, mechanism, comparison group, data source, method, welfare object, and contribution-ready design sentence.",
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
    design_rows = build_design_table(rows)
    count_rows = build_counts(rows)
    write_csv(args.outdir / "research_design_table.csv", design_rows)
    write_csv(args.outdir / "object_method_counts.csv", count_rows)
    write_note(args.outdir / "reproduction_note.txt", rows)
    print(f"Saved Week 10 reproduced design outputs to {args.outdir}")


if __name__ == "__main__":
    main()
