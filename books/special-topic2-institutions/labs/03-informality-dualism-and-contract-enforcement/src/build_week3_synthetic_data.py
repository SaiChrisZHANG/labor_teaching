from __future__ import annotations

import csv
import math
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def firm_rows() -> list[dict[str, object]]:
    firms = [
        ("textiles_micro", "manufacturing", 0.34, 0.30, 0.50, 0.29, 0.47),
        ("food_stall_cluster", "services", 0.28, 0.22, 0.42, 0.24, 0.38),
        ("repair_workshop", "services", 0.45, 0.38, 0.47, 0.31, 0.44),
        ("garment_exporter", "manufacturing", 0.74, 0.72, 0.38, 0.48, 0.66),
        ("logistics_medium", "transport", 0.62, 0.61, 0.44, 0.42, 0.58),
        ("construction_subcontractor", "construction", 0.53, 0.44, 0.56, 0.36, 0.51),
        ("retail_chain_unit", "retail", 0.69, 0.70, 0.40, 0.45, 0.63),
        ("own_account_services", "services", 0.25, 0.18, 0.34, 0.21, 0.35),
    ]
    rows: list[dict[str, object]] = []
    for firm_id, sector, base_prod, visibility, reg_cost, base_skill, benefit_value in firms:
        for year in range(2018, 2026):
            t = year - 2018
            productivity = clamp(base_prod + 0.015 * t + 0.025 * math.sin(t / 2.0 + base_prod), 0.18, 0.92)
            enforcement = clamp(0.18 + 0.58 * visibility + 0.020 * t + 0.018 * math.cos(t + visibility), 0.12, 0.92)
            payroll_tax = clamp(0.34 + 0.06 * math.sin(t / 3.0) + 0.05 * (sector in {"manufacturing", "construction"}), 0.25, 0.48)
            registration_cost = clamp(reg_cost - 0.010 * t + 0.012 * math.cos(t / 2.0), 0.18, 0.60)
            worker_skill = clamp(base_skill + 0.020 * t + 0.08 * productivity, 0.20, 0.82)
            registration_score = 0.30 + 0.45 * productivity + 0.25 * visibility + 0.20 * enforcement - 0.38 * registration_cost
            registered = int(registration_score >= 0.58)
            payroll_reported_share = clamp(
                0.12
                + 0.48 * registered
                + 0.22 * enforcement
                + 0.16 * productivity
                - 0.25 * payroll_tax
                + 0.06 * benefit_value,
                0.05,
                0.98,
            )
            hidden_worker_share = 1.0 - payroll_reported_share
            contract_quality = clamp(0.18 + 0.40 * registered + 0.22 * payroll_reported_share + 0.12 * productivity, 0.10, 0.96)
            enforceability = clamp(contract_quality * (0.45 + 0.55 * enforcement), 0.05, 0.92)
            firm_size = max(1, round(3 + 30 * productivity + 8 * registered - 5 * payroll_tax - 2 * hidden_worker_share))
            formal_wage = clamp(0.82 + 0.30 * productivity + 0.15 * worker_skill - 0.09 * payroll_tax + 0.05 * benefit_value, 0.72, 1.28)
            informal_wage = clamp(0.76 + 0.22 * productivity + 0.12 * worker_skill + 0.06 * hidden_worker_share, 0.62, 1.12)
            rows.append(
                {
                    "firm_id": firm_id,
                    "sector": sector,
                    "year": year,
                    "productivity_index": round(productivity, 3),
                    "visibility_index": round(visibility, 3),
                    "enforcement_index": round(enforcement, 3),
                    "registration_cost_index": round(registration_cost, 3),
                    "payroll_tax_index": round(payroll_tax, 3),
                    "worker_skill_index": round(worker_skill, 3),
                    "benefit_value_index": round(benefit_value, 3),
                    "registered_firm": registered,
                    "payroll_reported_share": round(payroll_reported_share, 3),
                    "hidden_worker_share": round(hidden_worker_share, 3),
                    "contract_quality_index": round(contract_quality, 3),
                    "effective_enforceability_index": round(enforceability, 3),
                    "firm_size": firm_size,
                    "formal_wage_index": round(formal_wage, 3),
                    "informal_wage_index": round(informal_wage, 3),
                }
            )
    return rows


def design_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "ulyssea_registration_payroll_model",
            "anchor": "Ulyssea 2018",
            "variation": "policy counterfactuals that change enforcement, registration costs, and payroll costs",
            "unit": "firm-year or firm type",
            "observed_margin": "registration, payroll reporting, hidden employment, productivity, firm size",
            "expected_object": "firm_compliance_registration",
        },
        {
            "design_id": "meghir_narita_robin_worker_firm_search",
            "anchor": "Meghir-Narita-Robin 2015",
            "variation": "estimated search equilibrium matching workers and firms across formal and informal jobs",
            "unit": "worker-firm match",
            "observed_margin": "wages, transitions, benefits, worker sorting",
            "expected_object": "wage_setting_worker_sorting",
        },
        {
            "design_id": "samaniego_fernandez_enforcement_cost",
            "anchor": "Samaniego-Fernandez 2024",
            "variation": "increase in the expected cost of informal employment",
            "unit": "worker-firm or firm-year",
            "observed_margin": "formal employment, payroll reporting, wages, firm response",
            "expected_object": "enforcement_formalization",
        },
        {
            "design_id": "gerard_health_insurance_discontinuity",
            "anchor": "Gerard 2021",
            "variation": "health insurance eligibility discontinuity around formal status",
            "unit": "worker or household",
            "observed_margin": "formalization, insurance take-up, labor supply, welfare",
            "expected_object": "policy_welfare_incidence",
        },
        {
            "design_id": "naidu_yuchtman_contract_enforcement",
            "anchor": "Naidu-Yuchtman 2013",
            "variation": "historical legal change in coercive contract enforcement",
            "unit": "district-year or labor market",
            "observed_margin": "wages, labor mobility, sensitivity to labor demand",
            "expected_object": "contract_enforceability",
        },
        {
            "design_id": "worker_panel_transition_matrix",
            "anchor": "worker panel design",
            "variation": "observed transitions across formal work, informal work, self-employment, and unemployment",
            "unit": "worker-year",
            "observed_margin": "transition hazards, wage changes, benefit changes",
            "expected_object": "worker_sorting_mobility",
        },
        {
            "design_id": "linked_payroll_registry_audit",
            "anchor": "matched administrative design",
            "variation": "linked firm registry, payroll records, and audit exposure",
            "unit": "worker-firm-year",
            "observed_margin": "reported employment, hidden employment proxy, wages, separations",
            "expected_object": "equilibrium_reallocation",
        },
    ]


def main() -> None:
    firm_fields = [
        "firm_id",
        "sector",
        "year",
        "productivity_index",
        "visibility_index",
        "enforcement_index",
        "registration_cost_index",
        "payroll_tax_index",
        "worker_skill_index",
        "benefit_value_index",
        "registered_firm",
        "payroll_reported_share",
        "hidden_worker_share",
        "contract_quality_index",
        "effective_enforceability_index",
        "firm_size",
        "formal_wage_index",
        "informal_wage_index",
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
        LAB / "original" / "reduced" / "firm_informality_synthetic.csv",
        firm_fields,
        firm_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "informality_designs_synthetic.csv",
        design_fields,
        design_rows(),
    )


if __name__ == "__main__":
    main()
