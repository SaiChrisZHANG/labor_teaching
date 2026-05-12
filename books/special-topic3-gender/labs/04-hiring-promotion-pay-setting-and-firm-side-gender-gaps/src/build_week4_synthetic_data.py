#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 4."""
from __future__ import annotations

import csv
import math
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def round4(value: float) -> str:
    return f"{value:.4f}"


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def make_old_boys_club_rows() -> list[dict[str, object]]:
    rng = random.Random(202606)
    rows: list[dict[str, object]] = []
    for worker_id in range(1, 721):
        female = int(worker_id % 2 == 0)
        unit = 1 + (worker_id % 12)
        cohort = 1 + (worker_id % 6)
        manager_overlap = int(((worker_id * 7 + unit) % 10) in {1, 2, 5, 8})
        baseline_performance = 0.05 * ((worker_id % 9) - 4) + rng.gauss(0.0, 0.55)
        pre_level = 1 + (worker_id % 4)
        prior_wage = 54_000 + 2_700 * pre_level + 2_000 * baseline_performance + rng.gauss(0.0, 1_100)

        informal_interaction = (
            0.40
            + 0.18 * manager_overlap
            - 0.07 * female
            + 0.17 * manager_overlap * (1 - female)
            + 0.10 * baseline_performance
            + rng.gauss(0.0, 0.08)
        )
        mentoring_score = (
            0.35
            + 0.16 * manager_overlap
            - 0.04 * female
            + 0.08 * baseline_performance
            + rng.gauss(0.0, 0.08)
        )
        promotion_probability = logistic(
            -1.65
            + 0.45 * baseline_performance
            + 0.16 * pre_level
            + 0.72 * informal_interaction
            + 0.22 * mentoring_score
            - 0.08 * female
        )
        promoted = int(rng.random() < promotion_probability)
        wage_growth = (
            0.030
            + 0.022 * promoted
            + 0.008 * manager_overlap
            + 0.010 * informal_interaction
            - 0.004 * female
            + rng.gauss(0.0, 0.010)
        )
        retained = int(rng.random() < logistic(1.55 + 0.25 * mentoring_score + 0.20 * promoted - 0.08 * female))

        rows.append(
            {
                "worker_id": worker_id,
                "unit": unit,
                "cohort": cohort,
                "female": female,
                "manager_overlap": manager_overlap,
                "baseline_performance": round4(baseline_performance),
                "pre_level": pre_level,
                "prior_wage": round4(prior_wage),
                "informal_interaction": round4(informal_interaction),
                "mentoring_score": round4(mentoring_score),
                "promoted": promoted,
                "wage_growth": round4(wage_growth),
                "retained": retained,
            }
        )
    return rows


def make_blind_audition_rows() -> list[dict[str, object]]:
    rng = random.Random(202607)
    rows: list[dict[str, object]] = []
    for candidate_id in range(1, 641):
        female = int(candidate_id % 2 == 1)
        cohort = 1 + (candidate_id % 8)
        blind_screen = int(((candidate_id * 5 + cohort) % 9) in {0, 2, 4, 7})
        baseline_score = 0.08 * ((candidate_id % 11) - 5) + rng.gauss(0.0, 0.50)
        audition_score = baseline_score + 0.04 * female + rng.gauss(0.0, 0.24)
        advancement_probability = logistic(
            -0.55
            + 1.05 * audition_score
            + 0.22 * blind_screen * female
            - 0.20 * (1 - blind_screen) * female
            + 0.08 * blind_screen
        )
        advanced = int(rng.random() < advancement_probability)
        rows.append(
            {
                "candidate_id": candidate_id,
                "cohort": cohort,
                "female": female,
                "blind_screen": blind_screen,
                "baseline_score": round4(baseline_score),
                "audition_score": round4(audition_score),
                "advanced": advanced,
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
    old_boys_rows = make_old_boys_club_rows()
    blind_audition_rows = make_blind_audition_rows()

    write_csv(ORIGINAL_DIR / "cullen_perez_truglia_old_boys_club_synthetic.csv", old_boys_rows)
    write_csv(TRANSFER_DIR / "goldin_rouse_blind_auditions_synthetic.csv", blind_audition_rows)

    print(f"Wrote {len(old_boys_rows)} manager-access rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(blind_audition_rows)} blind-screen rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
