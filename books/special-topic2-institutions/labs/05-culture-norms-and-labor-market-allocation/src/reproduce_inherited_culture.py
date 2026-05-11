from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


ORDER = [
    "egalitarian_family_role",
    "moderate_family_role",
    "traditional_family_role",
    "restrictive_family_role",
]

NUMERIC_FIELDS = [
    "origin_female_lfp",
    "origin_fertility",
    "family_role_norm_index",
    "current_peer_pressure_index",
    "host_labor_demand_index",
    "host_wage_index",
    "childcare_cost_index",
    "education_years",
    "married",
    "children_under6",
    "works_for_pay",
    "weekly_hours",
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


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["origin_norm_group"])].append(row)

    output: list[dict[str, object]] = []
    for group in ORDER:
        group_rows = grouped[group]
        output.append(
            {
                "origin_norm_group": group,
                "observations": len(group_rows),
                "origin_female_lfp": mean(group_rows, "origin_female_lfp"),
                "origin_fertility": mean(group_rows, "origin_fertility"),
                "family_role_norm_index": mean(group_rows, "family_role_norm_index"),
                "current_peer_pressure_index": mean(group_rows, "current_peer_pressure_index"),
                "host_labor_demand_index": mean(group_rows, "host_labor_demand_index"),
                "host_wage_index": mean(group_rows, "host_wage_index"),
                "childcare_cost_index": mean(group_rows, "childcare_cost_index"),
                "education_years": mean(group_rows, "education_years"),
                "children_under6_share": mean(group_rows, "children_under6"),
                "work_rate": mean(group_rows, "works_for_pay"),
                "mean_weekly_hours": mean(group_rows, "weekly_hours"),
            }
        )
    return output


def gap_rows(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    by_group = {str(row["origin_norm_group"]): row for row in summary}
    low = by_group["egalitarian_family_role"]
    high = by_group["restrictive_family_role"]
    rows = []
    for field in [
        "origin_female_lfp",
        "family_role_norm_index",
        "current_peer_pressure_index",
        "host_labor_demand_index",
        "host_wage_index",
        "childcare_cost_index",
        "work_rate",
        "mean_weekly_hours",
    ]:
        rows.append(
            {
                "comparison": "restrictive_minus_egalitarian",
                "field": field,
                "gap": round(float(high[field]) - float(low[field]), 4),
                "interpretation": interpretation(field),
            }
        )
    return rows


def interpretation(field: str) -> str:
    meanings = {
        "origin_female_lfp": "origin-country proxy for inherited work norms",
        "family_role_norm_index": "direct synthetic proxy for family-role norms",
        "current_peer_pressure_index": "current local social-pressure proxy",
        "host_labor_demand_index": "host-market demand control, not a norm proxy",
        "host_wage_index": "host wage control, not a norm proxy",
        "childcare_cost_index": "price or constraint proxy",
        "work_rate": "labor-supply outcome",
        "mean_weekly_hours": "hours outcome conditional and unconditional on work",
    }
    return meanings[field]


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 5 inherited-culture reproduction note",
                "",
                "This synthetic file is a teaching analog for Fernandez-Fogli style inherited-culture reasoning.",
                "Origin_female_lfp and family_role_norm_index are proxies for transmitted norms.",
                "Host_labor_demand_index, host_wage_index, childcare_cost_index, education, and children are price or constraint controls.",
                "A gap by origin group is not automatically a norm effect; students must diagnose selection, prices, and current peer pressure.",
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
    summary = summarize(rows)
    write_csv(
        args.outdir / "inherited_culture_summary.csv",
        [
            "origin_norm_group",
            "observations",
            "origin_female_lfp",
            "origin_fertility",
            "family_role_norm_index",
            "current_peer_pressure_index",
            "host_labor_demand_index",
            "host_wage_index",
            "childcare_cost_index",
            "education_years",
            "children_under6_share",
            "work_rate",
            "mean_weekly_hours",
        ],
        summary,
    )
    write_csv(
        args.outdir / "inherited_culture_gaps.csv",
        ["comparison", "field", "gap", "interpretation"],
        gap_rows(summary),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 5 inherited-culture outputs to {args.outdir}")


if __name__ == "__main__":
    main()
