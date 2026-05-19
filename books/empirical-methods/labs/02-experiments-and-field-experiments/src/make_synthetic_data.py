"""Create deterministic synthetic data for the Week 2 teaching lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35, 35)))


def make_encouragement_data() -> pd.DataFrame:
    rng = np.random.default_rng(2402)
    n_departments = 18
    department_sizes = rng.integers(14, 25, n_departments)
    rows = []
    worker_id = 1

    for dept_id, size in enumerate(department_sizes, start=1):
        dept_baseline = rng.normal(0.0, 0.35)
        assignment_rate = rng.choice([0.25, 0.40, 0.55])
        raw_assignment = rng.binomial(1, assignment_rate, size)

        if raw_assignment.sum() == 0:
            raw_assignment[rng.integers(0, size)] = 1
        if raw_assignment.sum() == size:
            raw_assignment[rng.integers(0, size)] = 0

        peer_assigned = (raw_assignment.sum() - raw_assignment) / (size - 1)

        for j in range(size):
            age = rng.integers(24, 64)
            tenure = np.maximum(0.2, rng.gamma(2.4, 2.2))
            salary = rng.normal(52000 + 650 * tenure + 240 * age + 2500 * dept_baseline, 8500)
            salary = np.maximum(28000, salary)
            prior_enrolled = rng.binomial(1, sigmoid(-2.2 + 0.000035 * salary + 0.04 * tenure + 0.015 * (age - 40)))
            assigned = int(raw_assignment[j])
            exposure = float(peer_assigned[j])

            attend_prob = sigmoid(
                -1.8
                + 1.45 * assigned
                + 0.65 * exposure
                + 0.32 * prior_enrolled
                + 0.000012 * salary
                + 0.03 * tenure
                + rng.normal(0, 0.18)
            )
            attended = rng.binomial(1, attend_prob)

            participation_prob = sigmoid(
                -2.35
                + 0.75 * attended
                + 0.35 * assigned
                + 0.55 * exposure
                + 1.25 * prior_enrolled
                + 0.000018 * salary
                + 0.015 * tenure
                + rng.normal(0, 0.20)
            )
            enrolled_after = rng.binomial(1, participation_prob)

            observed_prob = sigmoid(
                2.55
                - 0.18 * assigned
                + 0.12 * prior_enrolled
                + 0.000004 * salary
                - 0.04 * (dept_id % 3)
            )
            outcome_observed = rng.binomial(1, observed_prob)
            if outcome_observed == 0:
                enrolled_after_value = np.nan
            else:
                enrolled_after_value = enrolled_after

            rows.append(
                {
                    "worker_id": worker_id,
                    "department_id": dept_id,
                    "department_size": size,
                    "assigned_encouragement": assigned,
                    "peer_assignment_share": round(exposure, 4),
                    "attended_seminar": attended,
                    "enrolled_after": enrolled_after_value,
                    "outcome_observed": outcome_observed,
                    "baseline_enrolled": prior_enrolled,
                    "salary": round(salary, 2),
                    "tenure": round(tenure, 2),
                    "age": age,
                }
            )
            worker_id += 1

    return pd.DataFrame(rows)


def make_saturation_data() -> pd.DataFrame:
    rng = np.random.default_rng(3317)
    n_markets = 16
    market_sizes = rng.integers(18, 33, n_markets)
    saturation_rates = np.tile(np.array([0.20, 0.45, 0.70, 0.85]), 4)
    rng.shuffle(saturation_rates)
    rows = []
    worker_id = 1

    for market_id, (size, saturation) in enumerate(zip(market_sizes, saturation_rates), start=1):
        market_strength = rng.normal(0.0, 0.45)
        assignment = rng.binomial(1, saturation, size)
        if assignment.sum() == 0:
            assignment[rng.integers(0, size)] = 1
        if assignment.sum() == size:
            assignment[rng.integers(0, size)] = 0

        untreated_exposure = (assignment.sum() - assignment) / (size - 1)

        for j in range(size):
            education = rng.integers(10, 19)
            prior_employed = rng.binomial(1, sigmoid(-0.55 + 0.16 * (education - 12) + market_strength))
            baseline_skill = rng.normal(0.10 * (education - 12) + 0.35 * prior_employed, 0.85)
            assigned = int(assignment[j])
            exposure = float(untreated_exposure[j])
            takeup = rng.binomial(1, sigmoid(-1.2 + 1.35 * assigned + 0.24 * baseline_skill + 0.20 * prior_employed))

            employment_prob = sigmoid(
                -0.75
                + 0.62 * takeup
                + 0.25 * assigned
                + 0.34 * baseline_skill
                + 0.42 * prior_employed
                + market_strength
                - 0.38 * exposure
                + 0.20 * saturation
            )
            employed_after = rng.binomial(1, employment_prob)

            rows.append(
                {
                    "worker_id": worker_id,
                    "market_id": market_id,
                    "market_size": size,
                    "market_saturation": round(float(saturation), 2),
                    "assigned_assistance": assigned,
                    "took_assistance": takeup,
                    "untreated_exposure_share": round(exposure, 4),
                    "employed_after": employed_after,
                    "education": education,
                    "prior_employed": prior_employed,
                    "baseline_skill": round(float(baseline_skill), 3),
                }
            )
            worker_id += 1

    return pd.DataFrame(rows)


def main() -> None:
    encouragement_path = ROOT / "original" / "reduced" / "encouragement_synthetic.csv"
    transfer_path = ROOT / "transfer" / "data" / "saturation_synthetic.csv"
    encouragement_path.parent.mkdir(parents=True, exist_ok=True)
    transfer_path.parent.mkdir(parents=True, exist_ok=True)

    make_encouragement_data().to_csv(encouragement_path, index=False)
    make_saturation_data().to_csv(transfer_path, index=False)

    print(f"Wrote {encouragement_path}")
    print(f"Wrote {transfer_path}")


if __name__ == "__main__":
    main()
