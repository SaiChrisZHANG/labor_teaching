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


def boundary_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for district in range(96):
        exposed = 1 if district < 48 else 0
        pair_id = district % 24
        side_index = district // 48
        distance_to_boundary = round(1.5 + (pair_id % 12) * 2.25 + side_index * 0.35, 2)
        altitude_index = round(0.45 + (pair_id % 8) * 0.07 + (0.03 if exposed else 0.00), 3)
        ruggedness_index = round(0.25 + (pair_id % 6) * 0.05 + (0.02 if pair_id % 2 else 0.00), 3)
        precolonial_density = round(0.38 + (pair_id % 10) * 0.04 + (0.01 if exposed else 0.00), 3)
        public_goods_index = clamp(0.64 - 0.12 * exposed - 0.002 * distance_to_boundary + 0.03 * (pair_id % 3), 0.20, 0.90)
        road_access_index = clamp(0.68 - 0.10 * exposed - 0.001 * distance_to_boundary + 0.02 * (pair_id % 4), 0.20, 0.95)
        schooling_years = clamp(8.2 - 0.75 * exposed + 0.45 * public_goods_index - 0.15 * ruggedness_index, 4.5, 11.5)
        migration_rate = clamp(0.18 - 0.035 * exposed + 0.030 * road_access_index, 0.05, 0.40)
        nonfarm_share = clamp(0.46 - 0.065 * exposed + 0.060 * road_access_index + 0.018 * (pair_id % 5), 0.15, 0.80)
        wage_index = clamp(1.00 - 0.055 * exposed + 0.035 * schooling_years / 10 + 0.040 * nonfarm_share, 0.70, 1.35)
        employer_power_index = clamp(0.48 + 0.09 * exposed - 0.04 * migration_rate + 0.01 * (pair_id % 4), 0.20, 0.90)
        rows.append(
            {
                "district_id": f"wk7-district-{district + 1:03d}",
                "matched_pair": f"pair-{pair_id + 1:02d}",
                "historical_mita_exposure": exposed,
                "near_boundary": int(distance_to_boundary <= 16),
                "distance_to_boundary": distance_to_boundary,
                "altitude_index": round(altitude_index, 3),
                "ruggedness_index": round(ruggedness_index, 3),
                "precolonial_density": round(precolonial_density, 3),
                "public_goods_index": round(public_goods_index, 3),
                "road_access_index": round(road_access_index, 3),
                "schooling_years": round(schooling_years, 3),
                "migration_rate": round(migration_rate, 3),
                "nonfarm_share": round(nonfarm_share, 3),
                "wage_index": round(wage_index, 3),
                "employer_power_index": round(employer_power_index, 3),
            }
        )
    return rows


def persistence_claim_rows() -> list[dict[str, object]]:
    return [
        {
            "claim_id": "mita_public_goods_labor_access",
            "anchor": "Dell 2010",
            "historical_treatment": "forced labor draft boundary",
            "modern_outcome": "wage index and nonfarm work",
            "proposed_mechanism": "public goods, road access, and worker outside options",
            "claim_type": "institutional_persistence_labor_channel",
            "first_labor_margin": "outside options and market access",
            "alternative_fundamental": "altitude and precolonial settlement",
            "data_source": "historical map plus modern district outcomes",
            "expected_risk": "medium",
        },
        {
            "claim_id": "mountain_region_low_wages",
            "anchor": "negative control example",
            "historical_treatment": "mountain geography",
            "modern_outcome": "low wage index",
            "proposed_mechanism": "rugged terrain limits transport",
            "claim_type": "persistent_fundamentals",
            "first_labor_margin": "commuting and market access",
            "alternative_fundamental": "geography is the treatment",
            "data_source": "GIS terrain layer",
            "expected_risk": "low",
        },
        {
            "claim_id": "wartime_factory_cluster",
            "anchor": "Aizer et al. 2020 / Ferrara 2023",
            "historical_treatment": "wartime defense demand",
            "modern_outcome": "minority occupation upgrading",
            "proposed_mechanism": "temporary demand shock creates skills and employer networks",
            "claim_type": "path_dependence",
            "first_labor_margin": "occupational openings",
            "alternative_fundamental": "urban industrial potential",
            "data_source": "war production records and linked census",
            "expected_risk": "medium",
        },
        {
            "claim_id": "serfdom_abolition_mobility",
            "anchor": "Markevich-Zhuravskaya 2018",
            "historical_treatment": "abolition of serfdom",
            "modern_outcome": "migration and sectoral structure",
            "proposed_mechanism": "mobility, competition, and land-labor reallocation",
            "claim_type": "institutional_persistence_labor_channel",
            "first_labor_margin": "mobility and competition",
            "alternative_fundamental": "soil quality and estate selection",
            "data_source": "historical administrative records",
            "expected_risk": "medium",
        },
        {
            "claim_id": "ancestry_share_current_gap",
            "anchor": "proxy caution example",
            "historical_treatment": "ancestry share",
            "modern_outcome": "earnings gap",
            "proposed_mechanism": "unspecified historical legacy",
            "claim_type": "overclaimed_persistence",
            "first_labor_margin": "not specified",
            "alternative_fundamental": "migration selection and current networks",
            "data_source": "ancestry proxy and current survey",
            "expected_risk": "high",
        },
        {
            "claim_id": "reconstruction_schooling_occupation",
            "anchor": "Jones-Schmick 2025",
            "historical_treatment": "Reconstruction-era schooling access",
            "modern_outcome": "Black-White occupational inequality",
            "proposed_mechanism": "human capital and occupational standing",
            "claim_type": "institutional_persistence_labor_channel",
            "first_labor_margin": "schooling and job ladder access",
            "alternative_fundamental": "county development and selective migration",
            "data_source": "school archives and linked census",
            "expected_risk": "medium",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "mita_boundary_discontinuity",
            "anchor": "Dell 2010",
            "historical_variation": "mining mita boundary",
            "design_family": "historical_border_discontinuity",
            "labor_mechanism": "public goods, market access, outside options",
            "data_source": "historical map and district outcomes",
            "observed_margin": "wages, schooling, roads, occupations",
        },
        {
            "design_id": "coercive_contract_enforcement",
            "anchor": "Naidu-Yuchtman 2013",
            "historical_variation": "changes in employer ability to enforce labor contracts",
            "design_family": "archival_legal_contract_records",
            "labor_mechanism": "quitting costs, bargaining power, wage adjustment",
            "data_source": "court and labor-contract records",
            "observed_margin": "wages, separations, labor mobility",
        },
        {
            "design_id": "serfdom_abolition",
            "anchor": "Markevich-Zhuravskaya 2018",
            "historical_variation": "abolition of serfdom",
            "design_family": "regime_abolition_reform",
            "labor_mechanism": "mobility, competition, land-labor reallocation",
            "data_source": "imperial administrative records",
            "observed_margin": "migration, productivity, sectoral structure",
        },
        {
            "design_id": "wwii_minority_labor_reallocation",
            "anchor": "Aizer et al. 2020 / Ferrara 2023",
            "historical_variation": "war mobilization and defense demand",
            "design_family": "war_conflict_political_shock",
            "labor_mechanism": "occupational openings, discrimination changes, skill acquisition",
            "data_source": "war records and census outcomes",
            "observed_margin": "earnings gaps, occupations, participation",
        },
        {
            "design_id": "reconstruction_schooling_linkage",
            "anchor": "Jones-Schmick 2025",
            "historical_variation": "Reconstruction-era education access",
            "design_family": "linked_historical_microdata",
            "labor_mechanism": "human capital and occupational standing",
            "data_source": "school archives and linked census",
            "observed_margin": "occupation and racial inequality",
        },
        {
            "design_id": "postwar_forced_migration",
            "anchor": "Chevalier et al. 2024",
            "historical_variation": "forced migration after war",
            "design_family": "spatial_historical_gis",
            "labor_mechanism": "settlement, local public policy, labor demand",
            "data_source": "migration records and local policy data",
            "observed_margin": "migration, public goods, local labor-market entry",
        },
        {
            "design_id": "slavery_legacy_brazil",
            "anchor": "Laudares-Valencia Caicedo 2023",
            "historical_variation": "slavery exposure across regions",
            "design_family": "lineage_ancestry_share_proxy",
            "labor_mechanism": "land, schooling, hierarchy, occupational structure",
            "data_source": "historical slave records and modern inequality outcomes",
            "observed_margin": "earnings, schooling, occupational inequality",
        },
    ]


def main() -> None:
    write_rows(
        LAB / "original" / "reduced" / "mita_boundary_synthetic.csv",
        [
            "district_id",
            "matched_pair",
            "historical_mita_exposure",
            "near_boundary",
            "distance_to_boundary",
            "altitude_index",
            "ruggedness_index",
            "precolonial_density",
            "public_goods_index",
            "road_access_index",
            "schooling_years",
            "migration_rate",
            "nonfarm_share",
            "wage_index",
            "employer_power_index",
        ],
        boundary_rows(),
    )
    write_rows(
        LAB / "original" / "reduced" / "persistence_claims_synthetic.csv",
        [
            "claim_id",
            "anchor",
            "historical_treatment",
            "modern_outcome",
            "proposed_mechanism",
            "claim_type",
            "first_labor_margin",
            "alternative_fundamental",
            "data_source",
            "expected_risk",
        ],
        persistence_claim_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "historical_designs_synthetic.csv",
        [
            "design_id",
            "anchor",
            "historical_variation",
            "design_family",
            "labor_mechanism",
            "data_source",
            "observed_margin",
        ],
        transfer_rows(),
    )
    print("Wrote Week 7 synthetic data files")


if __name__ == "__main__":
    main()
