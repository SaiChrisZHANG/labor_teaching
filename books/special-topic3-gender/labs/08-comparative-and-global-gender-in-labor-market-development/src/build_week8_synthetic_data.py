#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 8."""
from __future__ import annotations

import csv
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


REGIMES = [
    ("nordic_care_state", "high_income_welfare", 0.86, 0.78, 0.86, 0.83, 0.22, 0.18, 0.34),
    ("continental_part_time", "high_income_welfare", 0.72, 0.68, 0.83, 0.78, 0.30, 0.25, 0.24),
    ("service_transition", "middle_income_transition", 0.48, 0.62, 0.58, 0.61, 0.42, 0.40, 0.20),
    ("public_employment", "public_employment_heavy", 0.54, 0.55, 0.66, 0.70, 0.45, 0.36, 0.38),
    ("high_informality", "low_income_high_informality", 0.28, 0.39, 0.38, 0.34, 0.63, 0.58, 0.10),
    ("restrictive_norms", "strong_norm_restrictive_law", 0.36, 0.44, 0.42, 0.46, 0.76, 0.66, 0.18),
]


TRANSFER_SETTINGS = [
    ("care_bind_high_service", 0.78, 0.84, 0.38, 0.22, 0.24, 0.79),
    ("norm_bind_high_service", 0.38, 0.78, 0.76, 0.50, 0.28, 0.58),
    ("mobility_bind_transition", 0.46, 0.62, 0.57, 0.70, 0.48, 0.54),
    ("informality_bind_legal_reform", 0.42, 0.52, 0.51, 0.44, 0.69, 0.74),
    ("public_jobs_with_care", 0.62, 0.55, 0.43, 0.32, 0.35, 0.82),
]


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


def bounded(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return min(high, max(low, value))


def make_family_policy_rows() -> list[dict[str, object]]:
    rng = random.Random(20260801)
    rows: list[dict[str, object]] = []
    country_id = 0

    for (
        regime_name,
        regime_type,
        care_index,
        service_share,
        legal_access,
        formality_rate,
        norm_restrictiveness,
        mobility_cost,
        public_employment_share,
    ) in REGIMES:
        for country_slot in range(1, 7):
            country_id += 1
            country_effect = rng.uniform(-0.035, 0.035)
            for year in (2005, 2012, 2019):
                trend = (year - 2005) / 14.0
                care = bounded(care_index + 0.055 * trend + rng.uniform(-0.025, 0.025))
                services = bounded(service_share + 0.045 * trend + rng.uniform(-0.030, 0.030))
                legal = bounded(legal_access + 0.025 * trend + rng.uniform(-0.020, 0.020))
                formal = bounded(formality_rate + 0.035 * trend + rng.uniform(-0.030, 0.030))
                norms = bounded(norm_restrictiveness - 0.030 * trend + rng.uniform(-0.025, 0.025))
                mobility = bounded(mobility_cost - 0.020 * trend + rng.uniform(-0.025, 0.025))
                public_jobs = bounded(public_employment_share + rng.uniform(-0.018, 0.018))
                leave_generosity = bounded(0.38 + 0.42 * care + 0.10 * legal + rng.uniform(-0.025, 0.025))

                female_lfp = bounded(
                    0.24
                    + 0.23 * care
                    + 0.24 * services
                    + 0.13 * legal
                    + 0.09 * formal
                    + 0.05 * public_jobs
                    - 0.20 * norms
                    - 0.12 * mobility
                    + country_effect
                    + rng.uniform(-0.018, 0.018)
                )
                female_hours = bounded(
                    0.38
                    + 0.20 * services
                    + 0.13 * care
                    + 0.06 * formal
                    - 0.11 * norms
                    - 0.08 * mobility
                    + rng.uniform(-0.016, 0.016)
                )
                job_continuity = bounded(
                    0.32
                    + 0.30 * care
                    + 0.16 * leave_generosity
                    + 0.10 * legal
                    + 0.07 * formal
                    - 0.12 * norms
                    + rng.uniform(-0.020, 0.020)
                )
                gender_wage_gap = bounded(
                    0.34
                    - 0.10 * care
                    - 0.09 * formal
                    - 0.07 * legal
                    - 0.04 * public_jobs
                    + 0.10 * norms
                    + 0.05 * mobility
                    + rng.uniform(-0.014, 0.014),
                    low=0.05,
                    high=0.42,
                )

                rows.append(
                    {
                        "country_id": f"C{country_id:02d}",
                        "regime": regime_name,
                        "regime_type": regime_type,
                        "year": year,
                        "care_index": round4(care),
                        "leave_generosity": round4(leave_generosity),
                        "service_share": round4(services),
                        "legal_access_index": round4(legal),
                        "formality_rate": round4(formal),
                        "norm_restrictiveness": round4(norms),
                        "mobility_cost": round4(mobility),
                        "public_employment_share": round4(public_jobs),
                        "female_lfp": round4(female_lfp),
                        "female_hours": round4(female_hours),
                        "job_continuity": round4(job_continuity),
                        "gender_wage_gap": round4(gender_wage_gap),
                    }
                )
    return rows


def make_transfer_rows() -> list[dict[str, object]]:
    rng = random.Random(20260802)
    rows: list[dict[str, object]] = []

    for setting, care, service, norms, mobility, informality, legal in TRANSFER_SETTINGS:
        for cell in range(1, 41):
            local_care = bounded(care + rng.uniform(-0.06, 0.06))
            local_service = bounded(service + rng.uniform(-0.07, 0.07))
            local_norms = bounded(norms + rng.uniform(-0.06, 0.06))
            local_mobility = bounded(mobility + rng.uniform(-0.06, 0.06))
            local_informality = bounded(informality + rng.uniform(-0.06, 0.06))
            local_legal = bounded(legal + rng.uniform(-0.04, 0.04))
            demand_opportunity = bounded(0.28 + 0.44 * local_service + 0.16 * (1 - local_informality))
            supply_feasibility = bounded(
                0.20 + 0.34 * local_care + 0.19 * local_legal - 0.25 * local_norms - 0.17 * local_mobility
            )
            female_lfp = bounded(
                0.18
                + 0.42 * supply_feasibility
                + 0.31 * demand_opportunity
                - 0.10 * local_informality
                + rng.uniform(-0.020, 0.020)
            )
            acceptable_service_jobs = bounded(
                0.15 + 0.47 * local_service - 0.28 * local_norms - 0.18 * local_mobility + rng.uniform(-0.020, 0.020)
            )
            transportability_score = bounded(
                0.25
                + 0.22 * local_care
                + 0.18 * local_legal
                + 0.16 * local_service
                - 0.18 * local_norms
                - 0.14 * local_informality
                - 0.11 * local_mobility
            )
            rows.append(
                {
                    "setting": setting,
                    "local_cell": cell,
                    "care_index": round4(local_care),
                    "service_share": round4(local_service),
                    "norm_restrictiveness": round4(local_norms),
                    "mobility_cost": round4(local_mobility),
                    "informality_rate": round4(local_informality),
                    "legal_access_index": round4(local_legal),
                    "demand_opportunity": round4(demand_opportunity),
                    "supply_feasibility": round4(supply_feasibility),
                    "female_lfp": round4(female_lfp),
                    "acceptable_service_jobs": round4(acceptable_service_jobs),
                    "transportability_score": round4(transportability_score),
                }
            )
    return rows


def main() -> None:
    family_rows = make_family_policy_rows()
    transfer_rows = make_transfer_rows()

    write_csv(ORIGINAL_DIR / "olivetti_petrongolo_family_policy_synthetic.csv", family_rows)
    write_csv(TRANSFER_DIR / "jayachandran_norms_transfer_synthetic.csv", transfer_rows)

    print(f"Wrote {len(family_rows)} comparative family-policy rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer_rows)} norms-transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
