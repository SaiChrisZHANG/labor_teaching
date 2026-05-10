from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def gift_exchange() -> pd.DataFrame:
    rows = []
    arms = ["control", "cash_gift", "noncash_gift", "piece_rate", "employer_return"]
    for worker in range(600):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        skill = 0.82 + 0.035 * (worker_type % 7)
        reciprocity_index = 0.25 + 0.10 * (worker_type % 6)
        baseline_minutes = 42 + 2.1 * (worker_type % 5)

        gift_value = 0.0
        employer_effort = 0.0
        piece_rate = 0.0
        framing_salience = 0.15
        if arm == "cash_gift":
            gift_value = 1.0
            framing_salience = 0.45
        elif arm == "noncash_gift":
            gift_value = 0.85
            employer_effort = 0.35
            framing_salience = 0.55
        elif arm == "piece_rate":
            piece_rate = 0.22
            framing_salience = 0.35
        elif arm == "employer_return":
            gift_value = 0.65
            employer_effort = 0.55
            framing_salience = 0.50

        extra_work_minutes = (
            baseline_minutes
            + 10.5 * gift_value * reciprocity_index
            + 13.0 * piece_rate
            + 4.5 * employer_effort
            + 1.3 * (worker_type % 3)
        )
        quality_score = (
            0.76
            + 0.028 * (worker_type % 5)
            + 0.035 * piece_rate
            + 0.018 * employer_effort
            - 0.012 * gift_value * (arm == "cash_gift")
        )
        quality_score = min(0.97, max(0.62, quality_score))
        output_units = 36 + skill * (0.52 * extra_work_minutes) + 7.0 * piece_rate + 1.8 * employer_effort
        productivity_value = output_units * quality_score
        productivity_per_minute = productivity_value / extra_work_minutes

        rows.append(
            {
                "worker_id": f"worker-{worker:03d}",
                "arm": arm,
                "skill": round(skill, 3),
                "reciprocity_index": round(reciprocity_index, 3),
                "gift_value": round(gift_value, 3),
                "employer_effort": round(employer_effort, 3),
                "piece_rate": round(piece_rate, 3),
                "framing_salience": round(framing_salience, 3),
                "extra_work_minutes": round(extra_work_minutes, 2),
                "output_units": round(output_units, 2),
                "quality_score": round(quality_score, 3),
                "productivity_value": round(productivity_value, 2),
                "productivity_per_minute": round(productivity_per_minute, 3),
            }
        )

    return pd.DataFrame(rows)


def monitoring() -> pd.DataFrame:
    rows = []
    arms = ["control", "pay_only", "monitoring_only", "pay_monitoring", "digital_dashboard"]
    for worker in range(500):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        baseline_productivity = 72 + 1.8 * (worker_type % 9)
        reciprocity_index = 0.35 + 0.07 * (worker_type % 5)

        bonus_rate = 0.0
        monitoring_intensity = 0.12
        feedback_score = 0.18
        digital_visibility = 0.0
        if arm == "pay_only":
            bonus_rate = 0.20
        elif arm == "monitoring_only":
            monitoring_intensity = 0.58
            feedback_score = 0.44
        elif arm == "pay_monitoring":
            bonus_rate = 0.20
            monitoring_intensity = 0.60
            feedback_score = 0.50
        elif arm == "digital_dashboard":
            bonus_rate = 0.12
            monitoring_intensity = 0.82
            feedback_score = 0.63
            digital_visibility = 1.0

        crowdout = 0.10 * max(0, monitoring_intensity - 0.55)
        relational_motivation = max(0.05, reciprocity_index - crowdout)
        visible_effort = baseline_productivity + 18 * bonus_rate + 10 * monitoring_intensity + 5 * feedback_score
        productive_output = baseline_productivity + 20 * bonus_rate + 6 * feedback_score + 4 * relational_motivation
        compliance_actions = 8 + 12 * monitoring_intensity + 1.5 * digital_visibility + (worker_type % 4)
        gaming_score = max(0, 0.15 + 0.52 * monitoring_intensity + 0.25 * bonus_rate - 0.20 * feedback_score)

        rows.append(
            {
                "worker_id": f"monitor-worker-{worker:03d}",
                "arm": arm,
                "bonus_rate": round(bonus_rate, 3),
                "monitoring_intensity": round(monitoring_intensity, 3),
                "feedback_score": round(feedback_score, 3),
                "digital_visibility": int(digital_visibility),
                "reciprocity_index": round(reciprocity_index, 3),
                "relational_motivation": round(relational_motivation, 3),
                "visible_effort": round(visible_effort, 2),
                "productive_output": round(productive_output, 2),
                "compliance_actions": round(compliance_actions, 2),
                "gaming_score": round(gaming_score, 3),
            }
        )

    return pd.DataFrame(rows)


def subjective_evaluation() -> pd.DataFrame:
    rows = []
    regimes = ["objective_metric", "subjective_low_discretion", "subjective_high_discretion"]
    for worker in range(360):
        regime = regimes[worker % len(regimes)]
        worker_type = worker // len(regimes)
        skill = 0.78 + 0.035 * (worker_type % 8)
        relationship_capital = 0.20 + 0.08 * (worker_type % 6)

        evaluation_weight = 0.15
        discretion = 0.10
        if regime == "subjective_low_discretion":
            evaluation_weight = 0.38
            discretion = 0.32
        elif regime == "subjective_high_discretion":
            evaluation_weight = 0.62
            discretion = 0.58

        influence_activity = 4.0 + 10.0 * evaluation_weight * relationship_capital + 1.2 * (worker_type % 3)
        productive_effort = 62 + 16 * skill - 0.45 * influence_activity + 2.0 * (regime == "objective_metric")
        objective_output = productive_effort * (0.78 + 0.04 * (worker_type % 4))
        subjective_rating = (
            0.55 * objective_output / 75
            + 0.36 * discretion * influence_activity
            + 0.18 * relationship_capital
        )
        pay_index = 0.65 * objective_output + 8.0 * evaluation_weight * subjective_rating

        rows.append(
            {
                "worker_id": f"eval-worker-{worker:03d}",
                "regime": regime,
                "skill": round(skill, 3),
                "relationship_capital": round(relationship_capital, 3),
                "evaluation_weight": round(evaluation_weight, 3),
                "discretion": round(discretion, 3),
                "influence_activity": round(influence_activity, 2),
                "productive_effort": round(productive_effort, 2),
                "objective_output": round(objective_output, 2),
                "subjective_rating": round(subjective_rating, 3),
                "pay_index": round(pay_index, 2),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    gift_exchange().to_csv(original / "gift_exchange_synthetic.csv", index=False)
    monitoring().to_csv(transfer / "monitoring_synthetic.csv", index=False)
    subjective_evaluation().to_csv(transfer / "subjective_evaluation_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
