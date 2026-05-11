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


def enforcement_rows() -> list[dict[str, object]]:
    localities = [
        ("capital_core", 1.00, 0.72, 0.68, 0.74, 0.16),
        ("industrial_corridor", 1.00, 0.66, 0.61, 0.69, 0.18),
        ("secondary_city", 1.00, 0.54, 0.54, 0.61, 0.21),
        ("border_services", 1.00, 0.47, 0.46, 0.55, 0.23),
        ("agrarian_hinterland", 1.00, 0.34, 0.38, 0.47, 0.27),
        ("frontier_town", 1.00, 0.28, 0.32, 0.42, 0.30),
    ]
    rows: list[dict[str, object]] = []
    for locality, legal_rule, base_access, base_knowledge, base_formal, wage_rigidity in localities:
        for year in range(2014, 2026):
            t = year - 2014
            inspector_access = clamp(base_access + 0.025 * math.sin(t / 2.0) + 0.008 * (t % 3), 0.12, 0.92)
            worker_knowledge = clamp(base_knowledge + 0.018 * math.cos(t / 3.0) + 0.006 * (t % 4), 0.10, 0.90)
            local_demand = clamp(0.88 + 0.012 * t + 0.025 * math.sin(t / 1.7), 0.80, 1.10)
            effective_law = legal_rule * inspector_access * worker_knowledge
            compliance = clamp(0.28 + 0.70 * effective_law + 0.04 * local_demand, 0.20, 0.94)
            benefit_receipt = clamp(0.18 + 0.76 * compliance + 0.05 * worker_knowledge, 0.18, 0.96)
            formal_share = clamp(base_formal + 0.23 * compliance - 0.10 * inspector_access + 0.08 * wage_rigidity, 0.30, 0.91)
            informal_share = 1.0 - formal_share
            formal_wage = clamp(1.04 - 0.15 * inspector_access + 0.06 * benefit_receipt + 0.04 * local_demand, 0.78, 1.18)
            rows.append(
                {
                    "locality": locality,
                    "year": year,
                    "legal_rule_index": round(legal_rule, 3),
                    "inspector_access_index": round(inspector_access, 3),
                    "worker_knowledge_index": round(worker_knowledge, 3),
                    "effective_law_index": round(effective_law, 3),
                    "compliance_index": round(compliance, 3),
                    "benefit_receipt_rate": round(benefit_receipt, 3),
                    "formal_share": round(formal_share, 3),
                    "informal_share": round(informal_share, 3),
                    "formal_wage_index": round(formal_wage, 3),
                    "local_demand_index": round(local_demand, 3),
                    "wage_rigidity_index": round(wage_rigidity, 3),
                }
            )
    return rows


def transfer_design_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "wrongful_discharge_doctrine",
            "anchor": "Autor-Donohue-Schwab",
            "variation": "court-made wrongful-discharge doctrine changes across states",
            "unit": "state-year or worker-state-year",
            "observed_margin": "employment and dismissal-sensitive outcomes",
            "expected_object": "law_on_books",
        },
        {
            "design_id": "inspector_distance",
            "anchor": "Almeida-Carneiro",
            "variation": "locality exposure to labor inspectors",
            "unit": "locality-year",
            "observed_margin": "compliance, wages, formality",
            "expected_object": "enforcement",
        },
        {
            "design_id": "rights_information_rct",
            "anchor": "Bertrand-Crepon",
            "variation": "randomized information about labor-law rules",
            "unit": "firm or worker",
            "observed_margin": "beliefs, claims, employment behavior",
            "expected_object": "knowledge",
        },
        {
            "design_id": "labor_rights_capacity_index",
            "anchor": "Berliner-Greenleaf-Lake-Noveck",
            "variation": "cross-country state-capacity and labor-rights measures",
            "unit": "country-year",
            "observed_margin": "broad labor-rights performance",
            "expected_object": "state_capacity_bundle",
        },
        {
            "design_id": "linked_payroll_inspection_records",
            "anchor": "matched employer-employee design",
            "variation": "linked inspection and payroll records",
            "unit": "worker-firm-year",
            "observed_margin": "wages, benefits, worker flows, sorting",
            "expected_object": "incidence_and_sorting",
        },
        {
            "design_id": "coenforcement_complaint_program",
            "anchor": "Amengual",
            "variation": "inspector linkages with unions and worker organizations",
            "unit": "workplace or locality",
            "observed_margin": "complaints, inspections, compliance",
            "expected_object": "effective_compliance",
        },
    ]


def main() -> None:
    enforcement_fields = [
        "locality",
        "year",
        "legal_rule_index",
        "inspector_access_index",
        "worker_knowledge_index",
        "effective_law_index",
        "compliance_index",
        "benefit_receipt_rate",
        "formal_share",
        "informal_share",
        "formal_wage_index",
        "local_demand_index",
        "wage_rigidity_index",
    ]
    transfer_fields = [
        "design_id",
        "anchor",
        "variation",
        "unit",
        "observed_margin",
        "expected_object",
    ]
    write_rows(
        LAB / "original" / "reduced" / "enforcement_informality_synthetic.csv",
        enforcement_fields,
        enforcement_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "implementation_designs_synthetic.csv",
        transfer_fields,
        transfer_design_rows(),
    )


if __name__ == "__main__":
    main()
