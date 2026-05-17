from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def safe_sd(values: list[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def platform_visibility_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for worker_number in range(1, 145):
        inexperienced = worker_number <= 96
        treated = 1 if inexperienced and worker_number % 3 != 0 else 0
        quality = clamp(0.36 + ((worker_number * 17) % 60) / 100)
        availability = clamp(0.30 + ((worker_number * 11) % 64) / 100)
        outside_option = clamp(0.24 + ((worker_number * 7) % 58) / 100)
        risk_tolerance = clamp(0.25 + ((worker_number * 19) % 60) / 100)
        baseline_reviews = 1 + (worker_number * 5) % 6 if inexperienced else 18 + (worker_number * 5) % 35

        public_signal = clamp(0.20 + 0.55 * quality + 0.10 * treated + ((worker_number * 13) % 8) / 100)
        ranking_position = 78 - 16 * treated - 19 * quality - 7 * availability + ((worker_number * 3) % 9)
        visibility_score = clamp(0.26 + 0.16 * treated + 0.22 * quality + 0.08 * availability - ranking_position / 260)
        employer_belief = clamp(0.28 + 0.38 * public_signal + 0.11 * baseline_reviews / 50 + 0.05 * treated)
        invitations = max(0, int(1 + 8 * visibility_score + 3 * employer_belief + (worker_number % 4 == 0)))
        applications = max(1, int(4 + 6 * availability + 2 * treated - 2 * outside_option + worker_number % 5))
        hire_probability = clamp(0.06 + 0.34 * employer_belief + 0.20 * visibility_score + 0.12 * quality - 0.05 * outside_option)
        hired = 1 if hire_probability + ((worker_number * 23) % 10) / 100 >= 0.43 else 0
        accepted_wage = 13.5 + 7.2 * quality + 2.1 * employer_belief + 1.4 * treated + 0.35 * invitations
        future_jobs = max(0, int(hired * (1 + 5 * quality + 2 * treated + invitations / 3)))
        earnings_risk = clamp(0.62 - 0.12 * treated - 0.11 * future_jobs / 10 + 0.17 * (1 - outside_option))
        flexibility_value = clamp(0.20 + 0.54 * availability + 0.10 * outside_option)

        rows.append(
            {
                "worker_id": f"P{worker_number:03d}",
                "experience_group": "inexperienced" if inexperienced else "experienced",
                "public_signal_treatment": treated,
                "baseline_reviews": baseline_reviews,
                "quality_index": round(quality, 3),
                "availability_index": round(availability, 3),
                "outside_option_index": round(outside_option, 3),
                "risk_tolerance_index": round(risk_tolerance, 3),
                "public_signal_score": round(public_signal, 3),
                "ranking_position": round(ranking_position, 3),
                "visibility_score": round(visibility_score, 3),
                "employer_belief_index": round(employer_belief, 3),
                "employer_invitations": invitations,
                "applications_sent": applications,
                "hire_probability": round(hire_probability, 3),
                "hired": hired,
                "accepted_hourly_wage": round(accepted_wage, 2),
                "future_jobs": future_jobs,
                "earnings_risk_index": round(earnings_risk, 3),
                "flexibility_value_index": round(flexibility_value, 3),
            }
        )

    return rows


def platform_steering_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for job_number in range(1, 97):
        guarantee = 1 if job_number % 2 == 0 else 0
        worker_quality = clamp(0.35 + ((job_number * 23) % 58) / 100)
        price_bid = 16 + ((job_number * 7) % 18) + 5 * worker_quality
        platform_fee_rate = 0.18 + 0.04 * guarantee
        buyer_trust = clamp(0.32 + 0.28 * guarantee + 0.24 * worker_quality + ((job_number * 5) % 9) / 100)
        assignment_probability = clamp(0.08 + 0.46 * buyer_trust + 0.18 * worker_quality - 0.006 * price_bid)
        assigned = 1 if assignment_probability + ((job_number * 17) % 10) / 100 >= 0.46 else 0
        worker_net_wage = price_bid * (1 - platform_fee_rate)
        dispute_risk = clamp(0.24 - 0.10 * guarantee + 0.12 * (1 - worker_quality))

        rows.append(
            {
                "job_id": f"G{job_number:03d}",
                "platform_guarantee": guarantee,
                "worker_quality_index": round(worker_quality, 3),
                "price_bid": round(price_bid, 2),
                "platform_fee_rate": round(platform_fee_rate, 3),
                "buyer_trust_index": round(buyer_trust, 3),
                "assignment_probability": round(assignment_probability, 3),
                "assigned": assigned,
                "worker_net_wage": round(worker_net_wage, 2),
                "dispute_risk_index": round(dispute_risk, 3),
            }
        )

    return rows


def summarize_visibility(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["experience_group"]), int(row["public_signal_treatment"]))].append(row)

    output: list[dict[str, object]] = []
    for experience_group in ("inexperienced", "experienced"):
        treatment_values = (0, 1) if experience_group == "inexperienced" else (0,)
        for treated in treatment_values:
            group_rows = grouped[(experience_group, treated)]
            if not group_rows:
                continue
            output.append(
                {
                    "experience_group": experience_group,
                    "public_signal_treatment": treated,
                    "workers": len(group_rows),
                    "mean_visibility_score": round(safe_mean([float(row["visibility_score"]) for row in group_rows]), 4),
                    "mean_employer_belief_index": round(safe_mean([float(row["employer_belief_index"]) for row in group_rows]), 4),
                    "mean_invitations": round(safe_mean([float(row["employer_invitations"]) for row in group_rows]), 4),
                    "mean_applications_sent": round(safe_mean([float(row["applications_sent"]) for row in group_rows]), 4),
                    "hire_rate": round(safe_mean([float(row["hired"]) for row in group_rows]), 4),
                    "mean_accepted_hourly_wage": round(safe_mean([float(row["accepted_hourly_wage"]) for row in group_rows]), 4),
                    "mean_future_jobs": round(safe_mean([float(row["future_jobs"]) for row in group_rows]), 4),
                    "mean_earnings_risk_index": round(safe_mean([float(row["earnings_risk_index"]) for row in group_rows]), 4),
                }
            )
    return output


def assignment_information_diagnostics(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    inexperienced = [row for row in rows if row["experience_group"] == "inexperienced"]
    treated = [row for row in inexperienced if int(row["public_signal_treatment"]) == 1]
    control = [row for row in inexperienced if int(row["public_signal_treatment"]) == 0]

    diagnostics = [
        (
            "visibility_or_ranking",
            "visibility_score and ranking position",
            safe_mean([float(row["visibility_score"]) for row in treated]) - safe_mean([float(row["visibility_score"]) for row in control]),
            "random public signal with ranking lift",
            "mechanical exposure can be mistaken for employer learning",
            "access to vacancies and invitations",
        ),
        (
            "employer_beliefs",
            "employer_belief_index",
            safe_mean([float(row["employer_belief_index"]) for row in treated])
            - safe_mean([float(row["employer_belief_index"]) for row in control]),
            "public reputation signal",
            "beliefs are latent and proxied by behavior",
            "match quality and worker reputation accumulation",
        ),
        (
            "hiring",
            "hire rate",
            safe_mean([float(row["hired"]) for row in treated]) - safe_mean([float(row["hired"]) for row in control]),
            "compare treated and control inexperienced workers",
            "treatment may bundle exposure and perceived quality",
            "employment access and future job ladder",
        ),
        (
            "wage_bargaining",
            "accepted hourly wage",
            safe_mean([float(row["accepted_hourly_wage"]) for row in treated])
            - safe_mean([float(row["accepted_hourly_wage"]) for row in control]),
            "observe accepted pay under the information rule",
            "accepted wages mix bargaining power, selection, and job composition",
            "earnings and surplus division",
        ),
        (
            "future_reputation",
            "future jobs",
            safe_mean([float(row["future_jobs"]) for row in treated]) - safe_mean([float(row["future_jobs"]) for row in control]),
            "follow future platform outcomes",
            "future jobs may reflect learning, persistence, or platform sorting",
            "dynamic access to work",
        ),
    ]

    return [
        {
            "design_object": design_object,
            "observed_margin": observed_margin,
            "treated_minus_control": round(effect, 4),
            "identification_design": identification_design,
            "remaining_threat": remaining_threat,
            "welfare_object": welfare_object,
        }
        for design_object, observed_margin, effect, identification_design, remaining_threat, welfare_object in diagnostics
    ]


def rule_incidence_diagnostics(
    visibility_rows: list[dict[str, object]],
    steering_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    treated = [row for row in visibility_rows if row["experience_group"] == "inexperienced" and int(row["public_signal_treatment"]) == 1]
    control = [row for row in visibility_rows if row["experience_group"] == "inexperienced" and int(row["public_signal_treatment"]) == 0]
    guaranteed = [row for row in steering_rows if int(row["platform_guarantee"]) == 1]
    unguaranteed = [row for row in steering_rows if int(row["platform_guarantee"]) == 0]

    return [
        {
            "rule_change": "public_signal_and_ranking_lift",
            "worker_margin": "accepted wage",
            "worker_effect": round(
                safe_mean([float(row["accepted_hourly_wage"]) for row in treated])
                - safe_mean([float(row["accepted_hourly_wage"]) for row in control]),
                4,
            ),
            "platform_or_employer_margin": "employer invitations",
            "platform_or_employer_effect": round(
                safe_mean([float(row["employer_invitations"]) for row in treated])
                - safe_mean([float(row["employer_invitations"]) for row in control]),
                4,
            ),
            "incidence_question": "Does better information raise worker surplus or mainly reallocate attention?",
            "main_threat": "Exposure, beliefs, and worker quality are bundled in realized platform outcomes.",
        },
        {
            "rule_change": "platform_guarantee",
            "worker_margin": "worker net wage",
            "worker_effect": round(
                safe_mean([float(row["worker_net_wage"]) for row in guaranteed])
                - safe_mean([float(row["worker_net_wage"]) for row in unguaranteed]),
                4,
            ),
            "platform_or_employer_margin": "buyer trust",
            "platform_or_employer_effect": round(
                safe_mean([float(row["buyer_trust_index"]) for row in guaranteed])
                - safe_mean([float(row["buyer_trust_index"]) for row in unguaranteed]),
                4,
            ),
            "incidence_question": "Does a guarantee improve trust while raising platform fees or changing worker net pay?",
            "main_threat": "Guaranteed workers may differ in unobserved ways if the guarantee is not randomized.",
        },
        {
            "rule_change": "platform_guarantee",
            "worker_margin": "dispute risk",
            "worker_effect": round(
                safe_mean([float(row["dispute_risk_index"]) for row in guaranteed])
                - safe_mean([float(row["dispute_risk_index"]) for row in unguaranteed]),
                4,
            ),
            "platform_or_employer_margin": "assignment rate",
            "platform_or_employer_effect": round(
                safe_mean([float(row["assigned"]) for row in guaranteed])
                - safe_mean([float(row["assigned"]) for row in unguaranteed]),
                4,
            ),
            "incidence_question": "Does steering reduce transaction risk or concentrate opportunity?",
            "main_threat": "Assignment effects may reflect platform credibility rather than worker productivity.",
        },
    ]


def worker_welfare_components(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        if row["experience_group"] == "inexperienced":
            grouped[int(row["public_signal_treatment"])].append(row)

    output: list[dict[str, object]] = []
    for treated in (0, 1):
        group_rows = grouped[treated]
        output.append(
            {
                "public_signal_treatment": treated,
                "workers": len(group_rows),
                "mean_earnings": round(safe_mean([float(row["accepted_hourly_wage"]) * float(row["hired"]) for row in group_rows]), 4),
                "earnings_standard_deviation": round(
                    safe_sd([float(row["accepted_hourly_wage"]) * float(row["hired"]) for row in group_rows]),
                    4,
                ),
                "mean_earnings_risk_index": round(safe_mean([float(row["earnings_risk_index"]) for row in group_rows]), 4),
                "mean_flexibility_value_index": round(safe_mean([float(row["flexibility_value_index"]) for row in group_rows]), 4),
                "mean_future_jobs": round(safe_mean([float(row["future_jobs"]) for row in group_rows]), 4),
                "welfare_warning": "Average earnings omit volatility, flexibility, future access, and platform monitoring burden.",
            }
        )
    return output


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "setting": "online_labor_market_public_signal",
            "rule": "randomized reputation disclosure or ranking lift",
            "labor_margin": "invitations, hires, accepted wages, future jobs",
            "counterfactual_rule": "same workers without public signal or ranking lift",
            "identification_strategy": "randomized information and visibility treatment",
            "welfare_object": "employment access, earnings, future reputation, and match quality",
            "main_threat": "information and attention effects are bundled",
        },
        {
            "setting": "platform_steering_or_guarantee",
            "rule": "platform endorsement or guarantee shown to buyers",
            "labor_margin": "buyer trust, assignments, worker net wages, dispute risk",
            "counterfactual_rule": "same eligible workers without guarantee display",
            "identification_strategy": "randomized guarantee eligibility or display",
            "welfare_object": "worker surplus, buyer trust, platform fees, and access",
            "main_threat": "platform may select workers for guarantees based on unobserved quality",
        },
        {
            "setting": "search_ranking_recommendation",
            "rule": "algorithmic ranking or recommended-worker list",
            "labor_margin": "profile views, applications, interviews, hires, wage bids",
            "counterfactual_rule": "old ranking or randomized search order",
            "identification_strategy": "A/B test or staggered ranking redesign",
            "welfare_object": "match quality, visibility inequality, worker access, and congestion",
            "main_threat": "equilibrium response can undo short-run ranking effects",
        },
        {
            "setting": "pay_transparency_in_job_posts",
            "rule": "required wage range disclosure",
            "labor_margin": "applications, applicant composition, posted wages, accepted wages",
            "counterfactual_rule": "same postings without wage information",
            "identification_strategy": "policy rollout, jurisdictional variation, or randomized disclosure",
            "welfare_object": "search efficiency, wage dispersion, bargaining power, and worker surplus",
            "main_threat": "employers may change titles, ranges, or posting behavior simultaneously",
        },
        {
            "setting": "platform_minimum_pay_rule",
            "rule": "minimum posted wage or platform wage floor",
            "labor_margin": "posting volume, bids, fill rates, accepted wages, worker entry",
            "counterfactual_rule": "same market without minimum pay rule",
            "identification_strategy": "wage-floor experiment or threshold-based policy change",
            "welfare_object": "earnings, employment, surplus incidence, and market thickness",
            "main_threat": "large pay rules can spill over across treated and untreated jobs",
        },
        {
            "setting": "ride_hailing_dynamic_pricing",
            "rule": "dynamic or personalized price and commission schedule",
            "labor_margin": "hours online, trips accepted, waiting time, earnings volatility",
            "counterfactual_rule": "uniform price or old commission rule",
            "identification_strategy": "platform policy change, randomized incentives, or quasi-random demand shocks",
            "welfare_object": "flexibility, risk, earnings, autonomy, and schedule control",
            "main_threat": "driver selection and local demand shocks confound labor-supply response",
        },
        {
            "setting": "platform_governance",
            "rule": "deactivation, dispute, refund, or monitoring rule",
            "labor_margin": "continuation, ratings, disputes, task acceptance, worker exit",
            "counterfactual_rule": "old governance procedure or randomized appeal access",
            "identification_strategy": "rule redesign, eligibility threshold, or randomized support intervention",
            "welfare_object": "income security, due process, quality, and platform dependence",
            "main_threat": "governance changes are often bundled with monitoring or quality reforms",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    visibility_rows = platform_visibility_rows()
    steering_rows = platform_steering_rows()
    visibility_summary = summarize_visibility(visibility_rows)
    assignment_diagnostics = assignment_information_diagnostics(visibility_rows)
    incidence_diagnostics = rule_incidence_diagnostics(visibility_rows, steering_rows)
    welfare_components = worker_welfare_components(visibility_rows)

    write_csv(lab_dir / "original" / "reduced" / "platform_visibility_synthetic.csv", visibility_rows)
    write_csv(lab_dir / "original" / "reduced" / "platform_steering_synthetic.csv", steering_rows)
    write_csv(lab_dir / "output" / "reproduced" / "visibility_information_summary.csv", visibility_summary)
    write_csv(lab_dir / "output" / "diagnosed" / "assignment_information_diagnostics.csv", assignment_diagnostics)
    write_csv(lab_dir / "output" / "diagnosed" / "rule_incidence_diagnostics.csv", incidence_diagnostics)
    write_csv(lab_dir / "output" / "diagnosed" / "worker_welfare_components.csv", welfare_components)
    write_csv(lab_dir / "output" / "transfer" / "platform_rule_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 4 platform-rules lab complete. Outputs reproduce an "
        "information and visibility summary, diagnose assignment, belief, wage, "
        "risk, and incidence margins, and transfer the design architecture to "
        "steering, transparency, wage-floor, dynamic-pricing, and governance settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
