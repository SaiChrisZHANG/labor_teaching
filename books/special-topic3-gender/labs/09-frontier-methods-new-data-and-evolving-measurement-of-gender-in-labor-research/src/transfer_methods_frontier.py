#!/usr/bin/env python3
"""Transfer Week 9 design logic to worker-firm and job-posting settings."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker-firm", required=True, help="Path to synthetic matched worker-firm CSV.")
    parser.add_argument("--postings", required=True, help="Path to synthetic job-posting policy CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for transfer outputs.")
    return parser.parse_args()


def read_rows(path: Path, required: set[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns in {path}: {sorted(missing)}")
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def f4(value: float) -> str:
    return f"{value:.4f}"


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def worker_firm_decomposition(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    firm_types = sorted({row["firm_type"] for row in rows})
    by_gender = {gender: [row for row in rows if row["gender"] == gender] for gender in ["man", "woman"]}
    mean_wage = {
        gender: mean([float(row["log_wage"]) for row in gender_rows]) for gender, gender_rows in by_gender.items()
    }
    shares: dict[tuple[str, str], float] = {}
    wages: dict[tuple[str, str], float] = {}
    for gender in ["man", "woman"]:
        total = len(by_gender[gender])
        for firm_type in firm_types:
            cell = [row for row in by_gender[gender] if row["firm_type"] == firm_type]
            shares[(gender, firm_type)] = len(cell) / total if total else 0.0
            wages[(gender, firm_type)] = mean([float(row["log_wage"]) for row in cell])

    total_gap = mean_wage["man"] - mean_wage["woman"]
    between = sum(
        (shares[("man", firm_type)] - shares[("woman", firm_type)]) * wages[("man", firm_type)]
        for firm_type in firm_types
    )
    within = sum(
        shares[("woman", firm_type)] * (wages[("man", firm_type)] - wages[("woman", firm_type)])
        for firm_type in firm_types
    )
    residual = total_gap - between - within
    avg_promotion_gap = mean([float(row["promoted"]) for row in by_gender["man"]]) - mean(
        [float(row["promoted"]) for row in by_gender["woman"]]
    )

    return [
        {
            "component": "total_log_wage_gap_man_minus_woman",
            "estimate": f4(total_gap),
            "interpretation": "descriptive wage gap in the synthetic worker-firm panel",
        },
        {
            "component": "between_firm_type_sorting",
            "estimate": f4(between),
            "interpretation": "part associated with different firm-type shares",
        },
        {
            "component": "within_firm_type_gap",
            "estimate": f4(within),
            "interpretation": "part associated with wage differences within firm-type cells",
        },
        {
            "component": "promotion_gap_man_minus_woman",
            "estimate": f4(avg_promotion_gap),
            "interpretation": "direct promotion margin, still descriptive without identifying variation",
        },
        {
            "component": "residual_rounding",
            "estimate": f4(residual),
            "interpretation": "rounding and interaction residual in this simple teaching decomposition",
        },
    ]


def posting_policy_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["period"]].append(row)

    ordered_periods = ["pre_ban", "post_ban"]
    output: list[dict[str, object]] = []
    period_means: dict[str, dict[str, float]] = {}
    for period in ordered_periods:
        group = grouped.get(period, [])
        period_means[period] = {
            "explicit_gender_preference_share": mean([float(row["explicit_gender_preference"]) for row in group]),
            "mean_gendered_language": mean([float(row["gendered_language_score"]) for row in group]),
            "mean_female_application_share": mean([float(row["female_application_share"]) for row in group]),
            "mean_posted_wage": mean([float(row["posted_wage"]) for row in group]),
            "mean_flexibility": mean([float(row["flexibility_score"]) for row in group]),
        }
        output.append(
            {
                "period": period,
                "ads": len(group),
                "explicit_gender_preference_share": f4(period_means[period]["explicit_gender_preference_share"]),
                "mean_gendered_language": f4(period_means[period]["mean_gendered_language"]),
                "mean_female_application_share": f4(period_means[period]["mean_female_application_share"]),
                "mean_posted_wage": f4(period_means[period]["mean_posted_wage"]),
                "mean_flexibility": f4(period_means[period]["mean_flexibility"]),
            }
        )

    output.append(
        {
            "period": "post_minus_pre",
            "ads": len(grouped.get("post_ban", [])) - len(grouped.get("pre_ban", [])),
            "explicit_gender_preference_share": f4(
                period_means["post_ban"]["explicit_gender_preference_share"]
                - period_means["pre_ban"]["explicit_gender_preference_share"]
            ),
            "mean_gendered_language": f4(
                period_means["post_ban"]["mean_gendered_language"]
                - period_means["pre_ban"]["mean_gendered_language"]
            ),
            "mean_female_application_share": f4(
                period_means["post_ban"]["mean_female_application_share"]
                - period_means["pre_ban"]["mean_female_application_share"]
            ),
            "mean_posted_wage": f4(
                period_means["post_ban"]["mean_posted_wage"] - period_means["pre_ban"]["mean_posted_wage"]
            ),
            "mean_flexibility": f4(
                period_means["post_ban"]["mean_flexibility"] - period_means["pre_ban"]["mean_flexibility"]
            ),
        }
    )
    return output


def transfer_design_map() -> list[dict[str, object]]:
    return [
        {
            "setting": "application data",
            "observed_margin": "applications by worker-job pair",
            "identifying_variation": "choice-set and job-attribute variation; causal work needs exogenous exposure or rules",
            "main_missing_margin": "jobs not shown, later firm treatment, hidden welfare costs",
            "best_use": "search and sorting decomposition",
        },
        {
            "setting": "matched worker-firm data",
            "observed_margin": "wages, firm matches, moves, promotion",
            "identifying_variation": "worker mobility across firms and policy or manager variation if available",
            "main_missing_margin": "nonapplications, unobserved tasks, climate, reasons for sorting",
            "best_use": "worker sorting versus firm treatment diagnosis",
        },
        {
            "setting": "job-posting policy data",
            "observed_margin": "ad language, stated restrictions, applications",
            "identifying_variation": "policy timing, posting bans, or platform rule changes",
            "main_missing_margin": "realized treatment after hire and equilibrium firm adaptation",
            "best_use": "demand-side text and posting-rule designs",
        },
    ]


def main() -> None:
    args = parse_args()
    worker_firm_rows = read_rows(
        Path(args.worker_firm),
        {"worker_id", "gender", "year", "firm_type", "log_wage", "promoted"},
    )
    posting_rows = read_rows(
        Path(args.postings),
        {
            "ad_id",
            "period",
            "posted_wage",
            "explicit_gender_preference",
            "gendered_language_score",
            "flexibility_score",
            "female_application_share",
        },
    )
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "worker_firm_sorting_decomposition.csv", worker_firm_decomposition(worker_firm_rows))
    write_dicts(outdir / "posting_policy_summary.csv", posting_policy_summary(posting_rows))
    write_dicts(outdir / "transfer_design_map.csv", transfer_design_map())

    note = "\n".join(
        [
            "This transfer exercise compares application, matched worker-firm, and job-posting designs.",
            "Each setting observes a different labor margin and supports a different econometric toolkit.",
            "Use the design map to state what is observed, what identifies the comparison, and what remains missing.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved Week 9 transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
