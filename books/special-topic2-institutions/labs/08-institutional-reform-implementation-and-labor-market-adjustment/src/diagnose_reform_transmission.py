from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


BOTTLENECK_LABELS = {
    "knowledge_beliefs": "worker and firm knowledge or beliefs",
    "implementation_capacity": "state capacity and local implementation",
    "coverage_exposure": "legal coverage and exposure",
    "private_benefit_of_formality": "low private benefit of formal compliance",
    "information_scope": "scope and salience of disclosed information",
    "administrative_delivery": "administrative delivery and agency quality",
}

BOTTLENECK_DIAGNOSTICS = {
    "knowledge_beliefs": "Measure whether actors know the rule and believe it can be invoked.",
    "implementation_capacity": "Measure inspectors, courts, records, sanctions, and local administrative reach.",
    "coverage_exposure": "Separate covered workers and firms from those outside the legal margin.",
    "private_benefit_of_formality": "Ask whether registration changes benefits, credit, procurement, or worker coverage.",
    "information_scope": "Track which pay, procedure, or comparison information is actually disclosed.",
    "administrative_delivery": "Name the agency task and test whether service quality changed.",
}

RISK_LABELS = {
    "low": "low interpretation risk",
    "medium": "medium interpretation risk",
    "high": "high interpretation risk",
}

WELFARE_LABELS = {
    "take_up_and_bargaining": "take-up, bargaining power, and information quality",
    "incidence_and_displacement": "incidence, displacement, and uncovered-worker spillovers",
    "employment_security_vs_hiring": "employment security versus hiring and entry margins",
    "registration_vs_worker_protection": "registration gains versus worker-protection gains",
    "inequality_and_average_wages": "inequality, pay compression, and average wage growth",
    "matching_and_incidence": "matching quality, benefit transitions, and incidence",
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


def classify(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    classified: list[dict[str, object]] = []
    bottleneck_counts: Counter[str] = Counter()
    welfare_counts: Counter[str] = Counter()
    for row in rows:
        bottleneck = row["primary_bottleneck"]
        welfare = row["welfare_margin"]
        bottleneck_counts[bottleneck] += 1
        welfare_counts[welfare] += 1
        classified.append(
            {
                "case_id": row["case_id"],
                "anchor": row["anchor"],
                "reform_family": row["reform_family"],
                "identifying_variation": row["identifying_variation"],
                "observed_margin": row["observed_margin"],
                "primary_bottleneck": BOTTLENECK_LABELS[bottleneck],
                "secondary_bottleneck": row["secondary_bottleneck"],
                "welfare_margin": WELFARE_LABELS[welfare],
                "interpretation_risk": RISK_LABELS[row["expected_risk"]],
                "diagnostic_next_step": BOTTLENECK_DIAGNOSTICS[bottleneck],
            }
        )

    bottleneck_rows = [
        {"primary_bottleneck": BOTTLENECK_LABELS[key], "case_count": value}
        for key, value in sorted(bottleneck_counts.items())
    ]
    welfare_rows = [
        {"welfare_margin": WELFARE_LABELS[key], "case_count": value}
        for key, value in sorted(welfare_counts.items())
    ]
    return classified, bottleneck_rows, welfare_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 8 reform-transmission diagnostic note",
                "",
                "Every reform case should identify the legal change, the implementation actor, exposure, and the observed labor margin.",
                "The bottleneck column says which part of the transmission chain is most likely to limit the reform.",
                "The welfare column reminds students that compliance, take-up, incidence, spillovers, and inequality are distinct objects.",
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
    classified, bottleneck_rows, welfare_rows = classify(rows)
    write_csv(
        args.outdir / "reform_transmission_diagnostic.csv",
        [
            "case_id",
            "anchor",
            "reform_family",
            "identifying_variation",
            "observed_margin",
            "primary_bottleneck",
            "secondary_bottleneck",
            "welfare_margin",
            "interpretation_risk",
            "diagnostic_next_step",
        ],
        classified,
    )
    write_csv(args.outdir / "bottleneck_counts.csv", ["primary_bottleneck", "case_count"], bottleneck_rows)
    write_csv(args.outdir / "welfare_margin_counts.csv", ["welfare_margin", "case_count"], welfare_rows)
    write_note(args.outdir / "diagnostic_note.txt")
    print(f"Wrote Week 8 reform diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
