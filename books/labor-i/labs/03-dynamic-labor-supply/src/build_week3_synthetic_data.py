#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Labor I Week 3."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def make_reproduction_data() -> pd.DataFrame:
    rng = np.random.default_rng(2026)
    rows = []
    for worker_id in range(1, 41):
        worker_effect = rng.normal(0.0, 0.35)
        lag_high_bonus = 0
        for shift in range(1, 19):
            high_bonus = int((worker_id + shift) % 3 == 0)
            posted_wage = 1.0 + 0.2 * high_bonus
            hours = 5.8 + worker_effect + 0.45 * high_bonus - 0.12 * lag_high_bonus + rng.normal(0, 0.18)
            hours = float(np.clip(hours, 3.5, 8.5))
            deliveries = 8.0 + 1.15 * hours + 0.55 * high_bonus + rng.normal(0, 0.4)
            earnings = posted_wage * deliveries
            rows.append(
                {
                    "worker_id": worker_id,
                    "shift": shift,
                    "high_bonus": high_bonus,
                    "lag_high_bonus": lag_high_bonus,
                    "posted_wage": round(posted_wage, 3),
                    "hours": round(hours, 3),
                    "deliveries": round(float(deliveries), 3),
                    "earnings": round(float(earnings), 3),
                }
            )
            lag_high_bonus = high_bonus
    return pd.DataFrame(rows)


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(3030)
    rows = []
    for worker_id in range(1, 49):
        friction_group = "low_adjustment_cost" if worker_id % 2 == 0 else "high_adjustment_cost"
        bonus_effect = 0.58 if friction_group == "low_adjustment_cost" else 0.24
        lag_penalty = 0.06 if friction_group == "low_adjustment_cost" else 0.22
        worker_effect = rng.normal(0.0, 0.3)
        lag_high_bonus = 0
        for shift in range(1, 17):
            high_bonus = int((worker_id * shift) % 4 < 2)
            posted_wage = 1.0 + 0.2 * high_bonus
            hours = 5.7 + worker_effect + bonus_effect * high_bonus - lag_penalty * lag_high_bonus + rng.normal(0, 0.17)
            hours = float(np.clip(hours, 3.4, 8.4))
            deliveries = 7.7 + 1.18 * hours + 0.45 * high_bonus + rng.normal(0, 0.45)
            earnings = posted_wage * deliveries
            rows.append(
                {
                    "worker_id": worker_id,
                    "shift": shift,
                    "friction_group": friction_group,
                    "high_bonus": high_bonus,
                    "lag_high_bonus": lag_high_bonus,
                    "posted_wage": round(posted_wage, 3),
                    "hours": round(hours, 3),
                    "deliveries": round(float(deliveries), 3),
                    "earnings": round(float(earnings), 3),
                }
            )
            lag_high_bonus = high_bonus
    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    reproduction = make_reproduction_data()
    transfer = make_transfer_data()

    reproduction.to_csv(ORIGINAL_DIR / "fehr_goette_shift_synthetic.csv", index=False)
    transfer.to_csv(TRANSFER_DIR / "fehr_goette_persistence_synthetic.csv", index=False)

    print(f"Wrote {len(reproduction)} reproduction rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer)} transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
