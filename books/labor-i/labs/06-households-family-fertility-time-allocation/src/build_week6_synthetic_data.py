#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Labor I Week 6."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def make_reproduction_data() -> pd.DataFrame:
    rng = np.random.default_rng(202606)
    rows = []
    for person_id in range(1, 641):
        age = 29 + ((person_id - 1) % 9)
        education = rng.integers(12, 19)
        prior_children = int((person_id % 6) == 0)
        partner_income = 40 + 4.2 * education + rng.normal(0.0, 8.0)
        baseline_hours = 33.5 + 0.65 * education - 1.8 * prior_children + rng.normal(0.0, 2.2)
        baseline_earnings = 54 + 4.8 * education + 0.55 * baseline_hours + rng.normal(0.0, 7.5)
        ivf_success = int(rng.random() < (0.42 + 0.015 * (age < 33) - 0.03 * prior_children))
        birth_within_two_years = int(rng.random() < (0.24 + 0.48 * ivf_success + 0.05 * prior_children))
        employment_after = 0.90 - 0.14 * birth_within_two_years + 0.015 * (education >= 16) + rng.normal(0.0, 0.025)
        employment_after = float(np.clip(employment_after, 0.55, 0.99))
        hours_after = baseline_hours - 5.2 * birth_within_two_years + 0.7 * ivf_success + rng.normal(0.0, 1.4)
        earnings_after = baseline_earnings - 11.0 * birth_within_two_years - 0.23 * partner_income + 0.52 * hours_after + rng.normal(0.0, 5.6)
        rows.append(
            {
                "person_id": person_id,
                "age_at_treatment": age,
                "education_years": int(education),
                "prior_children": prior_children,
                "partner_income_index": round(float(partner_income), 4),
                "baseline_hours": round(float(baseline_hours), 4),
                "baseline_earnings_index": round(float(baseline_earnings), 4),
                "ivf_success": ivf_success,
                "birth_within_two_years": birth_within_two_years,
                "employment_after": round(float(employment_after), 4),
                "hours_after": round(float(hours_after), 4),
                "earnings_after_index": round(float(earnings_after), 4),
            }
        )
    return pd.DataFrame(rows)


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(202607)
    rows = []
    household_id = 1
    for household_id in range(1, 241):
        mother_fe = rng.normal(0.0, 0.12)
        father_fe = rng.normal(0.08, 0.12)
        mother_base_hours = 35.5 + rng.normal(0.0, 1.5)
        father_base_hours = 41.0 + rng.normal(0.0, 1.2)
        mother_base_earnings = 3.62 + mother_fe
        father_base_earnings = 3.78 + father_fe
        for event_time in range(-5, 11):
            mother_penalty = 0.0 if event_time < 0 else -0.08 - 0.22 * (1 - np.exp(-event_time / 2.2))
            father_penalty = 0.0 if event_time < 0 else 0.008 * (1 - np.exp(-event_time / 3.8))
            mother_hours_penalty = 0.0 if event_time < 0 else -3.4 - 4.0 * (1 - np.exp(-event_time / 2.4))
            father_hours_penalty = 0.0 if event_time < 0 else -0.2 + 0.3 * (1 - np.exp(-event_time / 4.0))
            mother_participation = 0.93 if event_time < 0 else 0.93 - 0.17 * (1 - np.exp(-event_time / 2.0))
            father_participation = 0.97 if event_time < 0 else 0.97 - 0.01 * (1 - np.exp(-event_time / 4.0))

            for parent, base_earnings, earn_penalty, base_hours, hour_penalty, participation in [
                ("mother", mother_base_earnings, mother_penalty, mother_base_hours, mother_hours_penalty, mother_participation),
                ("father", father_base_earnings, father_penalty, father_base_hours, father_hours_penalty, father_participation),
            ]:
                rows.append(
                    {
                        "household_id": household_id,
                        "parent": parent,
                        "event_time": event_time,
                        "log_earnings": round(float(base_earnings + earn_penalty + rng.normal(0.0, 0.03)), 4),
                        "hours": round(float(base_hours + hour_penalty + rng.normal(0.0, 0.45)), 4),
                        "participation_rate": round(float(np.clip(participation + rng.normal(0.0, 0.012), 0.55, 0.995)), 4),
                    }
                )
    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    reproduction = make_reproduction_data()
    transfer = make_transfer_data()

    reproduction.to_csv(ORIGINAL_DIR / "lundborg_ivf_synthetic.csv", index=False)
    transfer.to_csv(TRANSFER_DIR / "kleven_child_penalty_synthetic.csv", index=False)

    print(f"Wrote {len(reproduction)} reproduction rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer)} transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
