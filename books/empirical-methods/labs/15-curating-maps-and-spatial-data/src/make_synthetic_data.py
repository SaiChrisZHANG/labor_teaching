"""Create deterministic synthetic data for the Week 15 spatial curation lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

SECTORS = ["manufacturing", "apparel", "logistics", "health", "business", "retail"]


def make_sector_shocks() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"sector": "manufacturing", "trade_shock": 0.220, "shock_note": "import-exposed durable manufacturing"},
            {"sector": "apparel", "trade_shock": 0.185, "shock_note": "import-exposed light manufacturing"},
            {"sector": "logistics", "trade_shock": 0.040, "shock_note": "transport and warehousing"},
            {"sector": "health", "trade_shock": -0.015, "shock_note": "local nontraded health services"},
            {"sector": "business", "trade_shock": 0.018, "shock_note": "business services"},
            {"sector": "retail", "trade_shock": 0.026, "shock_note": "local retail services"},
        ]
    )


def dirichlet_profile(cz_id: int) -> np.ndarray:
    profiles = {
        1: np.array([5.3, 2.1, 1.2, 1.0, 1.2, 1.4]),
        2: np.array([1.7, 4.8, 1.3, 1.2, 1.0, 1.6]),
        3: np.array([1.4, 1.0, 3.8, 1.2, 1.9, 1.5]),
        4: np.array([1.0, 0.8, 1.4, 4.2, 1.8, 1.6]),
        5: np.array([1.2, 0.9, 1.7, 1.5, 4.4, 1.5]),
    }
    return profiles[cz_id]


def make_tract_data() -> pd.DataFrame:
    rng = np.random.default_rng(1515)
    centers = {
        1: (18.0, 30.0),
        2: (38.0, 68.0),
        3: (57.0, 28.0),
        4: (72.0, 72.0),
        5: (90.0, 40.0),
    }
    rows: list[dict[str, object]] = []
    shocks = make_sector_shocks().set_index("sector")["trade_shock"]

    for tract_num in range(1, 61):
        cz_id = 1 + (tract_num - 1) // 12
        county_id = 1 + (tract_num - 1) // 6
        if tract_num in {12, 13, 24, 25, 36, 37, 48, 49}:
            county_id = max(1, county_id - 1)
        x_center, y_center = centers[cz_id]
        x_coord = float(x_center + rng.normal(0.0, 5.8))
        y_coord = float(y_center + rng.normal(0.0, 5.8))
        population = int(rng.integers(900, 4200))
        total_emp = int(population * rng.uniform(0.38, 0.68))
        shares = rng.dirichlet(dirichlet_profile(cz_id))
        sector_emp = np.maximum(np.round(shares * total_emp).astype(int), 3)
        total_emp = int(sector_emp.sum())
        exposure = float(sum((sector_emp[i] / total_emp) * shocks[sector] for i, sector in enumerate(SECTORS)))
        low_income_share = float(np.clip(0.18 + 0.20 * (cz_id in {1, 2}) + rng.normal(0.0, 0.055), 0.05, 0.72))
        black_share = float(np.clip(0.12 + 0.22 * (cz_id in {2, 3}) + 0.06 * (x_coord > 70) + rng.normal(0.0, 0.045), 0.02, 0.82))
        geocode_quality = str(rng.choice(["rooftop", "street", "zip_centroid"], p=[0.68, 0.22, 0.10]))
        jitter_radius = {"rooftop": 0.10, "street": 0.70, "zip_centroid": 2.60}[geocode_quality]
        employment_growth = (
            0.055
            - 0.70 * exposure
            + 0.035 * (sector_emp[SECTORS.index("health")] / total_emp)
            + 0.020 * (cz_id == 5)
            - 0.018 * low_income_share
            + rng.normal(0.0, 0.018)
        )
        rows.append(
            {
                "tract_id": f"T{tract_num:03d}",
                "county_id": f"C{county_id:02d}",
                "cz_id": f"CZ{cz_id:02d}",
                "x_coord": round(x_coord, 4),
                "y_coord": round(y_coord, 4),
                "population_1990": population,
                "baseline_employment_1990": total_emp,
                "low_income_share_1990": round(low_income_share, 4),
                "black_share_1990": round(black_share, 4),
                "geocode_quality": geocode_quality,
                "jitter_radius_miles": jitter_radius,
                "employment_growth_2000_2010": round(float(employment_growth), 5),
                **{f"emp_{sector}_1990": int(sector_emp[i]) for i, sector in enumerate(SECTORS)},
            }
        )
    return pd.DataFrame(rows)


def make_boundary_crosswalk(tracts: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(1516)
    split_tracts = {"T006", "T012", "T019", "T025", "T033", "T041", "T049", "T058"}
    rows: list[dict[str, object]] = []
    county_ids = sorted(tracts["county_id"].unique())
    for _, row in tracts.iterrows():
        source = str(row["tract_id"])
        county = str(row["county_id"])
        if source in split_tracts:
            alt_county = county_ids[(county_ids.index(county) + 1) % len(county_ids)]
            area_share = float(rng.uniform(0.55, 0.78))
            pop_share = float(np.clip(area_share + rng.normal(0.0, 0.12), 0.35, 0.90))
            emp_share = float(np.clip(area_share + rng.normal(0.0, 0.10), 0.32, 0.92))
            rows.append(
                {
                    "source_tract_id": source,
                    "target_county_id": county,
                    "area_weight": round(area_share, 4),
                    "population_weight": round(pop_share, 4),
                    "employment_weight": round(emp_share, 4),
                    "is_split_unit": 1,
                }
            )
            rows.append(
                {
                    "source_tract_id": source,
                    "target_county_id": alt_county,
                    "area_weight": round(1.0 - area_share, 4),
                    "population_weight": round(1.0 - pop_share, 4),
                    "employment_weight": round(1.0 - emp_share, 4),
                    "is_split_unit": 1,
                }
            )
        else:
            rows.append(
                {
                    "source_tract_id": source,
                    "target_county_id": county,
                    "area_weight": 1.0,
                    "population_weight": 1.0,
                    "employment_weight": 1.0,
                    "is_split_unit": 0,
                }
            )
    return pd.DataFrame(rows)


def make_transfer_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(1520)
    residence_rows: list[dict[str, object]] = []
    for tract_num in range(1, 41):
        west_side = tract_num <= 20
        x_coord = float(rng.normal(27.0 if west_side else 70.0, 10.0))
        y_coord = float(rng.normal(48.0, 18.0))
        resident_count = int(rng.integers(800, 5200))
        black_share = float(np.clip(0.38 if west_side else 0.13, 0.01, 0.80) + rng.normal(0.0, 0.055))
        black_share = float(np.clip(black_share, 0.02, 0.86))
        transit_dependency = int(rng.random() < (0.58 if west_side else 0.24))
        geocode_quality = str(rng.choice(["rooftop", "street", "zip_centroid"], p=[0.62, 0.25, 0.13]))
        residence_rows.append(
            {
                "residence_tract_id": f"R{tract_num:03d}",
                "x_coord": round(x_coord, 4),
                "y_coord": round(y_coord, 4),
                "resident_count": resident_count,
                "black_share": round(black_share, 4),
                "transit_dependency": transit_dependency,
                "geocode_quality": geocode_quality,
                "jitter_radius_miles": {"rooftop": 0.10, "street": 0.70, "zip_centroid": 2.60}[geocode_quality],
            }
        )

    center_specs = [
        ("J01", "downtown", 48.0, 49.0, 8400, "business", 0, 0),
        ("J02", "airport logistics", 86.0, 22.0, 6200, "logistics", 1, 0),
        ("J03", "north medical", 55.0, 82.0, 5100, "health", 0, 0),
        ("J04", "south industrial", 74.0, 9.0, 4700, "manufacturing", 1, 0),
        ("J05", "west retail", 22.0, 45.0, 2400, "retail", 0, 0),
        ("J06", "outer tech park", 111.0, 67.0, 5800, "business", 1, 1),
        ("J07", "east distribution", 96.0, 42.0, 4300, "logistics", 1, 0),
        ("J08", "college hospital", 35.0, 74.0, 3900, "health", 0, 0),
        ("J09", "suburban mall", 90.0, 77.0, 3300, "retail", 1, 0),
        ("J10", "outer assembly", 108.0, 19.0, 3600, "manufacturing", 1, 1),
        ("J11", "city services", 44.0, 33.0, 2900, "public", 0, 0),
        ("J12", "northwest warehouse", 16.0, 88.0, 2100, "logistics", 0, 0),
    ]
    center_rows = [
        {
            "job_center_id": center_id,
            "center_name": name,
            "x_coord": x_coord,
            "y_coord": y_coord,
            "jobs": jobs,
            "sector": sector,
            "suburban_center": suburban,
            "outside_study_frame": outside,
        }
        for center_id, name, x_coord, y_coord, jobs, sector, suburban, outside in center_specs
    ]
    return pd.DataFrame(residence_rows), pd.DataFrame(center_rows)


def main() -> None:
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    tracts = make_tract_data()
    shocks = make_sector_shocks()
    crosswalk = make_boundary_crosswalk(tracts)
    residences, centers = make_transfer_data()

    tracts.to_csv(original_dir / "tract_sector_employment_synthetic.csv", index=False)
    shocks.to_csv(original_dir / "sector_trade_shocks_synthetic.csv", index=False)
    crosswalk.to_csv(original_dir / "boundary_crosswalk_synthetic.csv", index=False)
    residences.to_csv(transfer_dir / "residential_tracts_synthetic.csv", index=False)
    centers.to_csv(transfer_dir / "workplace_centers_synthetic.csv", index=False)

    print(f"Wrote {original_dir / 'tract_sector_employment_synthetic.csv'}")
    print(f"Wrote {original_dir / 'sector_trade_shocks_synthetic.csv'}")
    print(f"Wrote {original_dir / 'boundary_crosswalk_synthetic.csv'}")
    print(f"Wrote {transfer_dir / 'residential_tracts_synthetic.csv'}")
    print(f"Wrote {transfer_dir / 'workplace_centers_synthetic.csv'}")


if __name__ == "__main__":
    main()
