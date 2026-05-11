from __future__ import annotations

import csv
import math
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def binary_from_rate(index: int, rate: float) -> int:
    threshold = int(round(rate * 100))
    return int((index * 37) % 100 < threshold)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def election_rows() -> list[dict[str, object]]:
    sectors = [
        ("hospital", 0.56, 0.64, 0.42, 1.12, 84),
        ("warehouse", 0.47, 0.72, 0.61, 1.03, 118),
        ("hotel", 0.52, 0.48, 0.55, 0.94, 76),
        ("food_processing", 0.58, 0.50, 0.49, 0.98, 103),
        ("nursing_home", 0.62, 0.58, 0.46, 0.91, 66),
        ("retail", 0.44, 0.45, 0.64, 0.89, 54),
        ("transport", 0.55, 0.69, 0.52, 1.06, 95),
        ("manufacturing", 0.50, 0.56, 0.57, 1.08, 140),
    ]
    rows: list[dict[str, object]] = []
    for index in range(48):
        sector, base_demand, base_tightness, base_opposition, base_wage, base_employment = sectors[index % len(sectors)]
        cycle = index // len(sectors)
        year = 2018 + (index % 6)
        demand = clamp(base_demand + 0.035 * math.sin(index / 3.0) + 0.015 * cycle, 0.28, 0.86)
        tightness = clamp(base_tightness + 0.040 * math.cos(index / 4.0), 0.24, 0.92)
        opposition = clamp(base_opposition + 0.030 * math.sin(index / 5.0 + 1.0), 0.20, 0.82)
        organizing_cost = clamp(0.58 - 0.20 * tightness + 0.18 * opposition - 0.10 * demand, 0.20, 0.78)
        vote_share = clamp(
            0.500
            + 0.095 * (demand - 0.52)
            + 0.055 * (tightness - 0.55)
            - 0.070 * (opposition - 0.52)
            - 0.035 * (organizing_cost - 0.45)
            + 0.030 * math.sin(index * 1.7),
            0.31,
            0.72,
        )
        recognized = int(vote_share >= 0.50)
        close_band = int(abs(vote_share - 0.50) <= 0.10)
        pre_wage = clamp(base_wage + 0.020 * cycle + 0.035 * tightness - 0.025 * opposition, 0.76, 1.32)
        wage_change = 0.012 + 0.030 * recognized + 0.012 * demand + 0.006 * tightness - 0.006 * opposition
        post_wage = clamp(pre_wage + wage_change, 0.78, 1.42)
        employment_pre = max(20, round(base_employment + 8 * cycle + 7 * tightness - 5 * opposition))
        employment_change = round(2 + 4 * tightness - 3 * opposition - 2 * recognized + 2 * demand)
        employment_post = max(10, employment_pre + employment_change)
        payroll_pre = pre_wage * employment_pre
        payroll_post = post_wage * employment_post
        survival_rate = clamp(0.88 + 0.05 * tightness + 0.02 * demand - 0.04 * opposition - 0.01 * recognized, 0.70, 0.98)
        rows.append(
            {
                "establishment_id": f"est-{index + 1:03d}",
                "sector": sector,
                "election_year": year,
                "union_vote_share": round(vote_share, 3),
                "won_recognition": recognized,
                "close_to_threshold": close_band,
                "organizing_demand_index": round(demand, 3),
                "labor_market_tightness_index": round(tightness, 3),
                "employer_opposition_index": round(opposition, 3),
                "organizing_cost_index": round(organizing_cost, 3),
                "pre_wage_index": round(pre_wage, 3),
                "post_wage_index": round(post_wage, 3),
                "wage_change": round(post_wage - pre_wage, 3),
                "employment_pre": employment_pre,
                "employment_post": employment_post,
                "employment_change": employment_post - employment_pre,
                "payroll_pre": round(payroll_pre, 3),
                "payroll_post": round(payroll_post, 3),
                "payroll_change": round(payroll_post - payroll_pre, 3),
                "survived_three_years": binary_from_rate(index + 5, survival_rate),
            }
        )
    return rows


def worker_rows(elections: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for est_index, est in enumerate(elections):
        recognized = int(est["won_recognition"])
        for worker_index in range(10):
            incumbent = int(worker_index < 7)
            skill = clamp(0.35 + 0.05 * (worker_index % 5) + 0.04 * math.sin(est_index / 4.0), 0.25, 0.72)
            pre_wage = float(est["pre_wage_index"]) + 0.060 * skill + 0.012 * (worker_index % 3)
            voice_gain = 0.018 * recognized + 0.010 * incumbent + 0.008 * float(est["organizing_demand_index"])
            post_wage = clamp(pre_wage + 0.010 + voice_gain - 0.004 * float(est["employer_opposition_index"]), 0.72, 1.55)
            separation_rate = clamp(0.24 - 0.060 * recognized - 0.040 * incumbent + 0.050 * float(est["employer_opposition_index"]), 0.06, 0.44)
            grievance_channel = clamp(0.20 + 0.42 * recognized + 0.18 * float(est["organizing_demand_index"]), 0.12, 0.88)
            rows.append(
                {
                    "worker_id": f"{est['establishment_id']}-w{worker_index + 1:02d}",
                    "establishment_id": est["establishment_id"],
                    "sector": est["sector"],
                    "won_recognition": recognized,
                    "incumbent_worker": incumbent,
                    "skill_index": round(skill, 3),
                    "pre_wage_index": round(pre_wage, 3),
                    "post_wage_index": round(post_wage, 3),
                    "wage_change": round(post_wage - pre_wage, 3),
                    "separated_within_two_years": binary_from_rate(est_index * 10 + worker_index + 3, separation_rate),
                    "grievance_channel_index": round(grievance_channel, 3),
                }
            )
    return rows


def design_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "close_certification_election_rd",
            "anchor": "DiNardo-Lee 2004",
            "variation": "union vote share barely crosses the recognition threshold",
            "unit": "establishment or bargaining unit",
            "observed_margin": "recognition, wages, employment, payroll, survival",
            "expected_object": "close_election_recognition",
        },
        {
            "design_id": "matched_worker_establishment_event",
            "anchor": "Frandsen 2021",
            "variation": "linked workers and establishments around new unionization",
            "unit": "worker-establishment-year",
            "observed_margin": "wages, separations, worker composition, payroll",
            "expected_object": "matched_worker_establishment_incidence",
        },
        {
            "design_id": "sectoral_coverage_decomposition",
            "anchor": "Fortin-Lemieux-Lloyd 2021",
            "variation": "wage distribution under observed and counterfactual coverage",
            "unit": "worker or wage cell",
            "observed_margin": "covered wages, uncovered wages, wage compression",
            "expected_object": "spillover_distribution",
        },
        {
            "design_id": "works_council_threshold_design",
            "anchor": "Harju-Jager-Schoefer 2021",
            "variation": "representation rights change at a legal or firm-size threshold",
            "unit": "firm or establishment",
            "observed_margin": "voice, governance, productivity, retention, wages",
            "expected_object": "voice_governance",
        },
        {
            "design_id": "tightness_organizing_demand_survey",
            "anchor": "Pezold-Jager-Nuss 2023",
            "variation": "labor-market tightness changes worker outside options and organizing activity",
            "unit": "worker, campaign, or local labor market",
            "observed_margin": "organizing demand, activity, fear, willingness to support representation",
            "expected_object": "organizing_demand",
        },
        {
            "design_id": "right_to_work_policy_reform",
            "anchor": "Feigenbaum-Hertel-Fernandez-Williamson 2018",
            "variation": "state right-to-work law changes union security and resources",
            "unit": "state-year or worker-year",
            "observed_margin": "union strength, wages, turnout, political participation",
            "expected_object": "political_feedback",
        },
        {
            "design_id": "international_bargaining_regime_comparison",
            "anchor": "Jager-Naidu-Schoefer 2024",
            "variation": "countries differ in membership, coverage, bargaining level, and extension rules",
            "unit": "country, sector, or wage cell",
            "observed_margin": "coverage, wage structure, inequality, membership",
            "expected_object": "comparative_coverage",
        },
    ]


def main() -> None:
    election_fields = [
        "establishment_id",
        "sector",
        "election_year",
        "union_vote_share",
        "won_recognition",
        "close_to_threshold",
        "organizing_demand_index",
        "labor_market_tightness_index",
        "employer_opposition_index",
        "organizing_cost_index",
        "pre_wage_index",
        "post_wage_index",
        "wage_change",
        "employment_pre",
        "employment_post",
        "employment_change",
        "payroll_pre",
        "payroll_post",
        "payroll_change",
        "survived_three_years",
    ]
    worker_fields = [
        "worker_id",
        "establishment_id",
        "sector",
        "won_recognition",
        "incumbent_worker",
        "skill_index",
        "pre_wage_index",
        "post_wage_index",
        "wage_change",
        "separated_within_two_years",
        "grievance_channel_index",
    ]
    design_fields = [
        "design_id",
        "anchor",
        "variation",
        "unit",
        "observed_margin",
        "expected_object",
    ]
    elections = election_rows()
    write_rows(
        LAB / "original" / "reduced" / "close_elections_synthetic.csv",
        election_fields,
        elections,
    )
    write_rows(
        LAB / "original" / "reduced" / "matched_worker_establishment_synthetic.csv",
        worker_fields,
        worker_rows(elections),
    )
    write_rows(
        LAB / "transfer" / "data" / "collective_institution_designs_synthetic.csv",
        design_fields,
        design_rows(),
    )


if __name__ == "__main__":
    main()
