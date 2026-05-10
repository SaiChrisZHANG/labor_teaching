from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def job_search_beliefs() -> pd.DataFrame:
    rows = []
    durations = [1, 4, 8, 12]
    for seeker in range(240):
        high_prospect = seeker % 5 in {0, 1}
        skill_index = ((seeker % 12) - 5.5) / 10
        optimism_type = seeker % 4 == 0
        baseline_true = 0.38 if high_prospect else 0.24

        for duration in durations:
            true_prob = max(0.05, baseline_true - 0.015 * duration + 0.04 * skill_index)
            model_prob = max(0.04, true_prob - 0.015)
            weak_update_gap = 0.09 if optimism_type else 0.04
            subjective_prob = max(0.03, min(0.92, model_prob + weak_update_gap - 0.004 * duration))
            draw = ((seeker * 37 + duration * 11) % 100) / 100
            applications = 5 + int(10 * subjective_prob) - int(duration / 4) + (seeker % 3)
            reservation_wage = 18.5 + 5.5 * subjective_prob + 1.6 * high_prospect - 0.08 * duration

            rows.append(
                {
                    "seeker_id": f"seeker-{seeker:03d}",
                    "duration_week": duration,
                    "high_prospect_type": int(high_prospect),
                    "optimism_type": int(optimism_type),
                    "model_predicted_prob_4wk": round(model_prob, 3),
                    "subjective_job_find_prob_4wk": round(subjective_prob, 3),
                    "realized_exit_next_4wk": int(draw < true_prob),
                    "applications_last_week": max(applications, 0),
                    "reservation_wage": round(reservation_wage, 2),
                }
            )

    return pd.DataFrame(rows)


def skill_certification() -> pd.DataFrame:
    rows = []
    for worker in range(300):
        certified = worker % 2 == 0
        true_skill = 45 + (worker % 30) * 1.6 + (worker % 7) * 0.8
        prior_belief = true_skill + ((worker % 9) - 4) * 2.1
        posterior_belief = 0.55 * prior_belief + 0.45 * true_skill if certified else prior_belief
        targeted_high_skill = int(posterior_belief >= 66)
        firm_signal = true_skill if certified else 0.65 * true_skill + ((worker % 11) - 5) * 2.0
        interview_score = 0.45 * firm_signal + 0.30 * true_skill + 4.5 * targeted_high_skill
        hired = int(interview_score >= 52 + 3.0 * targeted_high_skill)

        rows.append(
            {
                "worker_id": f"worker-{worker:03d}",
                "certified": int(certified),
                "true_skill_score": round(true_skill, 2),
                "prior_self_belief": round(prior_belief, 2),
                "posterior_self_belief": round(posterior_belief, 2),
                "targets_high_skill_vacancies": targeted_high_skill,
                "firm_signal_score": round(firm_signal, 2),
                "hired": hired,
            }
        )

    return pd.DataFrame(rows)


def wage_signal_applications() -> pd.DataFrame:
    rows = []
    wages = [18, 24, 30]
    for seeker in range(180):
        confidence = 0.35 + 0.1 * (seeker % 5)
        for posted_wage in wages:
            expected_payoff = 0.08 * posted_wage
            perceived_competition = 0.18 + 0.022 * posted_wage - 0.28 * confidence
            application_index = expected_payoff - perceived_competition + 0.03 * (seeker % 4)
            applied = int(application_index >= 1.35)
            rows.append(
                {
                    "seeker_id": f"seeker-{seeker:03d}",
                    "posted_wage": posted_wage,
                    "confidence_index": round(confidence, 2),
                    "perceived_competition": round(perceived_competition, 3),
                    "application_index": round(application_index, 3),
                    "applied": applied,
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    job_search_beliefs().to_csv(original / "job_search_beliefs_synthetic.csv", index=False)
    skill_certification().to_csv(transfer / "skill_certification_synthetic.csv", index=False)
    wage_signal_applications().to_csv(transfer / "wage_signal_applications_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
