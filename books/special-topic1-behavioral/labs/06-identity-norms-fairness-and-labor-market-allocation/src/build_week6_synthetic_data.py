from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def peer_pressure() -> pd.DataFrame:
    rows = []
    arms = ["low_peer_visible", "average_peer_visible", "high_peer_hidden", "high_peer_visible"]
    for worker in range(720):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        baseline_skill = 0.78 + 0.035 * (worker_type % 8)
        intrinsic_effort = 42 + 1.5 * (worker_type % 6)
        peer_effort_norm = 45.0
        peer_visibility = 1.0
        learning_signal = 0.12
        social_pressure = 0.16

        if arm == "low_peer_visible":
            peer_effort_norm = 38.0
            social_pressure = 0.20
        elif arm == "average_peer_visible":
            peer_effort_norm = 45.0
            social_pressure = 0.18
        elif arm == "high_peer_hidden":
            peer_effort_norm = 53.0
            peer_visibility = 0.0
            learning_signal = 0.22
            social_pressure = 0.04
        elif arm == "high_peer_visible":
            peer_effort_norm = 53.0
            learning_signal = 0.24
            social_pressure = 0.26

        peer_learning_gain = learning_signal * (peer_effort_norm - 42.0)
        conformity_gain = peer_visibility * social_pressure * (peer_effort_norm - intrinsic_effort)
        effort_units = intrinsic_effort + peer_learning_gain + conformity_gain + 0.35 * (worker_type % 4)
        deviation_from_norm = abs(effort_units - peer_effort_norm)
        social_penalty_index = peer_visibility * social_pressure * deviation_from_norm
        productivity_value = 24 + baseline_skill * effort_units - 0.45 * social_penalty_index
        attendance_index = 0.82 + 0.012 * (worker_type % 5) - 0.006 * social_penalty_index

        rows.append(
            {
                "worker_id": f"peer-worker-{worker:03d}",
                "shift_id": f"shift-{worker % 60:02d}",
                "exposure_arm": arm,
                "baseline_skill": round(baseline_skill, 3),
                "intrinsic_effort": round(intrinsic_effort, 2),
                "peer_effort_norm": round(peer_effort_norm, 2),
                "peer_visibility": int(peer_visibility),
                "learning_signal": round(learning_signal, 3),
                "social_pressure": round(social_pressure, 3),
                "effort_units": round(effort_units, 2),
                "deviation_from_norm": round(deviation_from_norm, 2),
                "social_penalty_index": round(social_penalty_index, 3),
                "productivity_value": round(productivity_value, 2),
                "attendance_index": round(attendance_index, 3),
            }
        )

    return pd.DataFrame(rows)


def pay_comparisons() -> pd.DataFrame:
    rows = []
    arms = ["equal_pay", "underpaid_hidden", "underpaid_informed", "manager_salary_info", "compressed_pay"]
    for worker in range(500):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        base_wage = 18.00 + 0.30 * (worker_type % 5)
        peer_ref_wage = 19.20
        manager_ref_wage = 29.00
        comparison_info = 0
        transparency_depth = 0.0

        wage = base_wage
        if arm == "equal_pay":
            wage = peer_ref_wage
        elif arm == "underpaid_hidden":
            wage = base_wage
            comparison_info = 0
        elif arm == "underpaid_informed":
            wage = base_wage
            comparison_info = 1
            transparency_depth = 0.55
        elif arm == "manager_salary_info":
            wage = base_wage + 0.20
            comparison_info = 1
            transparency_depth = 0.85
        elif arm == "compressed_pay":
            wage = 18.95 + 0.05 * (worker_type % 3)
            peer_ref_wage = 19.05
            comparison_info = 1
            transparency_depth = 0.45

        peer_gap = max(0.0, peer_ref_wage - wage)
        manager_gap = max(0.0, manager_ref_wage - wage)
        fairness_cost = comparison_info * (0.75 * peer_gap + 0.10 * transparency_depth * manager_gap)
        morale_index = 82 - 5.8 * fairness_cost + 0.4 * (worker_type % 4)
        effort_units = 51 + 0.55 * (wage - 18) - 1.8 * fairness_cost + 0.25 * (worker_type % 6)
        quit_intent = 0.10 + 0.055 * fairness_cost + 0.01 * (arm == "manager_salary_info")

        rows.append(
            {
                "worker_id": f"fair-worker-{worker:03d}",
                "comparison_arm": arm,
                "wage": round(wage, 2),
                "peer_ref_wage": round(peer_ref_wage, 2),
                "manager_ref_wage": round(manager_ref_wage, 2),
                "comparison_info": comparison_info,
                "transparency_depth": round(transparency_depth, 2),
                "peer_gap": round(peer_gap, 2),
                "manager_gap": round(manager_gap, 2),
                "fairness_cost": round(fairness_cost, 3),
                "morale_index": round(morale_index, 2),
                "effort_units": round(effort_units, 2),
                "quit_intent": round(quit_intent, 3),
            }
        )

    return pd.DataFrame(rows)


def culture_sorting() -> pd.DataFrame:
    rows = []
    messages = ["neutral", "collaborative", "competitive", "flexible", "inclusive_growth"]
    worker_types = ["team_oriented", "career_accelerator", "flexibility_pref", "mission_fit"]
    for applicant in range(800):
        message = messages[applicant % len(messages)]
        worker_type = worker_types[(applicant // len(messages)) % len(worker_types)]
        baseline_interest = 0.42 + 0.02 * (applicant % 7)
        culture_fit = 0.18

        if message == "collaborative" and worker_type == "team_oriented":
            culture_fit = 0.42
        elif message == "competitive" and worker_type == "career_accelerator":
            culture_fit = 0.40
        elif message == "flexible" and worker_type == "flexibility_pref":
            culture_fit = 0.44
        elif message == "inclusive_growth" and worker_type in {"mission_fit", "team_oriented"}:
            culture_fit = 0.39
        elif message == "neutral":
            culture_fit = 0.22

        apply_score = baseline_interest + culture_fit
        accept_score = 0.50 + 0.55 * culture_fit + 0.02 * (applicant % 5)
        expected_retention = 0.58 + 0.33 * culture_fit

        rows.append(
            {
                "applicant_id": f"culture-app-{applicant:03d}",
                "culture_message": message,
                "worker_type": worker_type,
                "baseline_interest": round(baseline_interest, 3),
                "culture_fit": round(culture_fit, 3),
                "apply_score": round(apply_score, 3),
                "accept_score": round(accept_score, 3),
                "expected_retention": round(expected_retention, 3),
            }
        )

    return pd.DataFrame(rows)


def manager_transmission() -> pd.DataFrame:
    rows = []
    manager_norms = ["supportive_growth", "traditional_gatekeeping", "high_pressure_merit"]
    for worker in range(540):
        manager_norm = manager_norms[worker % len(manager_norms)]
        worker_type = worker // len(manager_norms)
        baseline_performance = 72 + 1.6 * (worker_type % 9)
        prior_team_culture = 0.44 + 0.04 * (worker_type % 6)

        support_index = 0.42
        promotion_standard = 0.50
        conformity_pressure = 0.22
        if manager_norm == "supportive_growth":
            support_index = 0.72
            promotion_standard = 0.48
            conformity_pressure = 0.16
        elif manager_norm == "traditional_gatekeeping":
            support_index = 0.30
            promotion_standard = 0.68
            conformity_pressure = 0.36
        elif manager_norm == "high_pressure_merit":
            support_index = 0.48
            promotion_standard = 0.76
            conformity_pressure = 0.42

        culture_alignment = 0.55 * prior_team_culture + 0.35 * support_index - 0.18 * conformity_pressure
        promotion_score = baseline_performance + 18 * support_index - 14 * promotion_standard + 5 * culture_alignment
        retention_index = 0.62 + 0.20 * support_index + 0.11 * culture_alignment - 0.16 * conformity_pressure
        local_norm_shift = culture_alignment - prior_team_culture

        rows.append(
            {
                "worker_id": f"manager-worker-{worker:03d}",
                "manager_norm": manager_norm,
                "baseline_performance": round(baseline_performance, 2),
                "prior_team_culture": round(prior_team_culture, 3),
                "support_index": round(support_index, 3),
                "promotion_standard": round(promotion_standard, 3),
                "conformity_pressure": round(conformity_pressure, 3),
                "culture_alignment": round(culture_alignment, 3),
                "promotion_score": round(promotion_score, 2),
                "retention_index": round(retention_index, 3),
                "local_norm_shift": round(local_norm_shift, 3),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    peer_pressure().to_csv(original / "peer_pressure_synthetic.csv", index=False)
    pay_comparisons().to_csv(transfer / "pay_comparison_synthetic.csv", index=False)
    culture_sorting().to_csv(transfer / "culture_sorting_synthetic.csv", index=False)
    manager_transmission().to_csv(transfer / "manager_transmission_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
