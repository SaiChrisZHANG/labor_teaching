from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


PROGRAMS = [
    {"program": "Metro General", "capacity": 12, "training_value": 0.82, "shortage_pressure": 0.33, "urban": 1.0},
    {"program": "North County", "capacity": 10, "training_value": 0.70, "shortage_pressure": 0.68, "urban": 0.0},
    {"program": "Central Research", "capacity": 11, "training_value": 0.90, "shortage_pressure": 0.29, "urban": 1.0},
    {"program": "Riverside Public", "capacity": 10, "training_value": 0.74, "shortage_pressure": 0.72, "urban": 0.0},
    {"program": "Harbor Teaching", "capacity": 11, "training_value": 0.86, "shortage_pressure": 0.41, "urban": 1.0},
    {"program": "Prairie Regional", "capacity": 10, "training_value": 0.66, "shortage_pressure": 0.79, "urban": 0.0},
    {"program": "Westside Specialty", "capacity": 11, "training_value": 0.88, "shortage_pressure": 0.36, "urban": 1.0},
    {"program": "Valley Service", "capacity": 9, "training_value": 0.62, "shortage_pressure": 0.84, "urban": 0.0},
]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def applicant_affinity(applicant_number: int, program_index: int) -> float:
    return clamp(0.16 + ((applicant_number * (program_index + 7) + program_index * 19) % 82) / 100)


def make_applicants() -> list[dict[str, object]]:
    applicants: list[dict[str, object]] = []
    total_capacity = sum(int(program["capacity"]) for program in PROGRAMS)

    for applicant_number in range(1, total_capacity + 1):
        ability = clamp(0.32 + ((applicant_number * 17) % 62) / 100)
        research_orientation = clamp(0.25 + ((applicant_number * 13) % 70) / 100)
        service_orientation = clamp(0.24 + ((applicant_number * 23) % 69) / 100)
        outside_option = clamp(0.22 + ((applicant_number * 29) % 65) / 100)
        risk_exposure = clamp(0.18 + ((applicant_number * 31) % 72) / 100)
        urban_preference = 1.0 if applicant_number % 3 != 0 else 0.0

        affinities = {
            program["program"]: applicant_affinity(applicant_number, program_index)
            for program_index, program in enumerate(PROGRAMS)
        }
        priorities = {
            program["program"]: clamp(
                0.15
                + 0.38 * ability
                + 0.18 * research_orientation * float(program["training_value"])
                + 0.16 * service_orientation * float(program["shortage_pressure"])
                + 0.12 * affinities[program["program"]]
                + ((applicant_number + program_index * 3) % 7) / 100
            )
            for program_index, program in enumerate(PROGRAMS)
        }
        preferences = sorted(
            [program["program"] for program in PROGRAMS],
            key=lambda program_name: (
                0.45 * affinities[program_name]
                + 0.18 * next(item["training_value"] for item in PROGRAMS if item["program"] == program_name)
                + 0.14
                * (1 - abs(urban_preference - next(item["urban"] for item in PROGRAMS if item["program"] == program_name)))
                + 0.10 * service_orientation * next(item["shortage_pressure"] for item in PROGRAMS if item["program"] == program_name)
                - 0.12 * risk_exposure * next(item["shortage_pressure"] for item in PROGRAMS if item["program"] == program_name)
            ),
            reverse=True,
        )

        applicants.append(
            {
                "applicant_id": f"A{applicant_number:03d}",
                "ability_index": round(ability, 3),
                "research_orientation_index": round(research_orientation, 3),
                "service_orientation_index": round(service_orientation, 3),
                "outside_option_index": round(outside_option, 3),
                "risk_exposure_index": round(risk_exposure, 3),
                "urban_preference": int(urban_preference),
                "preferences": preferences,
                "priority_scores": priorities,
                "affinity_scores": affinities,
            }
        )

    return applicants


def deferred_acceptance_assignments(applicants: list[dict[str, object]]) -> dict[str, str]:
    capacities = {program["program"]: int(program["capacity"]) for program in PROGRAMS}
    proposals_used = {str(applicant["applicant_id"]): 0 for applicant in applicants}
    applicant_by_id = {str(applicant["applicant_id"]): applicant for applicant in applicants}
    tentative: dict[str, list[str]] = {program["program"]: [] for program in PROGRAMS}
    free = [str(applicant["applicant_id"]) for applicant in applicants]

    while free:
        next_free: list[str] = []
        for applicant_id in free:
            applicant = applicant_by_id[applicant_id]
            preferences = list(applicant["preferences"])
            proposal_index = proposals_used[applicant_id]
            if proposal_index >= len(preferences):
                continue
            program_name = str(preferences[proposal_index])
            proposals_used[applicant_id] += 1
            tentative[program_name].append(applicant_id)

        for program_name, candidates in tentative.items():
            priority_sorted = sorted(
                candidates,
                key=lambda candidate_id: float(applicant_by_id[candidate_id]["priority_scores"][program_name]),
                reverse=True,
            )
            accepted = priority_sorted[: capacities[program_name]]
            rejected = priority_sorted[capacities[program_name] :]
            tentative[program_name] = accepted
            next_free.extend(rejected)
        free = next_free

    return {
        applicant_id: program_name
        for program_name, candidates in tentative.items()
        for applicant_id in candidates
    }


def early_offer_assignments(applicants: list[dict[str, object]]) -> dict[str, str]:
    capacities = {program["program"]: int(program["capacity"]) for program in PROGRAMS}
    applicant_by_id = {str(applicant["applicant_id"]): applicant for applicant in applicants}
    assignments: dict[str, str] = {}

    for program in sorted(PROGRAMS, key=lambda item: (float(item["training_value"]), -float(item["shortage_pressure"])), reverse=True):
        program_name = str(program["program"])
        candidates = [
            applicant
            for applicant in applicants
            if str(applicant["applicant_id"]) not in assignments
        ]
        ranked = sorted(
            candidates,
            key=lambda applicant: (
                0.50 * float(applicant["priority_scores"][program_name])
                + 0.20 * float(applicant["ability_index"])
                + 0.12 * float(applicant["outside_option_index"])
                - 0.06 * (list(applicant["preferences"]).index(program_name) + 1)
            ),
            reverse=True,
        )
        for applicant in ranked[: capacities[program_name]]:
            assignments[str(applicant["applicant_id"])] = program_name

    unassigned = [applicant for applicant in applicants if str(applicant["applicant_id"]) not in assignments]
    remaining_capacity = defaultdict(int)
    for program in PROGRAMS:
        program_name = str(program["program"])
        remaining_capacity[program_name] = int(program["capacity"]) - sum(1 for value in assignments.values() if value == program_name)

    for applicant in unassigned:
        for program_name in list(applicant["preferences"]):
            if remaining_capacity[program_name] > 0:
                assignments[str(applicant["applicant_id"])] = str(program_name)
                remaining_capacity[program_name] -= 1
                break

    if len(assignments) != len(applicant_by_id):
        raise ValueError("Early-offer assignment left applicants unassigned.")

    return assignments


def program_lookup(program_name: str) -> dict[str, object]:
    return next(program for program in PROGRAMS if program["program"] == program_name)


def assignment_outcomes(
    applicants: list[dict[str, object]],
    assignments: dict[str, str],
    mechanism: str,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for applicant in applicants:
        applicant_id = str(applicant["applicant_id"])
        program_name = assignments[applicant_id]
        program = program_lookup(program_name)
        preferences = list(applicant["preferences"])
        preference_rank = preferences.index(program_name) + 1
        priority_score = float(applicant["priority_scores"][program_name])
        affinity_score = float(applicant["affinity_scores"][program_name])
        training_value = float(program["training_value"])
        shortage_pressure = float(program["shortage_pressure"])
        service_orientation = float(applicant["service_orientation_index"])
        outside_option = float(applicant["outside_option_index"])
        risk_exposure = float(applicant["risk_exposure_index"])
        location_fit = 1 - abs(float(applicant["urban_preference"]) - float(program["urban"]))
        preference_value = (len(PROGRAMS) - preference_rank) / (len(PROGRAMS) - 1)

        match_quality = clamp(
            0.24
            + 0.26 * affinity_score
            + 0.20 * priority_score
            + 0.16 * training_value
            + 0.14 * preference_value
        )
        worker_welfare = clamp(
            0.20
            + 0.28 * preference_value
            + 0.18 * affinity_score
            + 0.14 * location_fit
            + 0.12 * training_value
            + 0.08 * service_orientation * shortage_pressure
            - 0.11 * outside_option * risk_exposure
        )
        program_staffing_value = clamp(
            0.18
            + 0.30 * priority_score
            + 0.22 * shortage_pressure
            + 0.16 * service_orientation
            + 0.14 * training_value
        )
        equilibrium_pressure = clamp(
            0.20
            + 0.20 * shortage_pressure
            + 0.18 * outside_option
            + 0.14 * risk_exposure
            - 0.12 * preference_value
        )

        rows.append(
            {
                "mechanism": mechanism,
                "applicant_id": applicant_id,
                "assigned_program": program_name,
                "preference_rank": preference_rank,
                "top_three_assignment": int(preference_rank <= 3),
                "priority_alignment_index": round(priority_score, 3),
                "affinity_index": round(affinity_score, 3),
                "training_value_index": round(training_value, 3),
                "shortage_pressure_index": round(shortage_pressure, 3),
                "location_fit": int(location_fit),
                "match_quality_index": round(match_quality, 3),
                "worker_welfare_index": round(worker_welfare, 3),
                "program_staffing_value_index": round(program_staffing_value, 3),
                "equilibrium_pressure_index": round(equilibrium_pressure, 3),
                "outside_option_index": round(outside_option, 3),
            }
        )

    return rows


def summarize_outcomes(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["mechanism"])].append(row)

    output: list[dict[str, object]] = []
    for mechanism in ("deferred_acceptance", "early_offers"):
        group = grouped[mechanism]
        output.append(
            {
                "mechanism": mechanism,
                "applicants": len(group),
                "avg_preference_rank": round(safe_mean([float(row["preference_rank"]) for row in group]), 3),
                "share_top_three": round(safe_mean([float(row["top_three_assignment"]) for row in group]), 3),
                "avg_priority_alignment": round(safe_mean([float(row["priority_alignment_index"]) for row in group]), 3),
                "avg_match_quality": round(safe_mean([float(row["match_quality_index"]) for row in group]), 3),
                "avg_worker_welfare": round(safe_mean([float(row["worker_welfare_index"]) for row in group]), 3),
                "avg_program_staffing_value": round(safe_mean([float(row["program_staffing_value_index"]) for row in group]), 3),
                "avg_shortage_pressure_assigned": round(safe_mean([float(row["shortage_pressure_index"]) for row in group]), 3),
                "avg_equilibrium_pressure": round(safe_mean([float(row["equilibrium_pressure_index"]) for row in group]), 3),
            }
        )
    return output


def mechanism_diagnostics(summary_rows: list[dict[str, object]]) -> list[dict[str, str]]:
    summary_by_mechanism = {str(row["mechanism"]): row for row in summary_rows}
    da = summary_by_mechanism["deferred_acceptance"]
    early = summary_by_mechanism["early_offers"]

    def diff(column: str) -> float:
        return round(float(da[column]) - float(early[column]), 3)

    return [
        {
            "object": "mechanism",
            "diagnostic": "deferred acceptance compared with early offers",
            "observed_difference": "rule changes assignment order and priority handling",
            "interpretation": "direct design effect is clear in the synthetic path",
            "main_threat": "real applicants may strategically rank or accept outside offers",
        },
        {
            "object": "preference_rank",
            "diagnostic": "average assigned rank difference",
            "observed_difference": str(diff("avg_preference_rank")),
            "interpretation": "lower rank is better for applicant placement",
            "main_threat": "rank improvements need not equal welfare if wages, training, or risk change",
        },
        {
            "object": "match_quality",
            "diagnostic": "average match-quality difference",
            "observed_difference": str(diff("avg_match_quality")),
            "interpretation": "combines affinity, program priority, training value, and assigned rank",
            "main_threat": "real match quality may depend on unobserved fit and post-match outcomes",
        },
        {
            "object": "worker_welfare",
            "diagnostic": "average worker-welfare difference",
            "observed_difference": str(diff("avg_worker_welfare")),
            "interpretation": "synthetic welfare includes rank, fit, training, service value, outside options, and risk",
            "main_threat": "real welfare requires preferences, wages, amenities, and outside options",
        },
        {
            "object": "equilibrium_response",
            "diagnostic": "average equilibrium-pressure difference",
            "observed_difference": str(diff("avg_equilibrium_pressure")),
            "interpretation": "higher pressure flags markets where spillovers and reallocation may matter",
            "main_threat": "single-market estimates may miss congestion across linked markets",
        },
    ]


def portability_diagnostics() -> list[dict[str, str]]:
    return [
        {
            "setting": "medical match",
            "portable_mechanism": "centralized matching changes timing, stability, and strategic ranking",
            "local_institutional_detail": "specialty training, hospital capacity, ranking norms, couples, and residency rules",
            "data_need": "rank lists, capacities, matches, post-match outcomes, outside options",
            "welfare_risk": "better rank may not capture training value, wages, or long-run career outcomes",
        },
        {
            "setting": "Army officer assignment",
            "portable_mechanism": "deferred acceptance changes assignment priority and preference alignment",
            "local_institutional_detail": "service obligations, branch priorities, promotion ladders, and mission constraints",
            "data_need": "preferences, priorities, assignments, training, retention, promotions",
            "welfare_risk": "organizational staffing gains may diverge from worker welfare",
        },
        {
            "setting": "platform labor market",
            "portable_mechanism": "ranking and visibility rules redirect attention and bargaining",
            "local_institutional_detail": "algorithmic exposure, fees, reputations, wage bids, and multi-homing",
            "data_need": "impressions, bids, messages, hires, wages, retention, outside platforms",
            "welfare_risk": "higher hiring can shift risk or surplus away from workers",
        },
        {
            "setting": "public-sector staffing",
            "portable_mechanism": "priority rules trade worker preferences against hard-to-staff vacancies",
            "local_institutional_detail": "wage rigidity, political constraints, mission value, and exit options",
            "data_need": "applications, assignments, staffing outcomes, service quality, retention",
            "welfare_risk": "priority-site fill can rise while morale or retention falls",
        },
    ]


def transfer_designs() -> list[dict[str, str]]:
    return [
        {
            "project": "platform ranking pilot",
            "rule": "change worker visibility in search results",
            "mechanism": "attention and information",
            "labor_margin": "views, bids, hires, wages",
            "counterfactual": "old ranking rule",
            "main_spillover": "attention shifts away from untreated workers",
            "welfare_object": "worker surplus and employer match quality",
        },
        {
            "project": "recruiting timing reform",
            "rule": "ban exploding offers or coordinate offer dates",
            "mechanism": "timing and congestion",
            "labor_margin": "interviews, acceptances, vacancy fill, match quality",
            "counterfactual": "decentralized early offers",
            "main_spillover": "firms may move screening earlier or use informal promises",
            "welfare_object": "worker option value and employer staffing",
        },
        {
            "project": "pay transparency rollout",
            "rule": "require posted wage ranges",
            "mechanism": "information and bargaining",
            "labor_margin": "applications, wage offers, acceptance, sorting",
            "counterfactual": "no posting requirement",
            "main_spillover": "employers may compress ranges or change vacancy text",
            "welfare_object": "worker wages, sorting, and surplus incidence",
        },
        {
            "project": "teacher placement reform",
            "rule": "centralize assignment with school priorities",
            "mechanism": "matching under public staffing constraints",
            "labor_margin": "preference rank, hard-to-staff fill, retention",
            "counterfactual": "decentralized hiring or old priority rule",
            "main_spillover": "schools and teachers may change ranking behavior",
            "welfare_object": "teacher welfare, student access, and public staffing",
        },
        {
            "project": "internal assignment market",
            "rule": "introduce ranked internal job bidding",
            "mechanism": "within-firm mobility and information",
            "labor_margin": "transfers, promotions, retention, productivity",
            "counterfactual": "manager-directed assignment",
            "main_spillover": "managers may retain workers strategically",
            "welfare_object": "worker career value and firm productivity",
        },
        {
            "project": "AI screening audit",
            "rule": "algorithmic shortlist for applicants",
            "mechanism": "screening and information aggregation",
            "labor_margin": "callbacks, interviews, offers, match quality",
            "counterfactual": "human screening or old score rule",
            "main_spillover": "applicants and employers may adapt resumes and criteria",
            "welfare_object": "access, match quality, and distributional fairness",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows supplied for {path}.")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    applicants = make_applicants()
    da_assignments = deferred_acceptance_assignments(applicants)
    early_assignments = early_offer_assignments(applicants)
    da_rows = assignment_outcomes(applicants, da_assignments, "deferred_acceptance")
    early_rows = assignment_outcomes(applicants, early_assignments, "early_offers")
    all_rows = da_rows + early_rows
    summary_rows = summarize_outcomes(all_rows)

    preference_rows = []
    for applicant in applicants:
        preference_rows.append(
            {
                "applicant_id": applicant["applicant_id"],
                "ability_index": applicant["ability_index"],
                "service_orientation_index": applicant["service_orientation_index"],
                "outside_option_index": applicant["outside_option_index"],
                "risk_exposure_index": applicant["risk_exposure_index"],
                "first_choice": list(applicant["preferences"])[0],
                "second_choice": list(applicant["preferences"])[1],
                "third_choice": list(applicant["preferences"])[2],
            }
        )

    write_csv(lab_dir / "original/reduced/professional_entry_preferences_synthetic.csv", preference_rows)
    write_csv(lab_dir / "original/reduced/design_evaluation_observations_synthetic.csv", all_rows)
    write_csv(lab_dir / "output/reproduced/matching_counterfactual_summary.csv", summary_rows)
    write_csv(lab_dir / "output/diagnosed/mechanism_counterfactual_diagnostics.csv", mechanism_diagnostics(summary_rows))
    write_csv(lab_dir / "output/diagnosed/equilibrium_portability_diagnostics.csv", portability_diagnostics())
    write_csv(lab_dir / "output/transfer/frontier_research_designs.csv", transfer_designs())
    write_text(
        lab_dir / "output/reproduced/reproduction_note.txt",
        (
            "Synthetic teaching path for Week 6. This is not an official replication package. "
            "It reproduces the research-design logic of comparing mechanisms, stating a counterfactual, "
            "and diagnosing welfare and equilibrium threats in labor-market design."
        ),
    )


if __name__ == "__main__":
    main()
