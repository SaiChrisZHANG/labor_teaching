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


def binary_from_rate(index: int, rate: float) -> int:
    threshold = int(round(rate * 100))
    return int((index * 37) % 100 < threshold)


def inherited_norms_rows() -> list[dict[str, object]]:
    groups = [
        ("low_family_obligation", 0.24, 0.68, 0.32, 0.70, 0.54, 0.42),
        ("medium_family_obligation", 0.50, 0.58, 0.49, 0.64, 0.45, 0.55),
        ("high_family_obligation", 0.76, 0.48, 0.67, 0.57, 0.35, 0.69),
    ]
    rows: list[dict[str, object]] = []
    for group, obligation, trust, regulation_support, employment, mobility, female_lfp in groups:
        for worker in range(90):
            local_demand = 0.92 + (worker % 6) * 0.025
            formal_protection = 0.42 + ((worker + len(group)) % 5) * 0.07
            rows.append(
                {
                    "worker_id": f"{group[:4]}-{worker:03d}",
                    "origin_norm_group": group,
                    "family_obligation_index": round(obligation + ((worker % 7) - 3) * 0.01, 3),
                    "generalized_trust_index": round(trust + ((worker % 5) - 2) * 0.012, 3),
                    "formal_protection_index": round(formal_protection, 3),
                    "local_labor_demand_index": round(local_demand, 3),
                    "supports_employment_protection": binary_from_rate(worker, regulation_support),
                    "employed": binary_from_rate(worker + 5, employment),
                    "changed_region_for_work": binary_from_rate(worker + 11, mobility),
                    "female_labor_force_participation": binary_from_rate(worker + 17, female_lfp),
                }
            )
    return rows


def network_mobility_rows() -> list[dict[str, object]]:
    groups = [
        ("weak_network_insurance", 0.28, 0.62, 0.18, 0.28, 1.31, 0.58),
        ("middle_network_insurance", 0.52, 0.46, 0.33, 0.39, 1.24, 0.51),
        ("strong_network_insurance", 0.78, 0.30, 0.54, 0.52, 1.18, 0.44),
    ]
    rows: list[dict[str, object]] = []
    for group, insurance, migration, network_job, obligation, wage_gap, urban_job_access in groups:
        for worker in range(80):
            rows.append(
                {
                    "worker_id": f"{group[:4]}-{worker:03d}",
                    "network_group": group,
                    "informal_insurance_index": round(insurance + ((worker % 8) - 3.5) * 0.008, 3),
                    "network_job_share": round(network_job + ((worker % 4) - 1.5) * 0.01, 3),
                    "community_obligation_index": round(obligation + ((worker % 6) - 2.5) * 0.012, 3),
                    "urban_wage_offer_ratio": round(wage_gap + ((worker % 5) - 2) * 0.015, 3),
                    "urban_job_access_index": round(urban_job_access + ((worker % 7) - 3) * 0.01, 3),
                    "migrated_to_city": binary_from_rate(worker + 3, migration),
                    "took_network_job": binary_from_rate(worker + 13, network_job),
                }
            )
    return rows


def main() -> None:
    inherited_fields = [
        "worker_id",
        "origin_norm_group",
        "family_obligation_index",
        "generalized_trust_index",
        "formal_protection_index",
        "local_labor_demand_index",
        "supports_employment_protection",
        "employed",
        "changed_region_for_work",
        "female_labor_force_participation",
    ]
    network_fields = [
        "worker_id",
        "network_group",
        "informal_insurance_index",
        "network_job_share",
        "community_obligation_index",
        "urban_wage_offer_ratio",
        "urban_job_access_index",
        "migrated_to_city",
        "took_network_job",
    ]
    write_rows(
        LAB / "original" / "reduced" / "inherited_norms_labor_synthetic.csv",
        inherited_fields,
        inherited_norms_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "network_mobility_synthetic.csv",
        network_fields,
        network_mobility_rows(),
    )


if __name__ == "__main__":
    main()
