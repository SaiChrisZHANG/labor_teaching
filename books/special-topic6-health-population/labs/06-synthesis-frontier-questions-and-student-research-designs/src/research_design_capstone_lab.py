from __future__ import annotations

import csv
from pathlib import Path


EVENT_YEARS = list(range(-3, 6))


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def synthetic_panel() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for worker_num in range(1, 181):
        affected = 1 if worker_num % 3 != 0 else 0
        baseline_capacity = clamp(0.92 - 0.012 * (worker_num % 8) + 0.008 * (worker_num % 5), 0.60, 1.0)
        baseline_wage = 0.78 + 0.045 * (worker_num % 9)
        firm_accommodation_capacity = clamp(0.20 + 0.08 * ((worker_num + 2) % 8))
        household_buffer = clamp(0.18 + 0.07 * ((worker_num + 5) % 7))
        program_access = clamp(0.12 + 0.09 * ((worker_num + 3) % 6))
        high_skill_job = 1 if worker_num % 5 in (0, 1) else 0
        flexible_job = 1 if worker_num % 4 in (0, 2) else 0

        for event_year in EVENT_YEARS:
            post_onset = 1 if event_year >= 0 else 0
            anticipation = 1 if event_year == -1 and affected else 0
            severity = 0.0
            if affected:
                severity = clamp(
                    0.08 * anticipation
                    + post_onset * (0.34 + 0.035 * min(event_year, 4) + 0.02 * (worker_num % 4))
                )

            accommodation = 0
            if affected and event_year >= 1:
                accommodation = 1 if firm_accommodation_capacity + 0.18 * flexible_job + 0.10 * high_skill_job > 0.62 else 0

            benefit_receipt = 0
            if affected and event_year >= 2:
                benefit_receipt = 1 if program_access + severity - 0.16 * accommodation > 0.62 else 0

            job_mobility = clamp(
                0.035
                + 0.14 * severity
                + 0.06 * post_onset * (1 - flexible_job)
                - 0.04 * accommodation
                + 0.015 * max(event_year, 0)
            )
            capacity_index = clamp(
                baseline_capacity
                - 0.48 * severity
                + 0.08 * accommodation
                - 0.03 * benefit_receipt
            )
            employment = clamp(
                0.92
                - 0.50 * severity
                + 0.11 * accommodation
                - 0.18 * benefit_receipt
                - 0.06 * job_mobility
                + 0.04 * flexible_job
            )
            hours = max(
                0.0,
                38.0
                - 18.0 * severity
                + 3.6 * accommodation
                - 5.4 * benefit_receipt
                + 2.2 * flexible_job
            )
            earnings = max(
                0.0,
                100.0
                * baseline_wage
                * employment
                * (hours / 38.0)
                * (1.0 + 0.018 * event_year + 0.05 * high_skill_job)
            )
            transfers = 18.0 * benefit_receipt + 3.5 * household_buffer * post_onset
            consumption = max(0.0, 52.0 + 0.42 * earnings + transfers - 7.5 * severity + 2.0 * household_buffer)
            welfare_index = clamp(
                0.86
                - 0.36 * severity
                + 0.09 * accommodation
                + 0.08 * household_buffer
                - 0.05 * benefit_receipt
                - 0.05 * job_mobility
            )

            rows.append(
                {
                    "worker_id": f"worker_{worker_num:03d}",
                    "event_year": event_year,
                    "affected": affected,
                    "baseline_capacity": round(baseline_capacity, 3),
                    "firm_accommodation_capacity": round(firm_accommodation_capacity, 3),
                    "household_buffer": round(household_buffer, 3),
                    "program_access": round(program_access, 3),
                    "high_skill_job": high_skill_job,
                    "flexible_job": flexible_job,
                    "severity": round(severity, 3),
                    "capacity_index": round(capacity_index, 3),
                    "accommodation": accommodation,
                    "benefit_receipt": benefit_receipt,
                    "job_mobility": round(job_mobility, 3),
                    "employment": round(employment, 3),
                    "hours": round(hours, 3),
                    "earnings": round(earnings, 3),
                    "consumption": round(consumption, 3),
                    "welfare_index": round(welfare_index, 3),
                }
            )
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def mean_for(rows: list[dict[str, object]], event_year: int, affected: int, outcome: str) -> float:
    return mean(
        [
            float(row[outcome])
            for row in rows
            if int(row["event_year"]) == event_year and int(row["affected"]) == affected
        ]
    )


def profile_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    outcomes = [
        "severity",
        "capacity_index",
        "employment",
        "hours",
        "earnings",
        "consumption",
        "accommodation",
        "benefit_receipt",
        "job_mobility",
        "welfare_index",
    ]
    output: list[dict[str, object]] = []
    for event_year in EVENT_YEARS:
        item: dict[str, object] = {"event_year": event_year}
        for outcome in outcomes:
            affected_mean = mean_for(rows, event_year, 1, outcome)
            reference_mean = mean_for(rows, event_year, 0, outcome)
            pre_affected = mean_for(rows, -1, 1, outcome)
            pre_reference = mean_for(rows, -1, 0, outcome)
            item[f"affected_{outcome}"] = round(affected_mean, 3)
            item[f"reference_{outcome}"] = round(reference_mean, 3)
            item[f"diff_{outcome}"] = round(affected_mean - reference_mean, 3)
            item[f"event_study_{outcome}"] = round((affected_mean - pre_affected) - (reference_mean - pre_reference), 3)
        output.append(item)
    return output


def row_for(profile: list[dict[str, object]], event_year: int) -> dict[str, object]:
    return next(row for row in profile if int(row["event_year"]) == event_year)


def diagnosis_rows(profile: list[dict[str, object]]) -> list[dict[str, object]]:
    shock = row_for(profile, 0)
    medium = row_for(profile, 2)
    long = row_for(profile, 5)

    comparisons = [
        (
            "capacity_loss_at_onset",
            float(shock["event_study_capacity_index"]),
            "work_capacity_effect",
            "The immediate drop in capacity identifies the onset object, but not whether work conditions also caused health decline.",
        ),
        (
            "employment_and_hours_path",
            float(long["event_study_employment"]) - float(shock["event_study_employment"]),
            "dynamic_labor_supply_and_selection",
            "Employment and hours keep changing after onset, so a one-year estimate misses adaptation, exit, and selection.",
        ),
        (
            "accommodation_response",
            float(medium["event_study_accommodation"]),
            "firm_response",
            "Accommodation rises after onset, but worker-only data would not reveal which firms can retain constrained workers.",
        ),
        (
            "benefit_receipt_response",
            float(long["event_study_benefit_receipt"]),
            "program_incentives_and_insurance",
            "Benefit receipt protects income for some workers while also changing labor supply incentives and observed attachment.",
        ),
        (
            "consumption_vs_earnings",
            float(long["event_study_consumption"]) - float(long["event_study_earnings"]),
            "household_insurance",
            "Consumption falls less than earnings when transfers and household buffers partially insure the shock.",
        ),
        (
            "welfare_beyond_earnings",
            float(long["event_study_welfare_index"]) - 0.01 * float(long["event_study_earnings"]),
            "hidden_welfare_incidence",
            "Welfare captures capacity loss, flexibility, benefits, mobility, and accommodation, not only earnings.",
        ),
    ]

    return [
        {
            "diagnostic_margin": name,
            "event_study_signal": round(value, 3),
            "dominant_issue": issue,
            "design_lesson": lesson,
        }
        for name, value, issue, lesson in comparisons
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "mental_health_treatment_and_retention",
            "mechanism": "treatment access, disclosure, stigma, and job design",
            "labor_object": "retention, absenteeism, presenteeism, productivity, and worker welfare",
            "unit": "worker-by-firm panel",
            "timing": "waiting-list, policy, or provider-access shock",
            "counterfactual": "similar workers before access or in lower-access firms/places",
            "main_threat": "treatment take-up and disclosure are selected on severity, stigma, and job quality",
            "welfare_object": "symptom burden, job quality, stigma, productivity, and retention",
        },
        {
            "scenario": "caregiving_onset_and_older_worker_flexibility",
            "mechanism": "parent or spouse care need interacting with schedule flexibility",
            "labor_object": "hours, job switching, retirement, and late-career earnings",
            "unit": "worker-household panel",
            "timing": "care onset, hospitalization, or long-term-care entry",
            "counterfactual": "pre-onset path and matched households without care onset",
            "main_threat": "care needs may be anticipated and correlated with family resources",
            "welfare_object": "earnings, care time, stress, retirement distortion, and family insurance",
        },
        {
            "scenario": "disease_exposure_and_migration",
            "mechanism": "local disease exposure plus remote-work and housing constraints",
            "labor_object": "migration, employment, hours, sector switching, and wage incidence",
            "unit": "worker-by-place or occupation-by-place panel",
            "timing": "epidemic wave, policy phase, or exposure gradient",
            "counterfactual": "less exposed places or occupations with similar pre-trends",
            "main_threat": "migration changes the composition of observed workers and places",
            "welfare_object": "risk, family care, immobility, job amenities, and local opportunity",
        },
        {
            "scenario": "heat_exposure_and_productivity",
            "mechanism": "temperature and fatigue interacting with task demands",
            "labor_object": "output, hours, absences, safety, shift timing, and capital substitution",
            "unit": "worker-establishment-day panel",
            "timing": "daily heat variation and adaptation over seasons",
            "counterfactual": "same workers or establishments on cooler comparable days",
            "main_threat": "seasonality, product demand, avoidance, and firm adaptation",
            "welfare_object": "fatigue, injury risk, recovery time, and unsafe amenities",
        },
        {
            "scenario": "aging_automation_and_accommodation",
            "mechanism": "older-worker health constraints and demographic pressure",
            "labor_object": "automation, vacancies, retirement, retention, wages, and job redesign",
            "unit": "firm-by-local-labor-market panel",
            "timing": "cohort aging exposure and technology adoption window",
            "counterfactual": "firms in less exposed local labor markets or industries",
            "main_threat": "technology adoption, migration, and labor scarcity are jointly determined",
            "welfare_object": "late-career feasibility, displacement, accommodation, and care-sector demand",
        },
        {
            "scenario": "firm_accommodation_and_employer_power",
            "mechanism": "accommodation policy, job redesign, and constrained outside options",
            "labor_object": "retention, wages, job lock, productivity, and quits",
            "unit": "linked employer-employee panel",
            "timing": "policy change, accommodation request, or health-shock onset",
            "counterfactual": "similar workers in firms with different accommodation capacity",
            "main_threat": "firms may accommodate workers with higher expected productivity",
            "welfare_object": "work capacity, flexibility, bargaining power, and job quality",
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
    diagnosis = diagnosis_rows(profile)
    transfer = transfer_rows()

    write_csv(lab_dir / "original" / "reduced" / "capstone_research_design_synthetic.csv", panel)
    write_csv(lab_dir / "output" / "reproduced" / "disability_onset_research_profile.csv", profile)
    write_csv(lab_dir / "output" / "diagnosed" / "research_design_diagnosis.csv", diagnosis)
    write_csv(lab_dir / "output" / "transfer" / "frontier_design_transfer.csv", transfer)

    note = (
        "Synthetic Week 6 capstone lab complete. Outputs reproduce a disability-onset "
        "research profile, diagnose design objects and failure modes, and transfer the "
        "architecture to frontier health, population, and labor-market settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
