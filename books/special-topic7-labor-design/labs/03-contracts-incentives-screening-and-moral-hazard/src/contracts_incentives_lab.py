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


def performance_pay_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for worker_number in range(1, 97):
        ability = clamp(0.43 + ((worker_number * 17) % 53) / 100)
        commitment = clamp(0.34 + ((worker_number * 11) % 61) / 100)
        risk_tolerance = clamp(0.28 + ((worker_number * 19) % 58) / 100)
        hours = 7.2 + ((worker_number * 5) % 10) / 10
        baseline_output = 42 + 34 * ability + 6 * commitment - 3 * risk_tolerance + ((worker_number * 7) % 9)
        baseline_quality = clamp(0.72 + 0.18 * ability + 0.04 * commitment - ((worker_number * 3) % 7) / 100)
        baseline_task_share = clamp(0.48 + ((worker_number * 13) % 20) / 100)
        baseline_pay = 19.5 * hours + 0.18 * baseline_output

        low_fit_exit = ability < 0.70 and worker_number % 4 == 0
        high_risk_exit = risk_tolerance < 0.43 and worker_number % 7 == 0
        retained = not (low_fit_exit or high_risk_exit)

        rows.append(
            {
                "worker_id": f"W{worker_number:03d}",
                "period": "hourly_baseline",
                "contract": "hourly_pay",
                "worker_status": "baseline_incumbent",
                "ability_index": round(ability, 3),
                "commitment_index": round(commitment, 3),
                "risk_tolerance_index": round(risk_tolerance, 3),
                "retained_into_performance_pay": int(retained),
                "hours_worked": round(hours, 2),
                "output_units": round(baseline_output, 3),
                "quality_score": round(baseline_quality, 3),
                "measured_task_share": round(baseline_task_share, 3),
                "pay": round(baseline_pay, 2),
                "entry_source": "incumbent",
            }
        )

        if retained:
            incentive_response = 7.8 + 5.4 * ability + 3.2 * commitment + 2.4 * risk_tolerance
            post_output = baseline_output + incentive_response
            post_quality = clamp(baseline_quality - 0.035 - 0.025 * (baseline_task_share > 0.60) + 0.015 * commitment)
            post_task_share = clamp(baseline_task_share + 0.13 + 0.04 * risk_tolerance)
            post_hours = hours + 0.18 + 0.22 * commitment
            post_pay = 15.0 * post_hours + 1.22 * post_output
            rows.append(
                {
                    "worker_id": f"W{worker_number:03d}",
                    "period": "performance_pay",
                    "contract": "piece_rate",
                    "worker_status": "continuing_incumbent",
                    "ability_index": round(ability, 3),
                    "commitment_index": round(commitment, 3),
                    "risk_tolerance_index": round(risk_tolerance, 3),
                    "retained_into_performance_pay": 1,
                    "hours_worked": round(post_hours, 2),
                    "output_units": round(post_output, 3),
                    "quality_score": round(post_quality, 3),
                    "measured_task_share": round(post_task_share, 3),
                    "pay": round(post_pay, 2),
                    "entry_source": "incumbent",
                }
            )

    for entrant_number in range(97, 115):
        ability = clamp(0.66 + ((entrant_number * 13) % 30) / 100)
        commitment = clamp(0.36 + ((entrant_number * 17) % 56) / 100)
        risk_tolerance = clamp(0.45 + ((entrant_number * 23) % 45) / 100)
        hours = 7.4 + ((entrant_number * 3) % 9) / 10
        output = 53 + 38 * ability + 7 * commitment + 3 * risk_tolerance + ((entrant_number * 5) % 8)
        quality = clamp(0.70 + 0.17 * ability + 0.03 * commitment - ((entrant_number * 2) % 8) / 100)
        task_share = clamp(0.62 + ((entrant_number * 7) % 20) / 100)
        pay = 15.0 * hours + 1.22 * output

        rows.append(
            {
                "worker_id": f"W{entrant_number:03d}",
                "period": "performance_pay",
                "contract": "piece_rate",
                "worker_status": "new_entrant",
                "ability_index": round(ability, 3),
                "commitment_index": round(commitment, 3),
                "risk_tolerance_index": round(risk_tolerance, 3),
                "retained_into_performance_pay": 0,
                "hours_worked": round(hours, 2),
                "output_units": round(output, 3),
                "quality_score": round(quality, 3),
                "measured_task_share": round(task_share, 3),
                "pay": round(pay, 2),
                "entry_source": "entrant",
            }
        )

    return rows


def subjective_evaluation_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case_number in range(1, 81):
        ability = clamp(0.40 + ((case_number * 17) % 55) / 100)
        evaluator_known = 1 if case_number % 2 == 0 else 0
        evaluator_favorability = clamp(0.25 + ((case_number * 11) % 65) / 100)
        public_service_motivation = clamp(0.32 + ((case_number * 7) % 60) / 100)
        influence_activity = clamp(
            0.10
            + 0.24 * evaluator_known
            + 0.14 * evaluator_favorability
            - 0.05 * public_service_motivation
            + ((case_number * 5) % 10) / 100,
        )
        objective_output = 61 + 24 * ability + 9 * public_service_motivation - 8 * influence_activity + ((case_number * 3) % 8)
        subjective_rating = (
            55
            + 0.38 * objective_output
            + 12 * evaluator_favorability
            + 9 * influence_activity * evaluator_known
            + ((case_number * 13) % 7)
        )
        promotion_probability = clamp(-0.20 + subjective_rating / 100 + 0.15 * evaluator_known)

        rows.append(
            {
                "case_id": f"S{case_number:03d}",
                "evaluator_known": evaluator_known,
                "ability_index": round(ability, 3),
                "public_service_motivation": round(public_service_motivation, 3),
                "evaluator_favorability": round(evaluator_favorability, 3),
                "influence_activity_index": round(influence_activity, 3),
                "objective_output_index": round(objective_output, 3),
                "subjective_rating": round(subjective_rating, 3),
                "promotion_probability": round(promotion_probability, 3),
            }
        )
    return rows


def summarize_performance(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["period"])].append(row)

    output: list[dict[str, object]] = []
    for period in ("hourly_baseline", "performance_pay"):
        period_rows = grouped[period]
        output.append(
            {
                "period": period,
                "workers": len(period_rows),
                "mean_output_units": round(safe_mean([float(row["output_units"]) for row in period_rows]), 3),
                "mean_quality_score": round(safe_mean([float(row["quality_score"]) for row in period_rows]), 4),
                "mean_hours_worked": round(safe_mean([float(row["hours_worked"]) for row in period_rows]), 3),
                "mean_pay": round(safe_mean([float(row["pay"]) for row in period_rows]), 3),
                "pay_standard_deviation": round(safe_sd([float(row["pay"]) for row in period_rows]), 3),
                "mean_measured_task_share": round(safe_mean([float(row["measured_task_share"]) for row in period_rows]), 4),
                "mean_ability_index": round(safe_mean([float(row["ability_index"]) for row in period_rows]), 4),
                "entrant_share": round(safe_mean([1.0 if row["entry_source"] == "entrant" else 0.0 for row in period_rows]), 4),
            }
        )
    return output


def decompose_incentives_and_sorting(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    baseline = [row for row in rows if row["period"] == "hourly_baseline"]
    post = [row for row in rows if row["period"] == "performance_pay"]
    retained_ids = {str(row["worker_id"]) for row in post if row["worker_status"] == "continuing_incumbent"}
    baseline_retained = [row for row in baseline if str(row["worker_id"]) in retained_ids]
    post_retained = [row for row in post if row["worker_status"] == "continuing_incumbent"]

    metrics = [
        ("output_units", "Higher measured output is the headline performance-pay fact."),
        ("quality_score", "Quality warns that measured output is not true performance."),
        ("pay", "Pay captures worker surplus and risk exposure, not only productivity."),
        ("measured_task_share", "Task share diagnoses multitasking toward rewarded margins."),
        ("ability_index", "Ability diagnoses workforce-composition change."),
    ]

    output: list[dict[str, object]] = []
    for metric, interpretation in metrics:
        baseline_all = safe_mean([float(row[metric]) for row in baseline])
        baseline_retained_mean = safe_mean([float(row[metric]) for row in baseline_retained])
        post_retained_mean = safe_mean([float(row[metric]) for row in post_retained])
        post_all = safe_mean([float(row[metric]) for row in post])
        output.append(
            {
                "metric": metric,
                "baseline_all": round(baseline_all, 4),
                "baseline_retained": round(baseline_retained_mean, 4),
                "post_retained": round(post_retained_mean, 4),
                "post_all": round(post_all, 4),
                "raw_gap": round(post_all - baseline_all, 4),
                "within_worker_change": round(post_retained_mean - baseline_retained_mean, 4),
                "baseline_selection_component": round(baseline_retained_mean - baseline_all, 4),
                "post_composition_component": round(post_all - post_retained_mean, 4),
                "interpretation": interpretation,
            }
        )
    return output


def summarize_subjective_evaluation(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["evaluator_known"])].append(row)

    output: list[dict[str, object]] = []
    for evaluator_known in (0, 1):
        group_rows = grouped[evaluator_known]
        output.append(
            {
                "evaluation_environment": "known_evaluator" if evaluator_known else "unknown_or_rotating_evaluator",
                "cases": len(group_rows),
                "mean_influence_activity_index": round(safe_mean([float(row["influence_activity_index"]) for row in group_rows]), 4),
                "mean_objective_output_index": round(safe_mean([float(row["objective_output_index"]) for row in group_rows]), 4),
                "mean_subjective_rating": round(safe_mean([float(row["subjective_rating"]) for row in group_rows]), 4),
                "mean_promotion_probability": round(safe_mean([float(row["promotion_probability"]) for row in group_rows]), 4),
            }
        )
    return output


def hidden_object_diagnostics(
    performance_summary: list[dict[str, object]],
    decomposition: list[dict[str, object]],
    subjective_summary: list[dict[str, object]],
) -> list[dict[str, object]]:
    baseline = next(row for row in performance_summary if row["period"] == "hourly_baseline")
    post = next(row for row in performance_summary if row["period"] == "performance_pay")
    output_decomp = next(row for row in decomposition if row["metric"] == "output_units")
    quality_decomp = next(row for row in decomposition if row["metric"] == "quality_score")
    task_decomp = next(row for row in decomposition if row["metric"] == "measured_task_share")
    unknown_eval = next(row for row in subjective_summary if row["evaluation_environment"] == "unknown_or_rotating_evaluator")
    known_eval = next(row for row in subjective_summary if row["evaluation_environment"] == "known_evaluator")

    return [
        {
            "hidden_object": "effort",
            "observed_margin": "within-worker output change under performance pay",
            "synthetic_signal": output_decomp["within_worker_change"],
            "identification_design": "contract change with workers observed before and after",
            "remaining_threat": "learning, task assignment, or demand shocks may also raise output",
            "welfare_object": "productivity net of worker cost and risk",
        },
        {
            "hidden_object": "type",
            "observed_margin": "difference between raw output gap and within-worker change",
            "synthetic_signal": output_decomp["post_composition_component"],
            "identification_design": "separate incumbents, exits, and entrants",
            "remaining_threat": "entry and exit can respond to unobserved outside options",
            "welfare_object": "match quality, retention, and distribution of gains",
        },
        {
            "hidden_object": "risk_sharing",
            "observed_margin": "pay dispersion before and after performance pay",
            "synthetic_signal": round(float(post["pay_standard_deviation"]) - float(baseline["pay_standard_deviation"]), 4),
            "identification_design": "compare pay variance and average pay under contract regimes",
            "remaining_threat": "pay variance mixes risk exposure and productivity heterogeneity",
            "welfare_object": "worker insurance and surplus",
        },
        {
            "hidden_object": "multitasking",
            "observed_margin": "measured-task share and quality under the new contract",
            "synthetic_signal": f"task_share_gap={task_decomp['raw_gap']}; quality_gap={quality_decomp['raw_gap']}",
            "identification_design": "track rewarded and unrewarded performance dimensions",
            "remaining_threat": "quality may be measured noisily or with delay",
            "welfare_object": "true organizational output, not only measured units",
        },
        {
            "hidden_object": "subjective_evaluation_influence",
            "observed_margin": "influence activity and ratings when evaluator identity is known",
            "synthetic_signal": round(
                float(known_eval["mean_influence_activity_index"])
                - float(unknown_eval["mean_influence_activity_index"]),
                4,
            ),
            "identification_design": "evaluator rotation or random evaluator assignment",
            "remaining_threat": "known evaluators may also have better information",
            "welfare_object": "public-service output, fairness, and promotion quality",
        },
        {
            "hidden_object": "commitment",
            "observed_margin": "contract take-up, attendance, and target completion",
            "synthetic_signal": "not directly observed in the performance-pay panel",
            "identification_design": "randomized contract menu or commitment-framing experiment",
            "remaining_threat": "commitment demand can be confounded with liquidity and risk preferences",
            "welfare_object": "worker surplus from discipline versus coercive effort extraction",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "setting": "piece_rate_manufacturing",
            "hidden_object": "effort versus type",
            "observed_margin": "output per hour, quality, worker entry and exit",
            "variation_or_design": "pay reform from hourly wage to piece rate",
            "identification_strategy": "worker panel decomposition with incumbent and entrant comparisons",
            "welfare_object": "productivity, pay, risk exposure, and retention",
            "main_threat": "contract change may coincide with technology or demand changes",
        },
        {
            "setting": "public_agency_subjective_evaluation",
            "hidden_object": "evaluator favoritism and influence activities",
            "observed_margin": "ratings, promotion, objective output, evaluator-facing effort",
            "variation_or_design": "random evaluator assignment or evaluator uncertainty",
            "identification_strategy": "compare behavior when evaluator identity is known versus unknown",
            "welfare_object": "public-service output, fairness, and promotion quality",
            "main_threat": "evaluator-specific knowledge can be mistaken for favoritism",
        },
        {
            "setting": "attendance_commitment_contract",
            "hidden_object": "self-control and commitment demand",
            "observed_margin": "contract take-up, attendance, target completion, quits",
            "variation_or_design": "randomized contract menu with optional penalties or targets",
            "identification_strategy": "compare choices and outcomes under commitment and standard contracts",
            "welfare_object": "worker surplus, discipline benefits, stress, and earnings",
            "main_threat": "take-up may reflect liquidity constraints or risk preferences",
        },
        {
            "setting": "promotion_tournament",
            "hidden_object": "relative-performance incentives and peer effects",
            "observed_margin": "rank, promotion, peer output, helping, sabotage, turnover",
            "variation_or_design": "promotion threshold or tournament-prize change",
            "identification_strategy": "cohort or unit variation in tournament intensity",
            "welfare_object": "productivity, cooperation, inequality, and retention",
            "main_threat": "peer composition and manager discretion may change simultaneously",
        },
        {
            "setting": "retail_team_bonus",
            "hidden_object": "team effort, free riding, and peer monitoring",
            "observed_margin": "store output, individual schedules, absenteeism, quits",
            "variation_or_design": "team bonus rollout across stores",
            "identification_strategy": "staggered rollout with store and worker histories",
            "welfare_object": "team productivity, worker risk, schedule burden, and inequality",
            "main_threat": "local demand shocks may look like incentive effects",
        },
        {
            "setting": "platform_task_bonus",
            "hidden_object": "task allocation and gaming",
            "observed_margin": "completed tasks, acceptance rates, quality flags, time online",
            "variation_or_design": "platform bonus formula or threshold experiment",
            "identification_strategy": "randomized threshold or eligibility discontinuity",
            "welfare_object": "earnings, quality, platform output, and worker time risk",
            "main_threat": "workers can shift effort across tasks or accounts",
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
    performance_rows = performance_pay_rows()
    subjective_rows = subjective_evaluation_rows()
    performance_summary = summarize_performance(performance_rows)
    decomposition = decompose_incentives_and_sorting(performance_rows)
    subjective_summary = summarize_subjective_evaluation(subjective_rows)
    diagnostics = hidden_object_diagnostics(performance_summary, decomposition, subjective_summary)

    write_csv(lab_dir / "original" / "reduced" / "performance_pay_synthetic.csv", performance_rows)
    write_csv(lab_dir / "original" / "reduced" / "subjective_evaluation_synthetic.csv", subjective_rows)
    write_csv(lab_dir / "output" / "reproduced" / "performance_pay_summary.csv", performance_summary)
    write_csv(lab_dir / "output" / "diagnosed" / "incentive_sorting_decomposition.csv", decomposition)
    write_csv(lab_dir / "output" / "diagnosed" / "hidden_object_diagnostics.csv", diagnostics)
    write_csv(lab_dir / "output" / "diagnosed" / "subjective_evaluation_comparison.csv", subjective_summary)
    write_csv(lab_dir / "output" / "transfer" / "contract_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 3 contracts-incentives lab complete. Outputs reproduce a "
        "performance-pay summary, diagnose incentives versus sorting, risk sharing, "
        "multitasking, subjective evaluation, and commitment, and transfer the design "
        "architecture to neighboring labor-contract settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
