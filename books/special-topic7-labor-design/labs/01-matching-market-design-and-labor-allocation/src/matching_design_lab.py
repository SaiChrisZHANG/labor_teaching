from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


PROGRAMS = [
    {
        "program_id": "P01",
        "program_name": "Metro General Medicine",
        "region": "urban",
        "capacity": 14,
        "prestige": 0.92,
        "research_intensity": 0.82,
        "rural_priority": 0,
        "offer_speed": 1,
    },
    {
        "program_id": "P02",
        "program_name": "Lakeside Pediatrics",
        "region": "coastal",
        "capacity": 12,
        "prestige": 0.84,
        "research_intensity": 0.70,
        "rural_priority": 0,
        "offer_speed": 2,
    },
    {
        "program_id": "P03",
        "program_name": "Prairie Family Medicine",
        "region": "rural",
        "capacity": 12,
        "prestige": 0.68,
        "research_intensity": 0.42,
        "rural_priority": 1,
        "offer_speed": 4,
    },
    {
        "program_id": "P04",
        "program_name": "Capital Surgery",
        "region": "urban",
        "capacity": 10,
        "prestige": 0.95,
        "research_intensity": 0.88,
        "rural_priority": 0,
        "offer_speed": 1,
    },
    {
        "program_id": "P05",
        "program_name": "Valley Psychiatry",
        "region": "midwest",
        "capacity": 12,
        "prestige": 0.74,
        "research_intensity": 0.52,
        "rural_priority": 0,
        "offer_speed": 3,
    },
    {
        "program_id": "P06",
        "program_name": "Mountain Internal Medicine",
        "region": "rural",
        "capacity": 12,
        "prestige": 0.72,
        "research_intensity": 0.50,
        "rural_priority": 1,
        "offer_speed": 4,
    },
    {
        "program_id": "P07",
        "program_name": "Harbor Emergency Medicine",
        "region": "coastal",
        "capacity": 10,
        "prestige": 0.86,
        "research_intensity": 0.62,
        "rural_priority": 0,
        "offer_speed": 2,
    },
    {
        "program_id": "P08",
        "program_name": "River Public Service Track",
        "region": "rural",
        "capacity": 12,
        "prestige": 0.64,
        "research_intensity": 0.38,
        "rural_priority": 1,
        "offer_speed": 5,
    },
]


REGIONS = ["urban", "coastal", "rural", "midwest"]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def applicants() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number in range(1, 121):
        region_preference = REGIONS[number % len(REGIONS)]
        quality = clamp(0.56 + ((number * 17) % 43) / 100)
        research_orientation = clamp(0.20 + ((number * 11) % 70) / 100)
        service_commitment = 1 if number % 5 in (0, 1) else 0
        risk_aversion = clamp(0.22 + ((number * 13) % 65) / 100)
        couple_member = 1 if number % 37 in (0, 1) else 0
        rows.append(
            {
                "applicant_id": f"A{number:03d}",
                "region_preference": region_preference,
                "quality": round(quality, 3),
                "research_orientation": round(research_orientation, 3),
                "service_commitment": service_commitment,
                "risk_aversion": round(risk_aversion, 3),
                "couple_member": couple_member,
            }
        )
    return rows


def preference_score(applicant: dict[str, object], program: dict[str, object], program_index: int) -> float:
    region_match = 1 if applicant["region_preference"] == program["region"] else 0
    service_fit = int(applicant["service_commitment"]) * int(program["rural_priority"])
    deterministic_taste = ((int(applicant["applicant_id"][1:]) * (program_index + 3)) % 11 - 5) / 12
    return (
        50 * float(program["prestige"])
        + 15 * region_match
        + 8 * service_fit
        + 7 * float(applicant["research_orientation"]) * float(program["research_intensity"])
        + deterministic_taste
    )


def priority_score(applicant: dict[str, object], program: dict[str, object], program_index: int) -> float:
    region_match = 1 if applicant["region_preference"] == program["region"] else 0
    service_priority = int(applicant["service_commitment"]) * int(program["rural_priority"])
    deterministic_review = ((int(applicant["applicant_id"][1:]) * (program_index + 5)) % 13 - 6) / 14
    return (
        52 * float(applicant["quality"])
        + 17 * float(applicant["research_orientation"]) * float(program["research_intensity"])
        + 12 * service_priority
        + 4 * region_match
        - 2 * int(applicant["couple_member"])
        + deterministic_review
    )


def pair_data(applicant_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    raw_rows: list[dict[str, object]] = []
    for applicant in applicant_rows:
        for program_index, program in enumerate(PROGRAMS):
            raw_rows.append(
                {
                    "applicant_id": applicant["applicant_id"],
                    "program_id": program["program_id"],
                    "program_name": program["program_name"],
                    "program_region": program["region"],
                    "capacity": program["capacity"],
                    "rural_priority": program["rural_priority"],
                    "applicant_region_preference": applicant["region_preference"],
                    "service_commitment": applicant["service_commitment"],
                    "risk_aversion": applicant["risk_aversion"],
                    "couple_member": applicant["couple_member"],
                    "preference_score": round(preference_score(applicant, program, program_index), 3),
                    "priority_score": round(priority_score(applicant, program, program_index), 3),
                }
            )

    by_applicant: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_program: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in raw_rows:
        by_applicant[str(row["applicant_id"])].append(row)
        by_program[str(row["program_id"])].append(row)

    applicant_rank: dict[tuple[str, str], int] = {}
    for applicant_id, rows in by_applicant.items():
        ranked = sorted(rows, key=lambda item: (-float(item["preference_score"]), str(item["program_id"])))
        for rank, row in enumerate(ranked, start=1):
            applicant_rank[(applicant_id, str(row["program_id"]))] = rank

    program_rank: dict[tuple[str, str], int] = {}
    for program_id, rows in by_program.items():
        ranked = sorted(rows, key=lambda item: (-float(item["priority_score"]), str(item["applicant_id"])))
        for rank, row in enumerate(ranked, start=1):
            program_rank[(str(row["applicant_id"]), program_id)] = rank

    for row in raw_rows:
        key = (str(row["applicant_id"]), str(row["program_id"]))
        row["applicant_rank"] = applicant_rank[key]
        row["program_rank"] = program_rank[key]
    return raw_rows


def lookup_maps(rows: list[dict[str, object]]) -> tuple[dict[str, list[str]], dict[str, dict[str, int]], dict[tuple[str, str], dict[str, object]]]:
    preferences: dict[str, list[str]] = defaultdict(list)
    program_priority_rank: dict[str, dict[str, int]] = defaultdict(dict)
    pair_lookup: dict[tuple[str, str], dict[str, object]] = {}

    for row in rows:
        pair_lookup[(str(row["applicant_id"]), str(row["program_id"]))] = row
        program_priority_rank[str(row["program_id"])][str(row["applicant_id"])] = int(row["program_rank"])

    by_applicant: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_applicant[str(row["applicant_id"])].append(row)
    for applicant_id, applicant_rows in by_applicant.items():
        preferences[applicant_id] = [
            str(row["program_id"])
            for row in sorted(applicant_rows, key=lambda item: (int(item["applicant_rank"]), str(item["program_id"])))
        ]

    return dict(preferences), dict(program_priority_rank), pair_lookup


def deferred_acceptance(rows: list[dict[str, object]], applicant_ids: list[str]) -> dict[str, str | None]:
    preferences, program_priority_rank, _ = lookup_maps(rows)
    capacities = {str(program["program_id"]): int(program["capacity"]) for program in PROGRAMS}
    held: dict[str, list[str]] = {program_id: [] for program_id in capacities}
    assignment: dict[str, str | None] = {applicant_id: None for applicant_id in applicant_ids}
    next_choice = {applicant_id: 0 for applicant_id in applicant_ids}

    while True:
        proposals: dict[str, list[str]] = defaultdict(list)
        for applicant_id in applicant_ids:
            if assignment[applicant_id] is not None:
                continue
            if next_choice[applicant_id] >= len(preferences[applicant_id]):
                continue
            program_id = preferences[applicant_id][next_choice[applicant_id]]
            next_choice[applicant_id] += 1
            proposals[program_id].append(applicant_id)

        if not proposals:
            break

        for program_id, proposers in proposals.items():
            pool = held[program_id] + proposers
            ranked_pool = sorted(pool, key=lambda applicant_id: program_priority_rank[program_id][applicant_id])
            held[program_id] = ranked_pool[: capacities[program_id]]
            rejected = ranked_pool[capacities[program_id] :]
            for applicant_id in held[program_id]:
                assignment[applicant_id] = program_id
            for applicant_id in rejected:
                assignment[applicant_id] = None

    return assignment


def decentralized_exploding_offers(rows: list[dict[str, object]], applicant_ids: list[str]) -> dict[str, str | None]:
    _, _, pair_lookup = lookup_maps(rows)
    capacities = {str(program["program_id"]): int(program["capacity"]) for program in PROGRAMS}
    remaining = dict(capacities)
    assignment: dict[str, str | None] = {applicant_id: None for applicant_id in applicant_ids}

    priority_lists: dict[str, list[str]] = {}
    for program in PROGRAMS:
        program_id = str(program["program_id"])
        priority_lists[program_id] = [
            str(row["applicant_id"])
            for row in sorted(
                [row for row in rows if row["program_id"] == program_id],
                key=lambda item: (int(item["program_rank"]), str(item["applicant_id"])),
            )
        ]

    pointer = {str(program["program_id"]): 0 for program in PROGRAMS}
    program_order = [str(program["program_id"]) for program in sorted(PROGRAMS, key=lambda item: (int(item["offer_speed"]), str(item["program_id"])))]

    for offer_round in range(1, 6):
        for program_id in program_order:
            if remaining[program_id] <= 0:
                continue
            offers_this_round = 0
            max_offers = max(2, capacities[program_id] // 2)
            while remaining[program_id] > 0 and offers_this_round < max_offers and pointer[program_id] < len(priority_lists[program_id]):
                applicant_id = priority_lists[program_id][pointer[program_id]]
                pointer[program_id] += 1
                if assignment[applicant_id] is not None:
                    continue

                pair = pair_lookup[(applicant_id, program_id)]
                applicant_rank = int(pair["applicant_rank"])
                risk_aversion = float(pair["risk_aversion"])
                accept_cutoff = 2 + offer_round + (2 if risk_aversion >= 0.65 else 0)
                if applicant_rank <= accept_cutoff or offer_round == 5:
                    assignment[applicant_id] = program_id
                    remaining[program_id] -= 1
                offers_this_round += 1

    return assignment


def blocking_pairs(assignment: dict[str, str | None], pair_lookup: dict[tuple[str, str], dict[str, object]]) -> int:
    assigned_by_program: dict[str, list[str]] = defaultdict(list)
    for applicant_id, program_id in assignment.items():
        if program_id is not None:
            assigned_by_program[program_id].append(applicant_id)

    capacities = {str(program["program_id"]): int(program["capacity"]) for program in PROGRAMS}
    count = 0
    for applicant_id, current_program in assignment.items():
        current_rank = 10_000 if current_program is None else int(pair_lookup[(applicant_id, current_program)]["applicant_rank"])
        for program in PROGRAMS:
            program_id = str(program["program_id"])
            if program_id == current_program:
                continue
            candidate_pair = pair_lookup[(applicant_id, program_id)]
            if int(candidate_pair["applicant_rank"]) >= current_rank:
                continue
            current_matches = assigned_by_program[program_id]
            if len(current_matches) < capacities[program_id]:
                count += 1
                continue
            worst_current_rank = max(int(pair_lookup[(matched_id, program_id)]["program_rank"]) for matched_id in current_matches)
            if int(candidate_pair["program_rank"]) < worst_current_rank:
                count += 1
    return count


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def scenario_summary(
    scenario: str,
    assignment: dict[str, str | None],
    pair_lookup: dict[tuple[str, str], dict[str, object]],
) -> dict[str, object]:
    matched_pairs = [(applicant_id, program_id) for applicant_id, program_id in assignment.items() if program_id is not None]
    matched_count = len(matched_pairs)
    total_capacity = sum(int(program["capacity"]) for program in PROGRAMS)
    service_applicants = [applicant_id for applicant_id in assignment if int(pair_lookup[(applicant_id, "P01")]["service_commitment"]) == 1]
    service_to_rural = [
        applicant_id
        for applicant_id, program_id in matched_pairs
        if int(pair_lookup[(applicant_id, program_id)]["service_commitment"]) == 1
        and int(pair_lookup[(applicant_id, program_id)]["rural_priority"]) == 1
    ]
    return {
        "scenario": scenario,
        "matched_applicants": matched_count,
        "unfilled_slots": total_capacity - matched_count,
        "blocking_pairs": blocking_pairs(assignment, pair_lookup),
        "mean_applicant_rank": round(safe_mean([int(pair_lookup[(a, p)]["applicant_rank"]) for a, p in matched_pairs]), 3),
        "mean_program_priority_rank": round(safe_mean([int(pair_lookup[(a, p)]["program_rank"]) for a, p in matched_pairs]), 3),
        "service_applicant_rural_match_rate": round(len(service_to_rural) / len(service_applicants), 3),
        "mean_preference_score": round(safe_mean([float(pair_lookup[(a, p)]["preference_score"]) for a, p in matched_pairs]), 3),
    }


def assignment_comparison(
    applicant_ids: list[str],
    centralized: dict[str, str | None],
    decentralized: dict[str, str | None],
    pair_lookup: dict[tuple[str, str], dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for applicant_id in applicant_ids:
        centralized_program = centralized[applicant_id]
        decentralized_program = decentralized[applicant_id]
        centralized_rank = "" if centralized_program is None else int(pair_lookup[(applicant_id, centralized_program)]["applicant_rank"])
        decentralized_rank = "" if decentralized_program is None else int(pair_lookup[(applicant_id, decentralized_program)]["applicant_rank"])
        rows.append(
            {
                "applicant_id": applicant_id,
                "centralized_program": centralized_program or "unmatched",
                "centralized_applicant_rank": centralized_rank,
                "decentralized_program": decentralized_program or "unmatched",
                "decentralized_applicant_rank": decentralized_rank,
                "same_assignment": int(centralized_program == decentralized_program),
            }
        )
    return rows


def diagnostic_rows(summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    centralized = next(row for row in summaries if row["scenario"] == "centralized_deferred_acceptance")
    decentralized = next(row for row in summaries if row["scenario"] == "decentralized_exploding_offers")

    return [
        {
            "diagnostic_margin": "stability_pressure",
            "centralized_value": centralized["blocking_pairs"],
            "decentralized_value": decentralized["blocking_pairs"],
            "design_lesson": "Blocking pairs diagnose whether workers and programs have mutual incentives to bypass the mechanism.",
            "data_need": "preferences, priorities, capacities, and final matches",
        },
        {
            "diagnostic_margin": "congestion_and_timing",
            "centralized_value": centralized["mean_applicant_rank"],
            "decentralized_value": decentralized["mean_applicant_rank"],
            "design_lesson": "Exploding offers can lock applicants into worse-ranked assignments before later information arrives.",
            "data_need": "offer timing, acceptance deadlines, rank data, and rejected offers",
        },
        {
            "diagnostic_margin": "program_priority_fit",
            "centralized_value": centralized["mean_program_priority_rank"],
            "decentralized_value": decentralized["mean_program_priority_rank"],
            "design_lesson": "A rule can improve applicant outcomes while changing how programs fill priority-ranked slots.",
            "data_need": "program priorities, applicant attributes, capacities, and match outcomes",
        },
        {
            "diagnostic_margin": "service_priority_placement",
            "centralized_value": centralized["service_applicant_rural_match_rate"],
            "decentralized_value": decentralized["service_applicant_rural_match_rate"],
            "design_lesson": "Fairness and staffing objectives require outcome measures beyond aggregate match quality.",
            "data_need": "service commitments, location assignments, staffing needs, and post-match retention",
        },
        {
            "diagnostic_margin": "welfare_beyond_stability",
            "centralized_value": centralized["mean_preference_score"],
            "decentralized_value": decentralized["mean_preference_score"],
            "design_lesson": "Stability is an allocation property, not a complete welfare measure.",
            "data_need": "rankings, wages, career outcomes, location preferences, and worker welfare measures",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "setting": "clinical_psychology_internships",
            "failure_mode": "bottlenecks, slow responses, and early contracting before information is complete",
            "needed_data": "applications, interviews, offer timing, acceptances, rankings, and placement outcomes",
            "counterfactual_design": "centralized match or coordinated response windows",
            "welfare_or_fairness_object": "match quality, training access, strategic burden, and geographic mobility",
            "main_threat": "timing reforms may coincide with changes in applicant supply or program accreditation",
        },
        {
            "setting": "specialist_fellowships",
            "failure_mode": "unraveling and early offers in thin professional submarkets",
            "needed_data": "fellowship rosters, offer dates, applicant characteristics, program capacities, and career paths",
            "counterfactual_design": "single match date versus early decentralized offers",
            "welfare_or_fairness_object": "mobility, specialty access, program staffing, and early-career trajectories",
            "main_threat": "participation in the match may be selected by program prestige and specialty demand",
        },
        {
            "setting": "judicial_clerkships",
            "failure_mode": "informal timing norms, exploding offers, and prestige-driven early contracting",
            "needed_data": "application timing, interview timing, offer deadlines, judge characteristics, and clerk outcomes",
            "counterfactual_design": "coordinated timing rule, offer-hold period, or clearinghouse",
            "welfare_or_fairness_object": "access, strategic burden, career starts, and distribution across law schools",
            "main_threat": "private offers and informal networks may be unobserved",
        },
        {
            "setting": "rural_public_service_placement",
            "failure_mode": "underserved-area staffing constraints and priority-rule tradeoffs",
            "needed_data": "preferences, service commitments, location priorities, staffing vacancies, and retention",
            "counterfactual_design": "rural priority, subsidy, quota, or targeted reserve system",
            "welfare_or_fairness_object": "underserved staffing, applicant welfare, service continuity, and access equity",
            "main_threat": "location preferences and long-run retention may differ from submitted rankings",
        },
        {
            "setting": "platform_mediated_professional_projects",
            "failure_mode": "algorithmic visibility, ranking congestion, and strategic applications",
            "needed_data": "recommendations, search rankings, applications, offers, acceptances, wages, and performance",
            "counterfactual_design": "ranking rule, application limit, signal, or priority display change",
            "welfare_or_fairness_object": "worker access, employer match quality, wage incidence, and visibility fairness",
            "main_threat": "platform experiments may change both search behavior and employer screening",
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
    applicant_rows = applicants()
    rows = pair_data(applicant_rows)
    applicant_ids = [str(row["applicant_id"]) for row in applicant_rows]
    _, _, pair_lookup = lookup_maps(rows)

    centralized = deferred_acceptance(rows, applicant_ids)
    decentralized = decentralized_exploding_offers(rows, applicant_ids)

    summaries = [
        scenario_summary("centralized_deferred_acceptance", centralized, pair_lookup),
        scenario_summary("decentralized_exploding_offers", decentralized, pair_lookup),
    ]

    write_csv(lab_dir / "original" / "reduced" / "professional_entry_matching_synthetic.csv", rows)
    write_csv(lab_dir / "output" / "reproduced" / "assignment_comparison.csv", assignment_comparison(applicant_ids, centralized, decentralized, pair_lookup))
    write_csv(lab_dir / "output" / "reproduced" / "match_summary.csv", summaries)
    write_csv(lab_dir / "output" / "diagnosed" / "design_diagnostics.csv", diagnostic_rows(summaries))
    write_csv(lab_dir / "output" / "transfer" / "professional_market_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 1 matching-design lab complete. Outputs reproduce a centralized "
        "many-to-one match, diagnose stability and timing differences against decentralized "
        "exploding offers, and transfer the design architecture to neighboring professional "
        "labor markets.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
