#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Labor I Week 5."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def make_reproduction_data() -> pd.DataFrame:
    rng = np.random.default_rng(202605)
    regions = ["atlantic", "quebec", "ontario", "prairies"]
    rows = []
    for person_id in range(1, 721):
        cohort = 1936 + ((person_id - 1) % 18)
        region = regions[(person_id - 1) % len(regions)]
        reform_region = int(region in {"quebec", "ontario"})
        post_reform = int(cohort >= 1946)
        compulsory_schooling = int(reform_region * post_reform)
        parental_schooling = rng.integers(7, 17)
        ability = rng.normal(0.0, 0.75)
        urban = int((person_id * 7) % 10 < 6)
        experience = max(4, min(42, 60 - (cohort - 1936) - rng.integers(10, 15)))
        schooling = (
            10.4
            + 0.95 * compulsory_schooling
            + 0.25 * reform_region
            + 0.38 * urban
            + 0.16 * parental_schooling
            + 0.55 * ability
            + 0.03 * (cohort - 1944)
            + rng.normal(0.0, 0.55)
        )
        log_wage = (
            1.58
            + 0.071 * schooling
            + 0.032 * experience
            - 0.00046 * experience**2
            + 0.055 * urban
            + 0.028 * reform_region
            + 0.048 * ability
            + rng.normal(0.0, 0.12)
        )
        rows.append(
            {
                "person_id": person_id,
                "birth_cohort": cohort,
                "region": region,
                "reform_region": reform_region,
                "post_reform": post_reform,
                "compulsory_schooling": compulsory_schooling,
                "parental_schooling": int(parental_schooling),
                "urban": urban,
                "experience": int(experience),
                "schooling_years": round(float(schooling), 4),
                "log_wage": round(float(log_wage), 4),
            }
        )
    return pd.DataFrame(rows)


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(202606)
    trend_map = {"stable_trend": 0.010, "rising_trend": 0.018, "steep_trend": 0.027}
    reform_map = {"stable_trend": 1947, "rising_trend": 1946, "steep_trend": 1948}
    rows = []
    person_id = 1
    for trend_group, trend_slope in trend_map.items():
        reform_cutoff = reform_map[trend_group]
        for cohort in range(1938, 1958):
            for _ in range(18):
                reform = int(cohort >= reform_cutoff)
                parental_schooling = rng.integers(6, 17)
                background = rng.normal(0.0, 0.8)
                schooling = (
                    10.1
                    + 0.82 * reform
                    + 0.18 * parental_schooling
                    + 0.10 * (cohort - 1947)
                    + 0.28 * background
                    + rng.normal(0.0, 0.58)
                )
                log_wage = (
                    1.52
                    + 0.066 * schooling
                    + trend_slope * (cohort - 1947)
                    + 0.020 * parental_schooling
                    + 0.04 * background
                    + rng.normal(0.0, 0.13)
                )
                rows.append(
                    {
                        "person_id": person_id,
                        "birth_cohort": cohort,
                        "trend_group": trend_group,
                        "reform": reform,
                        "parental_schooling": int(parental_schooling),
                        "schooling_years": round(float(schooling), 4),
                        "log_wage": round(float(log_wage), 4),
                    }
                )
                person_id += 1
    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    reproduction = make_reproduction_data()
    transfer = make_transfer_data()

    reproduction.to_csv(ORIGINAL_DIR / "oreopoulos_schooling_synthetic.csv", index=False)
    transfer.to_csv(TRANSFER_DIR / "stephens_yang_trends_synthetic.csv", index=False)

    print(f"Wrote {len(reproduction)} reproduction rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer)} transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
