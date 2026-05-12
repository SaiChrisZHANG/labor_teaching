#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 6."""
from __future__ import annotations

import csv
import math
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def round2(value: float) -> str:
    return f"{value:.2f}"


def round4(value: float) -> str:
    return f"{value:.4f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_pay_transparency_rows() -> list[dict[str, object]]:
    rng = random.Random(20260601)
    rows: list[dict[str, object]] = []
    worker_id = 0
    for firm_id in range(1, 121):
        firm_size = 150 + 5 * firm_id
        reporting_required = int(firm_size >= 250)
        firm_premium = 1700 * (firm_id % 7) + 520 * reporting_required
        high_bonus_firm = int(firm_id % 4 == 0)
        for slot in range(1, 25):
            worker_id += 1
            female = int((slot + firm_id) % 2 == 0)
            manager = int(slot % 9 == 0)
            baseline_base = 36000 + firm_premium + 1450 * (slot % 8) + 8500 * manager
            baseline_gap = -1650 * female - 2700 * female * manager
            baseline_bonus = (
                900
                + 1250 * high_bonus_firm
                + 2250 * manager
                - 420 * female
                - 800 * female * manager
            )
            for period in (-1, 1):
                post = int(period == 1)
                wage_growth = 1650 * post
                transparency_raise = 720 * post * reporting_required * female
                male_slowdown = -520 * post * reporting_required * (1 - female)
                manager_slowdown = -260 * post * reporting_required * manager * (1 - female)
                base_pay = (
                    baseline_base
                    + baseline_gap
                    + wage_growth
                    + transparency_raise
                    + male_slowdown
                    + manager_slowdown
                    + rng.gauss(0.0, 360)
                )
                bonus = (
                    baseline_bonus
                    + 340 * post
                    - 280 * post * reporting_required * (1 - female)
                    + 190 * post * reporting_required * female
                    - 180 * post * reporting_required * manager
                    + rng.gauss(0.0, 130)
                )
                exit_risk = logistic(
                    -3.35
                    + 0.10 * female
                    - 0.24 * reporting_required
                    - 0.20 * post * reporting_required * female
                    + 0.18 * post * reporting_required * (1 - female)
                    + 0.12 * manager
                )
                retained = int(not (post and rng.random() < exit_risk))
                rows.append(
                    {
                        "worker_id": worker_id,
                        "firm_id": firm_id,
                        "period": period,
                        "firm_size": firm_size,
                        "reporting_required": reporting_required,
                        "female": female,
                        "manager": manager,
                        "base_pay": round2(base_pay),
                        "bonus": round2(max(0.0, bonus)),
                        "total_pay": round2(base_pay + max(0.0, bonus)),
                        "retained": retained,
                    }
                )
    return rows


def make_equal_pay_rows() -> list[dict[str, object]]:
    rng = random.Random(20260602)
    job_families = ["operations", "sales", "technical", "administration"]
    rows: list[dict[str, object]] = []
    worker_id = 0
    for firm_id in range(1, 81):
        local_female_supply = 0.34 + 0.07 * (firm_id % 5)
        rule_exposed = int(firm_id % 2 == 0)
        high_segmentation = int(firm_id % 6 in {0, 1})
        for job_index, job_family in enumerate(job_families):
            for slot in range(1, 15):
                worker_id += 1
                female = int(rng.random() < local_female_supply)
                senior = int(slot % 7 == 0)
                female_concentrated_cell = int(
                    rule_exposed
                    and high_segmentation
                    and female
                    and job_family in {"administration", "operations"}
                )
                male_concentrated_cell = int(
                    rule_exposed
                    and high_segmentation
                    and (not female)
                    and job_family in {"technical", "sales"}
                )
                adjusted_job_cell = (
                    f"{job_family}_female_track"
                    if female_concentrated_cell
                    else f"{job_family}_male_track"
                    if male_concentrated_cell
                    else job_family
                )
                for period in (-1, 1):
                    post = int(period == 1)
                    base = 39000 + 3800 * job_index + 7600 * senior + 430 * firm_id
                    pre_gap = -1750 * female - 1400 * female * senior
                    compression = 920 * post * rule_exposed * female - 520 * post * rule_exposed * (1 - female)
                    segregation_premium = (
                        -620 * post * female_concentrated_cell
                        + 420 * post * male_concentrated_cell
                    )
                    wage = base + pre_gap + 980 * post + compression + segregation_premium + rng.gauss(0.0, 410)
                    rows.append(
                        {
                            "worker_id": worker_id,
                            "firm_id": firm_id,
                            "period": period,
                            "rule_exposed": rule_exposed,
                            "local_female_supply": round4(local_female_supply),
                            "female": female,
                            "senior": senior,
                            "original_job_family": job_family,
                            "adjusted_job_cell": adjusted_job_cell,
                            "female_concentrated_cell": female_concentrated_cell,
                            "male_concentrated_cell": male_concentrated_cell,
                            "wage": round2(wage),
                        }
                    )
    return rows


def main() -> None:
    transparency_rows = make_pay_transparency_rows()
    equal_pay_rows = make_equal_pay_rows()

    write_csv(
        ORIGINAL_DIR / "blundell_uk_pay_transparency_synthetic.csv",
        transparency_rows,
    )
    write_csv(
        TRANSFER_DIR / "gentile_equal_pay_similar_work_synthetic.csv",
        equal_pay_rows,
    )

    print(f"Wrote {len(transparency_rows)} pay-transparency worker-period rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(equal_pay_rows)} equal-pay worker-period rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
