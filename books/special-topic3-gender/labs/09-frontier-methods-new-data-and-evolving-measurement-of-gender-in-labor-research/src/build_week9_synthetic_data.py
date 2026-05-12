#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 9."""
from __future__ import annotations

import csv
import math
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


JOBS = [
    ("J01", "care", 27.0, 18, 0.78, 1, 0.18, 0.12, 0.82),
    ("J02", "care", 31.0, 32, 0.66, 0, 0.26, 0.18, 0.74),
    ("J03", "admin", 29.0, 22, 0.70, 1, 0.20, 0.22, 0.68),
    ("J04", "admin", 34.0, 38, 0.54, 0, 0.34, 0.28, 0.55),
    ("J05", "tech", 45.0, 42, 0.42, 0, 0.58, 0.64, 0.34),
    ("J06", "tech", 49.0, 30, 0.48, 1, 0.64, 0.58, 0.42),
    ("J07", "logistics", 36.0, 46, 0.32, 0, 0.46, 0.70, 0.28),
    ("J08", "logistics", 39.0, 28, 0.44, 0, 0.52, 0.62, 0.36),
    ("J09", "management", 52.0, 44, 0.30, 0, 0.72, 0.66, 0.30),
    ("J10", "management", 55.0, 34, 0.40, 1, 0.76, 0.52, 0.40),
    ("J11", "public", 33.0, 24, 0.76, 1, 0.30, 0.20, 0.80),
    ("J12", "public", 37.0, 36, 0.62, 0, 0.38, 0.26, 0.66),
]

OCCUPATION_FIT = {
    "general": {"care": 0.12, "admin": 0.10, "public": 0.08, "tech": -0.08, "logistics": -0.05, "management": -0.02},
    "technical": {"tech": 0.28, "management": 0.10, "admin": 0.06, "logistics": 0.02, "care": -0.10, "public": 0.04},
    "managerial": {"management": 0.30, "public": 0.08, "admin": 0.06, "tech": 0.04, "logistics": -0.06, "care": -0.08},
}

FIRM_TYPES = [
    ("low_premium_services", 0.10, 0.74, 0.62, 0.48),
    ("mid_premium_public", 0.32, 0.66, 0.58, 0.55),
    ("high_premium_technical", 0.62, 0.46, 0.38, 0.30),
    ("high_premium_management", 0.72, 0.40, 0.32, 0.34),
]


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def round4(value: float) -> str:
    return f"{value:.4f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_application_rows() -> list[dict[str, object]]:
    rng = random.Random(20260901)
    rows: list[dict[str, object]] = []

    for worker_num in range(1, 421):
        gender = "woman" if worker_num <= 210 else "man"
        track = rng.choices(["general", "technical", "managerial"], weights=[0.48, 0.31, 0.21], k=1)[0]
        skill = min(1.0, max(0.0, rng.gauss(0.58 if track != "general" else 0.52, 0.16)))
        care_constraint = min(1.0, max(0.0, rng.gauss(0.58 if gender == "woman" else 0.37, 0.18)))
        search_intensity = min(1.0, max(0.0, rng.gauss(0.64, 0.14) - 0.12 * care_constraint))
        risk_tolerance = min(1.0, max(0.0, rng.gauss(0.48 if gender == "woman" else 0.56, 0.16)))

        for job_id, occupation, wage, commute, flexibility, remote, firm_premium, gendered_language, family_friendly in JOBS:
            fit = OCCUPATION_FIT[track][occupation]
            wage_component = 0.055 * (wage - 35.0)
            commute_cost = 0.018 * commute * (0.55 + care_constraint)
            flexibility_value = 1.15 * flexibility * (0.50 + care_constraint)
            remote_value = 0.42 * remote * (0.40 + care_constraint)
            language_cost = gendered_language * (0.82 if gender == "woman" else 0.16)
            premium_value = firm_premium * (0.52 + 0.45 * risk_tolerance)
            score = (
                -1.35
                + 1.18 * search_intensity
                + 0.54 * skill
                + fit
                + wage_component
                + flexibility_value
                + remote_value
                + premium_value
                - commute_cost
                - language_cost
                + rng.uniform(-0.18, 0.18)
            )
            applied = int(rng.random() < logistic(score))
            callback_score = (
                -1.05
                + 1.38 * skill
                + 0.35 * firm_premium
                + 0.18 * (track == "technical" and occupation == "tech")
                + 0.12 * (track == "managerial" and occupation == "management")
                - 0.20 * (gender == "woman") * gendered_language
                + rng.uniform(-0.12, 0.12)
            )
            callback = int(applied and rng.random() < logistic(callback_score))
            rows.append(
                {
                    "worker_id": f"W{worker_num:03d}",
                    "gender": gender,
                    "track": track,
                    "skill_index": round4(skill),
                    "care_constraint": round4(care_constraint),
                    "search_intensity": round4(search_intensity),
                    "risk_tolerance": round4(risk_tolerance),
                    "job_id": job_id,
                    "occupation": occupation,
                    "posted_wage": round4(wage),
                    "commute_minutes": commute,
                    "flexibility_score": round4(flexibility),
                    "remote_option": remote,
                    "firm_premium": round4(firm_premium),
                    "gendered_language_score": round4(gendered_language),
                    "family_friendly_score": round4(family_friendly),
                    "applied": applied,
                    "callback": callback,
                }
            )
    return rows


def make_worker_firm_rows() -> list[dict[str, object]]:
    rng = random.Random(20260902)
    rows: list[dict[str, object]] = []

    for worker_num in range(1, 361):
        gender = "woman" if worker_num <= 180 else "man"
        skill = min(1.0, max(0.0, rng.gauss(0.56, 0.17)))
        care_constraint = min(1.0, max(0.0, rng.gauss(0.56 if gender == "woman" else 0.36, 0.15)))
        for year in (2021, 2022, 2023):
            firm_type, premium, flexibility, promotion_rate, climate = rng.choices(
                FIRM_TYPES,
                weights=(
                    [0.32, 0.30, 0.20, 0.18]
                    if gender == "woman"
                    else [0.22, 0.25, 0.27, 0.26]
                ),
                k=1,
            )[0]
            log_wage = (
                3.05
                + 0.62 * skill
                + 0.38 * premium
                + 0.08 * (year - 2021)
                - 0.06 * (gender == "woman") * (1.0 - flexibility)
                - 0.04 * care_constraint
                + rng.uniform(-0.04, 0.04)
            )
            promoted = int(rng.random() < max(0.02, promotion_rate + 0.12 * skill - 0.05 * care_constraint))
            rows.append(
                {
                    "worker_id": f"WF{worker_num:03d}",
                    "gender": gender,
                    "year": year,
                    "firm_type": firm_type,
                    "firm_premium": round4(premium),
                    "flexibility_score": round4(flexibility),
                    "climate_score": round4(climate),
                    "skill_index": round4(skill),
                    "care_constraint": round4(care_constraint),
                    "log_wage": round4(log_wage),
                    "promoted": promoted,
                }
            )
    return rows


def make_posting_rows() -> list[dict[str, object]]:
    rng = random.Random(20260903)
    rows: list[dict[str, object]] = []

    for ad_num in range(1, 241):
        period = "pre_ban" if ad_num <= 120 else "post_ban"
        occupation = rng.choice(["care", "admin", "tech", "logistics", "management", "public"])
        base_wage = {"care": 28, "admin": 32, "tech": 48, "logistics": 38, "management": 53, "public": 35}[occupation]
        wage = base_wage + rng.uniform(-4.0, 4.0)
        explicit_gender_preference = int(period == "pre_ban" and occupation in {"tech", "logistics", "management"} and rng.random() < 0.38)
        gendered_language = min(
            1.0,
            max(
                0.0,
                rng.gauss(0.58 if occupation in {"tech", "logistics", "management"} else 0.24, 0.12)
                - 0.18 * (period == "post_ban"),
            ),
        )
        flexibility = min(1.0, max(0.0, rng.gauss(0.38 if occupation in {"tech", "logistics", "management"} else 0.65, 0.14)))
        applications_total = max(8, int(rng.gauss(42, 10) + 12 * flexibility - 10 * explicit_gender_preference))
        female_share = min(
            0.88,
            max(
                0.12,
                0.52
                + 0.18 * flexibility
                - 0.22 * explicit_gender_preference
                - 0.20 * gendered_language
                + 0.05 * (period == "post_ban")
                + rng.uniform(-0.06, 0.06),
            ),
        )
        rows.append(
            {
                "ad_id": f"A{ad_num:03d}",
                "period": period,
                "occupation": occupation,
                "posted_wage": round4(wage),
                "explicit_gender_preference": explicit_gender_preference,
                "gendered_language_score": round4(gendered_language),
                "flexibility_score": round4(flexibility),
                "applications_total": applications_total,
                "female_application_share": round4(female_share),
            }
        )
    return rows


def main() -> None:
    application_rows = make_application_rows()
    worker_firm_rows = make_worker_firm_rows()
    posting_rows = make_posting_rows()

    write_csv(ORIGINAL_DIR / "fluchtmann_application_gap_synthetic.csv", application_rows)
    write_csv(TRANSFER_DIR / "card_worker_firm_synthetic.csv", worker_firm_rows)
    write_csv(TRANSFER_DIR / "kuhn_shen_posting_policy_synthetic.csv", posting_rows)

    print(f"Wrote {len(application_rows)} application choice-set rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(worker_firm_rows)} worker-firm rows to {TRANSFER_DIR}")
    print(f"Wrote {len(posting_rows)} posting-policy rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
