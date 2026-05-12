#!/usr/bin/env python3
"""Create a short research-memo scaffold for one Week 10 project idea."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def choose_project(
    ideas: list[dict[str, str]],
    scores: list[dict[str, str]],
    project_id: str | None,
) -> dict[str, str]:
    by_id = {row["project_id"]: row for row in ideas}
    if project_id:
        if project_id not in by_id:
            raise ValueError(f"Unknown project_id {project_id}")
        return by_id[project_id]

    ranked = sorted(scores, key=lambda row: (-int(row["total_score"]), row["project_id"]))
    selected_id = ranked[0]["project_id"]
    return by_id[selected_id]


def memo_fields(row: dict[str, str]) -> list[dict[str, str]]:
    contribution = (
        f"This project uses {row['method']} in a {row['data_source']} setting to identify how "
        f"{row['mechanism']} changes {row['labor_object']}, with implications for "
        f"{row['welfare_object']}."
    )
    return [
        {"field": "research_question", "draft": f"How does {row['mechanism']} shape {row['labor_object']}?"},
        {"field": "labor_market_object", "draft": row["labor_object"]},
        {"field": "mechanism", "draft": row["mechanism"]},
        {"field": "comparison_group_or_counterfactual", "draft": row["comparison_group"]},
        {"field": "key_labor_margin", "draft": row["key_margin"]},
        {"field": "data_source", "draft": row["data_source"]},
        {"field": "identification_strategy", "draft": row["method"]},
        {"field": "main_threats", "draft": row["main_threat"]},
        {"field": "portability_and_broad_relevance", "draft": row["portability_claim"]},
        {"field": "welfare_or_distributional_object", "draft": row["welfare_object"]},
        {"field": "contribution", "draft": contribution},
    ]


def write_memo(path: Path, row: dict[str, str], fields: list[dict[str, str]]) -> None:
    sections = {
        item["field"]: item["draft"]
        for item in fields
    }
    text = [
        f"# Research Memo Scaffold: {row['title']}",
        "",
        "## Research Question",
        sections["research_question"],
        "",
        "## Labor-Market Object",
        sections["labor_market_object"],
        "",
        "## Mechanism",
        sections["mechanism"],
        "",
        "## Comparison Group Or Counterfactual",
        sections["comparison_group_or_counterfactual"],
        "",
        "## Key Labor Margin",
        sections["key_labor_margin"],
        "",
        "## Data Source",
        sections["data_source"],
        "",
        "## Identification Strategy",
        sections["identification_strategy"],
        "",
        "## Main Threats",
        sections["main_threats"],
        "",
        "## Portability And Broad Relevance",
        sections["portability_and_broad_relevance"],
        "",
        "## Welfare Or Distributional Object",
        sections["welfare_or_distributional_object"],
        "",
        "## Contribution",
        sections["contribution"],
        "",
        "## Revision Prompts",
        "",
        "1. What would make the comparison group more credible?",
        "2. Which important labor margin remains unobserved?",
        "3. What should travel beyond this setting, and what should not?",
        "4. What claim would be overreaching?",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(text) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ideas", required=True, type=Path)
    parser.add_argument("--scores", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    parser.add_argument("--project-id", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ideas = read_rows(args.ideas)
    scores = read_rows(args.scores)
    selected = choose_project(ideas, scores, args.project_id)
    fields = memo_fields(selected)
    write_csv(args.outdir / "memo_fields.csv", fields)
    write_memo(args.outdir / "research_memo_scaffold.md", selected, fields)
    print(f"Saved memo scaffold for {selected['project_id']} to {args.outdir}")


if __name__ == "__main__":
    main()
