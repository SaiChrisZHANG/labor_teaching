#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 3."""
from __future__ import annotations

import csv
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def round4(value: float) -> str:
    return f"{value:.4f}"


def logistic(value: float) -> float:
    return 1.0 / (1.0 + pow(2.718281828459045, -value))


def make_role_model_rows() -> list[dict[str, object]]:
    rng = random.Random(202604)
    rows: list[dict[str, object]] = []
    for student_id in range(1, 721):
        female = int(student_id % 2 == 0)
        cohort = 1 + (student_id % 6)
        section = 1 + (student_id % 18)
        treated_section = int(section in {3, 4, 9, 10, 15, 16})
        role_model_exposure = treated_section
        baseline_gpa = 2.65 + 0.20 * ((student_id % 5) - 2) + rng.gauss(0.0, 0.18)
        prior_quant = 0.45 + 0.06 * ((student_id % 7) - 3) + rng.gauss(0.0, 0.06)
        belonging_index = 0.35 + 0.10 * female + 0.24 * female * role_model_exposure + rng.gauss(0.0, 0.08)
        expected_returns_index = 0.50 + 0.09 * role_model_exposure + 0.05 * prior_quant + rng.gauss(0.0, 0.06)
        latent_major = (
            -2.35
            + 0.50 * female
            + 0.24 * role_model_exposure
            + 0.62 * female * role_model_exposure
            + 0.38 * baseline_gpa
            + 0.75 * prior_quant
            + 0.45 * belonging_index
            + rng.gauss(0.0, 0.25)
        )
        economics_major = int(rng.random() < logistic(latent_major))
        rows.append(
            {
                "student_id": student_id,
                "cohort": cohort,
                "section": section,
                "female": female,
                "role_model_exposure": role_model_exposure,
                "baseline_gpa": round4(baseline_gpa),
                "prior_quant_index": round4(prior_quant),
                "belonging_index": round4(belonging_index),
                "expected_returns_index": round4(expected_returns_index),
                "economics_major": economics_major,
            }
        )
    return rows


def make_competitiveness_rows() -> list[dict[str, object]]:
    rng = random.Random(202605)
    rows: list[dict[str, object]] = []
    for student_id in range(1, 641):
        female = int(student_id % 2 == 1)
        math_score = 0.10 * ((student_id % 11) - 5) + rng.gauss(0.0, 0.55)
        competition_choice = int(rng.random() < logistic(-0.10 - 0.45 * female + 0.42 * math_score))
        confidence_index = 0.50 + 0.20 * math_score - 0.08 * female + rng.gauss(0.0, 0.15)
        high_variance_track = int(
            rng.random()
            < logistic(-0.65 - 0.22 * female + 0.80 * competition_choice + 0.35 * math_score + 0.22 * confidence_index)
        )
        rows.append(
            {
                "student_id": student_id,
                "female": female,
                "math_score": round4(math_score),
                "competition_choice": competition_choice,
                "confidence_index": round4(confidence_index),
                "high_variance_track": high_variance_track,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    role_model_rows = make_role_model_rows()
    competitiveness_rows = make_competitiveness_rows()

    write_csv(ORIGINAL_DIR / "porter_serra_role_models_synthetic.csv", role_model_rows)
    write_csv(TRANSFER_DIR / "buser_competitiveness_synthetic.csv", competitiveness_rows)

    print(f"Wrote {len(role_model_rows)} role-model rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(competitiveness_rows)} competitiveness rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
