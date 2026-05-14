from __future__ import annotations

import csv
from pathlib import Path


EVENT_TIMES = list(range(-3, 6))


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def synthetic_panel() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for household_num in range(1, 73):
        treated = 1 if household_num <= 48 else 0
        focal_age_at_event = 34 + ((household_num * 3) % 34)
        spouse_age_at_event = focal_age_at_event + ((household_num % 7) - 3)
        has_young_child = 1 if household_num % 5 in (0, 1) else 0
        baseline_assets = 45_000 + 7_500 * (household_num % 9) + 1_800 * max(focal_age_at_event - 45, 0)
        job_flexibility = [0.25, 0.40, 0.55, 0.72, 0.88][household_num % 5]
        baseline_wage = 0.72 + 0.012 * (household_num % 13) + 0.002 * max(focal_age_at_event - 35, 0)
        shock_severity = clamp(0.38 + 0.055 * (household_num % 7) + 0.12 * (1 - job_flexibility))

        for event_time in EVENT_TIMES:
            post = 1 if event_time >= 0 else 0
            focal_age = focal_age_at_event + event_time
            pension_eligible = 1 if focal_age >= 62 else 0
            late_career = 1 if focal_age >= 58 else 0
            anticipation = treated * (1 if event_time == -1 and shock_severity > 0.68 else 0)

            care_intensity = 0.0
            mortality_risk = 0.02 + 0.004 * max(focal_age - 50, 0)
            if treated and post:
                care_intensity = clamp(0.42 + 0.10 * max(event_time, 0) + 0.30 * shock_severity, 0.0, 1.0)
                mortality_risk = clamp(mortality_risk + 0.28 * shock_severity + 0.04 * max(event_time, 0), 0.0, 0.95)
            elif anticipation:
                care_intensity = 0.10
                mortality_risk = clamp(mortality_risk + 0.12, 0.0, 0.95)

            informal_care_hours = 0.0
            if treated:
                informal_care_hours = 2.0 * anticipation + post * (5.0 + 10.0 * care_intensity + 1.8 * has_young_child)

            income_replacement_push = 3.5 * post * treated * (1 - care_intensity)
            care_time_pull = 8.0 * post * treated * care_intensity * (1 - 0.55 * job_flexibility)
            retirement_pull = 5.5 * post * treated * pension_eligible * (care_intensity + 0.4 * shock_severity)
            child_time_pull = 1.6 * has_young_child
            focal_hours = (
                36.0
                + 0.10 * (focal_age_at_event - 45)
                + 2.2 * job_flexibility
                - child_time_pull
                + income_replacement_push
                - care_time_pull
                - retirement_pull
                - 1.8 * anticipation
            )
            focal_hours = clamp(focal_hours, 0.0, 46.0)

            spouse_capacity_loss = 0.0
            if treated and post:
                spouse_capacity_loss = 10.0 * shock_severity + 1.8 * max(event_time, 0)
            spouse_hours = clamp(34.0 - 1.2 * has_young_child - spouse_capacity_loss, 0.0, 44.0)

            flexible_job_switch = 1 if treated and post and job_flexibility < 0.55 and care_intensity > 0.55 and event_time >= 1 else 0
            retirement_claiming = 1 if pension_eligible and treated and post and care_intensity > 0.62 and baseline_assets < 105_000 else 0
            bridge_job_transition = 1 if late_career and treated and event_time >= 2 and job_flexibility >= 0.55 and care_intensity > 0.60 else 0
            post_retirement_work = 1 if retirement_claiming and job_flexibility >= 0.55 and event_time >= 2 else 0

            if retirement_claiming and not post_retirement_work:
                focal_hours = min(focal_hours, 8.0)
            elif bridge_job_transition:
                focal_hours = min(focal_hours, 24.0)

            focal_earnings = focal_hours * baseline_wage * 52
            spouse_earnings = spouse_hours * (baseline_wage * 0.86) * 52
            household_earnings = focal_earnings + spouse_earnings
            savings_drawdown = max(
                0.0,
                treated
                * post
                * (
                    1_800
                    + 2_250 * care_intensity
                    + 1_100 * shock_severity
                    - 1_600 * pension_eligible
                    - 950 * job_flexibility
                ),
            )
            retirement_savings_index = max(0.0, (baseline_assets - 2_400 * max(event_time, 0) * treated * post) / 100_000)

            rows.append(
                {
                    "household_id": f"household_{household_num:03d}",
                    "treated_family_shock": treated,
                    "event_time": event_time,
                    "focal_age": focal_age,
                    "spouse_age": spouse_age_at_event + event_time,
                    "has_young_child": has_young_child,
                    "pension_eligible": pension_eligible,
                    "baseline_assets": round(baseline_assets, 2),
                    "retirement_savings_index": round(retirement_savings_index, 3),
                    "job_flexibility": round(job_flexibility, 3),
                    "shock_severity": round(shock_severity, 3),
                    "mortality_risk": round(mortality_risk, 3),
                    "care_intensity": round(care_intensity, 3),
                    "informal_care_hours": round(informal_care_hours, 2),
                    "focal_hours": round(focal_hours, 2),
                    "spouse_hours": round(spouse_hours, 2),
                    "household_earnings_index": round(household_earnings, 2),
                    "savings_drawdown": round(savings_drawdown, 2),
                    "flexible_job_switch": flexible_job_switch,
                    "retirement_claiming": retirement_claiming,
                    "bridge_job_transition": bridge_job_transition,
                    "post_retirement_work": post_retirement_work,
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
        if int(row["event_time"]) == event_time and int(row["treated_family_shock"]) == treated
    ]


def event_study_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    outcomes = [
        "mortality_risk",
        "care_intensity",
        "informal_care_hours",
        "focal_hours",
        "spouse_hours",
        "household_earnings_index",
        "savings_drawdown",
        "flexible_job_switch",
        "retirement_claiming",
        "bridge_job_transition",
        "post_retirement_work",
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
        care_gap = float(row["treated_minus_comparison_informal_care_hours"])
        focal_hours_gap = float(row["treated_minus_comparison_focal_hours"])
        spouse_hours_gap = float(row["treated_minus_comparison_spouse_hours"])
        earnings_gap = float(row["treated_minus_comparison_household_earnings_index"])
        savings_gap = float(row["treated_minus_comparison_savings_drawdown"])
        flexibility_gap = float(row["treated_minus_comparison_flexible_job_switch"])
        retirement_gap = float(row["treated_minus_comparison_retirement_claiming"])
        bridge_gap = float(row["treated_minus_comparison_bridge_job_transition"])
        post_retirement_gap = float(row["treated_minus_comparison_post_retirement_work"])

        if event_time < 0 and care_gap > 0:
            phase = "anticipation_window"
            dominant_channel = "dynamic_selection_and_anticipation"
            diagnostic = "Pre-shock movement suggests expected decline or early care needs."
        elif event_time < 0:
            phase = "pre_shock_balance_window"
            dominant_channel = "selection_and_pre_trends"
            diagnostic = "Check whether treated and comparison households were already diverging."
        elif event_time in (0, 1) and focal_hours_gap < -2.0:
            phase = "short_run_care_disruption"
            dominant_channel = "care_time_demand"
            diagnostic = "Care hours rise faster than any income-replacement labor response."
        elif event_time in (0, 1) and focal_hours_gap >= -2.0:
            phase = "short_run_income_replacement"
            dominant_channel = "income_replacement"
            diagnostic = "The household preserves or raises work while absorbing the shock."
        elif retirement_gap > 0.10:
            phase = "retirement_and_pension_response"
            dominant_channel = "pension_or_benefit_incentives"
            diagnostic = "Retirement claiming moves with care needs and late-career age."
        elif bridge_gap > 0.08 or post_retirement_gap > 0.08:
            phase = "late_life_work_reallocation"
            dominant_channel = "bridge_jobs_and_post_retirement_work"
            diagnostic = "Flexible late-life work cushions complete exit."
        elif flexibility_gap > 0.12:
            phase = "job_flexibility_response"
            dominant_channel = "flexible_job_switching"
            diagnostic = "Workers adjust the job rather than only hours or participation."
        else:
            phase = "medium_run_household_reallocation"
            dominant_channel = "mixed_care_income_and_savings_response"
            diagnostic = "Persistent gaps mix care demand, savings, job flexibility, and selection."

        output.append(
            {
                "event_time": event_time,
                "phase": phase,
                "dominant_channel": dominant_channel,
                "informal_care_hours_gap": round(care_gap, 3),
                "focal_hours_gap": round(focal_hours_gap, 3),
                "spouse_hours_gap": round(spouse_hours_gap, 3),
                "household_earnings_gap": round(earnings_gap, 3),
                "savings_drawdown_gap": round(savings_gap, 3),
                "retirement_claiming_gap": round(retirement_gap, 3),
                "bridge_job_gap": round(bridge_gap, 3),
                "post_retirement_work_gap": round(post_retirement_gap, 3),
                "diagnostic_question": diagnostic,
            }
        )
    return output


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "scenario": "fertility_timing_child_penalty",
            "event_or_state": "first birth or child age relative to career stage",
            "labor_margin": "hours, earnings, occupation, promotion timing, mobility, and household specialization",
            "identifying_variation": "birth event timing, sibling timing, fertility-treatment variation, or policy timing",
            "visible_channel": "timing of care demand and experience accumulation",
            "remaining_threat": "fertility timing is selected and may be anticipated by job choice",
        },
        {
            "scenario": "caregiving_onset",
            "event_or_state": "parent, spouse, or elder care need crossing an intensity threshold",
            "labor_margin": "hours, participation, flexible jobs, location, and retirement timing",
            "identifying_variation": "linked family health timing, leave eligibility, formal-care access, or distance shocks",
            "visible_channel": "care-time demand and job-feasibility constraint",
            "remaining_threat": "care intensity, emotional load, and informal substitutes are partly hidden",
        },
        {
            "scenario": "pension_eligibility_reform",
            "event_or_state": "public or employer pension eligibility age, benefit accrual, or earnings-test reform",
            "labor_margin": "claiming, exit timing, partial retirement, savings, and reentry",
            "identifying_variation": "cohort rules, eligibility discontinuities, or reform timing",
            "visible_channel": "incentive effect on late-life labor supply",
            "remaining_threat": "health, labor demand, and care needs may move at the same ages",
        },
        {
            "scenario": "bridge_job_rehire_flexible_work",
            "event_or_state": "transition from career job to bridge job, rehire, part-time role, or post-retirement work",
            "labor_margin": "older-worker attachment, hours, job quality, and welfare",
            "identifying_variation": "employer flexibility, occupation tasks, pension rules, or phased-retirement policy",
            "visible_channel": "job-design margin that prevents full exit",
            "remaining_threat": "workers with stronger preferences or better health select into flexible jobs",
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

    write_csv(lab_dir / "original" / "reduced" / "lifecycle_family_shocks_synthetic.csv", panel)
    write_csv(lab_dir / "output" / "reproduced" / "family_health_shock_event_study.csv", event_rows)
    write_csv(lab_dir / "output" / "diagnosed" / "lifecycle_mechanism_diagnosis.csv", mechanism_rows(event_rows))
    write_csv(lab_dir / "output" / "transfer" / "lifecycle_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 3 lifecycle labor-allocation lab complete. Outputs compare "
        "family health-shock event-time profiles, diagnose care/income/pension/"
        "flexibility/selection channels, and transfer the design to fertility, "
        "caregiving, pension, and bridge-job settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
