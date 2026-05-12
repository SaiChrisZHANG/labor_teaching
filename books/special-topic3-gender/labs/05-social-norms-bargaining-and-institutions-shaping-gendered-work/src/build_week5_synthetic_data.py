#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for Gender Study Week 5."""
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


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def make_norm_misperception_rows() -> list[dict[str, object]]:
    rng = random.Random(202608)
    rows: list[dict[str, object]] = []
    for respondent_id in range(1, 721):
        cohort = 1 + (respondent_id % 8)
        district = 1 + (respondent_id % 12)
        treatment = int(((respondent_id * 7 + cohort) % 10) in {0, 2, 4, 6, 9})
        private_support_score = logistic(0.45 + 0.10 * (cohort % 3) + rng.gauss(0.0, 0.85))
        private_support = int(private_support_score > 0.55)
        perceived_peer_support = clamp(
            0.32 + 0.025 * (district % 5) + 0.08 * private_support + rng.gauss(0.0, 0.09),
            0.08,
            0.86,
        )
        true_peer_support = clamp(0.67 + 0.015 * (cohort % 4) + rng.gauss(0.0, 0.03), 0.55, 0.82)
        baseline_misperception = max(0.0, true_peer_support - perceived_peer_support)
        wife_interested_work = int(rng.random() < logistic(-0.30 + 1.10 * private_support_score + 0.45 * baseline_misperception))
        posterior_peer_support = clamp(
            perceived_peer_support + treatment * (0.18 + 0.55 * baseline_misperception) + rng.gauss(0.0, 0.025),
            0.05,
            0.95,
        )
        signup_probability = logistic(
            -1.25
            + 0.70 * private_support
            + 0.55 * wife_interested_work
            + 0.55 * treatment
            + 1.05 * treatment * baseline_misperception
            + 0.40 * (posterior_peer_support - perceived_peer_support)
        )
        job_matching_signup = int(rng.random() < signup_probability)
        followup_job_search = int(
            rng.random()
            < logistic(-1.00 + 1.10 * job_matching_signup + 0.25 * treatment + 0.45 * wife_interested_work)
        )
        followup_employment = int(
            rng.random()
            < logistic(-1.85 + 0.85 * followup_job_search + 0.35 * job_matching_signup + 0.25 * private_support)
        )

        rows.append(
            {
                "respondent_id": respondent_id,
                "cohort": cohort,
                "district": district,
                "information_treatment": treatment,
                "private_support": private_support,
                "perceived_peer_support": round4(perceived_peer_support),
                "true_peer_support": round4(true_peer_support),
                "baseline_misperception": round4(baseline_misperception),
                "wife_interested_work": wife_interested_work,
                "posterior_peer_support": round4(posterior_peer_support),
                "job_matching_signup": job_matching_signup,
                "followup_job_search": followup_job_search,
                "followup_employment": followup_employment,
            }
        )
    return rows


def make_relative_income_rows() -> list[dict[str, object]]:
    rng = random.Random(202609)
    rows: list[dict[str, object]] = []
    for household_id in range(1, 841):
        cohort = 1 + (household_id % 7)
        children = household_id % 4
        marriage_years = 1 + (household_id % 18)
        wife_potential = 36_000 + 2_100 * (cohort % 4) + rng.gauss(0.0, 8_500)
        husband_income = 42_000 + 2_800 * (cohort % 5) + rng.gauss(0.0, 9_200)
        potential_share = clamp(wife_potential / (wife_potential + husband_income), 0.18, 0.82)
        breadwinner_penalty = 0.0
        if potential_share > 0.50:
            breadwinner_penalty = 0.035 + 0.030 * min(potential_share - 0.50, 0.20) / 0.20
        wife_earning_share = clamp(potential_share - breadwinner_penalty + rng.gauss(0.0, 0.018), 0.12, 0.86)
        wife_earns_more = int(wife_earning_share > 0.50)
        wife_weekly_hours = clamp(
            34.0
            + 18.0 * (potential_share - 0.45)
            - 4.8 * wife_earns_more
            - 1.1 * children
            + rng.gauss(0.0, 3.2),
            4.0,
            58.0,
        )
        husband_weekly_hours = clamp(39.0 + 0.6 * children + rng.gauss(0.0, 3.0), 12.0, 62.0)
        wife_home_hours = clamp(
            17.0
            + 2.2 * children
            + 4.3 * wife_earns_more
            - 0.12 * wife_weekly_hours
            + rng.gauss(0.0, 2.1),
            2.0,
            42.0,
        )
        rows.append(
            {
                "household_id": household_id,
                "cohort": cohort,
                "children": children,
                "marriage_years": marriage_years,
                "wife_potential_share": round4(potential_share),
                "wife_earning_share": round4(wife_earning_share),
                "wife_earns_more": wife_earns_more,
                "wife_weekly_hours": round4(wife_weekly_hours),
                "husband_weekly_hours": round4(husband_weekly_hours),
                "wife_home_hours": round4(wife_home_hours),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    norm_rows = make_norm_misperception_rows()
    relative_income_rows = make_relative_income_rows()

    write_csv(ORIGINAL_DIR / "bursztyn_norm_misperceptions_synthetic.csv", norm_rows)
    write_csv(TRANSFER_DIR / "bertrand_relative_income_synthetic.csv", relative_income_rows)

    print(f"Wrote {len(norm_rows)} norm-misperception rows to {ORIGINAL_DIR}")
    print(f"Wrote {len(relative_income_rows)} relative-income rows to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
