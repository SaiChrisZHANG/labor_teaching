from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


NUMERIC_FIELDS = [
    "productivity_index",
    "visibility_index",
    "enforcement_index",
    "registration_cost_index",
    "payroll_tax_index",
    "worker_skill_index",
    "benefit_value_index",
    "payroll_reported_share",
    "hidden_worker_share",
    "contract_quality_index",
    "effective_enforceability_index",
    "firm_size",
    "formal_wage_index",
    "informal_wage_index",
]


def read_rows(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for field in NUMERIC_FIELDS:
            row[field] = float(row[field])
        row["year"] = int(row["year"])
        row["registered_firm"] = int(row["registered_firm"])
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
    if value < 0.62:
        return "middle enforcement"
    return "higher enforcement"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def grouped_mean(rows: list[dict[str, object]], field: str) -> float:
    if not rows:
        return 0.0
    return round(mean(float(row[field]) for row in rows), 4)


def summarize(rows: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    registered_share = mean(int(row["registered_firm"]) for row in rows)
    wage_gap = mean(float(row["formal_wage_index"]) - float(row["informal_wage_index"]) for row in rows)
    summary = [
        {"metric": "observations", "value": len(rows)},
        {"metric": "mean_productivity", "value": grouped_mean(rows, "productivity_index")},
        {"metric": "mean_enforcement", "value": grouped_mean(rows, "enforcement_index")},
        {"metric": "registered_firm_share", "value": round(registered_share, 4)},
        {"metric": "mean_payroll_reported_share", "value": grouped_mean(rows, "payroll_reported_share")},
        {"metric": "mean_hidden_worker_share", "value": grouped_mean(rows, "hidden_worker_share")},
        {"metric": "mean_effective_enforceability", "value": grouped_mean(rows, "effective_enforceability_index")},
        {"metric": "mean_firm_size", "value": grouped_mean(rows, "firm_size")},
        {"metric": "mean_formal_informal_wage_gap", "value": round(wage_gap, 4)},
        {"metric": "corr_enforcement_payroll_reporting", "value": round(correlation(rows, "enforcement_index", "payroll_reported_share"), 4)},
        {"metric": "corr_productivity_registration", "value": round(correlation(rows, "productivity_index", "registered_firm"), 4)},
        {"metric": "corr_payroll_tax_hidden_workers", "value": round(correlation(rows, "payroll_tax_index", "hidden_worker_share"), 4)},
    ]

    enforcement_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        enforcement_groups[enforcement_tier(float(row["enforcement_index"]))].append(row)

    tier_rows: list[dict[str, object]] = []
    for tier in ["lower enforcement", "middle enforcement", "higher enforcement"]:
        group = enforcement_groups[tier]
        tier_rows.append(
            {
                "enforcement_tier": tier,
                "observations": len(group),
                "registered_firm_share": round(mean(int(row["registered_firm"]) for row in group), 4) if group else 0.0,
                "mean_payroll_reported_share": grouped_mean(group, "payroll_reported_share"),
                "mean_hidden_worker_share": grouped_mean(group, "hidden_worker_share"),
                "mean_effective_enforceability": grouped_mean(group, "effective_enforceability_index"),
                "mean_firm_size": grouped_mean(group, "firm_size"),
            }
        )

    registration_groups: dict[str, list[dict[str, object]]] = {
        "unregistered": [row for row in rows if int(row["registered_firm"]) == 0],
        "registered": [row for row in rows if int(row["registered_firm"]) == 1],
    }
    registration_rows: list[dict[str, object]] = []
    for status in ["unregistered", "registered"]:
        group = registration_groups[status]
        registration_rows.append(
            {
                "registration_status": status,
                "observations": len(group),
                "mean_productivity": grouped_mean(group, "productivity_index"),
                "mean_enforcement": grouped_mean(group, "enforcement_index"),
                "mean_payroll_reported_share": grouped_mean(group, "payroll_reported_share"),
                "mean_hidden_worker_share": grouped_mean(group, "hidden_worker_share"),
                "mean_contract_quality": grouped_mean(group, "contract_quality_index"),
                "mean_effective_enforceability": grouped_mean(group, "effective_enforceability_index"),
                "mean_firm_size": grouped_mean(group, "firm_size"),
            }
        )
    return summary, tier_rows, registration_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 3 synthetic reproduction note",
                "",
                "The synthetic panel separates firm registration from payroll reporting.",
                "registered_firm is the extensive firm-side formality margin.",
                "payroll_reported_share and hidden_worker_share are intensive employment-reporting margins.",
                "effective_enforceability_index combines contract quality with enforcement intensity.",
                "Interpretation should remain diagnostic: a real causal design would need credible variation in enforcement, registration costs, payroll taxes, or policy thresholds.",
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
    summary, tier_rows, registration_rows = summarize(rows)
    write_csv(args.outdir / "firm_margin_summary.csv", ["metric", "value"], summary)
    write_csv(
        args.outdir / "margins_by_enforcement.csv",
        [
            "enforcement_tier",
            "observations",
            "registered_firm_share",
            "mean_payroll_reported_share",
            "mean_hidden_worker_share",
            "mean_effective_enforceability",
            "mean_firm_size",
        ],
        tier_rows,
    )
    write_csv(
        args.outdir / "margins_by_registration.csv",
        [
            "registration_status",
            "observations",
            "mean_productivity",
            "mean_enforcement",
            "mean_payroll_reported_share",
            "mean_hidden_worker_share",
            "mean_contract_quality",
            "mean_effective_enforceability",
            "mean_firm_size",
        ],
        registration_rows,
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 3 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
