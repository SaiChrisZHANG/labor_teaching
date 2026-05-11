from __future__ import annotations

import csv
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def binary_from_rate(index: int, rate: float) -> int:
    threshold = int(round(rate * 1000))
    return int((index * 37 + 17) % 1000 < threshold)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def inherited_culture_rows() -> list[dict[str, object]]:
    groups = [
        ("egalitarian_family_role", 0.72, 1.75, 0.22, 0.30),
        ("moderate_family_role", 0.60, 2.05, 0.42, 0.44),
        ("traditional_family_role", 0.44, 2.55, 0.65, 0.61),
        ("restrictive_family_role", 0.32, 3.05, 0.82, 0.76),
    ]
    rows: list[dict[str, object]] = []
    for group_index, (group, origin_lfp, origin_fertility, role_norm, peer_pressure) in enumerate(groups):
        for worker in range(96):
            row_index = group_index * 96 + worker
            host_demand = 0.44 + (worker % 8) * 0.055
            host_wage = 0.88 + ((worker + 2 * group_index) % 9) * 0.035
            childcare = 0.24 + ((worker + group_index) % 7) * 0.055
            education_years = 11 + ((worker + 2 * group_index) % 7)
            children_under6 = binary_from_rate(row_index + 3, 0.34 + 0.06 * group_index)
            married = binary_from_rate(row_index + 11, 0.55 + 0.05 * group_index)
            current_peer_pressure = clamp(peer_pressure + ((worker % 6) - 2.5) * 0.018, 0.12, 0.92)
            work_rate = clamp(
                0.44
                + 0.25 * origin_lfp
                - 0.22 * role_norm
                - 0.10 * current_peer_pressure
                + 0.12 * (host_demand - 0.55)
                + 0.10 * (host_wage - 1.00)
                - 0.12 * (childcare - 0.40)
                + 0.012 * (education_years - 13)
                - 0.07 * children_under6,
                0.14,
                0.92,
            )
            works = binary_from_rate(row_index + 19, work_rate)
            hours = 0
            if works:
                hours = round(
                    clamp(
                        26
                        + 10 * (host_demand - 0.55)
                        + 6 * (host_wage - 1.00)
                        - 7 * role_norm
                        - 4 * children_under6
                        + (worker % 5),
                        12,
                        45,
                    ),
                    1,
                )
            rows.append(
                {
                    "worker_id": f"wk5-{row_index + 1:03d}",
                    "origin_norm_group": group,
                    "origin_female_lfp": round(origin_lfp + ((worker % 5) - 2) * 0.006, 3),
                    "origin_fertility": round(origin_fertility + ((worker % 4) - 1.5) * 0.05, 3),
                    "family_role_norm_index": round(role_norm + ((worker % 7) - 3) * 0.01, 3),
                    "current_peer_pressure_index": round(current_peer_pressure, 3),
                    "host_labor_demand_index": round(host_demand, 3),
                    "host_wage_index": round(host_wage, 3),
                    "childcare_cost_index": round(childcare, 3),
                    "education_years": education_years,
                    "married": married,
                    "children_under6": children_under6,
                    "works_for_pay": works,
                    "weekly_hours": hours,
                }
            )
    return rows


def job_entry_rows() -> list[dict[str, object]]:
    frames = [
        ("neutral", 1.00, 0.00, 0.00),
        ("team_based", 0.98, 0.05, 0.01),
        ("competitive", 1.06, -0.14, 0.03),
        ("competitive_with_flexibility", 1.04, -0.06, 0.02),
        ("pink_collar", 0.97, 0.02, -0.16),
    ]
    rows: list[dict[str, object]] = []
    for frame_index, (frame, wage, women_effect, men_effect) in enumerate(frames):
        for worker in range(80):
            for group in ["women", "men"]:
                row_index = frame_index * 160 + worker * 2 + (0 if group == "women" else 1)
                care_obligation = 0.24 + ((worker + frame_index) % 6) * 0.06
                confidence = 0.44 + ((worker + 2 * frame_index) % 7) * 0.055
                if group == "women":
                    norm_fit = 0.58 + women_effect - 0.10 * (frame == "competitive")
                else:
                    norm_fit = 0.60 + men_effect - 0.12 * (frame == "pink_collar")
                norm_fit = clamp(norm_fit + ((worker % 5) - 2) * 0.012, 0.12, 0.92)
                application_rate = clamp(
                    0.36
                    + 0.20 * norm_fit
                    + 0.10 * (wage - 1.00)
                    + 0.07 * (confidence - 0.50)
                    - 0.06 * (care_obligation - 0.40),
                    0.10,
                    0.88,
                )
                rows.append(
                    {
                        "applicant_id": f"app-{row_index + 1:04d}",
                        "applicant_group": group,
                        "job_frame": frame,
                        "offered_wage_index": round(wage, 3),
                        "care_obligation_index": round(care_obligation, 3),
                        "self_promotion_confidence_index": round(confidence, 3),
                        "perceived_norm_fit_index": round(norm_fit, 3),
                        "application_submitted": binary_from_rate(row_index + 23, application_rate),
                    }
                )
    return rows


def design_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "second_generation_inherited_culture",
            "anchor": "Fernandez-Fogli 2009",
            "variation": "origin-country work and fertility proxies among descendants in a common host setting",
            "unit": "worker or household",
            "observed_margin": "labor-force participation, fertility, hours",
            "expected_object": "inherited_culture_transmission",
        },
        {
            "design_id": "historical_plough_persistence",
            "anchor": "Alesina-Giuliano-Nunn 2013",
            "variation": "historical agricultural technology predicts modern role norms",
            "unit": "ethnic group, country, or region",
            "observed_margin": "gender-role beliefs, female labor supply",
            "expected_object": "historical_persistence",
        },
        {
            "design_id": "competitive_job_entry_field_experiment",
            "anchor": "Flory-Leibbrandt-List 2015",
            "variation": "job advertisement randomly varies competitive compensation or framing",
            "unit": "potential applicant",
            "observed_margin": "application and job-entry decisions",
            "expected_object": "job_entry_response",
        },
        {
            "design_id": "gender_coded_occupation_entry",
            "anchor": "Delfino 2024",
            "variation": "information or recruitment changes entry into gender-coded occupations",
            "unit": "potential applicant",
            "observed_margin": "occupational entry",
            "expected_object": "job_entry_response",
        },
        {
            "design_id": "religion_reputation_acceptable_work",
            "anchor": "Carvalho 2013",
            "variation": "reputation-preserving conduct changes public work or mobility choices",
            "unit": "worker, household, or community",
            "observed_margin": "public work, mobility, sector choice",
            "expected_object": "religion_reputation_norm",
        },
        {
            "design_id": "workplace_networking_promotion",
            "anchor": "Cullen-Perez-Truglia 2023",
            "variation": "informal interaction with managers affects promotion opportunities",
            "unit": "worker-manager pair or worker-year",
            "observed_margin": "networking, visibility, promotion",
            "expected_object": "workplace_promotion_norm",
        },
        {
            "design_id": "local_unemployment_social_norm",
            "anchor": "Clark 2003",
            "variation": "local unemployment changes the social cost of nonemployment",
            "unit": "worker-year or local labor market",
            "observed_margin": "well-being, unemployment stigma, search",
            "expected_object": "local_social_environment",
        },
        {
            "design_id": "swiss_language_border_work_attitudes",
            "anchor": "Eugster-Lalive-Steinhauer-Zweimuller 2017",
            "variation": "language-region border shifts work attitudes under shared national policy",
            "unit": "worker or region",
            "observed_margin": "job search, benefit use, work attitudes",
            "expected_object": "local_social_environment",
        },
        {
            "design_id": "market_level_labor_supply_suppression",
            "anchor": "Breza-Kaur-Krishnaswamy 2019",
            "variation": "wage offers and social visibility change labor-supply acceptance",
            "unit": "worker or local labor market",
            "observed_margin": "wage acceptance, labor supply, undercutting",
            "expected_object": "market_supply_discipline",
        },
        {
            "design_id": "category_hierarchy_audit",
            "anchor": "Week 6 boundary case",
            "variation": "group names or category signals change employer callbacks",
            "unit": "application or employer",
            "observed_margin": "hiring access and employer beliefs",
            "expected_object": "structural_hierarchy_week6",
        },
    ]


def main() -> None:
    inherited_fields = [
        "worker_id",
        "origin_norm_group",
        "origin_female_lfp",
        "origin_fertility",
        "family_role_norm_index",
        "current_peer_pressure_index",
        "host_labor_demand_index",
        "host_wage_index",
        "childcare_cost_index",
        "education_years",
        "married",
        "children_under6",
        "works_for_pay",
        "weekly_hours",
    ]
    job_fields = [
        "applicant_id",
        "applicant_group",
        "job_frame",
        "offered_wage_index",
        "care_obligation_index",
        "self_promotion_confidence_index",
        "perceived_norm_fit_index",
        "application_submitted",
    ]
    design_fields = [
        "design_id",
        "anchor",
        "variation",
        "unit",
        "observed_margin",
        "expected_object",
    ]
    write_rows(
        LAB / "original" / "reduced" / "inherited_culture_norms_synthetic.csv",
        inherited_fields,
        inherited_culture_rows(),
    )
    write_rows(
        LAB / "original" / "reduced" / "job_entry_norm_framing_synthetic.csv",
        job_fields,
        job_entry_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "norm_designs_synthetic.csv",
        design_fields,
        design_rows(),
    )


if __name__ == "__main__":
    main()
