from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def unit_interval(index: int, salt: int = 0) -> float:
    return ((index * 37 + salt * 17) % 100) / 100


def job_search_information() -> tuple[pd.DataFrame, pd.DataFrame]:
    worker_rows = []
    duration_rows = []
    arms = ["control", "belief_info", "planning_prompt", "belief_planning"]

    for worker in range(800):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        baseline_belief = 0.24 + 0.018 * (worker_type % 10)
        baseline_applications = 2.0 + 0.45 * (worker_type % 5)
        search_cost_index = 0.25 + 0.035 * (worker_type % 8)
        prior_duration_weeks = 2 + (worker_type % 6)

        information_content = 0.0
        planning_support = 0.0
        salience_boost = 0.0
        if arm == "belief_info":
            information_content = 1.0
            planning_support = 0.20
            salience_boost = 0.35
        elif arm == "planning_prompt":
            information_content = 0.25
            planning_support = 1.0
            salience_boost = 0.45
        elif arm == "belief_planning":
            information_content = 1.0
            planning_support = 1.0
            salience_boost = 0.65

        post_belief = (
            baseline_belief
            + 0.115 * information_content
            + 0.035 * planning_support
            + 0.025 * salience_boost
            - 0.025 * search_cost_index
            + 0.004 * (worker_type % 3)
        )
        post_belief = min(0.78, max(0.08, post_belief))
        search_plan_score = (
            42
            + 13.0 * planning_support
            + 7.5 * information_content
            + 4.0 * salience_boost
            - 5.0 * search_cost_index
            + 0.6 * (worker_type % 6)
        )
        applications_week1 = (
            baseline_applications
            + 1.35 * information_content
            + 1.55 * planning_support
            + 0.45 * salience_boost
            - 0.70 * search_cost_index
            + 0.15 * (worker_type % 4)
        )
        applications_week1 = max(0.0, applications_week1)

        exit_week = 9
        for week in range(1, 9):
            hazard = (
                0.045
                + 0.13 * post_belief
                + 0.009 * applications_week1
                + 0.0014 * search_plan_score
                + 0.012 * week
                - 0.040 * search_cost_index
                - 0.004 * max(0, prior_duration_weeks - week)
            )
            hazard = min(0.55, max(0.02, hazard))
            if exit_week == 9:
                duration_rows.append(
                    {
                        "worker_id": f"search-worker-{worker:03d}",
                        "week": week,
                        "arm": arm,
                        "at_risk": 1,
                        "exit_this_week": int(unit_interval(worker, week) < hazard),
                        "hazard_probability": round(hazard, 3),
                        "belief_this_week": round(min(0.82, post_belief + 0.008 * week), 3),
                        "applications_this_week": round(max(0.0, applications_week1 - 0.12 * (week - 1)), 2),
                    }
                )
                if unit_interval(worker, week) < hazard:
                    exit_week = week

        observed_duration = min(exit_week, 8)
        worker_rows.append(
            {
                "worker_id": f"search-worker-{worker:03d}",
                "arm": arm,
                "treated": int(arm != "control"),
                "information_content": round(information_content, 3),
                "planning_support": round(planning_support, 3),
                "salience_boost": round(salience_boost, 3),
                "baseline_belief": round(baseline_belief, 3),
                "post_belief": round(post_belief, 3),
                "baseline_applications": round(baseline_applications, 2),
                "applications_week1": round(applications_week1, 2),
                "search_plan_score": round(search_plan_score, 2),
                "search_cost_index": round(search_cost_index, 3),
                "prior_duration_weeks": prior_duration_weeks,
                "exit_by_week4": int(exit_week <= 4),
                "observed_duration_weeks": observed_duration,
                "censored_at_week8": int(exit_week == 9),
            }
        )

    return pd.DataFrame(worker_rows), pd.DataFrame(duration_rows)


def gift_exchange_method() -> pd.DataFrame:
    rows = []
    arms = ["control", "cash_gift", "noncash_gift", "piece_rate", "employer_return"]

    for worker in range(600):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        baseline_skill = 0.78 + 0.035 * (worker_type % 8)
        reciprocity_index = 0.18 + 0.09 * (worker_type % 7)
        social_preference_weight = 0.20 + 0.06 * (worker_type % 6)

        gift_value = 0.0
        piece_rate = 0.0
        employer_effort = 0.0
        if arm == "cash_gift":
            gift_value = 1.0
        elif arm == "noncash_gift":
            gift_value = 0.85
            employer_effort = 0.25
        elif arm == "piece_rate":
            piece_rate = 0.22
        elif arm == "employer_return":
            gift_value = 0.65
            employer_effort = 0.55

        effort_minutes = (
            38
            + 7.5 * gift_value * reciprocity_index
            + 12.0 * piece_rate
            + 5.5 * employer_effort
            + 2.0 * social_preference_weight
            + 0.4 * (worker_type % 5)
        )
        output_units = 24 + baseline_skill * effort_minutes + 6.0 * piece_rate
        quality_score = min(
            0.98,
            0.72
            + 0.035 * (worker_type % 5)
            + 0.020 * employer_effort
            + 0.012 * social_preference_weight
            - 0.010 * (arm == "cash_gift"),
        )

        rows.append(
            {
                "worker_id": f"gift-worker-{worker:03d}",
                "arm": arm,
                "baseline_skill": round(baseline_skill, 3),
                "reciprocity_index": round(reciprocity_index, 3),
                "social_preference_weight": round(social_preference_weight, 3),
                "gift_value": round(gift_value, 3),
                "piece_rate": round(piece_rate, 3),
                "employer_effort": round(employer_effort, 3),
                "effort_minutes": round(effort_minutes, 2),
                "output_units": round(output_units, 2),
                "quality_score": round(quality_score, 3),
                "value_created": round(output_units * quality_score, 2),
            }
        )

    return pd.DataFrame(rows)


def schedule_bunching() -> pd.DataFrame:
    rows = []
    kink = 20000.0

    for worker in range(900):
        knowledge_group = "high_knowledge" if worker % 3 == 0 else "low_knowledge"
        worker_type = worker // 3
        desired_earnings = 16600 + 85 * (worker_type % 95) + 12 * (worker_type % 7)
        schedule_knowledge = 0.78 if knowledge_group == "high_knowledge" else 0.28
        distance = desired_earnings - kink
        adjustment_cost = 0.18 + 0.018 * (worker_type % 9)

        observed_earnings = desired_earnings
        if abs(distance) <= 1500:
            pull = schedule_knowledge * max(0.0, 1.0 - adjustment_cost)
            observed_earnings = desired_earnings - pull * distance
        elif distance > 1500:
            observed_earnings = desired_earnings - 0.10 * schedule_knowledge * distance

        phaseout_rate = 0.00 if observed_earnings <= kink else 0.21
        rows.append(
            {
                "worker_id": f"schedule-worker-{worker:03d}",
                "knowledge_group": knowledge_group,
                "desired_earnings": round(desired_earnings, 2),
                "observed_earnings": round(observed_earnings, 2),
                "kink": kink,
                "schedule_knowledge": round(schedule_knowledge, 3),
                "adjustment_cost": round(adjustment_cost, 3),
                "distance_to_kink": round(observed_earnings - kink, 2),
                "phaseout_rate": round(phaseout_rate, 3),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    workers, duration = job_search_information()
    workers.to_csv(original / "job_search_information_synthetic.csv", index=False)
    duration.to_csv(original / "job_search_duration_panel_synthetic.csv", index=False)
    gift_exchange_method().to_csv(transfer / "gift_exchange_method_synthetic.csv", index=False)
    schedule_bunching().to_csv(transfer / "schedule_bunching_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
