from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Industry:
    name: str
    robot_intensity: float
    ai_complementarity: float
    baseline_demand_growth: float


@dataclass(frozen=True)
class CommutingZone:
    name: str
    industry_shares: dict[str, float]
    exposed_occupation_share: float
    adjustment_capacity: float


@dataclass(frozen=True)
class Firm:
    name: str
    workforce_task_exposure: float
    realized_ai_adoption: float
    vacancy_ai_demand: float
    output_demand_growth: float


INDUSTRIES = [
    Industry("autos_and_machinery", robot_intensity=0.92, ai_complementarity=0.28, baseline_demand_growth=0.04),
    Industry("warehousing_logistics", robot_intensity=0.65, ai_complementarity=0.52, baseline_demand_growth=0.08),
    Industry("business_services", robot_intensity=0.12, ai_complementarity=0.78, baseline_demand_growth=0.06),
    Industry("health_services", robot_intensity=0.08, ai_complementarity=0.56, baseline_demand_growth=0.07),
    Industry("software_data_services", robot_intensity=0.03, ai_complementarity=0.88, baseline_demand_growth=0.09),
]

COMMUTING_ZONES = [
    CommutingZone(
        "Motor Belt",
        {
            "autos_and_machinery": 0.54,
            "warehousing_logistics": 0.16,
            "business_services": 0.12,
            "health_services": 0.12,
            "software_data_services": 0.06,
        },
        exposed_occupation_share=0.46,
        adjustment_capacity=0.30,
    ),
    CommutingZone(
        "Logistics Corridor",
        {
            "autos_and_machinery": 0.18,
            "warehousing_logistics": 0.44,
            "business_services": 0.18,
            "health_services": 0.12,
            "software_data_services": 0.08,
        },
        exposed_occupation_share=0.38,
        adjustment_capacity=0.45,
    ),
    CommutingZone(
        "Service Metro",
        {
            "autos_and_machinery": 0.08,
            "warehousing_logistics": 0.12,
            "business_services": 0.36,
            "health_services": 0.26,
            "software_data_services": 0.18,
        },
        exposed_occupation_share=0.24,
        adjustment_capacity=0.68,
    ),
    CommutingZone(
        "Care And Admin Hub",
        {
            "autos_and_machinery": 0.04,
            "warehousing_logistics": 0.10,
            "business_services": 0.28,
            "health_services": 0.46,
            "software_data_services": 0.12,
        },
        exposed_occupation_share=0.22,
        adjustment_capacity=0.58,
    ),
    CommutingZone(
        "AI Services City",
        {
            "autos_and_machinery": 0.03,
            "warehousing_logistics": 0.07,
            "business_services": 0.25,
            "health_services": 0.15,
            "software_data_services": 0.50,
        },
        exposed_occupation_share=0.18,
        adjustment_capacity=0.82,
    ),
]

FIRMS = [
    Firm("Auto parts producer", workforce_task_exposure=0.72, realized_ai_adoption=0.24, vacancy_ai_demand=0.22, output_demand_growth=0.02),
    Firm("National logistics platform", workforce_task_exposure=0.58, realized_ai_adoption=0.46, vacancy_ai_demand=0.62, output_demand_growth=0.07),
    Firm("Claims processing center", workforce_task_exposure=0.64, realized_ai_adoption=0.58, vacancy_ai_demand=0.70, output_demand_growth=0.04),
    Firm("Clinical services network", workforce_task_exposure=0.39, realized_ai_adoption=0.52, vacancy_ai_demand=0.48, output_demand_growth=0.06),
    Firm("Enterprise software firm", workforce_task_exposure=0.44, realized_ai_adoption=0.86, vacancy_ai_demand=0.90, output_demand_growth=0.10),
]


def industry_lookup() -> dict[str, Industry]:
    return {industry.name: industry for industry in INDUSTRIES}


def weighted_zone_value(zone: CommutingZone, field: str) -> float:
    industries = industry_lookup()
    total = sum(zone.industry_shares.values())
    if total <= 0:
        raise ValueError(f"{zone.name} has no industry mass")
    value = 0.0
    for industry_name, share in zone.industry_shares.items():
        industry = industries[industry_name]
        value += (share / total) * float(getattr(industry, field))
    return value


def local_exposure_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for zone in COMMUTING_ZONES:
        robot_exposure = weighted_zone_value(zone, "robot_intensity")
        ai_complementarity = weighted_zone_value(zone, "ai_complementarity")
        baseline_growth = weighted_zone_value(zone, "baseline_demand_growth")
        displacement_pressure = robot_exposure * zone.exposed_occupation_share
        output_offset = baseline_growth + 0.06 * ai_complementarity + 0.04 * zone.adjustment_capacity
        employment_change = 0.025 + output_offset - 0.50 * displacement_pressure
        wage_change = 0.018 + 0.035 * ai_complementarity - 0.20 * displacement_pressure + 0.015 * zone.adjustment_capacity
        rows.append(
            {
                "commuting_zone": zone.name,
                "robot_exposure": round(robot_exposure, 3),
                "ai_complementarity": round(ai_complementarity, 3),
                "exposed_occupation_share": round(zone.exposed_occupation_share, 3),
                "adjustment_capacity": round(zone.adjustment_capacity, 3),
                "employment_change_pp": round(100 * employment_change, 2),
                "wage_change_pp": round(100 * wage_change, 2),
            }
        )
    return rows


def diagnosis_rows(local_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in local_rows:
        employment = float(row["employment_change_pp"])
        wage = float(row["wage_change_pp"])
        robot_exposure = float(row["robot_exposure"])
        ai_complementarity = float(row["ai_complementarity"])
        if employment < 0 and wage < 0:
            pattern = "displacement_dominates"
        elif employment < 0 <= wage:
            pattern = "composition_or_augmentation_with_job_loss"
        elif employment >= 0 and wage < 0:
            pattern = "quantity_growth_with_wage_pressure"
        elif robot_exposure > 0.45 and ai_complementarity > 0.45:
            pattern = "offsetting_robot_and_ai_channels"
        else:
            pattern = "output_or_augmentation_dominates"
        rows.append(
            {
                "commuting_zone": row["commuting_zone"],
                "employment_change_pp": employment,
                "wage_change_pp": wage,
                "incidence_pattern": pattern,
                "interpretation": incidence_interpretation(pattern),
            }
        )
    return rows


def incidence_interpretation(pattern: str) -> str:
    labels = {
        "displacement_dominates": "robot_exposure_and_routine_task_share_are_high",
        "composition_or_augmentation_with_job_loss": "remaining_jobs_may_be_more_skill_intensive",
        "quantity_growth_with_wage_pressure": "scale_or_entry_expands_jobs_but_wage_incidence_is_weak",
        "offsetting_robot_and_ai_channels": "direct_displacement_and_productivity_offsets_coexist",
        "output_or_augmentation_dominates": "productivity_and_complementary_demand_offset_displacement",
    }
    return labels[pattern]


def firm_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for firm in FIRMS:
        displacement_risk = 0.70 * firm.workforce_task_exposure - 0.25 * firm.output_demand_growth
        augmentation_index = 0.55 * firm.realized_ai_adoption + 0.30 * firm.vacancy_ai_demand + 0.15 * firm.output_demand_growth
        net_labor_demand = 0.06 + 0.16 * augmentation_index + 0.12 * firm.output_demand_growth - 0.08 * displacement_risk
        if net_labor_demand > 0.14:
            likely_margin = "employment_growth_from_augmentation_and_scale"
        elif displacement_risk > augmentation_index:
            likely_margin = "task_displacement_risk"
        elif firm.vacancy_ai_demand > firm.realized_ai_adoption:
            likely_margin = "desired_skill_demand_ahead_of_adoption"
        else:
            likely_margin = "mixed_reorganization_margin"
        rows.append(
            {
                "firm": firm.name,
                "workforce_task_exposure": round(firm.workforce_task_exposure, 3),
                "realized_ai_adoption": round(firm.realized_ai_adoption, 3),
                "vacancy_ai_demand": round(firm.vacancy_ai_demand, 3),
                "output_demand_growth": round(firm.output_demand_growth, 3),
                "displacement_risk": round(displacement_risk, 3),
                "augmentation_index": round(augmentation_index, 3),
                "net_labor_demand_index": round(net_labor_demand, 3),
                "likely_margin": likely_margin,
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
    reproduced = local_exposure_rows()
    diagnosed = diagnosis_rows(reproduced)
    transferred = firm_transfer_rows()

    write_csv(lab_dir / "output" / "reproduced" / "local_robot_exposure.csv", reproduced)
    write_csv(lab_dir / "output" / "diagnosed" / "incidence_diagnosis.csv", diagnosed)
    write_csv(lab_dir / "output" / "transfer" / "firm_ai_transfer.csv", transferred)

    note = (
        "Synthetic Week 2 automation, AI, and labor-demand lab complete. "
        "Outputs reproduce local robot exposure logic, diagnose employment-wage "
        "incidence, and transfer the design to firm AI adoption.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
