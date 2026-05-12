#!/usr/bin/env python3
"""Reproduce bounded pay-transparency summaries for Week 6."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["base_pay", "bonus", "total_pay", "retained"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic pay-transparency CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def group_summary(rows: list[dict[str, str]], keys: list[str], outcomes: list[str]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["worker_periods"] = len(group)
        for outcome in outcomes:
            summary[f"mean_{outcome}"] = f"{mean([float(row[outcome]) for row in group]):.4f}"
        summaries.append(summary)
    return summaries


def baseline_balance(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    pre_rows = [row for row in rows if row["period"] == "-1"]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in pre_rows:
        grouped[row["reporting_required"]].append(row)

    output: list[dict[str, object]] = []
    for reporting_required, group in sorted(grouped.items()):
        women = [row for row in group if row["female"] == "1"]
        managers = [row for row in group if row["manager"] == "1"]
        output.append(
            {
                "reporting_required": reporting_required,
                "workers": len(group),
                "mean_firm_size": f"{mean([float(row['firm_size']) for row in group]):.4f}",
                "female_share": f"{len(women) / len(group):.4f}",
                "manager_share": f"{len(managers) / len(group):.4f}",
                "mean_total_pay": f"{mean([float(row['total_pay']) for row in group]):.4f}",
            }
        )
    return output


def pay_gap_event_study(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {
        (row["reporting_required"], row["female"], row["period"]): row
        for row in summary_rows
    }
    output: list[dict[str, object]] = []
    for reporting_required in ("0", "1"):
        for period in ("-1", "1"):
            men = lookup[(reporting_required, "0", period)]
            women = lookup[(reporting_required, "1", period)]
            output.append(
                {
                    "reporting_required": reporting_required,
                    "period": period,
                    "mean_men_total_pay": men["mean_total_pay"],
                    "mean_women_total_pay": women["mean_total_pay"],
                    "gender_gap_men_minus_women": f"{float(men['mean_total_pay']) - float(women['mean_total_pay']):.4f}",
                    "mean_men_bonus": men["mean_bonus"],
                    "mean_women_bonus": women["mean_bonus"],
                    "bonus_gap_men_minus_women": f"{float(men['mean_bonus']) - float(women['mean_bonus']):.4f}",
                    "mean_men_retained": men["mean_retained"],
                    "mean_women_retained": women["mean_retained"],
                }
            )
    return output


def make_decomposition(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {
        (row["reporting_required"], row["female"], row["period"]): row
        for row in summary_rows
    }

    rows: list[dict[str, object]] = []
    for reporting_required in ("0", "1"):
        men_pre = lookup[(reporting_required, "0", "-1")]
        men_post = lookup[(reporting_required, "0", "1")]
        women_pre = lookup[(reporting_required, "1", "-1")]
        women_post = lookup[(reporting_required, "1", "1")]
        men_pay_growth = float(men_post["mean_total_pay"]) - float(men_pre["mean_total_pay"])
        women_pay_growth = float(women_post["mean_total_pay"]) - float(women_pre["mean_total_pay"])
        men_bonus_growth = float(men_post["mean_bonus"]) - float(men_pre["mean_bonus"])
        women_bonus_growth = float(women_post["mean_bonus"]) - float(women_pre["mean_bonus"])
        pre_gap = float(men_pre["mean_total_pay"]) - float(women_pre["mean_total_pay"])
        post_gap = float(men_post["mean_total_pay"]) - float(women_post["mean_total_pay"])
        rows.append(
            {
                "reporting_required": reporting_required,
                "pre_gap": f"{pre_gap:.4f}",
                "post_gap": f"{post_gap:.4f}",
                "gap_change": f"{post_gap - pre_gap:.4f}",
                "men_total_pay_growth": f"{men_pay_growth:.4f}",
                "women_total_pay_growth": f"{women_pay_growth:.4f}",
                "women_minus_men_pay_growth": f"{women_pay_growth - men_pay_growth:.4f}",
                "men_bonus_growth": f"{men_bonus_growth:.4f}",
                "women_bonus_growth": f"{women_bonus_growth:.4f}",
                "women_minus_men_bonus_growth": f"{women_bonus_growth - men_bonus_growth:.4f}",
                "women_retention_change": f"{float(women_post['mean_retained']) - float(women_pre['mean_retained']):.4f}",
                "men_retention_change": f"{float(men_post['mean_retained']) - float(men_pre['mean_retained']):.4f}",
            }
        )

    treated = rows[1]
    comparison = rows[0]
    rows.append(
        {
            "reporting_required": "treated_minus_comparison",
            "pre_gap": "NA",
            "post_gap": "NA",
            "gap_change": f"{float(treated['gap_change']) - float(comparison['gap_change']):.4f}",
            "men_total_pay_growth": f"{float(treated['men_total_pay_growth']) - float(comparison['men_total_pay_growth']):.4f}",
            "women_total_pay_growth": f"{float(treated['women_total_pay_growth']) - float(comparison['women_total_pay_growth']):.4f}",
            "women_minus_men_pay_growth": f"{float(treated['women_minus_men_pay_growth']) - float(comparison['women_minus_men_pay_growth']):.4f}",
            "men_bonus_growth": f"{float(treated['men_bonus_growth']) - float(comparison['men_bonus_growth']):.4f}",
            "women_bonus_growth": f"{float(treated['women_bonus_growth']) - float(comparison['women_bonus_growth']):.4f}",
            "women_minus_men_bonus_growth": f"{float(treated['women_minus_men_bonus_growth']) - float(comparison['women_minus_men_bonus_growth']):.4f}",
            "women_retention_change": f"{float(treated['women_retention_change']) - float(comparison['women_retention_change']):.4f}",
            "men_retention_change": f"{float(treated['men_retention_change']) - float(comparison['men_retention_change']):.4f}",
        }
    )
    return rows


def make_diagnostics(decomposition_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    treated_minus_comparison = decomposition_rows[-1]
    return [
        {
            "object": "average_outcome_effect",
            "observed_output": "gender_gap_change",
            "value": treated_minus_comparison["gap_change"],
            "interpretation": "threshold-style transparency effect on the synthetic total-pay gap",
        },
        {
            "object": "incidence",
            "observed_output": "men_total_pay_growth; women_total_pay_growth; bonus_growth",
            "value": (
                f"men growth difference {treated_minus_comparison['men_total_pay_growth']}; "
                f"women growth difference {treated_minus_comparison['women_total_pay_growth']}"
            ),
            "interpretation": "gap change can reflect raises, slower men's pay growth, or bonus compression",
        },
        {
            "object": "firm_response",
            "observed_output": "bonus growth; retention change",
            "value": (
                f"bonus incidence {treated_minus_comparison['women_minus_men_bonus_growth']}; "
                f"women retention {treated_minus_comparison['women_retention_change']}"
            ),
            "interpretation": "observed firm margins are pay and retention; promotion and hiring remain missing",
        },
        {
            "object": "welfare",
            "observed_output": "not directly observed",
            "value": "NA",
            "interpretation": "smaller gaps do not identify utility, autonomy, job quality, or firm surplus",
        },
    ]


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    required = {"period", "firm_size", "reporting_required", "female", "manager", *OUTCOMES}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    write_dicts(outdir / "reporting_threshold_balance.csv", baseline_balance(rows))

    summary_rows = group_summary(rows, ["reporting_required", "female", "period"], OUTCOMES)
    event_rows = pay_gap_event_study(summary_rows)
    write_dicts(outdir / "pay_gap_event_study.csv", event_rows)

    decomposition_rows = make_decomposition(summary_rows)
    write_dicts(outdir / "transparency_decomposition.csv", decomposition_rows)

    diagnostics = make_diagnostics(decomposition_rows)
    write_dicts(outdir / "incidence_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This reproduction summarizes a synthetic pay-transparency threshold exercise.",
            "The treated unit is the firm above the reporting threshold.",
            "The observed margins are base pay, bonuses, total pay, and retention.",
            "Use the diagnostics to separate gap effects, incidence, firm response, and missing welfare objects.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved pay-transparency reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
