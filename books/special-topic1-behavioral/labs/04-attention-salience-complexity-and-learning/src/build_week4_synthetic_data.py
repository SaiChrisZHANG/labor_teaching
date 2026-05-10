from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def schedule_learning() -> pd.DataFrame:
    rows = []
    years = [1, 2, 3, 4]
    for worker in range(320):
        local_knowledge = worker % 6 in {0, 1}
        schedule_letter = worker % 4 == 0
        baseline_hours = 1240 + 22 * (worker % 8) + 10 * (worker % 3)
        hourly_wage = 17.5 + 0.45 * (worker % 9)
        true_net_return = 0.58 + 0.035 * (worker % 7)

        for year in years:
            letter_active = schedule_letter and year >= 2
            exposure_count = year - 1 + int(local_knowledge) + int(letter_active)
            learning_gap = max(0.025, 0.17 - 0.035 * exposure_count)
            perceived_net_return = true_net_return - learning_gap + 0.015 * int(letter_active)
            perceived_net_return = min(0.90, max(0.35, perceived_net_return))
            knowledge_gap = true_net_return - perceived_net_return
            hours = baseline_hours + 360 * (perceived_net_return - 0.58) - 8 * year
            earnings = hours * hourly_wage

            rows.append(
                {
                    "worker_id": f"worker-{worker:03d}",
                    "year": year,
                    "local_knowledge": int(local_knowledge),
                    "schedule_letter": int(schedule_letter),
                    "letter_active": int(letter_active),
                    "exposure_count": exposure_count,
                    "hourly_wage": round(hourly_wage, 2),
                    "true_net_return": round(true_net_return, 3),
                    "perceived_net_return": round(perceived_net_return, 3),
                    "knowledge_gap": round(knowledge_gap, 3),
                    "annual_hours": round(hours, 1),
                    "annual_earnings": round(earnings, 2),
                }
            )

    return pd.DataFrame(rows)


def policy_navigation() -> pd.DataFrame:
    rows = []
    arms = ["control", "information", "reminder", "simplified", "info_simplified"]
    for applicant in range(500):
        arm = arms[applicant % len(arms)]
        applicant_type = applicant // len(arms)
        eligible = applicant_type % 10 != 0
        prior_awareness = 0.34 + 0.07 * (applicant_type % 5) + 0.02 * (applicant_type % 2)
        hassle_index = 0.62 - 0.18 * (arm in {"simplified", "info_simplified"})
        salience_index = 0.40 + 0.22 * (arm in {"reminder", "info_simplified"})
        information_index = prior_awareness + 0.25 * (arm in {"information", "info_simplified"})
        perceived_eligibility = min(0.98, information_index + 0.12 * eligible - 0.06 * (not eligible))
        takeup_score = 0.40 * perceived_eligibility + 0.26 * salience_index - 0.28 * hassle_index
        action_threshold = 0.19 + 0.035 * (applicant_type % 5) + 0.04 * (applicant_type % 4 == 0)
        completed_claim = int(eligible and takeup_score >= action_threshold - 0.025)
        take_up = int(eligible and takeup_score >= action_threshold)

        rows.append(
            {
                "applicant_id": f"applicant-{applicant:03d}",
                "arm": arm,
                "eligible": int(eligible),
                "prior_awareness": round(prior_awareness, 3),
                "information_index": round(information_index, 3),
                "salience_index": round(salience_index, 3),
                "hassle_index": round(hassle_index, 3),
                "perceived_eligibility": round(perceived_eligibility, 3),
                "completed_claim": completed_claim,
                "take_up": take_up,
            }
        )

    return pd.DataFrame(rows)


def workplace_complexity() -> pd.DataFrame:
    rows = []
    contracts = ["simple", "opaque", "opaque_with_tutorial"]
    for worker in range(360):
        contract = contracts[worker % len(contracts)]
        true_bonus_rate = 0.18 + 0.02 * (worker % 4)
        complexity_gap = 0.0 if contract == "simple" else 0.075
        tutorial_gain = 0.045 if contract == "opaque_with_tutorial" else 0.0
        perceived_bonus_rate = true_bonus_rate - complexity_gap + tutorial_gain
        attention_minutes = 4.5 + 2.0 * (contract != "simple") + 2.3 * (contract == "opaque_with_tutorial")
        effort_units = 55 + 110 * perceived_bonus_rate + 0.6 * attention_minutes + (worker % 6)
        bonus_earned = effort_units * true_bonus_rate

        rows.append(
            {
                "worker_id": f"contract-worker-{worker:03d}",
                "contract": contract,
                "true_bonus_rate": round(true_bonus_rate, 3),
                "perceived_bonus_rate": round(perceived_bonus_rate, 3),
                "perception_gap": round(true_bonus_rate - perceived_bonus_rate, 3),
                "attention_minutes": round(attention_minutes, 2),
                "effort_units": round(effort_units, 2),
                "bonus_earned": round(bonus_earned, 2),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    schedule_learning().to_csv(original / "schedule_learning_synthetic.csv", index=False)
    policy_navigation().to_csv(transfer / "policy_navigation_synthetic.csv", index=False)
    workplace_complexity().to_csv(transfer / "workplace_complexity_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
