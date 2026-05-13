from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


TASKS = [
    "routine_admin",
    "routine_manual",
    "physical_precision",
    "prediction_classification",
    "language_generation",
    "social_coordination",
    "programming_data",
    "creative_problem_solving",
    "care_interaction",
    "maintenance_troubleshooting",
]


@dataclass(frozen=True)
class Occupation:
    name: str
    task_shares: dict[str, float]


@dataclass(frozen=True)
class TechnologyMeasure:
    name: str
    stage: str
    weights: dict[str, float]


@dataclass(frozen=True)
class Firm:
    name: str
    workforce_shares: dict[str, float]
    robot_adoption_intensity: float
    vacancy_ai_intensity: float
    ai_investment_intensity: float


OCCUPATIONS = [
    Occupation(
        "Production assembler",
        {
            "routine_admin": 0.05,
            "routine_manual": 0.40,
            "physical_precision": 0.25,
            "prediction_classification": 0.05,
            "language_generation": 0.02,
            "social_coordination": 0.05,
            "programming_data": 0.01,
            "creative_problem_solving": 0.02,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.15,
        },
    ),
    Occupation(
        "Maintenance technician",
        {
            "routine_admin": 0.00,
            "routine_manual": 0.15,
            "physical_precision": 0.20,
            "prediction_classification": 0.10,
            "language_generation": 0.02,
            "social_coordination": 0.08,
            "programming_data": 0.05,
            "creative_problem_solving": 0.05,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.35,
        },
    ),
    Occupation(
        "Payroll clerk",
        {
            "routine_admin": 0.55,
            "routine_manual": 0.01,
            "physical_precision": 0.00,
            "prediction_classification": 0.15,
            "language_generation": 0.10,
            "social_coordination": 0.10,
            "programming_data": 0.05,
            "creative_problem_solving": 0.03,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.01,
        },
    ),
    Occupation(
        "Customer support specialist",
        {
            "routine_admin": 0.20,
            "routine_manual": 0.00,
            "physical_precision": 0.00,
            "prediction_classification": 0.10,
            "language_generation": 0.25,
            "social_coordination": 0.30,
            "programming_data": 0.02,
            "creative_problem_solving": 0.03,
            "care_interaction": 0.10,
            "maintenance_troubleshooting": 0.00,
        },
    ),
    Occupation(
        "Software developer",
        {
            "routine_admin": 0.03,
            "routine_manual": 0.00,
            "physical_precision": 0.00,
            "prediction_classification": 0.15,
            "language_generation": 0.10,
            "social_coordination": 0.05,
            "programming_data": 0.45,
            "creative_problem_solving": 0.20,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.02,
        },
    ),
    Occupation(
        "Nurse coordinator",
        {
            "routine_admin": 0.10,
            "routine_manual": 0.00,
            "physical_precision": 0.05,
            "prediction_classification": 0.10,
            "language_generation": 0.10,
            "social_coordination": 0.20,
            "programming_data": 0.02,
            "creative_problem_solving": 0.03,
            "care_interaction": 0.35,
            "maintenance_troubleshooting": 0.05,
        },
    ),
    Occupation(
        "Logistics planner",
        {
            "routine_admin": 0.20,
            "routine_manual": 0.10,
            "physical_precision": 0.05,
            "prediction_classification": 0.25,
            "language_generation": 0.00,
            "social_coordination": 0.10,
            "programming_data": 0.10,
            "creative_problem_solving": 0.10,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.10,
        },
    ),
]


MEASURES = [
    TechnologyMeasure(
        "patent_text_capability",
        "invention_or_capability",
        {
            "routine_admin": 0.45,
            "routine_manual": 0.05,
            "physical_precision": 0.10,
            "prediction_classification": 0.95,
            "language_generation": 0.80,
            "social_coordination": 0.20,
            "programming_data": 0.75,
            "creative_problem_solving": 0.55,
            "care_interaction": 0.10,
            "maintenance_troubleshooting": 0.35,
        },
    ),
    TechnologyMeasure(
        "robot_embodied_adoption",
        "embodied_adoption",
        {
            "routine_admin": 0.20,
            "routine_manual": 0.95,
            "physical_precision": 0.85,
            "prediction_classification": 0.15,
            "language_generation": 0.05,
            "social_coordination": 0.05,
            "programming_data": 0.10,
            "creative_problem_solving": 0.05,
            "care_interaction": 0.00,
            "maintenance_troubleshooting": 0.45,
        },
    ),
    TechnologyMeasure(
        "vacancy_ai_skill_demand",
        "desired_skill_demand",
        {
            "routine_admin": 0.30,
            "routine_manual": 0.05,
            "physical_precision": 0.05,
            "prediction_classification": 0.80,
            "language_generation": 0.70,
            "social_coordination": 0.45,
            "programming_data": 0.95,
            "creative_problem_solving": 0.65,
            "care_interaction": 0.20,
            "maintenance_troubleshooting": 0.20,
        },
    ),
]


FIRMS = [
    Firm(
        "Logistics automation plant",
        {
            "Production assembler": 0.40,
            "Maintenance technician": 0.30,
            "Logistics planner": 0.20,
            "Payroll clerk": 0.10,
        },
        robot_adoption_intensity=0.90,
        vacancy_ai_intensity=0.25,
        ai_investment_intensity=0.35,
    ),
    Firm(
        "Regional hospital network",
        {
            "Nurse coordinator": 0.45,
            "Customer support specialist": 0.20,
            "Maintenance technician": 0.15,
            "Payroll clerk": 0.20,
        },
        robot_adoption_intensity=0.20,
        vacancy_ai_intensity=0.55,
        ai_investment_intensity=0.50,
    ),
    Firm(
        "Software services firm",
        {
            "Software developer": 0.55,
            "Customer support specialist": 0.15,
            "Logistics planner": 0.10,
            "Payroll clerk": 0.20,
        },
        robot_adoption_intensity=0.05,
        vacancy_ai_intensity=0.95,
        ai_investment_intensity=0.85,
    ),
    Firm(
        "Business support center",
        {
            "Payroll clerk": 0.45,
            "Customer support specialist": 0.35,
            "Software developer": 0.10,
            "Logistics planner": 0.10,
        },
        robot_adoption_intensity=0.05,
        vacancy_ai_intensity=0.65,
        ai_investment_intensity=0.55,
    ),
]


def normalized_task_shares(occupation: Occupation) -> dict[str, float]:
    total = sum(occupation.task_shares.values())
    if total <= 0:
        raise ValueError(f"{occupation.name} has no task mass")
    return {task: occupation.task_shares.get(task, 0.0) / total for task in TASKS}


def exposure(occupation: Occupation, measure: TechnologyMeasure) -> float:
    shares = normalized_task_shares(occupation)
    score = sum(shares[task] * measure.weights.get(task, 0.0) for task in TASKS)
    return round(score, 3)


def channel_label(occupation: Occupation) -> str:
    shares = normalized_task_shares(occupation)
    automation = (
        0.45 * shares["routine_admin"]
        + 0.75 * shares["routine_manual"]
        + 0.55 * shares["physical_precision"]
    )
    augmentation = (
        0.45 * shares["prediction_classification"]
        + 0.35 * shares["language_generation"]
        + 0.35 * shares["social_coordination"]
        + 0.25 * shares["care_interaction"]
    )
    new_tasks = (
        0.65 * shares["programming_data"]
        + 0.55 * shares["creative_problem_solving"]
        + 0.25 * shares["maintenance_troubleshooting"]
    )
    scores = {
        "automation_or_substitution": automation,
        "augmentation": augmentation,
        "new_task_or_reorganization": new_tasks,
    }
    return max(scores, key=scores.get)


def occupation_exposure_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for occupation in OCCUPATIONS:
        measure_scores = {measure.name: exposure(occupation, measure) for measure in MEASURES}
        dominant = max(measure_scores, key=measure_scores.get)
        rows.append(
            {
                "occupation": occupation.name,
                "patent_text_capability": measure_scores["patent_text_capability"],
                "robot_embodied_adoption": measure_scores["robot_embodied_adoption"],
                "vacancy_ai_skill_demand": measure_scores["vacancy_ai_skill_demand"],
                "dominant_measure": dominant,
                "likely_channel": channel_label(occupation),
            }
        )
    return rows


def ranks(rows: list[dict[str, object]], measure_name: str) -> dict[str, int]:
    ordered = sorted(rows, key=lambda row: float(row[measure_name]), reverse=True)
    return {str(row["occupation"]): rank + 1 for rank, row in enumerate(ordered)}


def contrast_rows(exposure_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    patent_rank = ranks(exposure_rows, "patent_text_capability")
    robot_rank = ranks(exposure_rows, "robot_embodied_adoption")
    vacancy_rank = ranks(exposure_rows, "vacancy_ai_skill_demand")
    rows: list[dict[str, object]] = []
    for row in exposure_rows:
        occupation = str(row["occupation"])
        rank_values = [
            patent_rank[occupation],
            robot_rank[occupation],
            vacancy_rank[occupation],
        ]
        spread = max(rank_values) - min(rank_values)
        if spread >= 4:
            interpretation = "measure_choice_changes_substantive_ranking"
        elif spread >= 2:
            interpretation = "measure_choice_changes_emphasis"
        else:
            interpretation = "measures_broadly_agree"
        rows.append(
            {
                "occupation": occupation,
                "patent_rank": patent_rank[occupation],
                "robot_rank": robot_rank[occupation],
                "vacancy_rank": vacancy_rank[occupation],
                "rank_spread": spread,
                "measurement_lesson": interpretation,
            }
        )
    return rows


def firm_rows(exposure_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_occupation = {str(row["occupation"]): row for row in exposure_rows}
    rows: list[dict[str, object]] = []
    for firm in FIRMS:
        patent = weighted_firm_score(firm, by_occupation, "patent_text_capability")
        robot = weighted_firm_score(firm, by_occupation, "robot_embodied_adoption")
        vacancy = weighted_firm_score(firm, by_occupation, "vacancy_ai_skill_demand")
        embodied_adoption = 0.70 * robot + 0.30 * firm.robot_adoption_intensity
        vacancy_demand = 0.60 * vacancy + 0.40 * firm.vacancy_ai_intensity
        realized_ai_use = (
            0.30 * patent
            + 0.20 * vacancy
            + 0.50 * firm.ai_investment_intensity
        )
        scores = {
            "workforce_capability_exposure": patent,
            "embodied_automation_measure": embodied_adoption,
            "vacancy_skill_demand_measure": vacancy_demand,
            "realized_ai_use_measure": realized_ai_use,
        }
        dominant = max(scores, key=scores.get)
        rows.append(
            {
                "firm": firm.name,
                "workforce_capability_exposure": round(patent, 3),
                "embodied_automation_measure": round(embodied_adoption, 3),
                "vacancy_skill_demand_measure": round(vacancy_demand, 3),
                "realized_ai_use_measure": round(realized_ai_use, 3),
                "dominant_measure": dominant,
                "interpretation": firm_interpretation(dominant),
            }
        )
    return rows


def weighted_firm_score(
    firm: Firm, by_occupation: dict[str, dict[str, object]], measure_name: str
) -> float:
    total = sum(firm.workforce_shares.values())
    if total <= 0:
        raise ValueError(f"{firm.name} has no workforce mass")
    score = 0.0
    for occupation, share in firm.workforce_shares.items():
        score += (share / total) * float(by_occupation[occupation][measure_name])
    return score


def firm_interpretation(dominant_measure: str) -> str:
    labels = {
        "workforce_capability_exposure": "task_portfolio_exposed_to_capability",
        "embodied_automation_measure": "realized_robot_margin_is_salient",
        "vacancy_skill_demand_measure": "hiring_signal_is_salient",
        "realized_ai_use_measure": "firm_adoption_margin_is_salient",
    }
    return labels[dominant_measure]


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
    reproduced = occupation_exposure_rows()
    diagnosed = contrast_rows(reproduced)
    transferred = firm_rows(reproduced)

    write_csv(lab_dir / "output" / "reproduced" / "exposure_by_occupation.csv", reproduced)
    write_csv(lab_dir / "output" / "diagnosed" / "measurement_contrast.csv", diagnosed)
    write_csv(lab_dir / "output" / "transfer" / "firm_measurement_contrast.csv", transferred)

    note = (
        "Synthetic Week 1 technology measurement lab complete. Outputs compare "
        "patent-text capability exposure, robot-style adoption exposure, vacancy "
        "skill-demand exposure, and firm-level transfer measures.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
