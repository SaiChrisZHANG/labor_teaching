from __future__ import annotations

import argparse
import csv
from collections import defaultdict
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


def shock_effects(row: dict[str, str]) -> dict[str, float]:
    shock = f(row, "demand_shock")
    elasticity = f(row, "housing_supply_elasticity")
    commute = f(row, "commuting_openness")
    moving = f(row, "moving_cost_index")
    rent_exposure = f(row, "rent_exposure")
    mobility_constraint = f(row, "mobility_constraint")
    ownership = f(row, "ownership_exposure")

    tightness = max(0.0, 1.0 - min(elasticity, 1.5) / 1.5)
    wage_change = shock * (0.34 + 0.16 * moving + 0.06 * tightness)
    rent_change = shock * (0.18 + 0.42 * tightness + 0.10 * (1.0 - commute))
    house_value_change = shock * (0.25 + 0.55 * tightness)
    population_change = shock * (0.16 + 0.22 * min(elasticity, 1.5) / 1.5 - 0.10 * moving)
    employment_change = shock * (0.28 + 0.18 * commute)
    commuting_change = shock * (0.05 + 0.32 * commute)
    moving_cost_drag = abs(shock) * 0.08 * mobility_constraint
    capital_gain = house_value_change * ownership * 0.55
    real_access_change = (
        wage_change
        - rent_exposure * rent_change
        - moving_cost_drag
        + capital_gain
    )
    return {
        "wage_change": wage_change,
        "rent_change": rent_change,
        "house_value_change": house_value_change,
        "population_change": population_change,
        "employment_change": employment_change,
        "commuting_change": commuting_change,
        "moving_cost_drag": moving_cost_drag,
        "capital_gain": capital_gain,
        "real_access_change": real_access_change,
    }


def incidence_label(row: dict[str, str], effects: dict[str, float]) -> str:
    group = row["worker_group"]
    real_access = effects["real_access_change"]
    if f(row, "demand_shock") < 0 and real_access < 0:
        return "immobile_workers_bear_local_decline"
    if group == "incumbent_homeowners" and effects["capital_gain"] > abs(effects["rent_change"]) * 0.20:
        return "homeowner_capitalization"
    if group == "in_commuters" and effects["employment_change"] > effects["population_change"]:
        return "commuter_access_gain"
    if group == "would_be_migrants" and real_access < 0:
        return "entry_blocked_by_rents_and_moving_costs"
    if group == "low_wealth_renters" and real_access < 0:
        return "rent_burden_offsets_wage_gain"
    if real_access > 0:
        return "worker_real_access_gain"
    return "mixed_or_ambiguous"


def transfer_rows(input_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in input_rows:
        effects = shock_effects(row)
        output_row: dict[str, object] = {
            "place_id": row["place_id"],
            "place_name": row["place_name"],
            "worker_group": row["worker_group"],
            "demand_shock": round(f(row, "demand_shock"), 3),
            "housing_supply_elasticity": round(f(row, "housing_supply_elasticity"), 3),
            "commuting_openness": round(f(row, "commuting_openness"), 3),
            "moving_cost_index": round(f(row, "moving_cost_index"), 3),
        }
        for key, value in effects.items():
            output_row[key] = round(value, 4)
        output_row["incidence_label"] = incidence_label(row, effects)
        output_row["interpretation"] = "notowidigdo_inspired_transfer_not_official_replication"
        rows.append(output_row)
    return rows


def summary_by_group(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["worker_group"])].append(row)
    output: list[dict[str, object]] = []
    for group in sorted(grouped):
        group_rows = grouped[group]
        output.append(
            {
                "worker_group": group,
                "row_count": len(group_rows),
                "avg_wage_change": round(avg(group_rows, "wage_change"), 4),
                "avg_rent_change": round(avg(group_rows, "rent_change"), 4),
                "avg_population_change": round(avg(group_rows, "population_change"), 4),
                "avg_employment_change": round(avg(group_rows, "employment_change"), 4),
                "avg_commuting_change": round(avg(group_rows, "commuting_change"), 4),
                "avg_real_access_change": round(avg(group_rows, "real_access_change"), 4),
                "negative_real_access_cases": sum(
                    1 for row in group_rows if float(row["real_access_change"]) < 0
                ),
            }
        )
    return output


def avg(rows: list[dict[str, object]], key: str) -> float:
    return sum(float(row[key]) for row in rows) / len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Notowidigdo-inspired local-demand incidence transfer."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=LAB_DIR / "transfer" / "data" / "local_demand_shocks_synthetic.csv",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=LAB_DIR / "output" / "transfer",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input if args.input.is_absolute() else LAB_DIR / args.input
    outdir = args.outdir if args.outdir.is_absolute() else LAB_DIR / args.outdir
    rows = transfer_rows(read_rows(input_path))
    write_rows(outdir / "local_demand_incidence_transfer.csv", rows)
    write_rows(outdir / "incidence_summary_by_group.csv", summary_by_group(rows))
    write_text(
        outdir / "transfer_note.txt",
        (
            "This transfer exercise is inspired by Notowidigdo's incidence logic "
            "for local labor-demand shocks. It uses synthetic place-by-group data "
            "to separate wage, rent, population, employment, commuting, ownership, "
            "moving-cost, and real-access margins. It is not an official "
            "replication package.\n"
        ),
    )


if __name__ == "__main__":
    main()

