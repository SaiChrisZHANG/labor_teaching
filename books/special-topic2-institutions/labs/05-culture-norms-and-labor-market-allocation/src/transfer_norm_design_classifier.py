from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


OBJECT_LABELS = {
    "inherited_culture_transmission": "inherited culture and transmitted role norms",
    "historical_persistence": "historical persistence of work-role norms",
    "job_entry_response": "job-entry response to acceptable-workplace framing",
    "religion_reputation_norm": "religion, reputation, and acceptable work",
    "workplace_promotion_norm": "networking and leadership-entry conduct norms",
    "local_social_environment": "current local work or unemployment norms",
    "market_supply_discipline": "market-level labor-supply and wage-acceptance discipline",
    "structural_hierarchy_week6": "structural hierarchy boundary reserved for Week 6",
}

CAUTIONS = {
    "inherited_culture_transmission": "Identifies transmission proxies, not current sanctions by peers or family.",
    "historical_persistence": "Historical proxies can bundle technology, institutions, ecology, and selection.",
    "job_entry_response": "Identifies response to the randomized entry environment, not the full norm system.",
    "religion_reputation_norm": "Separate religious conduct and reputation from legal exclusion, safety, and household constraints.",
    "workplace_promotion_norm": "Separate chosen networking conduct from structural access to networks and managers.",
    "local_social_environment": "Local social pressure can be correlated with labor demand, policy administration, and composition.",
    "market_supply_discipline": "External validity depends on repeated interaction, observability, and community enforcement.",
    "structural_hierarchy_week6": "Use Week 6 tools when category membership itself changes access, authority, or protection.",
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
        object_key = row["expected_object"]
        counts[object_key] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "identifying_variation": row["variation"],
                "unit": row["unit"],
                "observed_margin": row["observed_margin"],
                "identifies": OBJECT_LABELS[object_key],
                "diagnostic_caution": CAUTIONS[object_key],
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
                "Week 5 transfer note",
                "",
                "Norm designs identify different objects: transmission, historical persistence, entry response, reputation, promotion conduct, local pressure, or market-level discipline.",
                "The boundary row is intentional: category hierarchy and employer beliefs should move to Week 6 unless the Week 5 mechanism is explicitly acceptable conduct.",
                "For every paper, name the labor margin before using norm language.",
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
    print(f"Wrote Week 5 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
