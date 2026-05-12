#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 7."""
from __future__ import annotations

import csv
import math
import random
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def round4(value: float) -> str:
    return f"{value:.4f}"


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_workplace_violence_rows() -> list[dict[str, object]]:
    rng = random.Random(20260701)
    rows: list[dict[str, object]] = []
    worker_id = 0
    for firm_id in range(1, 41):
        event_firm = int(firm_id % 5 == 0)
        firm_risk = 0.18 + 0.10 * event_firm + 0.02 * (firm_id % 3)
        for slot in range(1, 31):
            worker_id += 1
            female = int((slot + firm_id) % 2 == 0)
            supervisor = int(slot % 11 == 0)
            reported_victim = int(event_firm and female and (slot in {6, 18}))
            coworker_exposed = int(event_firm and not reported_victim)
            exposure_group = "victim" if reported_victim else "coworker" if coworker_exposed else "comparison"
            baseline_wage = 41000 + 850 * (slot % 8) + 4200 * supervisor + 260 * firm_id

            for period in (-1, 1):
                post = int(period == 1)
                event_report = int(post and reported_victim)
                base_sep_index = (
                    -3.25
                    + 0.18 * female
                    + 0.24 * event_firm
                    + 1.65 * event_report
                    + 0.48 * post * coworker_exposed * female
                    + 0.18 * post * coworker_exposed * (1 - female)
                    - 0.30 * supervisor
                )
                separated = int(rng.random() < logistic(base_sep_index))
                sick_days = max(
                    0.0,
                    2.0
                    + 0.8 * female
                    + 6.8 * event_report
                    + 1.9 * post * coworker_exposed * female
                    + rng.gauss(0.0, 1.1),
                )
                wage = (
                    baseline_wage
                    + 1150 * post
                    - 620 * post * reported_victim
                    - 160 * post * coworker_exposed * female
                    + rng.gauss(0.0, 520)
                )
                new_hire = int(post and rng.random() < 0.055 + 0.030 * event_firm + 0.020 * separated)
                retained = int(not separated)
                rows.append(
                    {
                        "worker_id": worker_id,
                        "firm_id": firm_id,
                        "period": period,
                        "female": female,
                        "supervisor": supervisor,
                        "event_firm": event_firm,
                        "reported_victim": reported_victim,
                        "coworker_exposed": coworker_exposed,
                        "exposure_group": exposure_group,
                        "firm_risk_score": round4(firm_risk),
                        "reported_event": event_report,
                        "separated": separated,
                        "retained": retained,
                        "sick_days": round4(sick_days),
                        "wage": round4(wage),
                        "new_hire": new_hire,
                    }
                )
    return rows


def make_harassment_sorting_rows() -> list[dict[str, object]]:
    rng = random.Random(20260702)
    occupations = [
        ("care", 0.28, 0.18),
        ("retail", 0.42, 0.23),
        ("professional", 0.55, 0.21),
        ("transport", 0.78, 0.36),
        ("trades", 0.86, 0.39),
        ("finance", 0.63, 0.30),
    ]
    rows: list[dict[str, object]] = []
    for worker_id in range(1, 961):
        occ_name, male_share, baseline_risk = occupations[worker_id % len(occupations)]
        female = int(worker_id % 2 == 0)
        high_risk_job = int(baseline_risk >= 0.30)
        harassment_risk = min(0.88, baseline_risk + 0.10 * female + rng.gauss(0.0, 0.045))
        reporting_cost = 0.22 + 0.13 * high_risk_job + 0.09 * female + rng.gauss(0.0, 0.025)
        reported_harassment = int(
            rng.random()
            < max(0.01, harassment_risk * (0.33 - 0.18 * reporting_cost + 0.04 * female))
        )
        wage = (
            45500
            + 11800 * high_risk_job
            + 9000 * (occ_name in {"finance", "professional"})
            - 2100 * female
            + 1800 * harassment_risk
            + rng.gauss(0.0, 1400)
        )
        quit_next_year = int(
            rng.random()
            < logistic(-2.10 + 1.25 * harassment_risk + 0.42 * female + 0.22 * reported_harassment)
        )
        moves_to_safer_job = int(
            quit_next_year
            and rng.random() < min(0.85, 0.28 + 0.45 * female + 0.30 * harassment_risk)
        )
        job_quality_score = 0.72 - 0.44 * harassment_risk - 0.05 * high_risk_job + rng.gauss(0.0, 0.05)
        rows.append(
            {
                "worker_id": worker_id,
                "occupation": occ_name,
                "female": female,
                "occupation_male_share": round4(male_share),
                "high_risk_job": high_risk_job,
                "survey_harassment_risk": round4(harassment_risk),
                "reporting_cost": round4(reporting_cost),
                "reported_harassment": reported_harassment,
                "wage": round4(wage),
                "quit_next_year": quit_next_year,
                "moves_to_safer_job": moves_to_safer_job,
                "job_quality_score": round4(job_quality_score),
            }
        )
    return rows


def main() -> None:
    workplace_rows = make_workplace_violence_rows()
    harassment_rows = make_harassment_sorting_rows()

    write_csv(
        ORIGINAL_DIR / "adams_prassl_huttunen_nix_zhang_workplace_violence_synthetic.csv",
        workplace_rows,
    )
    write_csv(
        TRANSFER_DIR / "folke_rickne_harassment_sorting_synthetic.csv",
        harassment_rows,
    )

    print(f"Wrote {len(workplace_rows)} workplace-violence panel rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(harassment_rows)} harassment-sorting rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
