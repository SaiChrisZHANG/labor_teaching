from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


BARRIER_LABELS = {
    "belief_based_screening": "employer beliefs and differential treatment",
    "credential_recognition": "credential recognition and immigrant-status screening",
    "network_based_access": "networks, referrals, and occupation persistence",
    "contact_integration_design": "contact and integration as institutional design",
    "legal_public_rule": "public rules, state action, and segregation",
    "spatial_local_governance": "spatial sorting and local governance",
    "macro_misallocation": "occupational barriers and macro talent misallocation",
    "conduct_norm_boundary": "Week 5 conduct norm boundary",
}

DIAGNOSTIC_QUESTIONS = {
    "belief_based_screening": "Does a category signal change access before productivity is observed?",
    "credential_recognition": "Are skills discounted because the credential or experience is not locally legible?",
    "network_based_access": "Does group membership change referral access, insurance, or the cost of mobility?",
    "contact_integration_design": "Does the structure of interaction reduce or reinforce hierarchy?",
    "legal_public_rule": "Does a public rule or administrative practice alter category-based access?",
    "spatial_local_governance": "Does place change job access, safety, enforcement, or protection?",
    "macro_misallocation": "Do barriers reallocate talent away from high-return occupations at scale?",
    "conduct_norm_boundary": "Is the mechanism a social cost of conduct rather than category-based access?",
}

CAUTIONS = {
    "belief_based_screening": "Identifies the hiring gate, not lifecycle wages or promotion.",
    "credential_recognition": "Separate employer screening from licensing rules and true productivity.",
    "network_based_access": "Separate useful information and insurance from exclusionary closure.",
    "contact_integration_design": "External validity depends on task structure and repeated interaction.",
    "legal_public_rule": "A rule shock may not identify private spillovers or long-run persistence.",
    "spatial_local_governance": "Place can bundle labor demand, housing, transport, safety, and enforcement.",
    "macro_misallocation": "Estimates depend on assumptions about talent, barriers, and equilibrium.",
    "conduct_norm_boundary": "Reserve for Week 5 unless category membership itself governs access.",
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
    diagnostics: list[dict[str, object]] = []
    barrier_counts: Counter[str] = Counter()
    level_counts: Counter[str] = Counter()
    for row in rows:
        barrier = row["expected_barrier"]
        level = row["evidence_level"]
        barrier_counts[barrier] += 1
        level_counts[level] += 1
        diagnostics.append(
            {
                "case_id": row["case_id"],
                "anchor": row["anchor"],
                "category_signal": row["category_signal"],
                "institutional_gate": row["institutional_gate"],
                "barrier_type": BARRIER_LABELS[barrier],
                "evidence_level": level,
                "observed_margin": row["observed_margin"],
                "diagnostic_question": DIAGNOSTIC_QUESTIONS[barrier],
                "caution": CAUTIONS[barrier],
                "week_boundary": row["week_boundary"],
            }
        )

    barrier_rows = [
        {"barrier_type": BARRIER_LABELS[key], "case_count": value}
        for key, value in sorted(barrier_counts.items())
    ]
    level_rows = [
        {"evidence_level": key, "case_count": value}
        for key, value in sorted(level_counts.items())
    ]
    return diagnostics, barrier_rows, level_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 6 hierarchy diagnostic note",
                "",
                "The diagnostic table separates belief, credential, network, contact, public-rule, spatial, and macro barriers.",
                "The evidence-level table distinguishes micro gates from meso institutions and macro allocation frameworks.",
                "The boundary row is intentional: conduct norms belong in Week 5 unless category membership governs access.",
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
    diagnostics, barrier_rows, level_rows = classify(rows)
    write_csv(
        args.outdir / "barrier_diagnostic.csv",
        [
            "case_id",
            "anchor",
            "category_signal",
            "institutional_gate",
            "barrier_type",
            "evidence_level",
            "observed_margin",
            "diagnostic_question",
            "caution",
            "week_boundary",
        ],
        diagnostics,
    )
    write_csv(args.outdir / "barrier_type_counts.csv", ["barrier_type", "case_count"], barrier_rows)
    write_csv(args.outdir / "evidence_level_counts.csv", ["evidence_level", "case_count"], level_rows)
    write_note(args.outdir / "diagnostic_note.txt")
    print(f"Wrote Week 6 hierarchy diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
