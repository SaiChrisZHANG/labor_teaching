from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Residence:
    code: str
    name: str
    rent_index: float
    amenity_index: float
    admin_area: str


@dataclass(frozen=True)
class Workplace:
    code: str
    name: str
    wage_index: float
    vacancies: int
    sector: str
    admin_area: str


RESIDENCES = [
    Residence("R1", "Northside", 14.0, 1.2, "city"),
    Residence("R2", "Central", 18.0, 2.4, "city"),
    Residence("R3", "West Flats", 11.5, 0.4, "suburb"),
    Residence("R4", "South Gate", 10.5, -0.3, "suburb"),
]

WORKPLACES = [
    Workplace("J1", "Downtown services", 31.0, 45, "services", "city"),
    Workplace("J2", "Medical district", 34.0, 35, "health", "city"),
    Workplace("J3", "University labs", 36.0, 25, "education", "city"),
    Workplace("J4", "Airport logistics", 27.0, 50, "logistics", "suburb"),
    Workplace("J5", "Outer tech park", 42.0, 30, "technology", "suburb"),
    Workplace("J6", "Warehouse belt", 24.0, 55, "logistics", "suburb"),
]

COMMUTE_COST = {
    ("R1", "J1"): 18,
    ("R1", "J2"): 24,
    ("R1", "J3"): 26,
    ("R1", "J4"): 42,
    ("R1", "J5"): 48,
    ("R1", "J6"): 44,
    ("R2", "J1"): 10,
    ("R2", "J2"): 15,
    ("R2", "J3"): 18,
    ("R2", "J4"): 34,
    ("R2", "J5"): 40,
    ("R2", "J6"): 38,
    ("R3", "J1"): 35,
    ("R3", "J2"): 38,
    ("R3", "J3"): 42,
    ("R3", "J4"): 24,
    ("R3", "J5"): 26,
    ("R3", "J6"): 20,
    ("R4", "J1"): 44,
    ("R4", "J2"): 46,
    ("R4", "J3"): 50,
    ("R4", "J4"): 28,
    ("R4", "J5"): 36,
    ("R4", "J6"): 18,
}

SHOCK_REDUCTION = {
    ("R3", "J4"): 8,
    ("R3", "J5"): 8,
    ("R3", "J6"): 6,
    ("R4", "J4"): 10,
    ("R4", "J5"): 9,
    ("R4", "J6"): 7,
}

THRESHOLDS = [25, 35, 45]


def weighted_average(values: list[tuple[float, int]]) -> float:
    total_weight = sum(weight for _, weight in values)
    if total_weight == 0:
        return 0.0
    return sum(value * weight for value, weight in values) / total_weight


def commute_cost(residence: Residence, workplace: Workplace, shock: bool = False) -> float:
    base = COMMUTE_COST[(residence.code, workplace.code)]
    if not shock:
        return float(base)
    return float(max(5, base - SHOCK_REDUCTION.get((residence.code, workplace.code), 0)))


def utility(residence: Residence, workplace: Workplace, shock: bool = False) -> float:
    return (
        workplace.wage_index
        - residence.rent_index
        - 0.18 * commute_cost(residence, workplace, shock=shock)
        + residence.amenity_index
    )


def access_label(accessible_vacancies: int) -> str:
    if accessible_vacancies >= 150:
        return "broad_flow_market"
    if accessible_vacancies >= 90:
        return "intermediate_flow_market"
    return "narrow_flow_market"


def accessible_jobs(residence: Residence, threshold: int, shock: bool = False) -> list[Workplace]:
    return [
        workplace
        for workplace in WORKPLACES
        if commute_cost(residence, workplace, shock=shock) <= threshold
    ]


def reproduce_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for residence in RESIDENCES:
        for threshold in THRESHOLDS:
            jobs = accessible_jobs(residence, threshold)
            wage_values = [(job.wage_index, job.vacancies) for job in jobs]
            commute_values = [
                (commute_cost(residence, job), job.vacancies) for job in jobs
            ]
            vacancies = sum(job.vacancies for job in jobs)
            best_utility = max((utility(residence, job) for job in jobs), default=0.0)
            rows.append(
                {
                    "residence": residence.name,
                    "residence_admin_area": residence.admin_area,
                    "threshold": threshold,
                    "accessible_workplaces": len(jobs),
                    "accessible_vacancies": vacancies,
                    "average_accessible_wage": round(weighted_average(wage_values), 2),
                    "average_commute_cost": round(weighted_average(commute_values), 2),
                    "best_net_opportunity": round(best_utility, 2),
                    "access_based_market": access_label(vacancies),
                }
            )
    return rows


def diagnosis_rows() -> list[dict[str, str]]:
    return [
        {
            "object": "commuting_flow",
            "classification": "flow_based_market_definition",
            "week1_question": "Which residences and workplaces are connected by feasible travel costs?",
        },
        {
            "object": "workplace_wage",
            "classification": "nominal_workplace_measure",
            "week1_question": "What does the job pay before rents, commuting costs, and amenities?",
        },
        {
            "object": "residential_rent",
            "classification": "residence_based_cost",
            "week1_question": "How much of the wage is capitalized into housing access?",
        },
        {
            "object": "accessible_jobs",
            "classification": "opportunity_set",
            "week1_question": "Which jobs are feasible under a generalized commuting-cost budget?",
        },
        {
            "object": "realized_commute",
            "classification": "chosen_match_not_access",
            "week1_question": "Which commute is chosen after offers, search, housing, and preferences?",
        },
        {
            "object": "best_net_opportunity",
            "classification": "spatial_equilibrium_object",
            "week1_question": "How do wages, rents, commuting costs, and amenities combine in welfare?",
        },
        {
            "object": "urban_wage_premium",
            "classification": "channel_decomposition",
            "week1_question": "Is the premium productivity, learning, sorting, or compensation?",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    threshold = 30
    for residence in RESIDENCES:
        baseline_jobs = accessible_jobs(residence, threshold, shock=False)
        shock_jobs = accessible_jobs(residence, threshold, shock=True)
        baseline_vacancies = sum(job.vacancies for job in baseline_jobs)
        shock_vacancies = sum(job.vacancies for job in shock_jobs)
        baseline_best = max(
            (utility(residence, job, shock=False) for job in baseline_jobs),
            default=0.0,
        )
        shock_best = max(
            (utility(residence, job, shock=True) for job in shock_jobs),
            default=0.0,
        )
        rows.append(
            {
                "residence": residence.name,
                "threshold": threshold,
                "baseline_accessible_vacancies": baseline_vacancies,
                "shock_accessible_vacancies": shock_vacancies,
                "delta_accessible_vacancies": shock_vacancies - baseline_vacancies,
                "baseline_best_net_opportunity": round(baseline_best, 2),
                "shock_best_net_opportunity": round(shock_best, 2),
                "delta_best_net_opportunity": round(shock_best - baseline_best, 2),
                "interpretation": "commuting_friction_change_not_migration",
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    write_csv(lab_dir / "output" / "reproduced" / "job_access_by_residence.csv", reproduce_rows())
    write_csv(lab_dir / "output" / "diagnosed" / "spatial_objects_map.csv", diagnosis_rows())
    write_csv(lab_dir / "output" / "transfer" / "commuting_shock_summary.csv", transfer_rows())
    note = (
        "Synthetic Week 1 access lab complete. Outputs distinguish access, "
        "realized commute, workplace wages, residential rents, and net opportunity.\n"
    )
    (lab_dir / "output" / "reproduced" / "reproduction_note.txt").write_text(
        note, encoding="utf-8"
    )
    print(note.strip())


if __name__ == "__main__":
    main()
