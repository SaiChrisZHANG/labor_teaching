from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


OBJECT_LABELS = {
    "audit_differential_treatment": "audit evidence on employer beliefs and differential treatment",
    "credential_resume_screening": "credential and resume evidence on immigrant-status screening",
    "network_occupation_persistence": "network evidence on referrals, insurance, and occupation persistence",
    "contact_integration": "contact experiment evidence on integration design",
    "public_rule_state_action": "historical or public-rule evidence on state action",
    "macro_talent_misallocation": "macro framework for occupational barriers and talent allocation",
    "stratification_synthesis": "stratification framework for intergroup inequality",
}

DESIGN_FAMILY = {
    "audit_differential_treatment": "audit study",
    "credential_resume_screening": "credential / resume experiment",
    "network_occupation_persistence": "network and migration design",
    "contact_integration": "contact experiment",
    "public_rule_state_action": "historical / public-rule shock",
    "macro_talent_misallocation": "macro or structural misallocation framework",
    "stratification_synthesis": "conceptual synthesis",
}

CAUTIONS = {
    "audit_differential_treatment": "Identifies first-stage differential treatment, not all later labor-market outcomes.",
    "credential_resume_screening": "Identifies employer response to visible signals, not true productivity or licensing alone.",
    "network_occupation_persistence": "Must separate network efficiency from exclusion and mobility traps.",
    "contact_integration": "Identifies the designed interaction, not the full hierarchy system.",
    "public_rule_state_action": "May require additional evidence for persistence and private-market spillovers.",
    "macro_talent_misallocation": "Depends on assumptions about talent distributions, barriers, and equilibrium wages.",
    "stratification_synthesis": "Frames mechanisms but does not itself supply a single causal estimate.",
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
                "design_family": DESIGN_FAMILY[object_key],
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
                "Week 6 transfer note",
                "",
                "Hierarchy designs identify different objects: hiring gates, credential recognition, networks, contact, public rules, macro misallocation, or stratification.",
                "For each paper, name the institutional gate before interpreting group inequality.",
                "Use the Week 5 boundary only when the mechanism is conduct rather than category-based access.",
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
            "design_family",
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
    print(f"Wrote Week 6 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
