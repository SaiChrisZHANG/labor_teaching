#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 2."""
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


def make_child_penalty_rows() -> list[dict[str, object]]:
    rng = random.Random(202602)
    rows: list[dict[str, object]] = []

    for household_id in range(1, 181):
        mother_fe = rng.gauss(0.0, 2.0)
        father_fe = rng.gauss(1.5, 2.0)
        mother_base_earnings = 72.0 + mother_fe + rng.gauss(0.0, 1.2)
        father_base_earnings = 79.0 + father_fe + rng.gauss(0.0, 1.2)
        mother_base_hours = 36.0 + rng.gauss(0.0, 0.8)
        father_base_hours = 41.5 + rng.gauss(0.0, 0.7)

        for event_time in range(-4, 9):
            post = max(event_time, 0)
            mother_dynamic = 0.0 if event_time < 0 else 1.0 - math.exp(-post / 2.0)
            father_dynamic = 0.0 if event_time < 0 else 1.0 - math.exp(-post / 4.0)

            for parent in ("mother", "father"):
                if parent == "mother":
                    earnings = mother_base_earnings - 4.0 * (event_time == 0) - 22.0 * mother_dynamic + rng.gauss(0.0, 1.4)
                    hours = mother_base_hours - 3.0 * (event_time == 0) - 7.2 * mother_dynamic + rng.gauss(0.0, 0.6)
                    employment = 0.94 - 0.16 * mother_dynamic + rng.gauss(0.0, 0.01)
                    job_quality = 68.0 - 7.5 * mother_dynamic + rng.gauss(0.0, 1.0)
                    care_hours = 12.0 + 18.0 * mother_dynamic + rng.gauss(0.0, 1.1)
                else:
                    earnings = father_base_earnings + 1.5 * father_dynamic + rng.gauss(0.0, 1.4)
                    hours = father_base_hours + 0.4 * father_dynamic + rng.gauss(0.0, 0.6)
                    employment = 0.97 - 0.01 * father_dynamic + rng.gauss(0.0, 0.008)
                    job_quality = 70.0 + 0.5 * father_dynamic + rng.gauss(0.0, 1.0)
                    care_hours = 8.0 + 5.2 * father_dynamic + rng.gauss(0.0, 0.9)

                rows.append(
                    {
                        "household_id": household_id,
                        "parent": parent,
                        "event_time": event_time,
                        "earnings_index": round4(earnings),
                        "hours": round4(hours),
                        "employment_rate": round4(min(max(employment, 0.50), 0.995)),
                        "job_quality_index": round4(job_quality),
                        "weekly_care_hours": round4(max(care_hours, 0.0)),
                    }
                )
    return rows


def make_ivf_rows() -> list[dict[str, object]]:
    rng = random.Random(202603)
    rows: list[dict[str, object]] = []

    for person_id in range(1, 501):
        age = 29 + (person_id % 8)
        education_years = 12 + (person_id % 7)
        prior_earnings = 62.0 + 3.0 * (education_years - 12) + rng.gauss(0.0, 4.0)
        prior_hours = 34.0 + 0.5 * (education_years - 12) + rng.gauss(0.0, 1.4)
        success_probability = 0.45 - 0.015 * max(age - 32, 0)
        ivf_success = int(rng.random() < success_probability)
        birth_probability = 0.20 + 0.45 * ivf_success
        birth_within_two_years = int(rng.random() < birth_probability)
        employment_after = 0.91 - 0.13 * birth_within_two_years + 0.01 * (education_years >= 16) + rng.gauss(0.0, 0.012)
        hours_after = prior_hours - 5.8 * birth_within_two_years + rng.gauss(0.0, 1.1)
        earnings_after = prior_earnings - 10.5 * birth_within_two_years + 0.35 * (hours_after - prior_hours) + rng.gauss(0.0, 3.2)

        rows.append(
            {
                "person_id": person_id,
                "age_at_treatment": age,
                "education_years": education_years,
                "prior_earnings_index": round4(prior_earnings),
                "prior_hours": round4(prior_hours),
                "ivf_success": ivf_success,
                "birth_within_two_years": birth_within_two_years,
                "employment_after": round4(min(max(employment_after, 0.50), 0.995)),
                "hours_after": round4(hours_after),
                "earnings_after_index": round4(earnings_after),
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
    child_penalty_rows = make_child_penalty_rows()
    ivf_rows = make_ivf_rows()

    write_csv(ORIGINAL_DIR / "kleven_child_penalty_synthetic.csv", child_penalty_rows)
    write_csv(TRANSFER_DIR / "lundborg_ivf_synthetic.csv", ivf_rows)

    print(f"Wrote {len(child_penalty_rows)} child-penalty rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(ivf_rows)} IVF-style rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
