#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for the Week 9 discrimination lab."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def logistic(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def build_callback_experiment(rng: np.random.Generator) -> pd.DataFrame:
    segments = {
        "national_chain": {"base": -2.15, "signal_gap": -0.30, "quality_return": 0.38},
        "local_service": {"base": -1.95, "signal_gap": -0.22, "quality_return": 0.28},
        "office_admin": {"base": -2.05, "signal_gap": -0.18, "quality_return": 0.34},
    }
    cities = ["Boston", "Chicago", "Atlanta", "Los Angeles"]
    rows: list[dict[str, float | int | str]] = []
    app_id = 1

    for segment, params in segments.items():
        for _ in range(720):
            quality = int(rng.binomial(1, 0.50))
            signal_group = int(rng.binomial(1, 0.50))
            city = str(rng.choice(cities))
            experience_years = int(rng.integers(2, 8))
            leadership = int(rng.binomial(1, 0.45 + 0.10 * quality))
            city_effect = {"Boston": 0.05, "Chicago": 0.00, "Atlanta": -0.03, "Los Angeles": 0.04}[city]
            latent = (
                params["base"]
                + params["quality_return"] * quality
                + 0.05 * experience_years
                + 0.12 * leadership
                + city_effect
                + params["signal_gap"] * signal_group
                + 0.08 * quality * (1 - signal_group)
            )
            callback = int(rng.random() < logistic(np.array([latent]))[0])
            rows.append(
                {
                    "application_id": app_id,
                    "firm_segment": segment,
                    "city": city,
                    "resume_quality": quality,
                    "signal_group": signal_group,
                    "experience_years": experience_years,
                    "leadership_signal": leadership,
                    "callback": callback,
                }
            )
            app_id += 1

    df = pd.DataFrame(rows)
    df["signal_label"] = np.where(df["signal_group"] == 1, "group_1", "group_0")
    df["quality_label"] = np.where(df["resume_quality"] == 1, "high_quality", "standard_quality")
    return df


def build_report_card_data(rng: np.random.Generator) -> pd.DataFrame:
    n_firms = 24
    firm_names = [f"firm_{idx:02d}" for idx in range(1, n_firms + 1)]
    segments = np.repeat(["retail", "logistics", "support", "sales"], repeats=6)
    firm_quality = rng.normal(0.0, 0.18, n_firms)
    true_gap = rng.normal(-0.18, 0.08, n_firms)
    baseline = rng.normal(-1.95, 0.15, n_firms)

    rows: list[dict[str, float | int | str]] = []
    application_id = 1
    for firm_idx, firm_name in enumerate(firm_names):
        n_apps = int(rng.integers(70, 121))
        for _ in range(n_apps):
            signal_group = int(rng.binomial(1, 0.50))
            quality = int(rng.binomial(1, 0.48))
            test_score = float(rng.normal(0.0 + 0.45 * quality, 1.0))
            referral = int(rng.binomial(1, 0.22))
            latent = (
                baseline[firm_idx]
                + 0.34 * quality
                + 0.16 * test_score
                + 0.11 * referral
                + true_gap[firm_idx] * signal_group
                + firm_quality[firm_idx]
            )
            callback = int(rng.random() < logistic(np.array([latent]))[0])
            rows.append(
                {
                    "application_id": application_id,
                    "firm_id": firm_idx + 1,
                    "firm_name": firm_name,
                    "segment": segments[firm_idx],
                    "signal_group": signal_group,
                    "resume_quality": quality,
                    "test_score": test_score,
                    "referral_signal": referral,
                    "callback": callback,
                    "true_gap": true_gap[firm_idx],
                }
            )
            application_id += 1

    df = pd.DataFrame(rows)
    df["signal_label"] = np.where(df["signal_group"] == 1, "group_1", "group_0")
    return df


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260509)
    callback_df = build_callback_experiment(rng)
    report_card_df = build_report_card_data(rng)

    callback_df.to_csv(
        ORIGINAL_DIR / "bertrand_mullainathan_callback_synthetic.csv",
        index=False,
    )
    report_card_df.to_csv(
        TRANSFER_DIR / "employer_report_card_synthetic.csv",
        index=False,
    )

    print(f"Wrote callback dataset to {ORIGINAL_DIR}")
    print(f"Wrote report-card dataset to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
