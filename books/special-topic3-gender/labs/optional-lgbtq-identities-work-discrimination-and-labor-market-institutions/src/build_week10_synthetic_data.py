#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study optional Week 10."""
from __future__ import annotations

import csv
import math
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"

OCCUPATIONS = [
    ("sales", 0.36, 0.48),
    ("clerical", 0.42, 0.54),
    ("finance", 0.30, 0.36),
    ("management", 0.28, 0.32),
    ("public", 0.46, 0.68),
    ("tech", 0.34, 0.38),
]

SECTORS = ["private_services", "finance", "tech", "public", "health"]


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def f4(value: float) -> str:
    return f"{value:.4f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_tilcsik_style_rows() -> list[dict[str, object]]:
    rng = random.Random(20261001)
    rows: list[dict[str, object]] = []

    for pair_num in range(1, 361):
        occupation, base_callback, inclusive_share = OCCUPATIONS[(pair_num - 1) % len(OCCUPATIONS)]
        employer_climate = rng.choices(
            ["low", "middle", "high"],
            weights=[0.42, 0.36, 0.22 + inclusive_share * 0.10],
            k=1,
        )[0]
        state_protection = int(rng.random() < (0.62 if employer_climate == "high" else 0.36))
        employer_size = rng.choice(["small", "medium", "large"])
        resume_quality = min(1.0, max(0.0, rng.gauss(0.61, 0.12)))
        local_unemployment = min(0.12, max(0.03, rng.gauss(0.064, 0.015)))

        for signal in ["control", "gay_signal"]:
            climate_buffer = {"low": 0.00, "middle": 0.13, "high": 0.25}[employer_climate]
            gay_penalty = -0.42 + climate_buffer + 0.07 * state_protection
            callback_index = (
                -1.02
                + 1.05 * resume_quality
                + 0.82 * base_callback
                - 2.20 * local_unemployment
                + (gay_penalty if signal == "gay_signal" else 0.0)
                + rng.uniform(-0.10, 0.10)
            )
            callback = int(rng.random() < logistic(callback_index))
            rows.append(
                {
                    "pair_id": f"P{pair_num:03d}",
                    "application_id": f"P{pair_num:03d}_{signal}",
                    "identity_signal": signal,
                    "occupation": occupation,
                    "employer_climate": employer_climate,
                    "state_protection": state_protection,
                    "employer_size": employer_size,
                    "resume_quality": f4(resume_quality),
                    "local_unemployment": f4(local_unemployment),
                    "callback": callback,
                }
            )
    return rows


def make_trans_hiring_rows() -> list[dict[str, object]]:
    rng = random.Random(20261002)
    rows: list[dict[str, object]] = []

    for pair_num in range(1, 241):
        occupation = rng.choice(["retail", "admin", "care", "tech", "public", "logistics"])
        customer_facing = int(occupation in {"retail", "care", "public"})
        employer_climate = rng.choices(["low", "middle", "high"], weights=[0.38, 0.39, 0.23], k=1)[0]
        resume_quality = min(1.0, max(0.0, rng.gauss(0.60, 0.13)))
        local_protection = int(rng.random() < (0.58 if employer_climate != "low" else 0.26))

        for signal in ["cis_signal", "trans_signal"]:
            trans_penalty = -0.48 + 0.16 * (employer_climate == "high") + 0.08 * local_protection
            trans_penalty -= 0.10 * customer_facing
            callback_index = (
                -0.88
                + 1.08 * resume_quality
                + 0.16 * (occupation in {"admin", "public"})
                + (trans_penalty if signal == "trans_signal" else 0.0)
                + rng.uniform(-0.10, 0.10)
            )
            rows.append(
                {
                    "pair_id": f"T{pair_num:03d}",
                    "application_id": f"T{pair_num:03d}_{signal}",
                    "identity_signal": signal,
                    "occupation": occupation,
                    "customer_facing": customer_facing,
                    "employer_climate": employer_climate,
                    "local_protection": local_protection,
                    "resume_quality": f4(resume_quality),
                    "callback": int(rng.random() < logistic(callback_index)),
                }
            )
    return rows


def make_marriage_policy_rows() -> list[dict[str, object]]:
    rng = random.Random(20261003)
    adoption_year = {
        "S01": 2012,
        "S02": 2013,
        "S03": 2013,
        "S04": 2014,
        "S05": 2014,
        "S06": 2015,
        "S07": 2015,
        "S08": 2015,
        "S09": 2016,
        "S10": 2016,
    }
    rows: list[dict[str, object]] = []

    for state, treated_year in adoption_year.items():
        state_effect = rng.uniform(-0.025, 0.025)
        for year in range(2010, 2019):
            event_time = year - treated_year
            post = int(event_time >= 0)
            for couple_type in ["different_sex_couple", "same_sex_couple"]:
                same_sex = int(couple_type == "same_sex_couple")
                policy_effect = same_sex * post * (0.018 + 0.004 * min(event_time, 3))
                specialization_effect = same_sex * post * (-0.016 - 0.003 * min(event_time, 3))
                employment_rate = (
                    0.742
                    - 0.024 * same_sex
                    + 0.006 * (year - 2010)
                    + state_effect
                    + policy_effect
                    + rng.uniform(-0.012, 0.012)
                )
                specialization_index = (
                    0.285
                    + 0.040 * same_sex
                    - 0.004 * (year - 2010)
                    + specialization_effect
                    + rng.uniform(-0.010, 0.010)
                )
                rows.append(
                    {
                        "state": state,
                        "year": year,
                        "event_time": event_time,
                        "post_recognition": post,
                        "couple_type": couple_type,
                        "employment_rate": f4(employment_rate),
                        "specialization_index": f4(specialization_index),
                    }
                )
    return rows


def make_benefit_rows() -> list[dict[str, object]]:
    rng = random.Random(20261004)
    rows: list[dict[str, object]] = []

    for employer_num in range(1, 301):
        sector = rng.choice(SECTORS)
        large_employer = int(rng.random() < (0.72 if sector in {"tech", "finance", "public"} else 0.45))
        unionized = int(rng.random() < (0.34 if sector in {"public", "health"} else 0.14))
        pre_domestic_partner = int(
            rng.random()
            < (
                0.30
                + 0.22 * large_employer
                + 0.12 * unionized
                + 0.16 * (sector in {"tech", "public"})
            )
        )
        retained_partner_benefits = int(
            pre_domestic_partner
            and rng.random()
            < (0.52 + 0.16 * unionized + 0.10 * (sector == "public") - 0.10 * (sector == "finance"))
        )
        expanded_spousal_coverage = int(
            rng.random()
            < (0.62 + 0.10 * large_employer + 0.08 * unionized + 0.08 * pre_domestic_partner)
        )
        rows.append(
            {
                "employer_id": f"E{employer_num:03d}",
                "sector": sector,
                "large_employer": large_employer,
                "unionized": unionized,
                "pre_domestic_partner_benefits": pre_domestic_partner,
                "post_retained_partner_benefits": retained_partner_benefits,
                "post_expanded_spousal_coverage": expanded_spousal_coverage,
            }
        )
    return rows


def main() -> None:
    audit_rows = make_tilcsik_style_rows()
    trans_rows = make_trans_hiring_rows()
    policy_rows = make_marriage_policy_rows()
    benefit_rows = make_benefit_rows()

    write_csv(ORIGINAL_DIR / "tilcsik_pride_prejudice_synthetic.csv", audit_rows)
    write_csv(TRANSFER_DIR / "granberg_andersson_ahmed_trans_hiring_synthetic.csv", trans_rows)
    write_csv(TRANSFER_DIR / "sansone_marriage_policy_synthetic.csv", policy_rows)
    write_csv(TRANSFER_DIR / "carpenter_postolek_warman_benefits_synthetic.csv", benefit_rows)

    print(f"Wrote {len(audit_rows)} Tilcsik-style audit rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(trans_rows)} transgender hiring rows to {TRANSFER_DIR}")
    print(f"Wrote {len(policy_rows)} marriage-policy rows to {TRANSFER_DIR}")
    print(f"Wrote {len(benefit_rows)} employer-benefit rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
