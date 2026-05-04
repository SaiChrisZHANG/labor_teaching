#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Labor I Week 4."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def make_reproduction_data() -> pd.DataFrame:
    rng = np.random.default_rng(202604)
    rows = []
    for child_id in range(1, 241):
        cohort = (child_id - 1) // 60
        treatment = int((child_id + cohort) % 2 == 0)
        baseline_skill = rng.normal(0.0, 0.85)
        maternal_schooling = rng.integers(6, 17)
        home_environment = 0.35 + 0.22 * treatment + 0.14 * baseline_skill + rng.normal(0.0, 0.12)
        parental_investment = 0.45 + 0.28 * treatment + 0.10 * maternal_schooling / 16 + 0.12 * baseline_skill + rng.normal(0.0, 0.11)
        endline_skill = (
            0.25
            + 0.58 * baseline_skill
            + 0.20 * parental_investment
            + 0.12 * home_environment
            + 0.11 * treatment
            + 0.06 * treatment * np.maximum(baseline_skill, 0.0)
            + rng.normal(0.0, 0.13)
        )
        followup_language = 0.18 + 0.52 * endline_skill + 0.04 * treatment + rng.normal(0.0, 0.12)
        rows.append(
            {
                "child_id": child_id,
                "cohort": cohort + 1,
                "treatment": treatment,
                "baseline_skill": round(float(baseline_skill), 4),
                "baseline_group": "higher_baseline" if baseline_skill >= 0 else "lower_baseline",
                "maternal_schooling": int(maternal_schooling),
                "home_environment": round(float(home_environment), 4),
                "parental_investment": round(float(parental_investment), 4),
                "endline_skill": round(float(endline_skill), 4),
                "followup_language": round(float(followup_language), 4),
            }
        )
    return pd.DataFrame(rows)


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(202605)
    qualities = ["low_quality", "medium_quality", "high_quality"]
    quality_effect = {"low_quality": 0.06, "medium_quality": 0.14, "high_quality": 0.25}
    rows = []
    for child_id in range(1, 301):
        center_quality = qualities[(child_id - 1) % 3]
        treatment = int((child_id * 3) % 5 < 2)
        baseline_skill = rng.normal(0.0, 0.8)
        classroom_input = 0.35 + quality_effect[center_quality] + 0.05 * treatment + rng.normal(0.0, 0.08)
        endline_skill = (
            0.22
            + 0.60 * baseline_skill
            + 0.24 * classroom_input
            + 0.08 * treatment
            + 0.22 * treatment * quality_effect[center_quality]
            + rng.normal(0.0, 0.14)
        )
        language_score = 0.12 + 0.48 * endline_skill + 0.02 * treatment + rng.normal(0.0, 0.11)
        rows.append(
            {
                "child_id": child_id,
                "center_quality": center_quality,
                "treatment": treatment,
                "baseline_skill": round(float(baseline_skill), 4),
                "classroom_input": round(float(classroom_input), 4),
                "endline_skill": round(float(endline_skill), 4),
                "language_score": round(float(language_score), 4),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    reproduction = make_reproduction_data()
    transfer = make_transfer_data()

    reproduction.to_csv(ORIGINAL_DIR / "attanasio_parenting_rct_synthetic.csv", index=False)
    transfer.to_csv(TRANSFER_DIR / "walters_center_quality_synthetic.csv", index=False)

    print(f"Wrote {len(reproduction)} reproduction rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(transfer)} transfer rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
