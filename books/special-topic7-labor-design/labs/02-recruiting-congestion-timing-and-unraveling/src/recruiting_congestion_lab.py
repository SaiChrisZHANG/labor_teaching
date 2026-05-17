from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


OCCUPATIONS = [
    "registered_nurse",
    "software_analyst",
    "manufacturing_technician",
    "public_service_caseworker",
    "research_assistant",
    "clinical_fellow",
]

MARKETS = [
    "gastroenterology_like_fellowships",
    "clinical_psychology_internships",
    "law_clerkships",
    "entry_level_professional_services",
]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def group_for_intensity(value: float) -> str:
    if value < 0.45:
        return "low_recruiting_intensity"
    if value < 0.70:
        return "middle_recruiting_intensity"
    return "high_recruiting_intensity"


def recruiting_funnel_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number in range(1, 97):
        occupation = OCCUPATIONS[number % len(OCCUPATIONS)]
        market = ["metro", "regional", "rural", "remote"][number % 4]
        wage_index = clamp(0.35 + ((number * 17) % 54) / 100)
        wage_transparent = 1 if number % 4 in (0, 1) else 0
        recruiting_intensity = clamp(0.24 + ((number * 7) % 61) / 100 + 0.08 * wage_transparent - 0.05 * (market == "remote"))
        hiring_standard = clamp(0.42 + ((number * 11) % 47) / 100 + 0.04 * (occupation == "clinical_fellow"))
        interview_capacity = 4 + ((number * 3) % 13) + (2 if recruiting_intensity >= 0.70 else 0)
        applications = int(
            24
            + ((number * 19) % 88)
            + 18 * wage_transparent
            + 16 * wage_index
            - 9 * (market == "remote")
            + 7 * (occupation in ("software_analyst", "clinical_fellow"))
        )
        applicant_quality = clamp(0.36 + 0.28 * wage_index + 0.11 * wage_transparent + ((number * 13) % 32) / 100 - applications / 650)
        qualified_share = clamp(0.18 + 0.58 * applicant_quality - 0.30 * hiring_standard)
        qualified_applicants = max(1, int(round(applications * qualified_share)))
        interviews = min(interview_capacity, qualified_applicants)
        offer_probability = clamp(0.22 + 0.48 * recruiting_intensity + 0.17 * wage_index - 0.24 * hiring_standard)
        offers = min(interviews, max(0, int(round(interviews * offer_probability))))
        exploding_offer = 1 if number % 5 in (0, 3) else 0
        offer_hold_days = 2 if exploding_offer else 8 + (number % 4)
        acceptance_probability = clamp(
            0.24
            + 0.34 * wage_index
            + 0.18 * wage_transparent
            + 0.16 * recruiting_intensity
            - 0.16 * exploding_offer
            - 0.06 * (market == "remote")
        )
        hires = min(offers, max(0, int(round(offers * acceptance_probability))))
        vacancy_duration = int(
            max(
                6,
                round(
                    70
                    - 29 * recruiting_intensity
                    - 16 * wage_index
                    - 7 * wage_transparent
                    + 17 * hiring_standard
                    + 9 * exploding_offer
                    + ((number * 5) % 12)
                ),
            )
        )

        rows.append(
            {
                "vacancy_id": f"V{number:03d}",
                "occupation": occupation,
                "market": market,
                "wage_index": round(wage_index, 3),
                "wage_transparent": wage_transparent,
                "recruiting_intensity": round(recruiting_intensity, 3),
                "intensity_group": group_for_intensity(recruiting_intensity),
                "hiring_standard": round(hiring_standard, 3),
                "interview_capacity": interview_capacity,
                "applications": applications,
                "applicant_quality_index": round(applicant_quality, 3),
                "qualified_applicants": qualified_applicants,
                "interviews": interviews,
                "offers": offers,
                "hires": hires,
                "vacancy_filled": int(hires > 0),
                "exploding_offer": exploding_offer,
                "offer_hold_days": offer_hold_days,
                "vacancy_duration_days": vacancy_duration,
                "interview_yield": round(interviews / applications, 4),
                "offer_yield": round(offers / interviews, 4) if interviews else 0,
                "vacancy_yield": round(hires / applications, 4),
            }
        )
    return rows


def timing_regime_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number in range(1, 65):
        market = MARKETS[number % len(MARKETS)]
        prestige_pressure = clamp(0.30 + ((number * 9) % 60) / 100)
        candidate_risk = clamp(0.25 + ((number * 14) % 58) / 100)
        late_information_value = clamp(0.20 + ((number * 5) % 66) / 100)
        for regime in ("decentralized_early_offers", "coordinated_timing"):
            early = regime == "decentralized_early_offers"
            offer_day = 18 + ((number * 3) % 18) if early else 55 + ((number * 2) % 16)
            deadline_days = 1 + (number % 2) if early else 7 + (number % 4)
            information_complete = int(offer_day >= 50)
            accepted_before_signal = int(early and candidate_risk + prestige_pressure > 1.00)
            match_quality = clamp(
                0.45
                + 0.20 * prestige_pressure
                + 0.22 * late_information_value
                + 0.08 * information_complete
                - 0.10 * accepted_before_signal
                - 0.04 * (deadline_days <= 2)
                + ((number * 7) % 9) / 100,
            )
            mobility_probability = clamp(
                0.28
                + 0.18 * information_complete
                - 0.12 * accepted_before_signal
                - 0.08 * early
                + 0.10 * late_information_value
            )
            rows.append(
                {
                    "case_id": f"T{number:03d}",
                    "market": market,
                    "regime": regime,
                    "prestige_pressure": round(prestige_pressure, 3),
                    "candidate_risk": round(candidate_risk, 3),
                    "late_information_value": round(late_information_value, 3),
                    "offer_day": offer_day,
                    "deadline_days": deadline_days,
                    "information_complete": information_complete,
                    "accepted_before_signal": accepted_before_signal,
                    "match_quality_index": round(match_quality, 3),
                    "mobility_probability": round(mobility_probability, 3),
                }
            )
    return rows


def summarize_recruiting(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["intensity_group"])].append(row)

    output: list[dict[str, object]] = []
    for group in ("low_recruiting_intensity", "middle_recruiting_intensity", "high_recruiting_intensity"):
        group_rows = grouped[group]
        output.append(
            {
                "intensity_group": group,
                "vacancies": len(group_rows),
                "mean_applications": round(safe_mean([float(row["applications"]) for row in group_rows]), 3),
                "mean_applicant_quality_index": round(safe_mean([float(row["applicant_quality_index"]) for row in group_rows]), 3),
                "mean_interviews": round(safe_mean([float(row["interviews"]) for row in group_rows]), 3),
                "mean_interview_yield": round(safe_mean([float(row["interview_yield"]) for row in group_rows]), 4),
                "mean_offer_yield": round(safe_mean([float(row["offer_yield"]) for row in group_rows]), 4),
                "mean_vacancy_yield": round(safe_mean([float(row["vacancy_yield"]) for row in group_rows]), 4),
                "fill_rate": round(safe_mean([float(row["vacancy_filled"]) for row in group_rows]), 4),
                "mean_vacancy_duration_days": round(safe_mean([float(row["vacancy_duration_days"]) for row in group_rows]), 3),
                "share_wage_transparent": round(safe_mean([float(row["wage_transparent"]) for row in group_rows]), 4),
            }
        )
    return output


def summarize_timing(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["regime"])].append(row)

    output: list[dict[str, object]] = []
    for regime in ("decentralized_early_offers", "coordinated_timing"):
        regime_rows = grouped[regime]
        output.append(
            {
                "regime": regime,
                "cases": len(regime_rows),
                "mean_offer_day": round(safe_mean([float(row["offer_day"]) for row in regime_rows]), 3),
                "mean_deadline_days": round(safe_mean([float(row["deadline_days"]) for row in regime_rows]), 3),
                "share_information_complete": round(safe_mean([float(row["information_complete"]) for row in regime_rows]), 4),
                "share_accepted_before_signal": round(safe_mean([float(row["accepted_before_signal"]) for row in regime_rows]), 4),
                "mean_match_quality_index": round(safe_mean([float(row["match_quality_index"]) for row in regime_rows]), 4),
                "mean_mobility_probability": round(safe_mean([float(row["mobility_probability"]) for row in regime_rows]), 4),
            }
        )
    return output


def diagnostic_rows(recruiting_summary: list[dict[str, object]], timing_summary: list[dict[str, object]]) -> list[dict[str, object]]:
    low = next(row for row in recruiting_summary if row["intensity_group"] == "low_recruiting_intensity")
    high = next(row for row in recruiting_summary if row["intensity_group"] == "high_recruiting_intensity")
    early = next(row for row in timing_summary if row["regime"] == "decentralized_early_offers")
    coordinated = next(row for row in timing_summary if row["regime"] == "coordinated_timing")

    return [
        {
            "diagnostic_margin": "recruiting_intensity",
            "baseline_measure": low["mean_vacancy_yield"],
            "comparison_measure": high["mean_vacancy_yield"],
            "interpretation": "Vacancy-to-hire conversion is higher when the synthetic firm works the vacancy more actively.",
            "data_need": "vacancy records, recruiter actions, applications, interviews, offers, hires",
            "counterfactual": "recruiter-capacity or recruiting-policy shock",
        },
        {
            "diagnostic_margin": "interview_bottleneck",
            "baseline_measure": low["mean_interview_yield"],
            "comparison_measure": high["mean_interview_yield"],
            "interpretation": "Applications alone do not reveal whether interview capacity is the scarce margin.",
            "data_need": "application counts, screening outcomes, interview capacity, callbacks",
            "counterfactual": "structured screening or expanded interview slots",
        },
        {
            "diagnostic_margin": "wage_transparency",
            "baseline_measure": low["share_wage_transparent"],
            "comparison_measure": high["share_wage_transparent"],
            "interpretation": "Wage disclosure changes applicant allocation and can alter the quality of the applicant pool.",
            "data_need": "posting content, wage ranges, applicant characteristics, application timing",
            "counterfactual": "wage-disclosure regime versus nondisclosure",
        },
        {
            "diagnostic_margin": "vacancy_duration",
            "baseline_measure": low["mean_vacancy_duration_days"],
            "comparison_measure": high["mean_vacancy_duration_days"],
            "interpretation": "Faster filling can reflect useful recruiting intensity, but it is not a welfare measure by itself.",
            "data_need": "opening and closing dates, hires, starting wages, retention, match quality",
            "counterfactual": "same demand shock with different recruiting policy",
        },
        {
            "diagnostic_margin": "unraveling_and_timing",
            "baseline_measure": early["share_accepted_before_signal"],
            "comparison_measure": coordinated["share_accepted_before_signal"],
            "interpretation": "Early decentralized offers can make workers accept before late information arrives.",
            "data_need": "offer dates, deadlines, acceptance timing, information arrival, placements",
            "counterfactual": "coordinated timing rule or centralized clearinghouse",
        },
        {
            "diagnostic_margin": "match_quality_under_timing_rules",
            "baseline_measure": early["mean_match_quality_index"],
            "comparison_measure": coordinated["mean_match_quality_index"],
            "interpretation": "Timing design matters when waiting allows participants to compare better information.",
            "data_need": "market rosters, rankings or preferences, offers, deadlines, outcomes",
            "counterfactual": "early contracting versus common offer date",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "setting": "online_job_platform",
            "frictive_object": "application congestion and queue visibility",
            "observed_margin": "applications per vacancy, queue length, callback rate, offer rate",
            "needed_data": "posting attributes, applications, platform rank, callbacks, offers, wages",
            "counterfactual_design": "application cap, preference signal, queue display, or vacancy auto-pause",
            "identification_strategy": "platform experiment or staggered interface change",
            "welfare_object": "match quality, worker search costs, employer screening costs, access fairness",
            "main_threat": "applications may move to neighboring vacancies rather than disappear",
        },
        {
            "setting": "wage_transparency_policy",
            "frictive_object": "wage opacity and misdirected search",
            "observed_margin": "posted wages, applicant composition, interview conversion, vacancy yield",
            "needed_data": "job posts, wage ranges, applicant characteristics, interviews, hires",
            "counterfactual_design": "mandatory pay range disclosure versus nondisclosure",
            "identification_strategy": "policy timing, border comparison, or occupation-by-firm exposure",
            "welfare_object": "worker sorting, pay equity, vacancy filling, retention",
            "main_threat": "firms may alter wage ranges or posting language strategically",
        },
        {
            "setting": "gastroenterology_like_fellowships",
            "frictive_object": "unraveling and early contracting",
            "observed_margin": "offer dates, offer-hold periods, accepted offers before information arrival",
            "needed_data": "program rosters, applicant lists, offers, deadlines, acceptances, placements",
            "counterfactual_design": "centralized clearinghouse or common offer date",
            "identification_strategy": "regime comparison with controls for participation selection",
            "welfare_object": "mobility, match quality, wages, program staffing, worker risk",
            "main_threat": "programs entering the match may differ from programs staying outside",
        },
        {
            "setting": "judicial_clerkships",
            "frictive_object": "exploding offers and prestige-driven early contracting",
            "observed_margin": "interview timing, offer timing, deadline length, school representation",
            "needed_data": "applications, interviews, offers, judge characteristics, clerk outcomes",
            "counterfactual_design": "offer-hold period, timing rule, or clearinghouse",
            "identification_strategy": "rule change across cohorts or courts",
            "welfare_object": "access, strategic burden, career starts, prestige allocation",
            "main_threat": "informal networks and private offers may remain unobserved",
        },
        {
            "setting": "public_service_recruiting",
            "frictive_object": "interview bottlenecks and location-specific staffing",
            "observed_margin": "applications by location, interviews, offers, acceptances, retention",
            "needed_data": "vacancies, applicant preferences, service commitments, interview logs, staffing outcomes",
            "counterfactual_design": "priority rule, targeted subsidy, or coordinated hiring window",
            "identification_strategy": "policy rollout or eligibility threshold",
            "welfare_object": "underserved-area staffing, worker welfare, service continuity",
            "main_threat": "short-run placement may not predict long-run retention",
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
    recruiting_rows = recruiting_funnel_rows()
    timing_rows = timing_regime_rows()
    recruiting_summary = summarize_recruiting(recruiting_rows)
    timing_summary = summarize_timing(timing_rows)

    write_csv(lab_dir / "original" / "reduced" / "recruiting_funnel_synthetic.csv", recruiting_rows)
    write_csv(lab_dir / "original" / "reduced" / "timing_regime_synthetic.csv", timing_rows)
    write_csv(lab_dir / "output" / "reproduced" / "vacancy_yield_summary.csv", recruiting_summary)
    write_csv(lab_dir / "output" / "diagnosed" / "timing_regime_comparison.csv", timing_summary)
    write_csv(lab_dir / "output" / "diagnosed" / "design_diagnostics.csv", diagnostic_rows(recruiting_summary, timing_summary))
    write_csv(lab_dir / "output" / "transfer" / "recruiting_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 2 recruiting-congestion lab complete. Outputs reproduce a "
        "within-vacancy yield summary, diagnose recruiting intensity, wage information, "
        "interview bottlenecks, vacancy duration, and timing/unraveling margins, and "
        "transfer the design architecture to neighboring labor-market settings.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
