from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


NUMERIC_FIELDS = [
    "inspector_access_index",
    "worker_knowledge_index",
    "effective_law_index",
    "compliance_index",
    "benefit_receipt_rate",
    "formal_share",
    "informal_share",
    "formal_wage_index",
]


def read_rows(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for field in NUMERIC_FIELDS + ["legal_rule_index", "local_demand_index", "wage_rigidity_index"]:
            row[field] = float(row[field])
        row["year"] = int(row["year"])
    return rows


def correlation(rows: list[dict[str, object]], left: str, right: str) -> float:
    xs = [float(row[left]) for row in rows]
    ys = [float(row[right]) for row in rows]
    xbar = mean(xs)
    ybar = mean(ys)
    numerator = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    xden = sum((x - xbar) ** 2 for x in xs) ** 0.5
    yden = sum((y - ybar) ** 2 for y in ys) ** 0.5
    if xden == 0 or yden == 0:
        return 0.0
    return numerator / (xden * yden)


def enforcement_tier(value: float) -> str:
    if value < 0.42:
        return "lower enforcement"
    if value < 0.60:
        return "middle enforcement"
    return "higher enforcement"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    summary = [
        {"metric": "mean_inspector_access", "value": round(mean(float(r["inspector_access_index"]) for r in rows), 4)},
        {"metric": "mean_worker_knowledge", "value": round(mean(float(r["worker_knowledge_index"]) for r in rows), 4)},
        {"metric": "mean_effective_law", "value": round(mean(float(r["effective_law_index"]) for r in rows), 4)},
        {"metric": "mean_compliance", "value": round(mean(float(r["compliance_index"]) for r in rows), 4)},
        {"metric": "mean_benefit_receipt", "value": round(mean(float(r["benefit_receipt_rate"]) for r in rows), 4)},
        {"metric": "mean_formal_share", "value": round(mean(float(r["formal_share"]) for r in rows), 4)},
        {"metric": "corr_inspector_compliance", "value": round(correlation(rows, "inspector_access_index", "compliance_index"), 4)},
        {"metric": "corr_inspector_formal_share", "value": round(correlation(rows, "inspector_access_index", "formal_share"), 4)},
        {"metric": "corr_inspector_formal_wage", "value": round(correlation(rows, "inspector_access_index", "formal_wage_index"), 4)},
    ]

    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[enforcement_tier(float(row["inspector_access_index"]))].append(row)

    tier_rows: list[dict[str, object]] = []
    for tier in ["lower enforcement", "middle enforcement", "higher enforcement"]:
        tier_group = groups[tier]
        tier_rows.append(
            {
                "enforcement_tier": tier,
                "observations": len(tier_group),
                "mean_inspector_access": round(mean(float(r["inspector_access_index"]) for r in tier_group), 4),
                "mean_effective_law": round(mean(float(r["effective_law_index"]) for r in tier_group), 4),
                "mean_compliance": round(mean(float(r["compliance_index"]) for r in tier_group), 4),
                "mean_benefit_receipt": round(mean(float(r["benefit_receipt_rate"]) for r in tier_group), 4),
                "mean_formal_share": round(mean(float(r["formal_share"]) for r in tier_group), 4),
                "mean_formal_wage_index": round(mean(float(r["formal_wage_index"]) for r in tier_group), 4),
            }
        )
    return summary, tier_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 2 synthetic reproduction note",
                "",
                "The legal_rule_index is constant in the bounded path, so the exercise is not a law-adoption design.",
                "The moving treatment is inspector_access_index, mediated by worker_knowledge_index into effective_law_index.",
                "The observed labor margins are compliance, benefit receipt, formal employment share, informal employment share, and formal wages.",
                "Interpretation should remain diagnostic: a real causal design would need exogenous inspection variation or stronger controls for local demand and state capacity.",
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
    summary, tier_rows = summarize(rows)
    write_csv(args.outdir / "enforcement_summary.csv", ["metric", "value"], summary)
    write_csv(
        args.outdir / "enforcement_by_tier.csv",
        [
            "enforcement_tier",
            "observations",
            "mean_inspector_access",
            "mean_effective_law",
            "mean_compliance",
            "mean_benefit_receipt",
            "mean_formal_share",
            "mean_formal_wage_index",
        ],
        tier_rows,
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 2 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
