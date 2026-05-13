from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Worker:
    worker_id: str
    displaced: bool
    baseline_earnings: float
    credit_buffer: float
    neighborhood_risk: float


@dataclass(frozen=True)
class ExposureDay:
    worker_id: str
    day: str
    setting: str
    heat_f: float
    pm25: float
    noise_db: float
    base_output: float
    scheduled_hours: float


@dataclass(frozen=True)
class JobOption:
    job: str
    nominal_wage: float
    rent_cost: float
    commute_minutes: float
    public_safety_risk: float
    workplace_risk: float
    environmental_exposure: float
    amenity_value: float


WORKERS = [
    Worker("W01", True, 720.0, 18.0, 2.5),
    Worker("W02", True, 680.0, 10.0, 3.0),
    Worker("W03", True, 760.0, 28.0, 1.8),
    Worker("W04", True, 700.0, 14.0, 2.2),
    Worker("W05", False, 715.0, 20.0, 2.4),
    Worker("W06", False, 690.0, 13.0, 3.1),
    Worker("W07", False, 745.0, 30.0, 1.7),
    Worker("W08", False, 705.0, 16.0, 2.1),
]

EVENT_TIMES = [-2, -1, 0, 1, 2]

EXPOSURE_DAYS = [
    ExposureDay("W01", "day_1", "moderate", 74.0, 11.0, 53.0, 100.0, 8.0),
    ExposureDay("W01", "day_2", "heat", 91.0, 14.0, 56.0, 100.0, 8.0),
    ExposureDay("W02", "day_1", "pollution", 82.0, 41.0, 58.0, 96.0, 8.0),
    ExposureDay("W02", "day_2", "combined", 94.0, 44.0, 68.0, 96.0, 8.0),
    ExposureDay("W03", "day_1", "moderate", 76.0, 10.0, 52.0, 104.0, 8.0),
    ExposureDay("W03", "day_2", "noise", 80.0, 13.0, 74.0, 104.0, 8.0),
    ExposureDay("W04", "day_1", "heat", 89.0, 15.0, 59.0, 98.0, 8.0),
    ExposureDay("W04", "day_2", "combined", 96.0, 38.0, 71.0, 98.0, 8.0),
]

JOB_OPTIONS = [
    JobOption("downtown_day_shift", 31.0, 15.0, 24.0, 0.8, 0.5, 0.7, 2.0),
    JobOption("warehouse_night_shift", 35.0, 11.0, 42.0, 2.5, 1.2, 2.0, -0.5),
    JobOption("clinic_support", 29.0, 17.0, 20.0, 0.6, 0.4, 0.5, 2.5),
    JobOption("airport_logistics", 34.0, 12.0, 48.0, 1.8, 0.9, 1.8, 0.2),
    JobOption("call_center", 27.0, 14.0, 28.0, 0.9, 0.7, 1.1, 1.4),
]


def worker_month(worker: Worker, event_time: int) -> dict[str, float | int | str]:
    post = event_time >= 0
    displaced_loss = 250.0 if worker.displaced and post else 0.0
    reemployment_recovery = 55.0 * event_time if worker.displaced and event_time > 0 else 0.0
    common_trend = 12.0 * event_time
    earnings = worker.baseline_earnings + common_trend - displaced_loss + reemployment_recovery
    legal_opportunity = 0.10 * earnings + 1.8 * worker.credit_buffer - 5.0 * worker.neighborhood_risk
    credit_stress = max(
        0.0,
        42.0
        - worker.credit_buffer
        + (95.0 if worker.displaced and post else 0.0)
        - 0.035 * earnings,
    )
    crime_risk_index = (
        7.0
        + 0.055 * max(0.0, 720.0 - earnings)
        + 0.10 * credit_stress
        + 1.4 * worker.neighborhood_risk
        - 0.09 * legal_opportunity
    )
    return {
        "worker_id": worker.worker_id,
        "displaced": int(worker.displaced),
        "event_time": event_time,
        "formal_earnings": round(earnings, 2),
        "legal_opportunity_index": round(legal_opportunity, 2),
        "credit_stress_index": round(credit_stress, 2),
        "crime_risk_index": round(crime_risk_index, 2),
    }


def average(values: list[float]) -> float:
    return sum(values) / len(values)


def event_study_rows() -> list[dict[str, object]]:
    individual_rows = [
        worker_month(worker, event_time)
        for worker in WORKERS
        for event_time in EVENT_TIMES
    ]
    baseline_diff: dict[str, float] = {}
    rows: list[dict[str, object]] = []
    for event_time in EVENT_TIMES:
        displaced_rows = [
            row
            for row in individual_rows
            if row["event_time"] == event_time and row["displaced"] == 1
        ]
        comparison_rows = [
            row
            for row in individual_rows
            if row["event_time"] == event_time and row["displaced"] == 0
        ]
        summary: dict[str, object] = {"event_time": event_time}
        for variable in [
            "formal_earnings",
            "legal_opportunity_index",
            "credit_stress_index",
            "crime_risk_index",
        ]:
            displaced_average = average([float(row[variable]) for row in displaced_rows])
            comparison_average = average([float(row[variable]) for row in comparison_rows])
            diff = displaced_average - comparison_average
            if event_time == -1:
                baseline_diff[variable] = diff
            summary[f"displaced_{variable}"] = round(displaced_average, 2)
            summary[f"comparison_{variable}"] = round(comparison_average, 2)
            summary[f"diff_{variable}"] = round(diff, 2)
            summary[f"did_vs_event_minus_1_{variable}"] = round(
                diff - baseline_diff.get(variable, diff), 2
            )
        summary["interpretation"] = "synthetic_event_study_not_official_replication"
        rows.append(summary)
    return rows


def diagnosis_rows() -> list[dict[str, str]]:
    return [
        {
            "claim": "Job loss increases crime through lower legal opportunity.",
            "direction": "labor_to_crime",
            "labor_object": "formal_earnings_and_job_access",
            "counterfactual": "same worker without displacement at the event date",
            "main_threat": "job loss also changes credit, stress, networks, and enforcement exposure",
        },
        {
            "claim": "Unsafe commuting routes reduce willingness to accept late shifts.",
            "direction": "risk_to_labor",
            "labor_object": "feasible_shift_set",
            "counterfactual": "same wage and job with lower route risk",
            "main_threat": "route risk may be correlated with transit time and local demand",
        },
        {
            "claim": "Workplace harassment pushes workers out of high-wage occupations.",
            "direction": "workplace_risk_to_sorting",
            "labor_object": "retention_and_occupational_choice",
            "counterfactual": "same worker in a workplace with lower harassment risk",
            "main_threat": "complaints measure reporting behavior as well as exposure",
        },
        {
            "claim": "Pollution lowers output while workers remain employed.",
            "direction": "environment_to_productivity",
            "labor_object": "within_worker_task_output",
            "counterfactual": "same worker and task under lower exposure",
            "main_threat": "workers may select out of high-exposure shifts or tasks",
        },
        {
            "claim": "A risky job pays more, so workers are fully compensated.",
            "direction": "welfare_interpretation",
            "labor_object": "risk_adjusted_value_not_wage_only",
            "counterfactual": "same worker with equal mobility and full risk information",
            "main_threat": "compensation may be incomplete and rents may capitalize safety",
        },
    ]


def exposure_penalty(day: ExposureDay) -> float:
    heat_penalty = max(0.0, day.heat_f - 78.0) * 0.006
    pollution_penalty = max(0.0, day.pm25 - 12.0) * 0.004
    noise_penalty = max(0.0, day.noise_db - 55.0) * 0.003
    return heat_penalty + pollution_penalty + noise_penalty


def environmental_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for day in EXPOSURE_DAYS:
        penalty = exposure_penalty(day)
        predicted_output = day.base_output * (1.0 - penalty)
        predicted_hours = (
            day.scheduled_hours
            - max(0.0, day.heat_f - 88.0) * 0.035
            - max(0.0, day.pm25 - 35.0) * 0.020
        )
        rows.append(
            {
                "worker_id": day.worker_id,
                "day": day.day,
                "setting": day.setting,
                "heat_f": day.heat_f,
                "pm25": day.pm25,
                "noise_db": day.noise_db,
                "scheduled_hours": day.scheduled_hours,
                "predicted_hours": round(max(0.0, predicted_hours), 2),
                "base_output": day.base_output,
                "exposure_penalty": round(penalty, 3),
                "predicted_output": round(predicted_output, 2),
                "interpretation": "environment_to_productivity_transfer",
            }
        )
    return rows


def adjusted_value(job: JobOption) -> float:
    return (
        job.nominal_wage
        - job.rent_cost
        - 0.18 * job.commute_minutes
        - 3.8 * job.public_safety_risk
        - 4.5 * job.workplace_risk
        - 3.2 * job.environmental_exposure
        + job.amenity_value
    )


def job_ranking_rows() -> list[dict[str, object]]:
    by_wage = {
        job.job: rank + 1
        for rank, job in enumerate(
            sorted(JOB_OPTIONS, key=lambda option: option.nominal_wage, reverse=True)
        )
    }
    by_adjusted = {
        job.job: rank + 1
        for rank, job in enumerate(
            sorted(JOB_OPTIONS, key=adjusted_value, reverse=True)
        )
    }
    return [
        {
            "job": job.job,
            "nominal_wage": job.nominal_wage,
            "rent_cost": job.rent_cost,
            "commute_minutes": job.commute_minutes,
            "public_safety_risk": job.public_safety_risk,
            "workplace_risk": job.workplace_risk,
            "environmental_exposure": job.environmental_exposure,
            "amenity_value": job.amenity_value,
            "risk_adjusted_value": round(adjusted_value(job), 2),
            "nominal_wage_rank": by_wage[job.job],
            "risk_adjusted_rank": by_adjusted[job.job],
        }
        for job in JOB_OPTIONS
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    write_csv(
        lab_dir / "output" / "reproduced" / "displacement_crime_event_study.csv",
        event_study_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "risk_mechanism_diagnosis.csv",
        diagnosis_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "environment_productivity_transfer.csv",
        environmental_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "risk_adjusted_job_ranking.csv",
        job_ranking_rows(),
    )
    note = (
        "Synthetic Week 4 lab complete. Outputs distinguish displacement, "
        "mechanism diagnosis, environmental productivity, and risk-adjusted wages.\n"
    )
    (lab_dir / "output" / "reproduced" / "reproduction_note.txt").write_text(
        note, encoding="utf-8"
    )
    print(note.strip())


if __name__ == "__main__":
    main()
