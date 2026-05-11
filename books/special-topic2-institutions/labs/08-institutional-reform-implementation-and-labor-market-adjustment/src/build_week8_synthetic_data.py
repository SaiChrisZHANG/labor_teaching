from __future__ import annotations

import csv
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def legal_information_rows() -> list[dict[str, object]]:
    sectors = ["retail", "manufacturing", "services", "construction"]
    firm_sizes = ["micro", "small", "medium", "large"]
    worker_types = ["new_entrant", "incumbent", "migrant", "low_wage"]
    rows: list[dict[str, object]] = []
    for worker in range(192):
        sector = sectors[worker % len(sectors)]
        firm_size = firm_sizes[(worker // 4) % len(firm_sizes)]
        worker_type = worker_types[(worker // 8) % len(worker_types)]
        treated = 1 if worker % 4 in (0, 1) else 0
        low_baseline = 1 if worker % 6 in (0, 1, 2) else 0
        local_capacity = round(0.42 + 0.09 * ((worker // 12) % 5), 3)
        firm_visibility = {
            "micro": 0.25,
            "small": 0.42,
            "medium": 0.62,
            "large": 0.82,
        }[firm_size]
        baseline_knowledge = clamp(0.34 + 0.08 * (1 - low_baseline) + 0.05 * firm_visibility, 0.20, 0.75)
        knowledge_gain = 0.24 * treated + 0.06 * treated * low_baseline + 0.04 * local_capacity
        followup_knowledge = clamp(baseline_knowledge + knowledge_gain, 0.20, 0.98)
        perceived_enforcement = clamp(0.28 + 0.20 * treated + 0.30 * local_capacity + 0.08 * firm_visibility, 0.10, 0.95)
        claim_intention = clamp(0.18 + 0.20 * followup_knowledge + 0.10 * perceived_enforcement - 0.05 * (firm_size == "micro"), 0.05, 0.90)
        formal_contract_score = 0.35 + 0.18 * firm_visibility + 0.10 * local_capacity + 0.06 * treated - 0.08 * (sector == "construction")
        formal_contract = 1 if formal_contract_score >= 0.56 else 0
        employment_score = 0.68 + 0.05 * firm_visibility + 0.03 * treated - 0.06 * (worker_type == "new_entrant")
        employment_at_followup = 1 if employment_score >= 0.66 else 0
        wage_index = clamp(
            0.92
            + 0.05 * formal_contract
            + 0.03 * treated
            + 0.04 * firm_visibility
            + 0.02 * (worker_type == "incumbent")
            - 0.03 * (sector == "construction"),
            0.70,
            1.20,
        )
        rows.append(
            {
                "worker_id": f"wk8-worker-{worker + 1:03d}",
                "firm_id": f"wk8-firm-{(worker // 3) + 1:03d}",
                "treated_information": treated,
                "sector": sector,
                "firm_size": firm_size,
                "worker_type": worker_type,
                "low_baseline_knowledge": low_baseline,
                "local_capacity_index": round(local_capacity, 3),
                "firm_visibility_index": round(firm_visibility, 3),
                "baseline_knowledge_index": round(baseline_knowledge, 3),
                "followup_knowledge_index": round(followup_knowledge, 3),
                "perceived_enforcement_index": round(perceived_enforcement, 3),
                "claim_intention_index": round(claim_intention, 3),
                "formal_contract": formal_contract,
                "employment_at_followup": employment_at_followup,
                "wage_index": round(wage_index, 3),
            }
        )
    return rows


def reform_case_rows() -> list[dict[str, object]]:
    return [
        {
            "case_id": "south_africa_legal_information",
            "anchor": "Bertrand-Crepon 2021",
            "reform_family": "legal_information",
            "identifying_variation": "randomized labor-law information treatment",
            "observed_margin": "legal knowledge, perceived enforcement, formal contract, employment",
            "primary_bottleneck": "knowledge_beliefs",
            "secondary_bottleneck": "firm_adaptation",
            "welfare_margin": "take_up_and_bargaining",
            "expected_risk": "medium",
        },
        {
            "case_id": "brazil_enforcement_informality",
            "anchor": "Almeida-Carneiro 2012",
            "reform_family": "enforcement_expansion",
            "identifying_variation": "local enforcement intensity",
            "observed_margin": "informality, compliance, wages, employment",
            "primary_bottleneck": "implementation_capacity",
            "secondary_bottleneck": "informality_evasion",
            "welfare_margin": "incidence_and_displacement",
            "expected_risk": "medium",
        },
        {
            "case_id": "wrongful_discharge_state_adoption",
            "anchor": "Autor-Donohue-Schwab 2004",
            "reform_family": "dismissal_protection",
            "identifying_variation": "staggered state adoption of wrongful-discharge doctrines",
            "observed_margin": "employment, hiring, firing, turnover",
            "primary_bottleneck": "coverage_exposure",
            "secondary_bottleneck": "firm_adaptation",
            "welfare_margin": "employment_security_vs_hiring",
            "expected_risk": "medium",
        },
        {
            "case_id": "formalization_assistance_enforcement",
            "anchor": "de Andrade-Bruhn-McKenzie 2016",
            "reform_family": "formalization_compliance",
            "identifying_variation": "randomized information, assistance, and enforcement pressure",
            "observed_margin": "registration and compliance behavior",
            "primary_bottleneck": "private_benefit_of_formality",
            "secondary_bottleneck": "worker_coverage",
            "welfare_margin": "registration_vs_worker_protection",
            "expected_risk": "high",
        },
        {
            "case_id": "pay_transparency_gender_gap",
            "anchor": "Baker et al. 2023",
            "reform_family": "pay_transparency",
            "identifying_variation": "coverage threshold or mandate timing",
            "observed_margin": "wage gaps, pay compression, bargaining",
            "primary_bottleneck": "information_scope",
            "secondary_bottleneck": "equilibrium_spillovers",
            "welfare_margin": "inequality_and_average_wages",
            "expected_risk": "medium",
        },
        {
            "case_id": "public_employment_service_rollout",
            "anchor": "Dustmann et al. 2014",
            "reform_family": "administrative_reform",
            "identifying_variation": "regional rollout or bundled reform timing",
            "observed_margin": "job-finding, unemployment duration, wages",
            "primary_bottleneck": "administrative_delivery",
            "secondary_bottleneck": "policy_bundling",
            "welfare_margin": "matching_and_incidence",
            "expected_risk": "high",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "wrongful_discharge_event_study",
            "anchor": "Autor-Donohue-Schwab 2004",
            "reform_family": "dismissal_protection",
            "identifying_variation": "staggered adoption of state common-law exceptions",
            "design_family": "staggered_adoption_event_study",
            "observed_margin": "employment, separations, hiring composition",
            "likely_spillover": "firms may adjust hiring before separations are observed",
        },
        {
            "design_id": "labor_inspection_intensity",
            "anchor": "Almeida-Carneiro 2012",
            "reform_family": "enforcement_expansion",
            "identifying_variation": "local variation in inspection or enforcement intensity",
            "design_family": "local_enforcement_exposure",
            "observed_margin": "formality, wages, compliance, employment",
            "likely_spillover": "workers may move between covered and uncovered firms",
        },
        {
            "design_id": "legal_information_rct",
            "anchor": "Bertrand-Crepon 2021",
            "reform_family": "legal_information",
            "identifying_variation": "randomized exposure to labor-law information",
            "design_family": "randomized_information_intervention",
            "observed_margin": "knowledge, beliefs, take-up, labor outcomes",
            "likely_spillover": "untreated workers or firms may learn indirectly",
        },
        {
            "design_id": "formalization_field_experiment",
            "anchor": "de Andrade-Bruhn-McKenzie 2016",
            "reform_family": "formalization_compliance",
            "identifying_variation": "randomized assistance, information, or enforcement threat",
            "design_family": "field_experiment_compliance",
            "observed_margin": "registration, payroll, contract form",
            "likely_spillover": "registered firms may change competition for informal firms",
        },
        {
            "design_id": "pay_transparency_threshold",
            "anchor": "Baker et al. 2023",
            "reform_family": "pay_transparency",
            "identifying_variation": "firm-size threshold or mandate timing",
            "design_family": "threshold_or_coverage_design",
            "observed_margin": "wage gaps, pay compression, promotions, quits",
            "likely_spillover": "uncovered firms may respond to disclosed comparison wages",
        },
        {
            "design_id": "blind_audition_procedure",
            "anchor": "Goldin-Rouse 2000",
            "reform_family": "equal_opportunity_procedure",
            "identifying_variation": "change in evaluation procedure",
            "design_family": "procedural_reform_event_study",
            "observed_margin": "shortlist composition, advancement, hiring",
            "likely_spillover": "selection into auditions may change once procedures are known",
        },
        {
            "design_id": "employment_service_rollout",
            "anchor": "Dustmann et al. 2014",
            "reform_family": "administrative_reform",
            "identifying_variation": "regional rollout or administrative exposure",
            "design_family": "administrative_rollout_did",
            "observed_margin": "matching, unemployment duration, job-finding, wages",
            "likely_spillover": "local labor demand and vacancy posting may adjust",
        },
    ]


def main() -> None:
    write_rows(
        LAB / "original" / "reduced" / "legal_information_trial_synthetic.csv",
        [
            "worker_id",
            "firm_id",
            "treated_information",
            "sector",
            "firm_size",
            "worker_type",
            "low_baseline_knowledge",
            "local_capacity_index",
            "firm_visibility_index",
            "baseline_knowledge_index",
            "followup_knowledge_index",
            "perceived_enforcement_index",
            "claim_intention_index",
            "formal_contract",
            "employment_at_followup",
            "wage_index",
        ],
        legal_information_rows(),
    )
    write_rows(
        LAB / "original" / "reduced" / "reform_cases_synthetic.csv",
        [
            "case_id",
            "anchor",
            "reform_family",
            "identifying_variation",
            "observed_margin",
            "primary_bottleneck",
            "secondary_bottleneck",
            "welfare_margin",
            "expected_risk",
        ],
        reform_case_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "reform_designs_synthetic.csv",
        [
            "design_id",
            "anchor",
            "reform_family",
            "identifying_variation",
            "design_family",
            "observed_margin",
            "likely_spillover",
        ],
        transfer_rows(),
    )
    print("Wrote Week 8 synthetic reform data.")


if __name__ == "__main__":
    main()
