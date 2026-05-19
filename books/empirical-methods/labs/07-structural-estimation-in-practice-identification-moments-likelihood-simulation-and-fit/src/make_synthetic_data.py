"""Create deterministic synthetic data for the Week 7 structural-estimation lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
N_STATES = 9
DELTA = 0.92


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35.0, 35.0)))


def replacement_transition_matrices(n_states: int = N_STATES) -> np.ndarray:
    matrices = np.zeros((2, n_states, n_states))
    for state in range(n_states):
        for next_state, prob in [
            (state, 0.16),
            (min(state + 1, n_states - 1), 0.62),
            (min(state + 2, n_states - 1), 0.22),
        ]:
            matrices[0, state, next_state] += prob
        for next_state, prob in [(0, 0.68), (1, 0.26), (2, 0.06)]:
            matrices[1, state, next_state] += prob
    return matrices


def solve_replacement_model(
    replacement_cost: float,
    maintenance_slope: float,
    transitions: np.ndarray,
    delta: float = DELTA,
    tolerance: float = 1e-10,
    max_iter: int = 10_000,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    states = np.arange(transitions.shape[1], dtype=float)
    value = np.zeros_like(states)
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


def make_replacement_panel() -> pd.DataFrame:
    rng = np.random.default_rng(6707)
    transitions = replacement_transition_matrices()
    true_replacement_cost = 4.40
    true_maintenance_slope = 0.54
    _, _, _, replace_prob = solve_replacement_model(
        true_replacement_cost,
        true_maintenance_slope,
        transitions,
    )

    rows: list[dict[str, float | int]] = []
    n_units = 160
    n_periods = 34
    for unit_id in range(1, n_units + 1):
        state = int(rng.integers(0, 4))
        unit_quality = rng.normal(0.0, 0.20)
        for period in range(n_periods):
            prob = float(np.clip(replace_prob[state] + 0.035 * unit_quality, 0.01, 0.98))
            replace = int(rng.random() < prob)
            if replace:
                operating_cost = true_replacement_cost + rng.normal(0.0, 0.24)
                downtime = max(0.0, rng.normal(0.35, 0.12))
            else:
                operating_cost = 0.45 + true_maintenance_slope * state + rng.normal(0.0, 0.22)
                downtime = max(0.0, 0.05 + 0.08 * state + rng.normal(0.0, 0.06))
            next_state = draw_from_probs(rng, transitions[replace, state])
            rows.append(
                {
                    "unit_id": unit_id,
                    "period": period,
                    "mileage_state": state,
                    "replace": replace,
                    "next_mileage_state": next_state,
                    "operating_cost": round(float(operating_cost), 5),
                    "downtime_days": round(float(downtime), 5),
                    "true_replacement_probability": round(prob, 5),
                    "synthetic_unit_quality": round(float(unit_quality), 5),
                }
            )
            state = next_state
    return pd.DataFrame(rows)


def make_schooling_panel() -> pd.DataFrame:
    rng = np.random.default_rng(6717)
    n_people = 1_000
    n_periods = 7
    ability = rng.normal(0.0, 1.0, n_people)
    schooling = rng.choice([10.0, 11.0, 12.0], n_people, p=[0.20, 0.35, 0.45])
    experience = rng.choice([0.0, 1.0], n_people, p=[0.82, 0.18])
    grant = rng.choice([0.0, 1_500.0], n_people, p=[0.70, 0.30])
    rows: list[dict[str, float | int]] = []

    for period in range(n_periods):
        for idx in range(n_people):
            age = 18 + period
            base_tuition = 5_200.0 + 360.0 * period + rng.normal(0.0, 300.0)
            tuition = max(700.0, base_tuition - grant[idx])
            wage_offer = np.exp(
                9.18
                + 0.082 * schooling[idx]
                + 0.058 * experience[idx]
                + 0.14 * ability[idx]
                + rng.normal(0.0, 0.11)
            )
            school_index = (
                0.95
                - 0.33 * (schooling[idx] - 12.0)
                - 0.22 * experience[idx]
                + 0.42 * ability[idx]
                - 0.20 * (tuition / 1_000.0)
                - 0.55 * (np.log(wage_offer) - np.log(35_000.0))
                + 0.24 * float(period <= 2)
            )
            can_school = schooling[idx] < 16.0
            school_prob = float(sigmoid(school_index)) if can_school else 0.0
            choose_school = int(rng.random() < school_prob)
            work = int(1 - choose_school)
            observed_wage = float(wage_offer + rng.normal(0.0, 900.0)) if work else np.nan
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
    replacement_path = ROOT / "original" / "reduced" / "replacement_estimation_synthetic.csv"
    schooling_path = ROOT / "transfer" / "data" / "schooling_lifecycle_synthetic.csv"
    replacement_path.parent.mkdir(parents=True, exist_ok=True)
    schooling_path.parent.mkdir(parents=True, exist_ok=True)
    make_replacement_panel().to_csv(replacement_path, index=False)
    make_schooling_panel().to_csv(schooling_path, index=False)
    print(f"Wrote {replacement_path}")
    print(f"Wrote {schooling_path}")


if __name__ == "__main__":
    main()
