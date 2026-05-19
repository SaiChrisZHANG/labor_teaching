"""Create deterministic synthetic data for the Week 6 structural-estimation lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
N_STATES = 10
DELTA = 0.92


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35.0, 35.0)))


def replacement_transition_matrices(n_states: int = N_STATES) -> np.ndarray:
    """Return transition matrices for continue and replace actions."""
    matrices = np.zeros((2, n_states, n_states))
    for state in range(n_states):
        next_states = [state, min(state + 1, n_states - 1), min(state + 2, n_states - 1)]
        probs = [0.12, 0.64, 0.24]
        for next_state, prob in zip(next_states, probs):
            matrices[0, state, next_state] += prob

        reset_states = [0, 1, 2]
        reset_probs = [0.72, 0.24, 0.04]
        for next_state, prob in zip(reset_states, reset_probs):
            matrices[1, state, next_state] += prob
    return matrices


def solve_replacement_model(
    replacement_cost: float,
    maintenance_slope: float,
    transitions: np.ndarray,
    delta: float = DELTA,
    tolerance: float = 1e-11,
    max_iter: int = 20_000,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Solve a two-action dynamic logit replacement model."""
    n_states = transitions.shape[1]
    states = np.arange(n_states, dtype=float)
    value = np.zeros(n_states)
    for _ in range(max_iter):
        continue_value = -maintenance_slope * states + delta * transitions[0] @ value
        replace_value = -replacement_cost + delta * transitions[1] @ value
        new_value = np.logaddexp(continue_value, replace_value)
        if np.max(np.abs(new_value - value)) < tolerance:
            value = new_value
            break
        value = new_value

    continue_value = -maintenance_slope * states + delta * transitions[0] @ value
    replace_value = -replacement_cost + delta * transitions[1] @ value
    log_denom = np.logaddexp(continue_value, replace_value)
    replace_prob = np.exp(replace_value - log_denom)
    return value, continue_value, replace_value, replace_prob


def draw_from_probs(rng: np.random.Generator, probs: np.ndarray) -> int:
    return int(rng.choice(np.arange(len(probs)), p=probs))


def make_replacement_data() -> pd.DataFrame:
    rng = np.random.default_rng(6606)
    transitions = replacement_transition_matrices()
    true_replacement_cost = 4.65
    true_maintenance_slope = 0.56
    _, _, _, replace_prob = solve_replacement_model(
        true_replacement_cost,
        true_maintenance_slope,
        transitions,
    )

    rows: list[dict[str, float | int]] = []
    n_units = 180
    n_periods = 38
    for unit_id in range(1, n_units + 1):
        state = int(rng.integers(0, 4))
        unit_quality = rng.normal(0.0, 0.18)
        for period in range(n_periods):
            prob = float(np.clip(replace_prob[state] + unit_quality * 0.035, 0.01, 0.98))
            replace = int(rng.random() < prob)
            if replace:
                operating_cost = true_replacement_cost + rng.normal(0.0, 0.25)
            else:
                operating_cost = 0.35 + true_maintenance_slope * state + rng.normal(0.0, 0.22)
            next_state = draw_from_probs(rng, transitions[replace, state])
            rows.append(
                {
                    "unit_id": unit_id,
                    "period": period,
                    "mileage_state": state,
                    "replace": replace,
                    "next_mileage_state": next_state,
                    "operating_cost": round(float(operating_cost), 5),
                    "true_replacement_probability": round(prob, 5),
                    "synthetic_unit_quality": round(float(unit_quality), 5),
                }
            )
            state = next_state
    return pd.DataFrame(rows)


def make_career_choice_data() -> pd.DataFrame:
    rng = np.random.default_rng(6616)
    n_people = 1_200
    n_periods = 8
    rows: list[dict[str, float | int]] = []

    ability = rng.normal(0.0, 1.0, size=n_people)
    schooling = rng.choice([10, 11, 12], size=n_people, p=[0.22, 0.34, 0.44]).astype(float)
    experience = rng.choice([0, 1], size=n_people, p=[0.78, 0.22]).astype(float)
    tuition_grant = rng.choice([0.0, 1_200.0], size=n_people, p=[0.68, 0.32])

    for period in range(n_periods):
        age = 18 + period
        for idx in range(n_people):
            base_tuition = 4_800 + 320 * period + rng.normal(0.0, 260.0)
            tuition = max(500.0, base_tuition - tuition_grant[idx])
            wage_offer = np.exp(
                9.22
                + 0.078 * schooling[idx]
                + 0.055 * experience[idx]
                + 0.145 * ability[idx]
                + rng.normal(0.0, 0.10)
            )
            school_index = (
                1.05
                - 0.36 * (schooling[idx] - 12.0)
                - 0.24 * experience[idx]
                + 0.48 * ability[idx]
                - 0.00016 * tuition
                + 0.30 * (period <= 2)
                - 0.000012 * (wage_offer - 35_000)
            )
            can_school = schooling[idx] < 16
            school_prob = float(sigmoid(school_index)) if can_school else 0.0
            choose_school = int(rng.random() < school_prob)
            work = int(1 - choose_school)
            observed_wage = float(wage_offer + rng.normal(0.0, 850.0)) if work else np.nan

            rows.append(
                {
                    "person_id": idx + 1,
                    "period": period,
                    "age": age,
                    "schooling_years": round(float(schooling[idx]), 5),
                    "experience_years": round(float(experience[idx]), 5),
                    "tuition": round(float(tuition), 2),
                    "wage_offer": round(float(wage_offer), 2),
                    "choose_school": choose_school,
                    "work": work,
                    "observed_wage": round(observed_wage, 2) if work else np.nan,
                    "synthetic_ability": round(float(ability[idx]), 5),
                    "true_school_probability": round(school_prob, 5),
                }
            )

            if choose_school:
                schooling[idx] += 1.0
            else:
                experience[idx] += 1.0

    return pd.DataFrame(rows)


def main() -> None:
    replacement_path = ROOT / "original" / "reduced" / "replacement_synthetic.csv"
    career_path = ROOT / "transfer" / "data" / "career_choice_synthetic.csv"

    replacement_path.parent.mkdir(parents=True, exist_ok=True)
    career_path.parent.mkdir(parents=True, exist_ok=True)

    make_replacement_data().to_csv(replacement_path, index=False)
    make_career_choice_data().to_csv(career_path, index=False)

    print(f"Wrote {replacement_path}")
    print(f"Wrote {career_path}")


if __name__ == "__main__":
    main()
