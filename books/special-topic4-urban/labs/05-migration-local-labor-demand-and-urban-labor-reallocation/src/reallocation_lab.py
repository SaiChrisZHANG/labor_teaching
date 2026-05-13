from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Place:
    code: str
    name: str
    demand_shock: float
    housing_elasticity: float
    commute_openness: float
    moving_friction: float
    firm_entry_capacity: float
    specialization: float
    diversity: float
    baseline_employment: int
    baseline_population: int
    baseline_rent: float


@dataclass(frozen=True)
class Neighborhood:
    name: str
    professional_inflow: float
    service_demand_shock: float
    rent_pressure: float
    incumbent_renter_share: float
    transit_access: float
    small_business_turnover: float


@dataclass(frozen=True)
class IndustryPlace:
    name: str
    specialization: float
    diversity: float
    skill_transferability: float
    housing_elasticity: float
    sector_shock: float


PLACES = [
    Place("P1", "Metro Center", 12.0, 0.35, 0.82, 0.28, 0.72, 0.45, 0.78, 210000, 305000, 1850.0),
    Place("P2", "Milltown", -9.0, 0.58, 0.36, 0.62, 0.24, 0.78, 0.31, 86000, 132000, 940.0),
    Place("P3", "Riverport", 6.5, 0.74, 0.55, 0.34, 0.61, 0.52, 0.62, 118000, 174000, 1220.0),
    Place("P4", "Lake Junction", -4.0, 0.42, 0.68, 0.46, 0.38, 0.61, 0.49, 96000, 148000, 1080.0),
]


NEIGHBORHOODS = [
    Neighborhood("Old Market", 0.70, 0.62, 0.68, 0.74, 0.80, 0.45),
    Neighborhood("South Works", 0.32, 0.48, 0.36, 0.69, 0.42, 0.28),
    Neighborhood("Harbor Flats", 0.55, 0.54, 0.51, 0.58, 0.64, 0.38),
]


INDUSTRY_PLACES = [
    IndustryPlace("Single-industry mill city", 0.86, 0.22, 0.34, 0.50, -10.0),
    IndustryPlace("Diversified regional hub", 0.38, 0.76, 0.68, 0.58, -10.0),
    IndustryPlace("Amenity tech center", 0.54, 0.64, 0.72, 0.32, -10.0),
]


def local_adjustment_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for place in PLACES:
        shock = place.demand_shock
        wage_delta_pct = 0.22 * shock * (1.0 - 0.25 * place.commute_openness)
        rent_delta_pct = 0.18 * shock * (1.0 - place.housing_elasticity) + 0.04 * shock
        population_delta_pct = 0.11 * shock * place.housing_elasticity * (1.0 - place.moving_friction)
        commuting_delta_pct = 0.16 * shock * place.commute_openness
        employment_delta_pct = 0.20 * shock + 0.05 * commuting_delta_pct + 0.04 * place.firm_entry_capacity * shock
        unemployment_delta_pp = -0.10 * shock * (0.45 + place.diversity)
        firm_entry_delta_pct = 0.07 * shock * place.firm_entry_capacity
        sector_composition_delta = 0.05 * shock * (1.0 - place.specialization)
        incumbent_real_access_delta = (
            wage_delta_pct
            - rent_delta_pct
            - 0.03 * abs(commuting_delta_pct)
            - 0.04 * max(0.0, -employment_delta_pct)
        )
        rows.append(
            {
                "place": place.name,
                "demand_shock_index": round(shock, 2),
                "delta_wage_pct": round(wage_delta_pct, 2),
                "delta_employment_pct": round(employment_delta_pct, 2),
                "delta_unemployment_pp": round(unemployment_delta_pp, 2),
                "delta_resident_population_pct": round(population_delta_pct, 2),
                "delta_in_commuting_pct": round(commuting_delta_pct, 2),
                "delta_rent_pct": round(rent_delta_pct, 2),
                "delta_firm_entry_pct": round(firm_entry_delta_pct, 2),
                "delta_sector_composition_index": round(sector_composition_delta, 2),
                "incumbent_real_access_delta": round(incumbent_real_access_delta, 2),
                "interpretation": adjustment_interpretation(
                    incumbent_real_access_delta, rent_delta_pct, commuting_delta_pct
                ),
            }
        )
    return rows


def adjustment_interpretation(
    real_access: float, rent_delta: float, commuting_delta: float
) -> str:
    if real_access > 0.75 and commuting_delta > 0.5:
        return "worker_gain_with_commuting_margin"
    if real_access > 0.75:
        return "incumbent_real_access_gain"
    if rent_delta > 1.0 and real_access <= 0.75:
        return "rent_capitalization_limits_incumbent_gain"
    if real_access < -0.75:
        return "persistent_worker_loss_risk"
    return "mixed_adjustment_requires_incidence_data"


def incidence_rows() -> list[dict[str, str]]:
    return [
        {
            "claim": "A demand shock raises workplace employment in Metro Center.",
            "unit": "place_and_commuters",
            "main_margin": "commuting_and_firm_entry",
            "welfare_object": "workplace_jobs_not_resident_welfare",
            "needed_data": "residence_workplace_flows_and_incumbent_worker_panel",
            "main_threat": "employment growth may accrue to in-commuters or migrants",
        },
        {
            "claim": "Rents rise after a local boom.",
            "unit": "renters_landlords_homeowners",
            "main_margin": "housing_capitalization",
            "welfare_object": "real_access_net_of_rent",
            "needed_data": "tenure_specific rents prices earnings and moves",
            "main_threat": "nominal wage gains may overstate renter welfare",
        },
        {
            "claim": "Milltown's unemployment rate partly recovers after out-migration.",
            "unit": "place_versus_people",
            "main_margin": "selective_migration",
            "welfare_object": "incumbent_worker_recovery",
            "needed_data": "pre_shock_incumbent_worker_longitudinal_outcomes",
            "main_threat": "place recovery can hide worker scarring",
        },
        {
            "claim": "A commuting improvement connects Riverport residents to a job center.",
            "unit": "residents_and_workplaces",
            "main_margin": "commuting_access",
            "welfare_object": "reachable_jobs_less_travel_cost",
            "needed_data": "travel_times residence_workplace_links and wages",
            "main_threat": "transport shocks may also move neighborhood demand and rents",
        },
        {
            "claim": "A diversified hub loses fewer jobs after a sector shock.",
            "unit": "workers_in_local_labor_market",
            "main_margin": "local_reallocation_capacity",
            "welfare_object": "worker_insurance_against_unemployment",
            "needed_data": "industry_mix worker_transitions earnings and migration",
            "main_threat": "diversity may proxy for size human capital or amenities",
        },
    ]


def gentrification_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in NEIGHBORHOODS:
        service_jobs_delta = 12.0 * n.service_demand_shock + 4.0 * n.professional_inflow
        professional_jobs_delta = 9.0 * n.professional_inflow
        incumbent_rent_burden_delta = 7.5 * n.rent_pressure * n.incumbent_renter_share
        reachable_job_gain = (service_jobs_delta + professional_jobs_delta) * n.transit_access
        small_business_disruption = 6.0 * n.small_business_turnover
        incumbent_net_access = (
            0.18 * reachable_job_gain
            - incumbent_rent_burden_delta
            - 0.35 * small_business_disruption
        )
        rows.append(
            {
                "neighborhood": n.name,
                "delta_service_jobs_index": round(service_jobs_delta, 2),
                "delta_professional_jobs_index": round(professional_jobs_delta, 2),
                "delta_rent_burden_index": round(incumbent_rent_burden_delta, 2),
                "reachable_job_gain_index": round(reachable_job_gain, 2),
                "small_business_disruption_index": round(small_business_disruption, 2),
                "incumbent_net_access_index": round(incumbent_net_access, 2),
                "interpretation": gentrification_interpretation(incumbent_net_access),
            }
        )
    return rows


def gentrification_interpretation(net_access: float) -> str:
    if net_access > 1.0:
        return "incumbent_labor_access_gain_possible"
    if net_access < -1.0:
        return "rent_and_disruption_dominate_for_incumbents"
    return "composition_and_commuting_data_needed"


def diversification_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for place in INDUSTRY_PLACES:
        direct_job_loss = abs(place.sector_shock) * (0.55 + 0.45 * place.specialization)
        reallocation_capacity = (
            10.0 * place.diversity
            + 5.0 * place.skill_transferability
            + 2.0 * place.housing_elasticity
        )
        net_employment_loss = max(0.0, direct_job_loss - 0.45 * reallocation_capacity)
        migration_pressure = max(0.0, net_employment_loss - 2.0 * place.housing_elasticity)
        insurance_value = reallocation_capacity - direct_job_loss
        rows.append(
            {
                "place_type": place.name,
                "specialization_index": round(place.specialization, 2),
                "diversity_index": round(place.diversity, 2),
                "skill_transferability_index": round(place.skill_transferability, 2),
                "sector_shock_index": round(place.sector_shock, 2),
                "direct_job_loss_index": round(direct_job_loss, 2),
                "reallocation_capacity_index": round(reallocation_capacity, 2),
                "net_employment_loss_index": round(net_employment_loss, 2),
                "migration_pressure_index": round(migration_pressure, 2),
                "worker_insurance_value_index": round(insurance_value, 2),
                "interpretation": diversification_interpretation(insurance_value),
            }
        )
    return rows


def diversification_interpretation(insurance_value: float) -> str:
    if insurance_value > 1.0:
        return "diversification_buffers_worker_shock"
    if insurance_value < -1.0:
        return "specialization_exposes_workers_to_loss"
    return "ambiguous_resilience_requires_worker_flows"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    write_csv(
        lab_dir / "output" / "reproduced" / "local_adjustment_vector.csv",
        local_adjustment_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "incidence_diagnosis.csv",
        incidence_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "gentrification_restructuring.csv",
        gentrification_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "diversification_resilience.csv",
        diversification_rows(),
    )


if __name__ == "__main__":
    main()
