from __future__ import annotations

import csv
from pathlib import Path


EVENT_TIMES = list(range(-3, 6))


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def synthetic_panel() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for worker_num in range(1, 73):
        treated = 1 if worker_num <= 48 else 0
        group_offset = (worker_num % 8) / 100
        age_at_onset = 38 + (worker_num % 20)
        education_years = 11 + ((worker_num * 2) % 8)
        baseline_capacity = clamp(0.88 + group_offset + 0.012 * (education_years - 14))
        physical_demand = [0.25, 0.45, 0.60, 0.78][worker_num % 4]
        local_demand = [0.35, 0.50, 0.65, 0.80][(worker_num * 3) % 4]
        employer_quality = [0.30, 0.45, 0.60, 0.75][(worker_num * 5) % 4]
        condition_severity = clamp(0.35 + 0.07 * (worker_num % 6) + 0.12 * physical_demand)

        for event_time in EVENT_TIMES:
            post = 1 if event_time >= 0 else 0
            chronic_progression = max(event_time, 0) * 0.035 if treated else 0.0
            immediate_shock = 0.24 * post if treated else 0.0
            recovery_from_treatment = 0.04 * max(event_time - 1, 0) if treated and employer_quality > 0.55 else 0.0
            capacity = clamp(
                baseline_capacity
                - immediate_shock
                - chronic_progression
                - 0.06 * condition_severity * post * treated
                + recovery_from_treatment
            )

            accommodation = 1 if treated and event_time >= 1 and employer_quality + local_demand > 1.05 else 0
            benefit_receipt = 1 if treated and event_time >= 2 and capacity < 0.55 and local_demand < 0.70 else 0
            mobility = 1 if treated and event_time >= 2 and accommodation == 0 and local_demand > 0.55 else 0
            feasible_jobs = max(
                0,
                round(
                    7.5 * capacity
                    + 1.4 * accommodation
                    + 1.0 * local_demand
                    - 2.6 * physical_demand
                    - 1.1 * benefit_receipt
                ),
            )

            employment_score = (
                0.12
                + 0.78 * capacity
                + 0.11 * accommodation
                + 0.08 * local_demand
                - 0.18 * physical_demand
                - 0.30 * benefit_receipt
                - 0.03 * post * treated
            )
            threshold = 0.50 + 0.025 * (worker_num % 5)
            employed = 1 if employment_score > threshold else 0
            if benefit_receipt and event_time >= 3:
                employed = 0

            hours = 0.0
            earnings = 0.0
            if employed:
                hours = clamp(
                    15
                    + 28 * capacity
                    + 3.0 * accommodation
                    + 1.6 * local_demand
                    - 6.0 * physical_demand
                    - 2.0 * mobility,
                    8,
                    45,
                )
                wage_index = clamp(
                    0.62
                    + 0.015 * (education_years - 12)
                    + 0.12 * employer_quality
                    + 0.08 * capacity
                    - 0.035 * physical_demand
                    - 0.025 * mobility
                )
                earnings = hours * wage_index * 52

            rows.append(
                {
                    "worker_id": f"worker_{worker_num:03d}",
                    "treated_onset": treated,
                    "event_time": event_time,
                    "age_at_onset": age_at_onset,
                    "education_years": education_years,
                    "condition_severity": round(condition_severity, 3),
                    "physical_demand": round(physical_demand, 3),
                    "local_labor_demand": round(local_demand, 3),
                    "employer_quality": round(employer_quality, 3),
                    "latent_work_capacity": round(capacity, 3),
                    "accommodation_received": accommodation,
                    "benefit_receipt": benefit_receipt,
                    "job_mobility": mobility,
                    "feasible_jobs": feasible_jobs,
                    "employed": employed,
                    "hours": round(hours, 2),
                    "annual_earnings_index": round(earnings, 2),
                }
            )
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def rows_for(rows: list[dict[str, object]], event_time: int, treated: int) -> list[dict[str, object]]:
    return [
        row
        for row in rows
        if int(row["event_time"]) == event_time and int(row["treated_onset"]) == treated
    ]


def event_study_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    outcomes = [
        "latent_work_capacity",
        "employed",
        "hours",
        "annual_earnings_index",
        "feasible_jobs",
        "accommodation_received",
        "benefit_receipt",
        "job_mobility",
    ]
    output: list[dict[str, object]] = []
    for event_time in EVENT_TIMES:
        treated_rows = rows_for(rows, event_time, 1)
        comparison_rows = rows_for(rows, event_time, 0)
        row: dict[str, object] = {"event_time": event_time}
        for outcome in outcomes:
            treated_mean = mean([float(item[outcome]) for item in treated_rows])
            comparison_mean = mean([float(item[outcome]) for item in comparison_rows])
            row[f"treated_mean_{outcome}"] = round(treated_mean, 3)
            row[f"comparison_mean_{outcome}"] = round(comparison_mean, 3)
            row[f"treated_minus_comparison_{outcome}"] = round(treated_mean - comparison_mean, 3)
        output.append(row)
    return output


def mechanism_rows(event_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for row in event_rows:
        event_time = int(row["event_time"])
        capacity_gap = float(row["treated_minus_comparison_latent_work_capacity"])
        employment_gap = float(row["treated_minus_comparison_employed"])
        hours_gap = float(row["treated_minus_comparison_hours"])
        accommodation_gap = float(row["treated_minus_comparison_accommodation_received"])
        benefit_gap = float(row["treated_minus_comparison_benefit_receipt"])
        mobility_gap = float(row["treated_minus_comparison_job_mobility"])

        if event_time < 0:
            phase = "pre_onset_balance_window"
            dominant_channel = "selection_and_pre_trends"
            diagnostic = "Check whether treated and comparison paths are already diverging."
        elif event_time in (0, 1):
            phase = "short_run_disruption"
            dominant_channel = "direct_work_capacity_effect"
            diagnostic = "Capacity and hours move before benefit receipt is common."
        elif benefit_gap > 0.20:
            phase = "medium_run_program_interaction"
            dominant_channel = "program_incentives_and_benefit_receipt"
            diagnostic = "Benefit receipt and employment gaps move together."
        elif accommodation_gap > 0.20 and employment_gap > -0.15:
            phase = "accommodation_buffer"
            dominant_channel = "employer_accommodation_or_workplace_treatment"
            diagnostic = "Accommodation appears to cushion exit despite lower capacity."
        elif mobility_gap > 0.08:
            phase = "job_reallocation"
            dominant_channel = "local_labor_demand_and_feasible_job_set"
            diagnostic = "Mobility indicates search for a more feasible match."
        else:
            phase = "long_run_scarring"
            dominant_channel = "persistent_capacity_loss_and_selection"
            diagnostic = "Persistent gaps may mix health limits, selection, and local opportunity."

        output.append(
            {
                "event_time": event_time,
                "phase": phase,
                "dominant_channel": dominant_channel,
                "capacity_gap": round(capacity_gap, 3),
                "employment_gap": round(employment_gap, 3),
                "hours_gap": round(hours_gap, 3),
                "accommodation_gap": round(accommodation_gap, 3),
                "benefit_receipt_gap": round(benefit_gap, 3),
                "job_mobility_gap": round(mobility_gap, 3),
                "diagnostic_question": diagnostic,
            }
        )
    return output


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "acute_hospitalization",
            "health_object": "hospital admission as sharp health shock",
            "labor_margin": "employment, hours, and earnings before versus after admission",
            "identifying_variation": "event-time comparison with matched nonhospitalized workers",
            "visible_channel": "short-run work-capacity disruption and recovery",
            "remaining_threat": "severity, treatment intensity, insurance, and employer retention are bundled",
        },
        {
            "scenario": "employer_accommodation_access",
            "health_object": "documented limitation plus accommodation receipt",
            "labor_margin": "retention, hours, SSDI claiming, and job mobility",
            "identifying_variation": "firm policy, supervisor discretion, or matched employer-employee heterogeneity",
            "visible_channel": "workplace treatment and feasible-set expansion",
            "remaining_threat": "accommodation is selected by worker value, firm quality, and information",
        },
        {
            "scenario": "disability_program_threshold",
            "health_object": "program award, reassessment, or earnings-test margin",
            "labor_margin": "benefit receipt, employment, reentry, and earnings",
            "identifying_variation": "examiner assignment, threshold rules, or return-to-work reform",
            "visible_channel": "program incentives and benefit receipt",
            "remaining_threat": "local average treatment effect for marginal applicants only",
        },
        {
            "scenario": "treatment_or_return_to_work_reform",
            "health_object": "expanded treatment access or lower reentry penalty",
            "labor_margin": "hours, employment attachment, job quality, and exit timing",
            "identifying_variation": "policy timing, eligibility cutoff, or staggered access",
            "visible_channel": "capacity restoration and reentry incentives",
            "remaining_threat": "treatment changes health, reporting, and program response at the same time",
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
    event_rows = event_study_rows(panel)

    write_csv(lab_dir / "original" / "reduced" / "disability_chronic_conditions_synthetic.csv", panel)
    write_csv(lab_dir / "output" / "reproduced" / "disability_onset_event_study.csv", event_rows)
    write_csv(lab_dir / "output" / "diagnosed" / "mechanism_diagnosis.csv", mechanism_rows(event_rows))
    write_csv(lab_dir / "output" / "transfer" / "disability_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 2 disability and chronic-conditions lab complete. Outputs "
        "compare onset event-time profiles, diagnose capacity/program/accommodation/"
        "demand/selection channels, and transfer the design to alternative settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
