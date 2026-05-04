#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Labor I Week 7."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def logistic(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def make_reproduction_data() -> pd.DataFrame:
    rng = np.random.default_rng(202607)
    rows: list[dict[str, float | int | str]] = []
    choice_id = 1
    for worker_id in range(1, 501):
        caregiver = int(worker_id % 5 in {1, 2})
        long_commute = int(worker_id % 4 == 0)
        for _ in range(6):
            wage_a = rng.integers(20, 35)
            wage_b = rng.integers(20, 35)
            predictable_a = int(rng.random() < 0.52)
            predictable_b = int(rng.random() < 0.52)
            remote_a = int(rng.random() < 0.34)
            remote_b = int(rng.random() < 0.34)
            flexibility_a = int(rng.random() < 0.45)
            flexibility_b = int(rng.random() < 0.45)

            beta_w = 0.28
            beta_predictable = 0.85 + 0.45 * caregiver
            beta_remote = 0.55 + 0.40 * long_commute
            beta_flexibility = 1.00 + 0.35 * caregiver

            utility_diff = (
                beta_w * (wage_a - wage_b)
                + beta_predictable * (predictable_a - predictable_b)
                + beta_remote * (remote_a - remote_b)
                + beta_flexibility * (flexibility_a - flexibility_b)
                + rng.normal(0.0, 0.85)
            )
            choose_a = int(rng.random() < logistic(np.array([utility_diff]))[0])

            rows.append(
                {
                    "choice_id": choice_id,
                    "worker_id": worker_id,
                    "caregiver": caregiver,
                    "long_commute": long_commute,
                    "wage_a": int(wage_a),
                    "wage_b": int(wage_b),
                    "predictable_a": predictable_a,
                    "predictable_b": predictable_b,
                    "remote_a": remote_a,
                    "remote_b": remote_b,
                    "flexibility_a": flexibility_a,
                    "flexibility_b": flexibility_b,
                    "chosen_offer_a": choose_a,
                }
            )
            choice_id += 1
    return pd.DataFrame(rows)


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(202608)
    rows: list[dict[str, float | int | str]] = []
    for worker_id in range(1, 721):
        worker_group = "professional_track" if worker_id % 5 in {0, 1} else "frontline_track"
        premium = int(worker_group == "professional_track")
        hourly_wage = (
            22.0
            + 8.5 * premium
            + rng.normal(0.0, 2.4)
        )
        predictable_schedule = int(rng.random() < (0.76 if premium else 0.44))
        remote_option = int(rng.random() < (0.58 if premium else 0.12))
        low_injury_risk = int(rng.random() < (0.84 if premium else 0.52))
        autonomy_score = float(
            np.clip(rng.normal(0.74 if premium else 0.39, 0.12), 0.05, 1.0)
        )
        commute_minutes = int(
            np.clip(rng.normal(24 if premium else 39, 8), 8, 75)
        )
        rows.append(
            {
                "worker_id": worker_id,
                "worker_group": worker_group,
                "hourly_wage": round(float(hourly_wage), 3),
                "predictable_schedule": predictable_schedule,
                "remote_option": remote_option,
                "low_injury_risk": low_injury_risk,
                "autonomy_score": round(float(autonomy_score), 4),
                "commute_minutes": commute_minutes,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    reproduction = make_reproduction_data()
    transfer = make_transfer_data()

    reproduction.to_csv(ORIGINAL_DIR / "mas_pallais_job_choice_synthetic.csv", index=False)
    transfer.to_csv(TRANSFER_DIR / "maestas_working_conditions_synthetic.csv", index=False)

    print(f"Wrote {len(reproduction)} reproduction rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer)} transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
