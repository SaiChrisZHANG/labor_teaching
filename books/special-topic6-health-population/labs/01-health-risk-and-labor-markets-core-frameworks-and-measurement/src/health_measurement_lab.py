from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class HealthMeasure:
    name: str
    column: str
    higher_value_meaning: str
    closest_object: str
    main_threat: str


MEASURES = [
    HealthMeasure(
        "latent_work_capacity",
        "latent_work_capacity",
        "better capacity",
        "work capacity and feasible set",
        "unobserved in most real data",
    ),
    HealthMeasure(
        "self_reported_poor_health",
        "self_reported_poor_health",
        "worse health",
        "private information on function, pain, and fatigue",
        "reporting heterogeneity and justification bias",
    ),
    HealthMeasure(
        "diagnosed_condition_severity",
        "diagnosed_condition_severity",
        "worse health",
        "clinically recognized condition burden",
        "misses undiagnosed conditions and task feasibility",
    ),
    HealthMeasure(
        "biomarker_risk",
        "biomarker_risk",
        "worse health",
        "objective risk and physiological severity",
        "may be distant from day-to-day work capacity",
    ),
    HealthMeasure(
        "administrative_disability_status",
        "administrative_disability_status",
        "worse health",
        "health plus program classification",
        "blends health, rules, applications, and incentives",
    ),
    HealthMeasure(
        "mortality_risk_proxy",
        "mortality_risk_proxy",
        "worse health",
        "severe underlying risk",
        "weak for nonfatal functional constraints",
    ),
    HealthMeasure(
        "mental_health_burden",
        "mental_health_burden",
        "worse health",
        "latent mental health, stress, and functioning",
        "stigma, underreporting, and reverse causality",
    ),
    HealthMeasure(
        "treatment_access",
        "treatment_access",
        "better access",
        "insurance-linked recovery and care access",
        "jointly determined with employment and job quality",
    ),
]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def synthetic_workers() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for idx in range(1, 121):
        age = 50 + (idx % 16)
        education_years = 10 + ((idx * 3) % 9)
        ses_index = round(clamp(0.18 + 0.055 * (education_years - 10) + 0.04 * (idx % 5)), 3)
        physical_demand = [0.15, 0.35, 0.55, 0.75, 0.9][idx % 5]
        chronic_load = ((idx * 7) % 11) / 10
        mental_burden = ((idx * 5 + 3) % 10) / 10
        severe_event = 1 if idx % 23 == 0 or idx % 37 == 0 else 0
        insured = 1 if ses_index > 0.42 or idx % 7 in (0, 1, 2) else 0
        treatment_access = 1 if insured and (ses_index > 0.48 or idx % 4 != 0) else 0

        diagnosis_score = clamp(0.20 + 0.55 * chronic_load + 0.18 * severe_event - 0.08 * treatment_access)
        biomarker_risk = clamp(0.12 + 0.48 * chronic_load + 0.24 * severe_event + 0.12 * (age - 50) / 15)
        latent_capacity = clamp(
            0.93
            - 0.34 * chronic_load
            - 0.22 * mental_burden
            - 0.20 * severe_event
            - 0.06 * physical_demand
            + 0.12 * treatment_access
            + 0.08 * ses_index
        )
        employment_propensity = clamp(
            0.10
            + 0.88 * latent_capacity
            - 0.20 * physical_demand
            - 0.10 * mental_burden
            + 0.06 * ses_index
        )
        employment_threshold = [0.42, 0.48, 0.53, 0.58][idx % 4]
        employed = 1 if employment_propensity > employment_threshold else 0
        self_reported_poor = 1 if (1 - latent_capacity + 0.13 * (1 - employed) + 0.10 * mental_burden) > 0.46 else 0
        administrative_disability = 1 if latent_capacity < 0.46 and diagnosis_score > 0.48 and employed == 0 else 0
        mortality_risk = clamp(0.08 + 0.36 * biomarker_risk + 0.20 * severe_event + 0.06 * (age - 50) / 15)
        feasible_jobs = max(0, round(7 * latent_capacity + 1.5 * treatment_access - 2.5 * physical_demand))
        hours = 0.0
        if employed:
            hours = clamp(
                16
                + 26 * latent_capacity
                - 5.5 * physical_demand
                - 3.0 * mental_burden
                + 2.0 * treatment_access,
                8,
                45,
            )
        wage_index = clamp(0.55 + 0.32 * ses_index + 0.12 * latent_capacity - 0.05 * physical_demand)

        rows.append(
            {
                "worker_id": f"worker_{idx:03d}",
                "age": age,
                "education_years": education_years,
                "ses_index": round(ses_index, 3),
                "physical_demand": round(physical_demand, 3),
                "latent_work_capacity": round(latent_capacity, 3),
                "self_reported_poor_health": self_reported_poor,
                "diagnosed_condition_severity": round(diagnosis_score, 3),
                "biomarker_risk": round(biomarker_risk, 3),
                "administrative_disability_status": administrative_disability,
                "mortality_risk_proxy": round(mortality_risk, 3),
                "mental_health_burden": round(mental_burden, 3),
                "insured": insured,
                "treatment_access": treatment_access,
                "employed": employed,
                "hours": round(hours, 2),
                "feasible_jobs": feasible_jobs,
                "wage_index": round(wage_index, 3),
            }
        )
    return rows


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Cannot take mean of an empty list")
    return sum(values) / len(values)


def slope(x_values: list[float], y_values: list[float]) -> float:
    x_bar = mean(x_values)
    y_bar = mean(y_values)
    numerator = sum((x - x_bar) * (y - y_bar) for x, y in zip(x_values, y_values))
    denominator = sum((x - x_bar) ** 2 for x in x_values)
    if abs(denominator) < 1e-12:
        return 0.0
    return numerator / denominator


def residualize(values: list[float], control: list[float]) -> list[float]:
    fitted_slope = slope(control, values)
    intercept = mean(values) - fitted_slope * mean(control)
    return [value - (intercept + fitted_slope * c) for value, c in zip(values, control)]


def adjusted_slope(x_values: list[float], y_values: list[float], control: list[float]) -> float:
    return slope(residualize(x_values, control), residualize(y_values, control))


def correlation(x_values: list[float], y_values: list[float]) -> float:
    x_bar = mean(x_values)
    y_bar = mean(y_values)
    numerator = sum((x - x_bar) * (y - y_bar) for x, y in zip(x_values, y_values))
    x_ss = sum((x - x_bar) ** 2 for x in x_values)
    y_ss = sum((y - y_bar) ** 2 for y in y_values)
    if x_ss <= 0 or y_ss <= 0:
        return 0.0
    return numerator / (x_ss * y_ss) ** 0.5


def column(rows: list[dict[str, object]], name: str) -> list[float]:
    return [float(row[name]) for row in rows]


def labor_gradient_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    employed = column(rows, "employed")
    hours = column(rows, "hours")
    feasible_jobs = column(rows, "feasible_jobs")
    ses = column(rows, "ses_index")
    output: list[dict[str, object]] = []
    for measure in MEASURES:
        x_values = column(rows, measure.column)
        output.append(
            {
                "measure": measure.name,
                "higher_value_meaning": measure.higher_value_meaning,
                "employment_slope": round(slope(x_values, employed), 4),
                "employment_ses_adjusted_slope": round(adjusted_slope(x_values, employed, ses), 4),
                "hours_slope": round(slope(x_values, hours), 4),
                "feasible_jobs_slope": round(slope(x_values, feasible_jobs), 4),
                "interpretation": interpretation_label(measure),
            }
        )
    return output


def interpretation_label(measure: HealthMeasure) -> str:
    if measure.name == "latent_work_capacity":
        return "benchmark_unobserved_capacity_gradient"
    if measure.name == "administrative_disability_status":
        return "program_status_blends_health_and_incentives"
    if measure.name == "treatment_access":
        return "access_margin_can_reflect_job_lock_or_recovery"
    if measure.name == "self_reported_poor_health":
        return "private_information_plus_reporting_bias"
    return "health_proxy_requires_measurement_diagnosis"


def diagnostic_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    capacity = column(rows, "latent_work_capacity")
    ses = column(rows, "ses_index")
    output: list[dict[str, object]] = []
    for measure in MEASURES:
        x_values = column(rows, measure.column)
        output.append(
            {
                "measure": measure.name,
                "closest_object": measure.closest_object,
                "main_threat": measure.main_threat,
                "corr_with_latent_capacity": round(correlation(x_values, capacity), 3),
                "corr_with_ses": round(correlation(x_values, ses), 3),
                "diagnostic_question": diagnostic_question(measure.name),
            }
        )
    return output


def diagnostic_question(measure_name: str) -> str:
    questions = {
        "latent_work_capacity": "What would be required to observe this object in real data?",
        "self_reported_poor_health": "Is reporting shaped by employment status or benefit application?",
        "diagnosed_condition_severity": "Who is diagnosed, and what severity or function remains hidden?",
        "biomarker_risk": "Does the biomarker predict the actual task and schedule constraint?",
        "administrative_disability_status": "How much is health and how much is program screening?",
        "mortality_risk_proxy": "Does severe risk proxy for routine work capacity?",
        "mental_health_burden": "What stigma, treatment, and workplace feedback remain unmeasured?",
        "treatment_access": "Is access a recovery input, a job amenity, or both?",
    }
    return questions[measure_name]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "acute_hospitalization",
            "health_object": "hospital admission as severe health shock",
            "labor_margin": "employment and hours before versus after shock",
            "identification_logic": "event-time comparison with matched nonshocked workers",
            "main_remaining_threat": "pre-trends and unobserved severity",
            "student_task": "separate immediate work-capacity loss from insurance and employer retention responses",
        },
        {
            "scenario": "disability_onset",
            "health_object": "administrative disability entry",
            "labor_margin": "labor-force exit, earnings, and consumption",
            "identification_logic": "onset timing or examiner/threshold variation",
            "main_remaining_threat": "program rules and application selection",
            "student_task": "explain why disability status is not pure health",
        },
        {
            "scenario": "mental_health_treatment",
            "health_object": "treatment start or symptom scale",
            "labor_margin": "attendance, hours, retention, and productivity",
            "identification_logic": "timing around access expansion or provider availability",
            "main_remaining_threat": "stigma, underreporting, and treatment selection",
            "student_task": "state which latent condition and workplace margin are visible",
        },
        {
            "scenario": "insurance_linked_treatment_access",
            "health_object": "coverage and treatment access",
            "labor_margin": "job lock, mobility, recovery, and hours",
            "identification_logic": "policy threshold, coverage change, or employer benefit variation",
            "main_remaining_threat": "coverage changes both health and job incentives",
            "student_task": "separate recovery from job-lock and compensation-package channels",
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
    rows = synthetic_workers()

    write_csv(lab_dir / "original" / "reduced" / "health_measurement_synthetic.csv", rows)
    write_csv(lab_dir / "output" / "reproduced" / "health_measure_labor_gradient.csv", labor_gradient_rows(rows))
    write_csv(lab_dir / "output" / "diagnosed" / "measurement_bias_diagnostics.csv", diagnostic_rows(rows))
    write_csv(lab_dir / "output" / "transfer" / "health_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 1 health measurement lab complete. Outputs compare "
        "latent capacity, self-reported health, clinical/objective proxies, "
        "administrative disability status, mental health, and treatment access.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
