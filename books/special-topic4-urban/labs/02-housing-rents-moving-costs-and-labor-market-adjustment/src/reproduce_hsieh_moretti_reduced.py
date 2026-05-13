from __future__ import annotations

import argparse
import csv
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def f(row: dict[str, str], key: str) -> float:
    return float(row[key])


def classify_adjustment(row: dict[str, str]) -> str:
    rent_pressure = f(row, "rent_growth") + 0.50 * f(row, "house_price_growth")
    quantity_response = f(row, "population_growth") + f(row, "employment_growth")
    commuting_response = f(row, "in_commuting_growth")
    if rent_pressure > 0.32 and quantity_response < 0.22:
        return "price_adjustment"
    if quantity_response > 0.36 and rent_pressure < 0.22:
        return "quantity_adjustment"
    if commuting_response > 0.12 and f(row, "population_growth") < 0.10:
        return "commuting_adjustment"
    if f(row, "productivity_growth") > 0.12 and quantity_response < 0.08:
        return "limited_access"
    return "mixed_adjustment"


def classify_friction(row: dict[str, str]) -> str:
    housing_tight = f(row, "housing_supply_elasticity") < 0.75 or f(row, "regulation_index") > 0.60
    moving_costly = f(row, "moving_cost_index") > 0.60
    commute_open = f(row, "in_commuting_growth") > 0.10
    if housing_tight and moving_costly:
        return "housing_supply_and_moving_costs"
    if housing_tight:
        return "housing_supply_constraint"
    if moving_costly:
        return "moving_cost_friction"
    if commute_open:
        return "commuting_access_margin"
    return "not_binding_in_reduced_path"


def classify_incidence(row: dict[str, str], real_access_growth: float) -> str:
    rent_pressure = f(row, "rent_growth") + 0.50 * f(row, "house_price_growth")
    if real_access_growth < -0.04 and rent_pressure > 0.24:
        return "landlords_homeowners_or_excluded_migrants"
    if real_access_growth > 0.05 and f(row, "population_growth") > 0.10:
        return "workers_and_new_residents"
    if f(row, "in_commuting_growth") > 0.10 and f(row, "population_growth") < 0.10:
        return "commuters_and_firms"
    if f(row, "house_price_growth") > 0.25 and f(row, "rent_growth") > f(row, "wage_growth"):
        return "incumbent_homeowners_and_landlords"
    return "mixed_or_ambiguous"


def adjustment_rows(input_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in input_rows:
        real_access_growth = (
            f(row, "wage_growth")
            - f(row, "rent_growth")
            - f(row, "commute_cost_growth")
            - 0.05 * f(row, "moving_cost_index")
        )
        price_pressure = f(row, "rent_growth") + 0.50 * f(row, "house_price_growth")
        quantity_response = f(row, "population_growth") + f(row, "employment_growth")
        misallocation_flag = (
            f(row, "productivity_growth") >= 0.20
            and f(row, "housing_supply_elasticity") < 0.75
            and f(row, "population_growth") < 0.10
            and real_access_growth < 0.02
        )
        rows.append(
            {
                "metro_id": row["metro_id"],
                "metro_name": row["metro_name"],
                "region": row["region"],
                "productivity_growth": round(f(row, "productivity_growth"), 3),
                "wage_growth": round(f(row, "wage_growth"), 3),
                "rent_growth": round(f(row, "rent_growth"), 3),
                "house_price_growth": round(f(row, "house_price_growth"), 3),
                "population_growth": round(f(row, "population_growth"), 3),
                "employment_growth": round(f(row, "employment_growth"), 3),
                "in_commuting_growth": round(f(row, "in_commuting_growth"), 3),
                "housing_supply_elasticity": round(f(row, "housing_supply_elasticity"), 3),
                "price_pressure_index": round(price_pressure, 3),
                "quantity_response_index": round(quantity_response, 3),
                "real_access_growth": round(real_access_growth, 3),
                "adjustment_pattern": classify_adjustment(row),
                "likely_binding_friction": classify_friction(row),
                "incidence_reading": classify_incidence(row, real_access_growth),
                "misallocation_teaching_flag": int(misallocation_flag),
            }
        )
    return rows


def summary_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups = {
        "constrained": [
            row
            for row in rows
            if float(row["housing_supply_elasticity"]) < 0.75
        ],
        "less_constrained": [
            row
            for row in rows
            if float(row["housing_supply_elasticity"]) >= 0.75
        ],
    }
    output: list[dict[str, object]] = []
    for group, group_rows in groups.items():
        if not group_rows:
            continue
        output.append(
            {
                "constraint_group": group,
                "metro_count": len(group_rows),
                "avg_productivity_growth": round(avg(group_rows, "productivity_growth"), 3),
                "avg_wage_growth": round(avg(group_rows, "wage_growth"), 3),
                "avg_rent_growth": round(avg(group_rows, "rent_growth"), 3),
                "avg_population_growth": round(avg(group_rows, "population_growth"), 3),
                "avg_real_access_growth": round(avg(group_rows, "real_access_growth"), 3),
                "misallocation_flags": sum(int(row["misallocation_teaching_flag"]) for row in group_rows),
            }
        )
    return output


def avg(rows: list[dict[str, object]], key: str) -> float:
    return sum(float(row[key]) for row in rows) / len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the reduced Hsieh-Moretti teaching reproduction."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=LAB_DIR / "original" / "reduced" / "housing_constraints_reduced.csv",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=LAB_DIR / "output" / "reproduced",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input if args.input.is_absolute() else LAB_DIR / args.input
    outdir = args.outdir if args.outdir.is_absolute() else LAB_DIR / args.outdir
    source_rows = read_rows(input_path)
    rows = adjustment_rows(source_rows)
    write_rows(outdir / "housing_constraint_adjustment.csv", rows)
    write_rows(outdir / "housing_constraint_summary.csv", summary_rows(rows))
    write_text(
        outdir / "reproduction_note.txt",
        (
            "This reduced reproduction is a deterministic teaching path inspired by "
            "Hsieh and Moretti on housing constraints and spatial misallocation. "
            "It uses synthetic city-level data to classify productivity, rents, "
            "prices, population, commuting, real access, and incidence. It is not "
            "the full official replication package and should not be interpreted "
            "as published evidence about actual cities.\n"
        ),
    )


if __name__ == "__main__":
    main()

