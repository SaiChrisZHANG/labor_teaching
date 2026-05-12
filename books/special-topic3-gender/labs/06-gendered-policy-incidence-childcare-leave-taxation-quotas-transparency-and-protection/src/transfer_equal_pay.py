#!/usr/bin/env python3
"""Transfer Week 6 diagnostics to a bounded equal-pay exercise."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic equal-pay CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for transfer outputs.")
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


def group_summary(rows: list[dict[str, str]], keys: list[str], outcome: str) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["worker_periods"] = len(group)
        summary[f"mean_{outcome}"] = f"{mean([float(row[outcome]) for row in group]):.4f}"
        summaries.append(summary)
    return summaries


def gap_by_cell(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (row["rule_exposed"], row["period"], row["original_job_family"], row["female"])
        grouped[key].append(row)

    output: list[dict[str, object]] = []
    cells = sorted({(row["rule_exposed"], row["period"], row["original_job_family"]) for row in rows})
    for rule_exposed, period, job_family in cells:
        men = grouped.get((rule_exposed, period, job_family, "0"), [])
        women = grouped.get((rule_exposed, period, job_family, "1"), [])
        if not men or not women:
            continue
        output.append(
            {
                "rule_exposed": rule_exposed,
                "period": period,
                "original_job_family": job_family,
                "men_workers": len(men),
                "women_workers": len(women),
                "men_mean_wage": f"{mean([float(row['wage']) for row in men]):.4f}",
                "women_mean_wage": f"{mean([float(row['wage']) for row in women]):.4f}",
                "gap_men_minus_women": f"{mean([float(row['wage']) for row in men]) - mean([float(row['wage']) for row in women]):.4f}",
            }
        )
    return output


def segregation_response(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["rule_exposed"], row["period"])].append(row)

    output: list[dict[str, object]] = []
    for (rule_exposed, period), group in sorted(grouped.items()):
        female_track = [row for row in group if row["female_concentrated_cell"] == "1"]
        male_track = [row for row in group if row["male_concentrated_cell"] == "1"]
        changed_cell = [
            row for row in group
            if row["adjusted_job_cell"] != row["original_job_family"]
        ]
        output.append(
            {
                "rule_exposed": rule_exposed,
                "period": period,
                "worker_periods": len(group),
                "share_adjusted_job_cell": f"{len(changed_cell) / len(group):.4f}",
                "share_female_concentrated_cell": f"{len(female_track) / len(group):.4f}",
                "share_male_concentrated_cell": f"{len(male_track) / len(group):.4f}",
                "female_share": f"{mean([float(row['female']) for row in group]):.4f}",
                "mean_wage": f"{mean([float(row['wage']) for row in group]):.4f}",
            }
        )
    return output


def aggregate_gap(rows: list[dict[str, str]]) -> dict[tuple[str, str, str], float]:
    lookup: dict[tuple[str, str, str], float] = {}
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["rule_exposed"], row["period"], row["female"])].append(row)
    for key, group in grouped.items():
        lookup[key] = mean([float(row["wage"]) for row in group])
    return lookup


def transfer_diagnostics(rows: list[dict[str, str]], segregation_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    wage_lookup = aggregate_gap(rows)
    treated_pre_gap = wage_lookup[("1", "-1", "0")] - wage_lookup[("1", "-1", "1")]
    treated_post_gap = wage_lookup[("1", "1", "0")] - wage_lookup[("1", "1", "1")]
    comp_pre_gap = wage_lookup[("0", "-1", "0")] - wage_lookup[("0", "-1", "1")]
    comp_post_gap = wage_lookup[("0", "1", "0")] - wage_lookup[("0", "1", "1")]
    gap_did = (treated_post_gap - treated_pre_gap) - (comp_post_gap - comp_pre_gap)

    seg_lookup = {(row["rule_exposed"], row["period"]): row for row in segregation_rows}
    treated_seg_change = (
        float(seg_lookup[("1", "1")]["share_adjusted_job_cell"])
        - float(seg_lookup[("1", "-1")]["share_adjusted_job_cell"])
    )
    comp_seg_change = (
        float(seg_lookup[("0", "1")]["share_adjusted_job_cell"])
        - float(seg_lookup[("0", "-1")]["share_adjusted_job_cell"])
    )
    return [
        {
            "object": "average_outcome_effect",
            "observed_output": "aggregate_wage_gap_did",
            "value": f"{gap_did:.4f}",
            "interpretation": "effect of equal-pay exposure on the synthetic aggregate wage gap",
        },
        {
            "object": "firm_response",
            "observed_output": "adjusted_job_cell_share",
            "value": f"{treated_seg_change - comp_seg_change:.4f}",
            "interpretation": "job-cell segregation response induced by constraining similar-work pay gaps",
        },
        {
            "object": "incidence",
            "observed_output": "gap_did plus segregation response",
            "value": "tracked across pay and job cells",
            "interpretation": "workers may gain in comparable-cell pay while losing through sorting or classification",
        },
        {
            "object": "welfare",
            "observed_output": "not directly observed",
            "value": "NA",
            "interpretation": "welfare requires utility, mobility, job quality, firm surplus, and compliance costs",
        },
    ]


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    required = {
        "period",
        "rule_exposed",
        "female",
        "original_job_family",
        "adjusted_job_cell",
        "female_concentrated_cell",
        "male_concentrated_cell",
        "wage",
    }
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    cell_rows = gap_by_cell(rows)
    write_dicts(outdir / "equal_pay_gap_by_cell.csv", cell_rows)

    segregation_rows = segregation_response(rows)
    write_dicts(outdir / "segregation_response.csv", segregation_rows)

    diagnostics = transfer_diagnostics(rows, segregation_rows)
    write_dicts(outdir / "transfer_diagnostics.csv", diagnostics)

    note = "\n".join(
        [
            "This transfer exercise summarizes a synthetic equal-pay-for-similar-work setting.",
            "The observed margins are within-job-family wage gaps and adjusted job-cell segregation.",
            "Use the diagnostics to explain why equal-pay rules can affect both pay and sorting.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved equal-pay transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
