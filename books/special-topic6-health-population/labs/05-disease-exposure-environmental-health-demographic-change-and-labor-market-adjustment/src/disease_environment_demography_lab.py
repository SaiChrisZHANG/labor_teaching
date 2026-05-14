from __future__ import annotations

import csv
from pathlib import Path


YEARS = list(range(2018, 2024))

GROUPS = [
    {
        "group": "frontline_service",
        "remote_feasible": 0.08,
        "frontline": 1,
        "migrant_share": 0.24,
        "care_burden": 0.48,
        "environmental_risk": 0.32,
        "older_worker_share": 0.18,
        "base_wage": 0.72,
    },
    {
        "group": "remote_professional",
        "remote_feasible": 0.86,
        "frontline": 0,
        "migrant_share": 0.10,
        "care_burden": 0.34,
        "environmental_risk": 0.12,
        "older_worker_share": 0.16,
        "base_wage": 1.18,
    },
    {
        "group": "manufacturing_heat",
        "remote_feasible": 0.18,
        "frontline": 0,
        "migrant_share": 0.18,
        "care_burden": 0.26,
        "environmental_risk": 0.76,
        "older_worker_share": 0.24,
        "base_wage": 0.92,
    },
    {
        "group": "care_and_health",
        "remote_feasible": 0.12,
        "frontline": 1,
        "migrant_share": 0.20,
        "care_burden": 0.56,
        "environmental_risk": 0.24,
        "older_worker_share": 0.22,
        "base_wage": 0.84,
    },
    {
        "group": "migrant_food_and_delivery",
        "remote_feasible": 0.05,
        "frontline": 1,
        "migrant_share": 0.52,
        "care_burden": 0.38,
        "environmental_risk": 0.58,
        "older_worker_share": 0.12,
        "base_wage": 0.66,
    },
    {
        "group": "older_local_services",
        "remote_feasible": 0.20,
        "frontline": 0,
        "migrant_share": 0.08,
        "care_burden": 0.30,
        "environmental_risk": 0.30,
        "older_worker_share": 0.54,
        "base_wage": 0.78,
    },
]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def pandemic_intensity(year: int) -> float:
    return {
        2018: 0.0,
        2019: 0.0,
        2020: 1.0,
        2021: 0.55,
        2022: 0.22,
        2023: 0.10,
    }[year]


def policy_intensity(year: int) -> float:
    return {
        2018: 0.0,
        2019: 0.0,
        2020: 0.82,
        2021: 0.38,
        2022: 0.10,
        2023: 0.04,
    }[year]


def synthetic_panel() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for region_num in range(1, 37):
        region_heat = 0.18 + 0.035 * (region_num % 8)
        region_pollution = 0.14 + 0.028 * ((region_num * 2) % 9)
        baseline_aging = 0.14 + 0.012 * (region_num % 10)
        migration_access = clamp(0.78 - 0.035 * (region_num % 11))
        local_demand_base = 0.94 + 0.012 * ((region_num + 3) % 9)

        for group_info in GROUPS:
            for year in YEARS:
                pandemic = pandemic_intensity(year)
                policy = policy_intensity(year)
                time_trend = year - 2019
                frontline = int(group_info["frontline"])
                remote_feasible = float(group_info["remote_feasible"])
                migrant_share = float(group_info["migrant_share"])
                care_burden = float(group_info["care_burden"])
                environmental_risk = float(group_info["environmental_risk"])
                older_worker_share = float(group_info["older_worker_share"])

                aging_share = clamp(baseline_aging + 0.006 * time_trend + 0.18 * older_worker_share)
                dependency_ratio = clamp(0.46 + 0.42 * aging_share + 0.08 * (1 - remote_feasible))
                environmental_exposure = clamp(
                    0.45 * region_heat
                    + 0.35 * region_pollution
                    + 0.35 * environmental_risk
                    + 0.05 * max(year - 2020, 0)
                )
                disease_exposure = clamp(
                    0.08
                    + pandemic
                    * (
                        0.34
                        + 0.30 * frontline
                        + 0.18 * migrant_share
                        + 0.10 * older_worker_share
                        - 0.22 * remote_feasible
                    )
                )
                school_care_constraint = clamp(policy * care_burden * (1 - 0.45 * remote_feasible))
                demand_collapse = clamp(
                    policy * (0.34 * frontline + 0.26 * (1 - remote_feasible))
                    + pandemic * 0.10 * (1 - local_demand_base)
                )
                capacity_loss = clamp(
                    0.35 * disease_exposure
                    + 0.20 * environmental_exposure
                    + 0.12 * older_worker_share * pandemic
                )
                remote_work_rate = clamp(remote_feasible * (0.18 + 0.62 * pandemic + 0.45 * (year >= 2022)))
                migration_out_rate = clamp(
                    0.015
                    + 0.050 * disease_exposure
                    + 0.038 * environmental_exposure
                    + 0.030 * remote_work_rate
                    - 0.035 * migrant_share
                    - 0.025 * (1 - migration_access)
                )
                automation_adoption = clamp(
                    0.06
                    + 0.20 * aging_share
                    + 0.12 * environmental_exposure
                    + 0.09 * pandemic * (1 - remote_feasible)
                    + 0.05 * (year >= 2022)
                )

                employment_index = (
                    100.0
                    + 0.75 * time_trend
                    - 20.0 * demand_collapse
                    - 13.0 * capacity_loss
                    - 8.0 * school_care_constraint
                    - 4.0 * migration_out_rate
                    + 5.0 * remote_work_rate
                    - 3.2 * automation_adoption
                )
                hours_index = (
                    100.0
                    + 0.35 * time_trend
                    - 10.0 * capacity_loss
                    - 12.0 * school_care_constraint
                    - 4.0 * environmental_exposure
                    + 3.5 * remote_work_rate
                )
                productivity_index = (
                    100.0
                    + 0.55 * time_trend
                    - 10.5 * environmental_exposure
                    - 6.5 * disease_exposure
                    + 4.0 * automation_adoption
                    + 2.0 * remote_work_rate
                )
                wage_index = (
                    100.0
                    + 1.00 * time_trend
                    + 6.0 * capacity_loss
                    + 2.5 * automation_adoption
                    - 2.2 * demand_collapse
                    + 8.0 * (float(group_info["base_wage"]) - 0.85)
                )
                welfare_loss_index = (
                    100.0
                    * (
                        0.30 * disease_exposure
                        + 0.22 * environmental_exposure
                        + 0.18 * school_care_constraint
                        + 0.12 * migration_out_rate
                        + 0.08 * dependency_ratio
                        - 0.05 * remote_work_rate
                    )
                )

                rows.append(
                    {
                        "region_id": f"region_{region_num:02d}",
                        "worker_group": group_info["group"],
                        "year": year,
                        "frontline": frontline,
                        "remote_feasible": round(remote_feasible, 3),
                        "migrant_share": round(migrant_share, 3),
                        "care_burden": round(care_burden, 3),
                        "older_worker_share": round(older_worker_share, 3),
                        "aging_share": round(aging_share, 3),
                        "dependency_ratio": round(dependency_ratio, 3),
                        "disease_exposure": round(disease_exposure, 3),
                        "policy_intensity": round(policy, 3),
                        "environmental_exposure": round(environmental_exposure, 3),
                        "school_care_constraint": round(school_care_constraint, 3),
                        "demand_collapse": round(demand_collapse, 3),
                        "capacity_loss": round(capacity_loss, 3),
                        "remote_work_rate": round(remote_work_rate, 3),
                        "migration_out_rate": round(migration_out_rate, 3),
                        "automation_adoption": round(automation_adoption, 3),
                        "employment_index": round(employment_index, 3),
                        "hours_index": round(hours_index, 3),
                        "wage_index": round(wage_index, 3),
                        "productivity_index": round(productivity_index, 3),
                        "welfare_loss_index": round(welfare_loss_index, 3),
                    }
                )
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def selected(rows: list[dict[str, object]], selector) -> list[dict[str, object]]:
    return [row for row in rows if selector(row)]


def mean_for(rows: list[dict[str, object]], year: int, outcome: str) -> float:
    cells = [float(row[outcome]) for row in rows if int(row["year"]) == year]
    return mean(cells)


def profile_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups = [
        ("all_worker_groups", lambda row: True),
        ("frontline_jobs", lambda row: int(row["frontline"]) == 1),
        ("remote_feasible_jobs", lambda row: float(row["remote_feasible"]) >= 0.60),
        ("high_migrant_share", lambda row: float(row["migrant_share"]) >= 0.30),
        ("high_care_burden", lambda row: float(row["care_burden"]) >= 0.45),
        ("high_environmental_exposure", lambda row: float(row["environmental_exposure"]) >= 0.55),
        ("older_worker_concentration", lambda row: float(row["older_worker_share"]) >= 0.45),
        ("low_exposure_reference", lambda row: float(row["disease_exposure"]) <= 0.12 and float(row["environmental_exposure"]) < 0.45),
    ]
    outcomes = [
        "employment_index",
        "hours_index",
        "wage_index",
        "productivity_index",
        "migration_out_rate",
        "automation_adoption",
        "welfare_loss_index",
    ]

    output: list[dict[str, object]] = []
    for group_name, selector in groups:
        subset = selected(rows, selector)
        item: dict[str, object] = {
            "profile_group": group_name,
            "region_group_year_cells": len(subset),
            "mean_disease_exposure_2020": round(mean_for(subset, 2020, "disease_exposure"), 3),
            "mean_environmental_exposure_2020": round(mean_for(subset, 2020, "environmental_exposure"), 3),
            "mean_remote_work_rate_2020": round(mean_for(subset, 2020, "remote_work_rate"), 3),
            "mean_policy_intensity_2020": round(mean_for(subset, 2020, "policy_intensity"), 3),
        }
        for outcome in outcomes:
            pre = mean_for(subset, 2019, outcome)
            shock = mean_for(subset, 2020, outcome)
            recovery = mean_for(subset, 2023, outcome)
            item[f"{outcome}_2019"] = round(pre, 3)
            item[f"{outcome}_2020"] = round(shock, 3)
            item[f"{outcome}_delta_2020_2019"] = round(shock - pre, 3)
            item[f"{outcome}_recovery_2023_2020"] = round(recovery - shock, 3)
        output.append(item)
    return output


def row_named(profile: list[dict[str, object]], name: str) -> dict[str, object]:
    return next(row for row in profile if row["profile_group"] == name)


def diagnosis_rows(profile: list[dict[str, object]]) -> list[dict[str, object]]:
    all_groups = row_named(profile, "all_worker_groups")
    frontline = row_named(profile, "frontline_jobs")
    remote = row_named(profile, "remote_feasible_jobs")
    migrant = row_named(profile, "high_migrant_share")
    care = row_named(profile, "high_care_burden")
    environment = row_named(profile, "high_environmental_exposure")
    older = row_named(profile, "older_worker_concentration")
    low = row_named(profile, "low_exposure_reference")

    comparisons = [
        (
            "frontline_vs_remote_employment_drop",
            float(frontline["employment_index_delta_2020_2019"]) - float(remote["employment_index_delta_2020_2019"]),
            "disease_risk_policy_and_occupation_sorting",
            "Frontline employment falls more than remote-feasible employment, but the gap bundles risk, demand, shutdowns, and occupation.",
        ),
        (
            "care_burden_hours_drop",
            float(care["hours_index_delta_2020_2019"]) - float(all_groups["hours_index_delta_2020_2019"]),
            "caregiving_constraint",
            "High-care groups lose more hours when school and household constraints arrive with the health shock.",
        ),
        (
            "migrant_welfare_gap",
            float(migrant["welfare_loss_index_delta_2020_2019"]) - float(low["welfare_loss_index_delta_2020_2019"]),
            "migrant_vulnerability_and_limited_adjustment",
            "High-migrant groups show larger welfare loss because exposure is high and migration or job-switching options are constrained.",
        ),
        (
            "environment_productivity_gap",
            float(environment["productivity_index_delta_2020_2019"]) - float(low["productivity_index_delta_2020_2019"]),
            "environmental_productivity_incidence",
            "High environmental exposure lowers productivity even when employment is only one part of the incidence.",
        ),
        (
            "older_automation_response",
            float(older["automation_adoption_recovery_2023_2020"]) - float(all_groups["automation_adoption_recovery_2023_2020"]),
            "aging_and_firm_reorganization",
            "Older-worker regions show stronger automation growth, linking demographic pressure to firm response.",
        ),
        (
            "migration_as_adjustment_and_selection",
            float(remote["migration_out_rate_delta_2020_2019"]) - float(migrant["migration_out_rate_delta_2020_2019"]),
            "migration_selection",
            "Remote-feasible workers can move more easily, so movers and stayers are selected on job portability and resources.",
        ),
        (
            "wage_vs_welfare_incidence",
            float(all_groups["welfare_loss_index_delta_2020_2019"]) - float(all_groups["wage_index_delta_2020_2019"]),
            "hidden_welfare_incidence",
            "Welfare losses rise much more than wages change, showing why wages alone miss risk, fatigue, care, and unsafe amenities.",
        ),
    ]

    return [
        {
            "diagnostic_margin": name,
            "gap": round(gap, 3),
            "dominant_issue": issue,
            "diagnostic_question": question,
        }
        for name, gap, issue, question in comparisons
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "black_death_labor_scarcity",
            "shock": "mortality and population loss",
            "labor_outcome": "wages, bargaining power, labor institutions, migration, and inequality",
            "data_needed": "historical census, wage series, mortality, land-labor ratios, institutional records",
            "identifying_variation": "place-level plague intensity interacted with pre-shock labor and land structure",
            "main_threat": "institutional change and market access may be correlated with mortality intensity",
            "welfare_margin": "bargaining power and institutional constraints may not be visible in wages alone",
        },
        {
            "scenario": "tuberculosis_reporting_laws",
            "shock": "public-health reporting and disease-control capacity",
            "labor_outcome": "cohort health, schooling, work capacity, urban productivity, and migration",
            "data_needed": "mortality records, reporting-law timing, historical census, schooling, occupations, earnings proxies",
            "identifying_variation": "city or state reporting-law timing with pre-trend checks",
            "main_threat": "public-health adopters may differ in sanitation, income, and urban growth trends",
            "welfare_margin": "reduced disease risk and improved human capital can precede observed wage changes",
        },
        {
            "scenario": "hiv_aids_mortality_and_skill_premia",
            "shock": "working-age mortality and morbidity",
            "labor_outcome": "wages, employment, household labor allocation, care, and skill premia",
            "data_needed": "mortality, census, labor force, household composition, education, and regional disease intensity",
            "identifying_variation": "regional mortality exposure by skill and age group",
            "main_threat": "migration, survival selection, and concurrent macroeconomic change",
            "welfare_margin": "care burdens, orphanhood, morbidity, and household insurance losses exceed wage effects",
        },
        {
            "scenario": "pollution_productivity",
            "shock": "air pollution exposure",
            "labor_outcome": "labor supply, attendance, productivity, output quality, and job switching",
            "data_needed": "pollution monitors or satellite data linked to payroll, attendance, output, and residence or workplace",
            "identifying_variation": "regulatory, weather-driven, or plant-closure exposure shifts",
            "main_threat": "avoidance behavior, endogenous residence, and correlated local demand",
            "welfare_margin": "fatigue, risk, and lower job quality may remain hidden if workers stay employed",
        },
        {
            "scenario": "heat_and_manufacturing",
            "shock": "temperature and heat stress",
            "labor_outcome": "hours, productivity, absences, shift timing, injury risk, and capital substitution",
            "data_needed": "weather, plant output, attendance, wages, injuries, and shift schedules",
            "identifying_variation": "within-place heat variation with seasonality and demand controls",
            "main_threat": "adaptation, air conditioning, seasonality, and product demand may move with heat",
            "welfare_margin": "unsafe work and recovery costs can matter even when output is partly maintained",
        },
        {
            "scenario": "migrant_epidemic_vulnerability",
            "shock": "disease exposure interacted with migrant status and occupation",
            "labor_outcome": "job loss, hours, remittances, mobility, housing crowding, and access to benefits",
            "data_needed": "labor force, migrant status, occupation risk, housing, mobility, benefits, and health exposure",
            "identifying_variation": "occupation-by-policy exposure or place-by-migrant concentration",
            "main_threat": "legal status, selection into occupations, and undercounting in surveys",
            "welfare_margin": "income loss, health risk, remittance pressure, and immobility are jointly relevant",
        },
        {
            "scenario": "aging_automation_and_retirement",
            "shock": "population aging and fertility decline",
            "labor_outcome": "labor shortages, wages, retirement, care demand, technology adoption, and migration",
            "data_needed": "age structure, firm technology, vacancies, wages, retirement, care-sector employment, and migration",
            "identifying_variation": "regional cohort-size variation or differential aging exposure across local labor markets",
            "main_threat": "migration and endogenous technology adoption are both responses to aging",
            "welfare_margin": "late-career job feasibility and care burden can move without immediate wage effects",
        },
    ]


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
    panel = synthetic_panel()
    profile = profile_rows(panel)

    write_csv(lab_dir / "original" / "reduced" / "disease_environment_demography_synthetic.csv", panel)
    write_csv(lab_dir / "output" / "reproduced" / "labor_market_incidence_profile.csv", profile)
    write_csv(lab_dir / "output" / "diagnosed" / "adjustment_mechanism_diagnosis.csv", diagnosis_rows(profile))
    write_csv(lab_dir / "output" / "transfer" / "disease_environment_demography_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 5 disease/environment/demography lab complete. Outputs compare "
        "COVID-style incidence across occupation, exposure, care burden, migrant status, "
        "environmental risk, demography, migration, automation, and welfare; diagnose "
        "causal limits; and transfer the design to historical, development, environmental, "
        "migration, and aging settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
