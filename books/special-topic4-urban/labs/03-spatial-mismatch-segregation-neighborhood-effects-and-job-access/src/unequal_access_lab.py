from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Neighborhood:
    code: str
    name: str
    opportunity_index: float
    school_index: float
    network_index: float


@dataclass(frozen=True)
class FamilyMove:
    family_id: str
    origin: str
    destination: str
    child_age_at_move: int
    baseline_family_index: float


@dataclass(frozen=True)
class Residence:
    code: str
    name: str
    group: str


@dataclass(frozen=True)
class JobCenter:
    code: str
    name: str
    vacancies_before: int
    vacancies_after: int


NEIGHBORHOODS = {
    "N1": Neighborhood("N1", "East River", 42.0, 41.0, 38.0),
    "N2": Neighborhood("N2", "Lakeview", 68.0, 72.0, 64.0),
    "N3": Neighborhood("N3", "West Heights", 76.0, 81.0, 59.0),
    "N4": Neighborhood("N4", "South Junction", 50.0, 48.0, 72.0),
}

MOVES = [
    FamilyMove("F01", "N1", "N2", 3, 52.0),
    FamilyMove("F02", "N1", "N2", 9, 52.0),
    FamilyMove("F03", "N1", "N2", 15, 52.0),
    FamilyMove("F04", "N1", "N3", 4, 55.0),
    FamilyMove("F05", "N1", "N3", 12, 55.0),
    FamilyMove("F06", "N1", "N4", 6, 51.0),
    FamilyMove("F07", "N1", "N4", 14, 51.0),
]

RESIDENCES = [
    Residence("R1", "Central Green", "central_transit_reliant"),
    Residence("R2", "East River", "segregated_central"),
    Residence("R3", "North Loop", "mixed_access"),
    Residence("R4", "Outer Ridge", "suburban_auto_access"),
]

JOB_CENTERS = [
    JobCenter("J1", "Downtown services", 120, 85),
    JobCenter("J2", "Medical district", 90, 85),
    JobCenter("J3", "Airport logistics", 45, 80),
    JobCenter("J4", "Outer belt warehouses", 35, 95),
]

TRAVEL_COST = {
    ("R1", "J1"): 14,
    ("R1", "J2"): 18,
    ("R1", "J3"): 42,
    ("R1", "J4"): 52,
    ("R2", "J1"): 22,
    ("R2", "J2"): 26,
    ("R2", "J3"): 48,
    ("R2", "J4"): 58,
    ("R3", "J1"): 26,
    ("R3", "J2"): 24,
    ("R3", "J3"): 30,
    ("R3", "J4"): 38,
    ("R4", "J1"): 45,
    ("R4", "J2"): 40,
    ("R4", "J3"): 20,
    ("R4", "J4"): 18,
}


def childhood_exposure(age_at_move: int) -> float:
    return max(0.0, min(1.0, (18 - age_at_move) / 18))


def exposure_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for move in MOVES:
        origin = NEIGHBORHOODS[move.origin]
        destination = NEIGHBORHOODS[move.destination]
        exposure = childhood_exposure(move.child_age_at_move)
        opportunity_gain = destination.opportunity_index - origin.opportunity_index
        school_gain = destination.school_index - origin.school_index
        network_gain = destination.network_index - origin.network_index
        predicted_earnings_index = (
            move.baseline_family_index
            + 0.22 * exposure * opportunity_gain
            + 0.06 * exposure * school_gain
            + 0.04 * exposure * network_gain
        )
        rows.append(
            {
                "family_id": move.family_id,
                "origin": origin.name,
                "destination": destination.name,
                "child_age_at_move": move.child_age_at_move,
                "childhood_destination_exposure": round(exposure, 3),
                "destination_opportunity_gain": round(opportunity_gain, 2),
                "school_channel_gain": round(school_gain, 2),
                "network_channel_gain": round(network_gain, 2),
                "predicted_adult_earnings_index": round(predicted_earnings_index, 2),
                "design_logic": "age_at_move_exposure_not_current_access",
            }
        )
    return rows


def mechanism_rows() -> list[dict[str, str]]:
    return [
        {
            "claim": "Longer childhood exposure to a higher-opportunity destination raises adult earnings.",
            "labor_object": "adult_earnings",
            "counterfactual": "same family move with different child age or exposure duration",
            "clean_design_family": "mover_age_at_move",
            "main_threat": "endogenous timing and bundled school or peer channels",
        },
        {
            "claim": "A worker lives near many jobs but receives fewer callbacks because of address stigma.",
            "labor_object": "callback_or_interview",
            "counterfactual": "same application with randomized address or commute signal",
            "clean_design_family": "audit_correspondence",
            "main_threat": "callback margin may not equal equilibrium employment",
        },
        {
            "claim": "Neighbors help each other enter the same establishments.",
            "labor_object": "job_finding_through_referrals",
            "counterfactual": "same worker in a different neighbor-coworker network",
            "clean_design_family": "matched_employer_employee_network",
            "main_threat": "sorting into neighborhoods and firms",
        },
        {
            "claim": "A school boundary changes adult outcomes by changing school quality.",
            "labor_object": "human_capital_and_later_earnings",
            "counterfactual": "same residence near the boundary assigned to a different school",
            "clean_design_family": "school_boundary_or_admission",
            "main_threat": "housing capitalization and selection around boundaries",
        },
        {
            "claim": "Job suburbanization lowers employment for transit-reliant central neighborhoods.",
            "labor_object": "reachable_vacancies_and_employment",
            "counterfactual": "same residents facing the pre-suburbanization job geography",
            "clean_design_family": "policy_or_job_location_shock",
            "main_threat": "access effects may differ from realized employment effects",
        },
    ]


def access_score(residence: Residence, after: bool) -> float:
    score = 0.0
    for job in JOB_CENTERS:
        vacancies = job.vacancies_after if after else job.vacancies_before
        travel = TRAVEL_COST[(residence.code, job.code)]
        score += vacancies * math.exp(-0.035 * travel)
    return score


def reachable_vacancies(residence: Residence, after: bool, threshold: int = 35) -> int:
    total = 0
    for job in JOB_CENTERS:
        if TRAVEL_COST[(residence.code, job.code)] <= threshold:
            total += job.vacancies_after if after else job.vacancies_before
    return total


def transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for residence in RESIDENCES:
        before_score = access_score(residence, after=False)
        after_score = access_score(residence, after=True)
        before_reachable = reachable_vacancies(residence, after=False)
        after_reachable = reachable_vacancies(residence, after=True)
        rows.append(
            {
                "residence": residence.name,
                "group": residence.group,
                "access_score_before": round(before_score, 2),
                "access_score_after": round(after_score, 2),
                "delta_access_score": round(after_score - before_score, 2),
                "reachable_vacancies_before": before_reachable,
                "reachable_vacancies_after": after_reachable,
                "delta_reachable_vacancies": after_reachable - before_reachable,
                "interpretation": "job_suburbanization_access_shock_not_realized_employment",
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
    write_csv(
        lab_dir / "output" / "reproduced" / "exposure_timing_predictions.csv",
        exposure_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "mechanism_diagnosis.csv",
        mechanism_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "job_suburbanization_access.csv",
        transfer_rows(),
    )
    note = (
        "Synthetic Week 3 lab complete. Outputs distinguish exposure timing, "
        "mechanism diagnosis, and job-suburbanization access shocks.\n"
    )
    (lab_dir / "output" / "reproduced" / "reproduction_note.txt").write_text(
        note, encoding="utf-8"
    )
    print(note.strip())


if __name__ == "__main__":
    main()
