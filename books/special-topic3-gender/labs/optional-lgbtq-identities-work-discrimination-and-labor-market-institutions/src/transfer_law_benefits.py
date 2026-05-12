#!/usr/bin/env python3
"""Transfer LGBTQ+ labor design logic to law and benefit margins."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", required=True, help="Path to synthetic marriage-policy CSV.")
    parser.add_argument("--benefits", required=True, help="Path to synthetic employer-benefit CSV.")
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


def event_bin(event_time: int) -> str:
    if event_time <= -3:
        return "leq_minus_3"
    if event_time >= 3:
        return "geq_plus_3"
    return str(event_time)


def marriage_policy_event_study(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[event_bin(int(row["event_time"]))].append(row)

    output: list[dict[str, object]] = []
    ordered_bins = ["leq_minus_3", "-2", "-1", "0", "1", "2", "geq_plus_3"]
    for bin_name in ordered_bins:
        bin_rows = grouped.get(bin_name, [])
        same_sex_rows = [row for row in bin_rows if row["couple_type"] == "same_sex_couple"]
        different_sex_rows = [row for row in bin_rows if row["couple_type"] == "different_sex_couple"]
        same_employment = mean([float(row["employment_rate"]) for row in same_sex_rows])
        different_employment = mean([float(row["employment_rate"]) for row in different_sex_rows])
        same_specialization = mean([float(row["specialization_index"]) for row in same_sex_rows])
        different_specialization = mean([float(row["specialization_index"]) for row in different_sex_rows])
        output.append(
            {
                "event_time_bin": bin_name,
                "same_sex_observations": len(same_sex_rows),
                "employment_gap_same_minus_different": f4(same_employment - different_employment),
                "specialization_gap_same_minus_different": f4(same_specialization - different_specialization),
                "observed_margin": "couple employment and specialization around legal-recognition timing",
            }
        )
    return output


def benefit_response_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row["sector"]].append(row)

    for sector, sector_rows in sorted(groups.items()):
        output.append(
            {
                "sector": sector,
                "employers": len(sector_rows),
                "pre_domestic_partner_benefit_share": f4(
                    mean([float(row["pre_domestic_partner_benefits"]) for row in sector_rows])
                ),
                "post_retained_partner_benefit_share": f4(
                    mean([float(row["post_retained_partner_benefits"]) for row in sector_rows])
                ),
                "post_expanded_spousal_coverage_share": f4(
                    mean([float(row["post_expanded_spousal_coverage"]) for row in sector_rows])
                ),
                "large_employer_share": f4(mean([float(row["large_employer"]) for row in sector_rows])),
                "unionized_share": f4(mean([float(row["unionized"]) for row in sector_rows])),
            }
        )

    output.append(
        {
            "sector": "all",
            "employers": len(rows),
            "pre_domestic_partner_benefit_share": f4(
                mean([float(row["pre_domestic_partner_benefits"]) for row in rows])
            ),
            "post_retained_partner_benefit_share": f4(
                mean([float(row["post_retained_partner_benefits"]) for row in rows])
            ),
            "post_expanded_spousal_coverage_share": f4(
                mean([float(row["post_expanded_spousal_coverage"]) for row in rows])
            ),
            "large_employer_share": f4(mean([float(row["large_employer"]) for row in rows])),
            "unionized_share": f4(mean([float(row["unionized"]) for row in rows])),
        }
    )
    return output


def transfer_design_map() -> list[dict[str, object]]:
    return [
        {
            "setting": "Tilcsik-style correspondence audit",
            "observed_margin": "callback response to randomized gay identity signal",
            "identifying_variation": "random assignment of resume signal within comparable applications",
            "main_missing_margin": "nonapplications, post-hire treatment, disclosure costs, benefits, retention",
            "best_use": "hiring discrimination at screening stage",
        },
        {
            "setting": "transgender hiring audit",
            "observed_margin": "callback response to randomized trans identity signal",
            "identifying_variation": "random assignment of trans versus cis application signal",
            "main_missing_margin": "legal documents, transition timing, workplace climate, within-job safety",
            "best_use": "comparison of identity-signal treatment across occupations and employers",
        },
        {
            "setting": "marriage-recognition event study",
            "observed_margin": "employment and specialization for same-sex and different-sex couples",
            "identifying_variation": "timing of legal recognition across jurisdictions and years",
            "main_missing_margin": "employer treatment, individual identity for unpartnered workers, climate",
            "best_use": "legal recognition and household labor-market response",
        },
        {
            "setting": "employer benefit response",
            "observed_margin": "domestic partner benefits and spousal coverage",
            "identifying_variation": "benefit design before and after legal change, with employer heterogeneity",
            "main_missing_margin": "worker take-up, valuation, disclosure, wages, and retention",
            "best_use": "benefits as labor-market compensation and institutional response",
        },
    ]


def main() -> None:
    args = parse_args()
    policy_rows = read_rows(
        Path(args.policy),
        {"state", "year", "event_time", "couple_type", "employment_rate", "specialization_index"},
    )
    benefit_rows = read_rows(
        Path(args.benefits),
        {
            "employer_id",
            "sector",
            "large_employer",
            "unionized",
            "pre_domestic_partner_benefits",
            "post_retained_partner_benefits",
            "post_expanded_spousal_coverage",
        },
    )
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "marriage_policy_event_study.csv", marriage_policy_event_study(policy_rows))
    write_dicts(outdir / "benefit_response_summary.csv", benefit_response_summary(benefit_rows))
    write_dicts(outdir / "transfer_design_map.csv", transfer_design_map())

    note = "\n".join(
        [
            "This transfer exercise compares audit, policy/event-study, and employer-benefit margins.",
            "Legal recognition is not the same object as workplace treatment.",
            "Benefit design is labor-market compensation and can move worker welfare even when wages are not observed.",
        ]
    )
    (outdir / "transfer_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved Week 10 transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
