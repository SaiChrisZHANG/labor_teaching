from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


OBJECT_LABELS = {
    "close_election_recognition": "recognition at certification threshold",
    "matched_worker_establishment_incidence": "worker and establishment incidence",
    "spillover_distribution": "spillovers and wage distribution",
    "voice_governance": "voice and governance",
    "organizing_demand": "organizing demand and formation",
    "political_feedback": "political spillovers and feedback",
    "comparative_coverage": "comparative coverage regime",
}

CAUTIONS = {
    "close_election_recognition": "Identifies marginal recognition among close campaigns, not all latent demand for unions.",
    "matched_worker_establishment_incidence": "Separate worker career effects from establishment payroll and composition effects.",
    "spillover_distribution": "Counterfactual wage structures require explicit assumptions about uncovered workers.",
    "voice_governance": "Do not reduce representation institutions to wage premia only.",
    "organizing_demand": "Observed activity reflects demand filtered through costs, opposition, law, and tightness.",
    "political_feedback": "Separate labor-market margins from downstream turnout and participation margins.",
    "comparative_coverage": "Membership, coverage, bargaining level, and extension rules are distinct objects.",
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
        identifies = row["expected_object"]
        counts[identifies] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "identifying_variation": row["variation"],
                "unit": row["unit"],
                "observed_margin": row["observed_margin"],
                "identifies": OBJECT_LABELS[identifies],
                "diagnostic_caution": CAUTIONS[identifies],
            }
        )
    count_rows = [
        {"identifies": OBJECT_LABELS[key], "design_count": value}
        for key, value in sorted(counts.items())
    ]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 4 transfer note",
                "",
                "Collective-institution designs identify different objects.",
                "Close-election RD identifies recognition at a legal threshold.",
                "Matched worker-establishment data help separate worker and firm incidence.",
                "Distributional decompositions are needed for uncovered-worker spillovers.",
                "Representation thresholds are especially useful for voice and governance.",
                "Right-to-work and bargaining-right reforms bundle labor-market and political-feedback margins.",
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
            "identifying_variation",
            "unit",
            "observed_margin",
            "identifies",
            "diagnostic_caution",
        ],
        classified,
    )
    write_csv(args.outdir / "design_object_counts.csv", ["identifies", "design_count"], count_rows)
    write_note(args.outdir / "transfer_note.txt")
    print(f"Wrote Week 4 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
