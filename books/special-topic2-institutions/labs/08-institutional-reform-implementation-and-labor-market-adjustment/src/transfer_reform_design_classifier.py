from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


DESIGN_LABELS = {
    "staggered_adoption_event_study": "staggered adoption or event-study design",
    "local_enforcement_exposure": "local enforcement-intensity or capacity design",
    "randomized_information_intervention": "randomized information intervention",
    "field_experiment_compliance": "field experiment on compliance or formalization",
    "threshold_or_coverage_design": "threshold or legal-coverage design",
    "procedural_reform_event_study": "procedural reform event study",
    "administrative_rollout_did": "administrative rollout difference-in-differences",
}

IDENTIFIES = {
    "staggered_adoption_event_study": "effects of policy adoption timing for exposed places or firms",
    "local_enforcement_exposure": "effects of enforcement intensity on compliance and labor outcomes",
    "randomized_information_intervention": "effects of making rights or rules known to treated actors",
    "field_experiment_compliance": "effects of assistance, information, or enforcement pressure on compliance",
    "threshold_or_coverage_design": "local effects around a legal or administrative coverage cutoff",
    "procedural_reform_event_study": "effects of changing the procedure used to evaluate workers",
    "administrative_rollout_did": "effects of public service delivery changes across rollout areas",
}

CAUTIONS = {
    "staggered_adoption_event_study": "Check anticipation, policy bundles, and heterogeneous treatment effects.",
    "local_enforcement_exposure": "Capacity may be correlated with local labor-market trends.",
    "randomized_information_intervention": "The estimand is information, not the full legal regime.",
    "field_experiment_compliance": "Registration may not imply payroll formalization or worker protection.",
    "threshold_or_coverage_design": "The estimate is local and may miss evasion around the cutoff.",
    "procedural_reform_event_study": "Selection into the evaluation process may change after the reform.",
    "administrative_rollout_did": "Administrative rollouts are often bundled with other reforms.",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def classify(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    classified: list[dict[str, object]] = []
    counts: Counter[str] = Counter()
    for row in rows:
        family = row["design_family"]
        counts[family] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "reform_family": row["reform_family"],
                "design_family": DESIGN_LABELS[family],
                "identifying_variation": row["identifying_variation"],
                "observed_margin": row["observed_margin"],
                "identifies": IDENTIFIES[family],
                "likely_spillover": row["likely_spillover"],
                "main_caution": CAUTIONS[family],
            }
        )
    count_rows = [
        {"design_family": DESIGN_LABELS[key], "design_count": value}
        for key, value in sorted(counts.items())
    ]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 8 transfer note",
                "",
                "Each reform design identifies a particular part of the reform-transmission chain.",
                "Use the observed-margin column to avoid interpreting a compliance result as a full welfare result.",
                "Use the spillover and caution columns to state what the bounded design cannot identify.",
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
    classified, count_rows = classify(rows)
    write_csv(
        args.outdir / "design_classification.csv",
        [
            "design_id",
            "anchor",
            "reform_family",
            "design_family",
            "identifying_variation",
            "observed_margin",
            "identifies",
            "likely_spillover",
            "main_caution",
        ],
        classified,
    )
    write_csv(args.outdir / "design_family_counts.csv", ["design_family", "design_count"], count_rows)
    write_note(args.outdir / "transfer_note.txt")
    print(f"Wrote Week 8 transfer classifications to {args.outdir}")


if __name__ == "__main__":
    main()
