from __future__ import annotations

import csv
from pathlib import Path


PERIODS = list(range(1, 7))


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def synthetic_panel() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for worker_num in range(1, 121):
        baseline_distress = clamp(0.18 + 0.045 * (worker_num % 9) + 0.035 * (worker_num % 4))
        job_strain = clamp(0.22 + 0.09 * (worker_num % 7))
        autonomy = clamp(0.82 - 0.08 * (worker_num % 6))
        conflict = clamp(0.08 + 0.07 * (worker_num % 5))
        isolation = clamp(0.10 + 0.06 * ((worker_num * 2) % 6))
        schedule_volatility = clamp(0.12 + 0.07 * ((worker_num * 3) % 7))
        supervision_support = clamp(0.78 - 0.06 * ((worker_num + 2) % 8))
        meaning = clamp(0.34 + 0.08 * ((worker_num + 4) % 7))
        stigma_climate = clamp(0.18 + 0.07 * ((worker_num + 1) % 8))
        treatment_access = clamp(0.32 + 0.09 * ((worker_num + 3) % 7))
        high_contact_job = 1 if worker_num % 4 in (0, 1) else 0
        safety_sensitive_job = 1 if worker_num % 6 in (0, 2) else 0

        for period in PERIODS:
            workplace_shock = 1 if period >= 4 and worker_num % 10 in (0, 1, 2) else 0
            job_quality_pressure = (
                0.26 * job_strain
                + 0.18 * conflict
                + 0.14 * isolation
                + 0.12 * schedule_volatility
                - 0.20 * autonomy
                - 0.18 * supervision_support
                - 0.16 * meaning
            )
            distress = clamp(
                baseline_distress
                + job_quality_pressure
                + 0.10 * workplace_shock
                + 0.03 * max(period - 3, 0)
            )
            high_distress = 1 if distress >= 0.50 else 0
            treatment_use = 1 if distress + treatment_access - 0.60 * stigma_climate > 0.58 else 0
            disclosed = 1 if high_distress and stigma_climate < 0.45 and supervision_support > 0.45 else 0
            accommodation = 1 if disclosed and treatment_access > 0.45 and period >= 3 else 0

            treatment_relief = 0.08 * treatment_use + 0.05 * accommodation
            stigma_penalty = 0.07 * high_distress * stigma_climate * (1 - disclosed)
            effective_distress = clamp(distress - treatment_relief + stigma_penalty)

            absenteeism_days = max(
                0.0,
                0.4
                + 3.0 * effective_distress
                + 0.8 * high_distress
                + 0.4 * safety_sensitive_job
                - 0.5 * accommodation
                - 0.3 * supervision_support,
            )
            presenteeism_score = clamp(
                0.08
                + 0.58 * effective_distress
                + 0.16 * high_contact_job
                + 0.10 * job_strain
                - 0.12 * autonomy
                - 0.08 * accommodation
            )
            performance_index = clamp(
                0.92
                - 0.22 * effective_distress
                - 0.06 * workplace_shock
                - 0.04 * conflict
                + 0.06 * meaning
                + 0.04 * accommodation,
                0.20,
                1.10,
            )
            quit_risk = clamp(
                0.04
                + 0.25 * effective_distress
                + 0.12 * job_strain
                + 0.08 * conflict
                - 0.10 * autonomy
                - 0.08 * meaning
                - 0.05 * accommodation
            )
            safety_incident_risk = clamp(
                0.02
                + 0.12 * effective_distress * safety_sensitive_job
                + 0.04 * schedule_volatility
                - 0.03 * supervision_support
            )
            welfare_index = clamp(
                0.88
                - 0.32 * distress
                - 0.12 * stigma_climate
                - 0.10 * job_strain
                + 0.12 * autonomy
                + 0.10 * meaning
                + 0.08 * treatment_use
                + 0.06 * accommodation,
                0.05,
                1.05,
            )

            rows.append(
                {
                    "worker_id": f"worker_{worker_num:03d}",
                    "period": period,
                    "distress_index": round(distress, 3),
                    "high_distress": high_distress,
                    "job_strain": round(job_strain, 3),
                    "autonomy": round(autonomy, 3),
                    "conflict": round(conflict, 3),
                    "isolation": round(isolation, 3),
                    "schedule_volatility": round(schedule_volatility, 3),
                    "supervision_support": round(supervision_support, 3),
                    "meaning": round(meaning, 3),
                    "stigma_climate": round(stigma_climate, 3),
                    "treatment_access": round(treatment_access, 3),
                    "treatment_use": treatment_use,
                    "disclosed": disclosed,
                    "accommodation": accommodation,
                    "workplace_shock": workplace_shock,
                    "high_contact_job": high_contact_job,
                    "safety_sensitive_job": safety_sensitive_job,
                    "absenteeism_days": round(absenteeism_days, 3),
                    "presenteeism_score": round(presenteeism_score, 3),
                    "performance_index": round(performance_index, 3),
                    "quit_risk": round(quit_risk, 3),
                    "safety_incident_risk": round(safety_incident_risk, 3),
                    "welfare_index": round(welfare_index, 3),
                }
            )
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def profile_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups = [
        ("low_distress", lambda row: int(row["high_distress"]) == 0),
        ("high_distress", lambda row: int(row["high_distress"]) == 1),
        ("high_distress_low_stigma", lambda row: int(row["high_distress"]) == 1 and float(row["stigma_climate"]) < 0.45),
        ("high_distress_high_stigma", lambda row: int(row["high_distress"]) == 1 and float(row["stigma_climate"]) >= 0.45),
        ("high_distress_high_autonomy", lambda row: int(row["high_distress"]) == 1 and float(row["autonomy"]) >= 0.55),
        ("high_distress_low_autonomy", lambda row: int(row["high_distress"]) == 1 and float(row["autonomy"]) < 0.55),
        ("high_distress_treatment_use", lambda row: int(row["high_distress"]) == 1 and int(row["treatment_use"]) == 1),
        ("high_distress_no_treatment", lambda row: int(row["high_distress"]) == 1 and int(row["treatment_use"]) == 0),
    ]
    outcomes = [
        "distress_index",
        "absenteeism_days",
        "presenteeism_score",
        "performance_index",
        "quit_risk",
        "safety_incident_risk",
        "treatment_use",
        "disclosed",
        "accommodation",
        "welfare_index",
    ]
    output: list[dict[str, object]] = []
    for group_name, selector in groups:
        selected = [row for row in rows if selector(row)]
        item: dict[str, object] = {"group": group_name, "worker_periods": len(selected)}
        for outcome in outcomes:
            item[f"mean_{outcome}"] = round(mean([float(row[outcome]) for row in selected]), 3)
        output.append(item)
    return output


def diagnosis_rows(profile: list[dict[str, object]]) -> list[dict[str, object]]:
    low = next(row for row in profile if row["group"] == "low_distress")
    high = next(row for row in profile if row["group"] == "high_distress")
    high_stigma = next(row for row in profile if row["group"] == "high_distress_high_stigma")
    low_stigma = next(row for row in profile if row["group"] == "high_distress_low_stigma")
    high_autonomy = next(row for row in profile if row["group"] == "high_distress_high_autonomy")
    low_autonomy = next(row for row in profile if row["group"] == "high_distress_low_autonomy")
    treatment = next(row for row in profile if row["group"] == "high_distress_treatment_use")
    no_treatment = next(row for row in profile if row["group"] == "high_distress_no_treatment")

    comparisons = [
        (
            "absenteeism_gap",
            float(high["mean_absenteeism_days"]) - float(low["mean_absenteeism_days"]),
            "productivity_loss_or_leave_access",
            "Higher absence among high-distress workers may reflect symptoms, treatment time, leave rules, or job strain.",
        ),
        (
            "presenteeism_gap",
            float(high["mean_presenteeism_score"]) - float(low["mean_presenteeism_score"]),
            "on_the_job_productivity_loss",
            "Presenteeism is close to the lecture object but remains partly self-reported and job-task dependent.",
        ),
        (
            "performance_gap",
            float(high["mean_performance_index"]) - float(low["mean_performance_index"]),
            "productivity_and_job_quality_bundle",
            "Lower performance may mix symptoms, workload, supervision, conflict, and task assignment.",
        ),
        (
            "quit_risk_gap",
            float(high["mean_quit_risk"]) - float(low["mean_quit_risk"]),
            "retention_and_dynamic_selection",
            "Quit risk can indicate worse job quality, lower mental health, constrained search, or selection out of observed employment.",
        ),
        (
            "stigma_disclosure_gap",
            float(low_stigma["mean_disclosed"]) - float(high_stigma["mean_disclosed"]),
            "stigma_and_information",
            "Disclosure is lower in high-stigma settings, so observed accommodation may understate need.",
        ),
        (
            "autonomy_welfare_gap",
            float(high_autonomy["mean_welfare_index"]) - float(low_autonomy["mean_welfare_index"]),
            "work_causing_mental_health_and_welfare",
            "Autonomy changes the welfare meaning of the same observed distress group.",
        ),
        (
            "treatment_performance_gap",
            float(treatment["mean_performance_index"]) - float(no_treatment["mean_performance_index"]),
            "treatment_selection",
            "Treatment users differ in access, severity, disclosure, and support; the gap is not a clean treatment effect.",
        ),
    ]
    return [
        {
            "diagnostic_margin": name,
            "gap": round(gap, 3),
            "dominant_issue": issue,
            "diagnostic_question": question,
        }
        for name, gap, issue, question in comparisons
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "treatment_access_shock",
            "latent_object": "distress, diagnosis, treatment take-up, and functioning",
            "labor_outcome": "absenteeism, presenteeism, retention, hours, and welfare",
            "identifying_variation": "provider supply, coverage, copayment, telehealth, or employee-assistance access",
            "main_threat": "treatment use is selected and access may change diagnosis intensity",
            "welfare_margin": "symptom relief and job feasibility may move before wages",
        },
        {
            "scenario": "waiting_time_shock",
            "latent_object": "delayed mental-health treatment and recovery path",
            "labor_outcome": "sick leave, return to work, performance, and quits",
            "identifying_variation": "queue length, provider capacity, or appointment availability",
            "main_threat": "severity and urgency may affect priority and waiting time",
            "welfare_margin": "waiting can lower well-being even when employment is preserved",
        },
        {
            "scenario": "job_loss_event_study",
            "latent_object": "mental health caused by displacement or nonemployment",
            "labor_outcome": "reemployment, job quality, earnings, treatment, and distress",
            "identifying_variation": "plant closure, mass layoff, or displacement timing",
            "main_threat": "pre-displacement health and firm decline may create pre-trends",
            "welfare_margin": "distress and loss of meaning can exceed earnings loss",
        },
        {
            "scenario": "pandemic_or_workplace_reorganization_shock",
            "latent_object": "stress, isolation, workload, and schedule control",
            "labor_outcome": "productivity, absences, quits, remote-work attachment, and welfare",
            "identifying_variation": "occupation feasibility, policy timing, or firm reorganization",
            "main_threat": "shocks move demand, caregiving, risk, and reporting at the same time",
            "welfare_margin": "remote work can improve flexibility while raising isolation",
        },
        {
            "scenario": "disclosure_destigmatization_intervention",
            "latent_object": "stigma, beliefs, disclosure, and help-seeking",
            "labor_outcome": "accommodations, attendance, treatment use, retention, and promotion",
            "identifying_variation": "randomized information, manager training, or rollout timing",
            "main_threat": "changed reporting can look like changed mental health",
            "welfare_margin": "safer disclosure may raise measured need while improving welfare",
        },
        {
            "scenario": "structural_job_search_model",
            "latent_object": "dynamic mental health, treatment, job quality, and search capacity",
            "labor_outcome": "job choice, quits, wages, productivity, and treatment",
            "identifying_variation": "model restrictions plus shocks to job offers, treatment access, or policies",
            "main_threat": "results depend on functional form and transition assumptions",
            "welfare_margin": "counterfactual job quality and treatment access can be valued directly",
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
    panel = synthetic_panel()
    profile = profile_rows(panel)

    write_csv(lab_dir / "original" / "reduced" / "mental_health_workplace_synthetic.csv", panel)
    write_csv(lab_dir / "output" / "reproduced" / "mental_health_productivity_profile.csv", profile)
    write_csv(lab_dir / "output" / "diagnosed" / "mental_health_mechanism_diagnosis.csv", diagnosis_rows(profile))
    write_csv(lab_dir / "output" / "transfer" / "mental_health_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 4 mental-health productivity lab complete. Outputs compare "
        "distress, absenteeism, presenteeism, performance, quits, disclosure, "
        "accommodations, stigma, treatment, job quality, and welfare; diagnose "
        "causal limits; and transfer the design to frontier settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
