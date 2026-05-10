from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def unit_interval(index: int, salt: int = 0) -> float:
    return ((index * 37 + salt * 17) % 100) / 100


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def takeup_design() -> tuple[pd.DataFrame, pd.DataFrame]:
    worker_rows = []
    duration_rows = []
    arms = ["control", "salience_notice", "simplified_form", "assistance", "full_support"]

    for worker in range(1000):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)

        expected_credit = 420 + 35 * (worker_type % 16)
        baseline_awareness = 0.16 + 0.028 * (worker_type % 12)
        baseline_trust = 0.32 + 0.035 * (worker_type % 9)
        admin_burden = 0.78 - 0.035 * (worker_type % 10)
        work_constraint = 0.20 + 0.032 * (worker_type % 11)

        salience = 0.0
        simplification = 0.0
        assistance = 0.0
        trust_support = 0.0
        if arm == "salience_notice":
            salience = 0.75
            trust_support = 0.10
        elif arm == "simplified_form":
            salience = 0.25
            simplification = 0.80
        elif arm == "assistance":
            salience = 0.25
            assistance = 0.85
            trust_support = 0.35
        elif arm == "full_support":
            salience = 0.80
            simplification = 0.80
            assistance = 0.75
            trust_support = 0.45

        post_awareness = clamp(
            baseline_awareness
            + 0.18 * salience
            + 0.12 * simplification
            + 0.10 * assistance
            + 0.06 * trust_support
            - 0.035 * work_constraint
            + 0.004 * (worker_type % 4),
            0.05,
            0.96,
        )
        perceived_value = expected_credit * clamp(0.50 + 0.55 * post_awareness + 0.10 * baseline_trust, 0.25, 1.15)
        procedural_cost = clamp(
            165
            + 105 * admin_burden
            + 75 * work_constraint
            - 70 * simplification
            - 65 * assistance
            - 35 * salience
            - 45 * trust_support,
            25,
            320,
        )
        net_perceived_gain = perceived_value - procedural_cost
        start_probability = clamp(
            0.12
            + 0.0010 * net_perceived_gain
            + 0.12 * salience
            + 0.08 * simplification
            + 0.07 * assistance
            + 0.05 * baseline_trust,
            0.02,
            0.96,
        )
        application_started = int(unit_interval(worker, 3) < start_probability)
        completion_probability = clamp(
            0.40
            + 0.0010 * net_perceived_gain
            + 0.18 * simplification
            + 0.16 * assistance
            + 0.05 * trust_support
            - 0.07 * work_constraint,
            0.02,
            0.98,
        )
        application_completed = int(application_started and unit_interval(worker, 7) < completion_probability)

        claim_week = 7
        for week in range(1, 7):
            if application_completed and claim_week == 7:
                hazard = clamp(
                    0.035
                    + 0.13 * post_awareness
                    + 0.00045 * net_perceived_gain
                    + 0.045 * simplification
                    + 0.040 * assistance
                    + 0.018 * week
                    - 0.035 * admin_burden,
                    0.01,
                    0.70,
                )
                claim_this_week = int(unit_interval(worker, week + 11) < hazard)
            else:
                hazard = 0.0
                claim_this_week = 0

            if claim_week == 7:
                duration_rows.append(
                    {
                        "worker_id": f"takeup-worker-{worker:04d}",
                        "week": week,
                        "arm": arm,
                        "at_risk": int(application_completed),
                        "claim_this_week": claim_this_week,
                        "model_hazard": round(hazard, 3),
                        "post_awareness": round(post_awareness, 3),
                        "procedural_cost": round(procedural_cost, 2),
                    }
                )
                if claim_this_week:
                    claim_week = week

        claimed_by_deadline = int(claim_week <= 6)
        filing_accuracy = clamp(
            0.56
            + 0.18 * post_awareness
            + 0.10 * simplification
            + 0.08 * assistance
            - 0.05 * work_constraint,
            0.05,
            0.98,
        )
        earnings_response_index = clamp(
            0.18
            + 0.32 * post_awareness
            + 0.08 * claimed_by_deadline
            - 0.05 * admin_burden,
            0.02,
            0.80,
        )

        worker_rows.append(
            {
                "worker_id": f"takeup-worker-{worker:04d}",
                "arm": arm,
                "treated": int(arm != "control"),
                "salience": round(salience, 3),
                "simplification": round(simplification, 3),
                "assistance": round(assistance, 3),
                "trust_support": round(trust_support, 3),
                "expected_credit": round(expected_credit, 2),
                "baseline_awareness": round(baseline_awareness, 3),
                "post_awareness": round(post_awareness, 3),
                "baseline_trust": round(baseline_trust, 3),
                "admin_burden": round(admin_burden, 3),
                "work_constraint": round(work_constraint, 3),
                "perceived_value": round(perceived_value, 2),
                "procedural_cost": round(procedural_cost, 2),
                "net_perceived_gain": round(net_perceived_gain, 2),
                "application_started": application_started,
                "application_completed": application_completed,
                "claimed_by_deadline": claimed_by_deadline,
                "weeks_to_claim": min(claim_week, 6),
                "filing_accuracy": round(filing_accuracy, 3),
                "earnings_response_index": round(earnings_response_index, 3),
            }
        )

    return pd.DataFrame(worker_rows), pd.DataFrame(duration_rows)


def eitc_knowledge() -> pd.DataFrame:
    rows = []
    phasein_end = 14000.0
    phaseout_start = 20500.0

    for worker in range(900):
        knowledge_group = "high_knowledge" if worker % 3 == 0 else "low_knowledge"
        worker_type = worker // 3
        neighborhood = f"neighborhood-{worker % 30:02d}"
        desired_earnings = 8200 + 72 * (worker_type % 235) + 9 * (worker_type % 8)
        local_knowledge = 0.78 if knowledge_group == "high_knowledge" else 0.30
        local_knowledge += 0.015 * (worker % 5)
        adjustment_cost = 0.18 + 0.016 * (worker_type % 9)

        observed_earnings = desired_earnings
        distance_phasein = desired_earnings - phasein_end
        distance_phaseout = desired_earnings - phaseout_start
        if abs(distance_phasein) <= 1600:
            observed_earnings -= local_knowledge * (1.0 - adjustment_cost) * distance_phasein * 0.55
        elif distance_phaseout > 0:
            observed_earnings -= local_knowledge * max(0.0, 1.0 - adjustment_cost) * distance_phaseout * 0.18

        segment = "phase_in"
        if observed_earnings >= phaseout_start:
            segment = "phaseout"
        elif observed_earnings > phasein_end:
            segment = "plateau"

        true_marginal_subsidy = 0.34 if segment == "phase_in" else (-0.16 if segment == "phaseout" else 0.0)
        perceived_subsidy = true_marginal_subsidy * local_knowledge
        rows.append(
            {
                "worker_id": f"eitc-worker-{worker:04d}",
                "knowledge_group": knowledge_group,
                "neighborhood": neighborhood,
                "desired_earnings": round(desired_earnings, 2),
                "observed_earnings": round(observed_earnings, 2),
                "distance_to_phasein_end": round(observed_earnings - phasein_end, 2),
                "segment": segment,
                "local_knowledge": round(local_knowledge, 3),
                "adjustment_cost": round(adjustment_cost, 3),
                "true_marginal_subsidy": round(true_marginal_subsidy, 3),
                "perceived_subsidy": round(perceived_subsidy, 3),
            }
        )

    return pd.DataFrame(rows)


def retirement_defaults() -> pd.DataFrame:
    rows = []
    arms = ["opt_in", "auto_enroll_3", "auto_enroll_6", "active_choice", "commitment_escalation"]

    for worker in range(750):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        inertia = 0.30 + 0.055 * (worker_type % 9)
        sophistication = 0.22 + 0.055 * (worker_type % 10)
        liquidity_need = 0.18 + 0.045 * (worker_type % 8)
        match_rate = 0.03 + 0.005 * (worker_type % 5)
        benchmark_rate = clamp(0.025 + match_rate + 0.030 * sophistication - 0.025 * liquidity_need, 0.0, 0.12)

        default_rate = 0.0
        active_prompt = 0.0
        commitment = 0.0
        if arm == "auto_enroll_3":
            default_rate = 0.03
        elif arm == "auto_enroll_6":
            default_rate = 0.06
        elif arm == "active_choice":
            active_prompt = 1.0
        elif arm == "commitment_escalation":
            default_rate = 0.03
            commitment = 1.0

        chosen_rate = benchmark_rate * (0.35 + 0.65 * sophistication)
        if default_rate > 0:
            chosen_rate = inertia * default_rate + (1 - inertia) * chosen_rate
        if active_prompt:
            chosen_rate = benchmark_rate * (0.75 + 0.20 * sophistication)
        if commitment:
            chosen_rate += 0.012 * (1.0 - liquidity_need)
        chosen_rate = clamp(chosen_rate, 0.0, 0.15)

        participation = int(chosen_rate > 0.005)
        welfare_gap = abs(chosen_rate - benchmark_rate)
        rows.append(
            {
                "worker_id": f"default-worker-{worker:04d}",
                "arm": arm,
                "inertia": round(inertia, 3),
                "sophistication": round(sophistication, 3),
                "liquidity_need": round(liquidity_need, 3),
                "match_rate": round(match_rate, 3),
                "default_rate": round(default_rate, 3),
                "active_prompt": round(active_prompt, 3),
                "commitment": round(commitment, 3),
                "benchmark_rate": round(benchmark_rate, 3),
                "chosen_rate": round(chosen_rate, 3),
                "participation": participation,
                "welfare_gap": round(welfare_gap, 3),
                "welfare_score": round(0.08 * participation - welfare_gap, 3),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    takeup, duration = takeup_design()
    takeup.to_csv(original / "benefit_takeup_synthetic.csv", index=False)
    duration.to_csv(original / "benefit_takeup_duration_synthetic.csv", index=False)
    eitc_knowledge().to_csv(transfer / "eitc_local_knowledge_synthetic.csv", index=False)
    retirement_defaults().to_csv(transfer / "retirement_default_welfare_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
