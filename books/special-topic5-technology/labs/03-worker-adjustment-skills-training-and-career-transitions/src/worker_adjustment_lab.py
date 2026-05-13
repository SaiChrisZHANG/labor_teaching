from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


TASK_WEIGHTS = {
    "routine_admin": 0.78,
    "routine_manual": 0.70,
    "prediction_classification": 0.82,
    "language_generation": 0.74,
    "programming_data": 0.56,
    "social_coordination": 0.18,
    "creative_problem_solving": 0.28,
    "maintenance_troubleshooting": 0.34,
    "care_interaction": 0.10,
}

PORTABILITY_WEIGHTS = {
    "routine_admin": 0.10,
    "routine_manual": 0.12,
    "prediction_classification": 0.34,
    "language_generation": 0.36,
    "programming_data": 0.72,
    "social_coordination": 0.82,
    "creative_problem_solving": 0.88,
    "maintenance_troubleshooting": 0.58,
    "care_interaction": 0.78,
}


@dataclass(frozen=True)
class Worker:
    name: str
    occupation: str
    firm: str
    local_market: str
    task_shares: dict[str, float]
    baseline_earnings: int
    age: int
    tenure: int
    training_access: float
    liquidity: float
    mobility_cost: float
    skepticism: float
    local_adjustment_capacity: float


@dataclass(frozen=True)
class LocalScenario:
    name: str
    technology_exposure: float
    training_capacity: float
    older_exposed_share: float
    retirement_option: float
    vacancy_growth: float


@dataclass(frozen=True)
class FirmAITraining:
    name: str
    ai_adoption: float
    exposed_incumbent_share: float
    incumbent_training: float
    new_hire_training: float
    vacancy_ai_demand: float


WORKERS = [
    Worker(
        "Avery",
        "Production assembler",
        "Auto parts producer",
        "Motor Belt",
        {
            "routine_admin": 0.04,
            "routine_manual": 0.44,
            "prediction_classification": 0.04,
            "language_generation": 0.02,
            "programming_data": 0.01,
            "social_coordination": 0.05,
            "creative_problem_solving": 0.02,
            "maintenance_troubleshooting": 0.22,
            "care_interaction": 0.00,
        },
        baseline_earnings=52000,
        age=54,
        tenure=18,
        training_access=0.22,
        liquidity=0.34,
        mobility_cost=0.76,
        skepticism=0.62,
        local_adjustment_capacity=0.30,
    ),
    Worker(
        "Blair",
        "Maintenance technician",
        "Auto parts producer",
        "Motor Belt",
        {
            "routine_admin": 0.02,
            "routine_manual": 0.12,
            "prediction_classification": 0.10,
            "language_generation": 0.02,
            "programming_data": 0.08,
            "social_coordination": 0.08,
            "creative_problem_solving": 0.08,
            "maintenance_troubleshooting": 0.45,
            "care_interaction": 0.00,
        },
        baseline_earnings=64000,
        age=41,
        tenure=11,
        training_access=0.56,
        liquidity=0.52,
        mobility_cost=0.42,
        skepticism=0.28,
        local_adjustment_capacity=0.42,
    ),
    Worker(
        "Casey",
        "Payroll clerk",
        "Claims processing center",
        "Service Metro",
        {
            "routine_admin": 0.50,
            "routine_manual": 0.00,
            "prediction_classification": 0.16,
            "language_generation": 0.12,
            "programming_data": 0.05,
            "social_coordination": 0.09,
            "creative_problem_solving": 0.04,
            "maintenance_troubleshooting": 0.01,
            "care_interaction": 0.00,
        },
        baseline_earnings=57000,
        age=37,
        tenure=8,
        training_access=0.48,
        liquidity=0.46,
        mobility_cost=0.38,
        skepticism=0.35,
        local_adjustment_capacity=0.68,
    ),
    Worker(
        "Devon",
        "Customer support specialist",
        "Claims processing center",
        "Service Metro",
        {
            "routine_admin": 0.18,
            "routine_manual": 0.00,
            "prediction_classification": 0.14,
            "language_generation": 0.24,
            "programming_data": 0.03,
            "social_coordination": 0.24,
            "creative_problem_solving": 0.04,
            "maintenance_troubleshooting": 0.00,
            "care_interaction": 0.10,
        },
        baseline_earnings=61000,
        age=29,
        tenure=4,
        training_access=0.70,
        liquidity=0.60,
        mobility_cost=0.24,
        skepticism=0.22,
        local_adjustment_capacity=0.72,
    ),
    Worker(
        "Ellis",
        "Software developer",
        "Enterprise software firm",
        "AI Services City",
        {
            "routine_admin": 0.03,
            "routine_manual": 0.00,
            "prediction_classification": 0.15,
            "language_generation": 0.10,
            "programming_data": 0.44,
            "social_coordination": 0.06,
            "creative_problem_solving": 0.20,
            "maintenance_troubleshooting": 0.02,
            "care_interaction": 0.00,
        },
        baseline_earnings=118000,
        age=33,
        tenure=5,
        training_access=0.84,
        liquidity=0.72,
        mobility_cost=0.20,
        skepticism=0.16,
        local_adjustment_capacity=0.82,
    ),
    Worker(
        "Finley",
        "Nurse coordinator",
        "Clinical services network",
        "Care And Admin Hub",
        {
            "routine_admin": 0.10,
            "routine_manual": 0.00,
            "prediction_classification": 0.12,
            "language_generation": 0.08,
            "programming_data": 0.02,
            "social_coordination": 0.20,
            "creative_problem_solving": 0.06,
            "maintenance_troubleshooting": 0.04,
            "care_interaction": 0.36,
        },
        baseline_earnings=76000,
        age=48,
        tenure=14,
        training_access=0.62,
        liquidity=0.55,
        mobility_cost=0.46,
        skepticism=0.30,
        local_adjustment_capacity=0.58,
    ),
    Worker(
        "Gray",
        "Logistics planner",
        "National logistics platform",
        "Logistics Corridor",
        {
            "routine_admin": 0.18,
            "routine_manual": 0.08,
            "prediction_classification": 0.25,
            "language_generation": 0.04,
            "programming_data": 0.12,
            "social_coordination": 0.12,
            "creative_problem_solving": 0.10,
            "maintenance_troubleshooting": 0.08,
            "care_interaction": 0.00,
        },
        baseline_earnings=69000,
        age=35,
        tenure=6,
        training_access=0.66,
        liquidity=0.58,
        mobility_cost=0.30,
        skepticism=0.24,
        local_adjustment_capacity=0.50,
    ),
    Worker(
        "Harper",
        "Warehouse coordinator",
        "National logistics platform",
        "Logistics Corridor",
        {
            "routine_admin": 0.20,
            "routine_manual": 0.30,
            "prediction_classification": 0.12,
            "language_generation": 0.04,
            "programming_data": 0.03,
            "social_coordination": 0.12,
            "creative_problem_solving": 0.04,
            "maintenance_troubleshooting": 0.10,
            "care_interaction": 0.00,
        },
        baseline_earnings=54000,
        age=58,
        tenure=21,
        training_access=0.28,
        liquidity=0.30,
        mobility_cost=0.82,
        skepticism=0.68,
        local_adjustment_capacity=0.44,
    ),
]

LOCAL_SCENARIOS = [
    LocalScenario("Motor Belt", 0.72, 0.30, 0.42, 0.70, 0.02),
    LocalScenario("Logistics Corridor", 0.58, 0.48, 0.34, 0.52, 0.07),
    LocalScenario("Service Metro", 0.44, 0.68, 0.22, 0.35, 0.08),
    LocalScenario("AI Services City", 0.38, 0.84, 0.14, 0.22, 0.11),
]

FIRM_AI_TRAINING = [
    FirmAITraining("Auto parts producer", 0.28, 0.62, 0.22, 0.36, 0.24),
    FirmAITraining("National logistics platform", 0.56, 0.48, 0.46, 0.62, 0.66),
    FirmAITraining("Claims processing center", 0.64, 0.58, 0.34, 0.74, 0.72),
    FirmAITraining("Clinical services network", 0.48, 0.32, 0.52, 0.42, 0.50),
    FirmAITraining("Enterprise software firm", 0.88, 0.26, 0.80, 0.86, 0.92),
]


def clip(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def weighted_sum(shares: dict[str, float], weights: dict[str, float]) -> float:
    total = sum(shares.values())
    if total <= 0:
        raise ValueError("Task shares must have positive mass")
    return sum((share / total) * weights[task] for task, share in shares.items())


def worker_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for worker in WORKERS:
        exposure = weighted_sum(worker.task_shares, TASK_WEIGHTS)
        portability = weighted_sum(worker.task_shares, PORTABILITY_WEIGHTS)
        training_probability = clip(
            0.10
            + 0.38 * worker.training_access
            + 0.18 * worker.liquidity
            + 0.12 * worker.local_adjustment_capacity
            + 0.10 * exposure
            - 0.20 * worker.skepticism
            - 0.12 * worker.mobility_cost
        )
        switching_probability = clip(
            0.08
            + 0.30 * exposure
            + 0.24 * portability
            + 0.12 * worker.local_adjustment_capacity
            - 0.24 * worker.mobility_cost
            - 0.08 * (worker.tenure / 25)
        )
        exit_probability = clip(
            0.04
            + 0.26 * exposure
            + 0.18 * worker.mobility_cost
            + (0.14 if worker.age >= 55 else 0.00)
            - 0.18 * worker.training_access
            - 0.16 * worker.local_adjustment_capacity
        )
        employment_stability = clip(
            0.88
            - 0.34 * exposure
            + 0.16 * portability
            + 0.14 * worker.training_access
            + 0.08 * worker.local_adjustment_capacity
            - 0.08 * worker.skepticism
        )
        earnings_change = (
            0.025
            - 0.16 * exposure
            + 0.08 * portability
            + 0.06 * training_probability
            + 0.04 * worker.local_adjustment_capacity
            - 0.04 * worker.mobility_cost
        )
        rows.append(
            {
                "worker": worker.name,
                "occupation": worker.occupation,
                "firm": worker.firm,
                "local_market": worker.local_market,
                "age": worker.age,
                "tenure": worker.tenure,
                "baseline_earnings": worker.baseline_earnings,
                "technology_exposure": round(exposure, 3),
                "skill_portability": round(portability, 3),
                "training_probability": round(training_probability, 3),
                "switching_probability": round(switching_probability, 3),
                "exit_probability": round(exit_probability, 3),
                "employment_stability": round(employment_stability, 3),
                "earnings_change_pct": round(100 * earnings_change, 2),
            }
        )
    return rows


def diagnosis_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    diagnosed: list[dict[str, object]] = []
    for row in rows:
        exposure = float(row["technology_exposure"])
        portability = float(row["skill_portability"])
        training = float(row["training_probability"])
        switching = float(row["switching_probability"])
        exit_risk = float(row["exit_probability"])
        stability = float(row["employment_stability"])
        age = int(row["age"])
        if exit_risk >= 0.34 and age >= 55:
            route = "early_retirement_or_exit"
        elif training >= 0.48 and stability >= 0.68:
            route = "training_and_internal_adaptation"
        elif switching >= 0.38 and portability >= 0.42:
            route = "occupation_or_employer_switch"
        elif exposure >= 0.52 and portability < 0.30:
            route = "persistent_loss_risk"
        elif stability >= 0.72:
            route = "stable_or_augmented"
        else:
            route = "mixed_adjustment"
        diagnosed.append(
            {
                "worker": row["worker"],
                "occupation": row["occupation"],
                "technology_exposure": exposure,
                "skill_portability": portability,
                "training_probability": training,
                "switching_probability": switching,
                "exit_probability": exit_risk,
                "employment_stability": stability,
                "adjustment_route": route,
                "interpretation": route_interpretation(route),
            }
        )
    return diagnosed


def route_interpretation(route: str) -> str:
    labels = {
        "early_retirement_or_exit": "adjustment_occurs_through_withdrawal_not_retraining",
        "training_and_internal_adaptation": "training_access_and_stability_support_incumbent_adjustment",
        "occupation_or_employer_switch": "portable_skills_make_mobility_feasible",
        "persistent_loss_risk": "high_exposure_and_low_portability_create_long_run_loss_risk",
        "stable_or_augmented": "exposure_is_offset_by_portability_or_complementarity",
        "mixed_adjustment": "multiple_margins_are_visible_but_no_single_response_dominates",
    }
    return labels[route]


def local_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for scenario in LOCAL_SCENARIOS:
        training_response = clip(
            0.08
            + 0.42 * scenario.training_capacity
            + 0.16 * scenario.vacancy_growth
            + 0.16 * scenario.technology_exposure
            - 0.20 * scenario.older_exposed_share
        )
        retirement_response = clip(
            0.04
            + 0.34 * scenario.older_exposed_share
            + 0.22 * scenario.retirement_option
            + 0.18 * scenario.technology_exposure
            - 0.22 * scenario.training_capacity
        )
        if training_response > retirement_response + 0.08:
            dominant_margin = "training_adjustment"
        elif retirement_response > training_response + 0.08:
            dominant_margin = "retirement_or_exit_adjustment"
        else:
            dominant_margin = "mixed_training_and_exit"
        rows.append(
            {
                "local_market": scenario.name,
                "technology_exposure": scenario.technology_exposure,
                "training_capacity": scenario.training_capacity,
                "older_exposed_share": scenario.older_exposed_share,
                "retirement_option": scenario.retirement_option,
                "vacancy_growth": scenario.vacancy_growth,
                "training_response_index": round(training_response, 3),
                "retirement_response_index": round(retirement_response, 3),
                "dominant_margin": dominant_margin,
            }
        )
    return rows


def ai_training_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for firm in FIRM_AI_TRAINING:
        incumbent_gap = firm.new_hire_training - firm.incumbent_training
        hidden_incumbent_risk = clip(
            0.18
            + 0.30 * firm.ai_adoption
            + 0.34 * firm.exposed_incumbent_share
            + 0.22 * max(incumbent_gap, 0)
            - 0.18 * firm.incumbent_training
        )
        if hidden_incumbent_risk >= 0.50:
            interpretation = "skill_upgrading_may_bypass_incumbents"
        elif firm.incumbent_training >= firm.new_hire_training:
            interpretation = "incumbent_training_supports_adaptation"
        elif firm.vacancy_ai_demand > firm.ai_adoption:
            interpretation = "hiring_demand_runs_ahead_of_realized_use"
        else:
            interpretation = "mixed_incumbent_and_new_hire_adjustment"
        rows.append(
            {
                "firm": firm.name,
                "ai_adoption": firm.ai_adoption,
                "exposed_incumbent_share": firm.exposed_incumbent_share,
                "incumbent_training": firm.incumbent_training,
                "new_hire_training": firm.new_hire_training,
                "vacancy_ai_demand": firm.vacancy_ai_demand,
                "hidden_incumbent_risk": round(hidden_incumbent_risk, 3),
                "interpretation": interpretation,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    reproduced = worker_rows()
    diagnosed = diagnosis_rows(reproduced)
    local_transfer = local_transfer_rows()
    ai_transfer = ai_training_transfer_rows()

    write_csv(lab_dir / "output" / "reproduced" / "worker_exposure_outcomes.csv", reproduced)
    write_csv(lab_dir / "output" / "diagnosed" / "adjustment_diagnosis.csv", diagnosed)
    write_csv(lab_dir / "output" / "transfer" / "training_retirement_transfer.csv", local_transfer)
    write_csv(lab_dir / "output" / "transfer" / "ai_training_transfer.csv", ai_transfer)

    note = (
        "Synthetic Week 3 worker-adjustment lab complete. Outputs reproduce "
        "worker-level exposure logic, diagnose adjustment routes, and transfer "
        "the design to training, retirement, and AI-training settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
