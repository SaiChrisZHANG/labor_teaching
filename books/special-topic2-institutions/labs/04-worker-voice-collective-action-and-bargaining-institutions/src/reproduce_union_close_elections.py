from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


ELECTION_NUMERIC_FIELDS = [
    "union_vote_share",
    "won_recognition",
    "close_to_threshold",
    "organizing_demand_index",
    "labor_market_tightness_index",
    "employer_opposition_index",
    "organizing_cost_index",
    "pre_wage_index",
    "post_wage_index",
    "wage_change",
    "employment_pre",
    "employment_post",
    "employment_change",
    "payroll_pre",
    "payroll_post",
    "payroll_change",
    "survived_three_years",
]

WORKER_NUMERIC_FIELDS = [
    "won_recognition",
    "incumbent_worker",
    "skill_index",
    "pre_wage_index",
    "post_wage_index",
    "wage_change",
    "separated_within_two_years",
    "grievance_channel_index",
]


def read_rows(path: Path, numeric_fields: list[str]) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for field in numeric_fields:
            row[field] = float(row[field])
        if "election_year" in row:
            row["election_year"] = int(row["election_year"])
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def mean_field(rows: list[dict[str, object]], field: str) -> float:
    if not rows:
        return 0.0
    return round(mean(float(row[field]) for row in rows), 4)


def group_label(row: dict[str, object]) -> str:
    if abs(float(row["union_vote_share"]) - 0.50) <= 0.10:
        return "close winner" if float(row["won_recognition"]) == 1.0 else "close loser"
    return "not close winner" if float(row["won_recognition"]) == 1.0 else "not close loser"


def group_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[group_label(row)].append(row)
    ordered = ["close loser", "close winner", "not close loser", "not close winner"]
    output: list[dict[str, object]] = []
    for label in ordered:
        group = groups[label]
        output.append(
            {
                "group": label,
                "observations": len(group),
                "mean_vote_share": mean_field(group, "union_vote_share"),
                "mean_demand": mean_field(group, "organizing_demand_index"),
                "mean_tightness": mean_field(group, "labor_market_tightness_index"),
                "mean_opposition": mean_field(group, "employer_opposition_index"),
                "mean_wage_change": mean_field(group, "wage_change"),
                "mean_employment_change": mean_field(group, "employment_change"),
                "mean_payroll_change": mean_field(group, "payroll_change"),
                "survival_share": mean_field(group, "survived_three_years"),
            }
        )
    return output


def treatment_difference(rows: list[dict[str, object]], field: str) -> float:
    winners = [row for row in rows if float(row["won_recognition"]) == 1.0]
    losers = [row for row in rows if float(row["won_recognition"]) == 0.0]
    return round(mean_field(winners, field) - mean_field(losers, field), 4)


def bandwidth_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for bandwidth in [0.04, 0.06, 0.08, 0.10, 0.15]:
        band_rows = [row for row in rows if abs(float(row["union_vote_share"]) - 0.50) <= bandwidth]
        output.append(
            {
                "bandwidth": bandwidth,
                "observations": len(band_rows),
                "winner_minus_loser_wage_change": treatment_difference(band_rows, "wage_change"),
                "winner_minus_loser_employment_change": treatment_difference(band_rows, "employment_change"),
                "winner_minus_loser_payroll_change": treatment_difference(band_rows, "payroll_change"),
                "winner_minus_loser_survival": treatment_difference(band_rows, "survived_three_years"),
            }
        )
    return output


def worker_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        recognition = "recognized" if float(row["won_recognition"]) == 1.0 else "not recognized"
        incumbent = "incumbent" if float(row["incumbent_worker"]) == 1.0 else "new hire"
        groups[f"{recognition}, {incumbent}"].append(row)
    ordered = [
        "not recognized, incumbent",
        "recognized, incumbent",
        "not recognized, new hire",
        "recognized, new hire",
    ]
    output: list[dict[str, object]] = []
    for label in ordered:
        group = groups[label]
        output.append(
            {
                "worker_group": label,
                "observations": len(group),
                "mean_wage_change": mean_field(group, "wage_change"),
                "separation_share": mean_field(group, "separated_within_two_years"),
                "mean_grievance_channel": mean_field(group, "grievance_channel_index"),
                "mean_skill": mean_field(group, "skill_index"),
            }
        )
    return output


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 4 synthetic reproduction note",
                "",
                "The close-election file treats won_recognition as the institutional threshold treatment.",
                "union_vote_share is the running variable and 0.50 is the recognition threshold.",
                "The summaries are diagnostic teaching objects, not causal estimates from real elections.",
                "Interpret close bandwidths as the DiNardo-Lee style margin: barely winning recognition among campaigns that reached an election.",
                "The matched worker-establishment file separates establishment recognition from worker wages, separations, and grievance channels.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--elections", type=Path, required=True)
    parser.add_argument("--workers", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    elections = read_rows(args.elections, ELECTION_NUMERIC_FIELDS)
    workers = read_rows(args.workers, WORKER_NUMERIC_FIELDS)
    write_csv(
        args.outdir / "close_election_group_summary.csv",
        [
            "group",
            "observations",
            "mean_vote_share",
            "mean_demand",
            "mean_tightness",
            "mean_opposition",
            "mean_wage_change",
            "mean_employment_change",
            "mean_payroll_change",
            "survival_share",
        ],
        group_summary(elections),
    )
    write_csv(
        args.outdir / "rd_bandwidth_differences.csv",
        [
            "bandwidth",
            "observations",
            "winner_minus_loser_wage_change",
            "winner_minus_loser_employment_change",
            "winner_minus_loser_payroll_change",
            "winner_minus_loser_survival",
        ],
        bandwidth_summary(elections),
    )
    write_csv(
        args.outdir / "worker_establishment_summary.csv",
        [
            "worker_group",
            "observations",
            "mean_wage_change",
            "separation_share",
            "mean_grievance_channel",
            "mean_skill",
        ],
        worker_summary(workers),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 4 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
