#!/usr/bin/env python3
"""Build a deterministic project-idea bank for Gender Study Week 10."""
from __future__ import annotations

import csv
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[1]
OUTFILE = LAB_DIR / "original" / "reduced" / "week10_candidate_project_ideas.csv"


IDEAS = [
    {
        "project_id": "P01",
        "title": "Childcare access and retention at high-premium firms",
        "domain": "care_firms",
        "labor_object": "retention at high-premium firms",
        "mechanism": "care constraints reduce feasible job continuity",
        "comparison_group": "workers near newly expanded childcare slots vs similar workers farther away",
        "key_margin": "retention and firm sorting",
        "data_source": "administrative worker-firm panel linked to childcare openings",
        "method": "difference-in-differences event study",
        "welfare_object": "earnings, job continuity, and care-time constraints",
        "portability_claim": "portable mechanism if care availability constrains access to high-premium firms",
        "main_threat": "childcare openings may target neighborhoods with changing labor demand",
    },
    {
        "project_id": "P02",
        "title": "Manager assignment and gendered promotion ratings",
        "domain": "firms_authority",
        "labor_object": "promotion and authority",
        "mechanism": "manager discretion changes evaluation and sponsorship",
        "comparison_group": "workers reassigned across managers after team restructuring",
        "key_margin": "promotion ratings and promotion transitions",
        "data_source": "personnel records with manager identifiers and evaluation text",
        "method": "manager-mover event study",
        "welfare_object": "career advancement and authority",
        "portability_claim": "portable to internal labor markets where managers allocate ratings and opportunities",
        "main_threat": "manager moves may be correlated with team performance shocks",
    },
    {
        "project_id": "P03",
        "title": "Commuting safety and application radius",
        "domain": "urban_safety",
        "labor_object": "job search radius",
        "mechanism": "safety risk narrows feasible commute options",
        "comparison_group": "job seekers exposed to transit-lighting improvements vs matched nearby routes",
        "key_margin": "applications by distance and shift time",
        "data_source": "job-board applications linked to route safety improvements",
        "method": "difference-in-differences with route fixed effects",
        "welfare_object": "job access, safety, and commute disutility",
        "portability_claim": "portable where mobility risk limits access to jobs",
        "main_threat": "route upgrades may coincide with local economic development",
    },
    {
        "project_id": "P04",
        "title": "Pay transparency and firm job redesign",
        "domain": "policy_firms",
        "labor_object": "pay-setting and job design",
        "mechanism": "public disclosure changes firm wage compression and task assignment",
        "comparison_group": "firms just above and below reporting thresholds",
        "key_margin": "wages, bonuses, vacancies, and task titles",
        "data_source": "firm payroll, job postings, and reporting-threshold records",
        "method": "threshold difference-in-differences",
        "welfare_object": "pay equality, promotion opportunities, and task allocation",
        "portability_claim": "portable to settings where disclosure changes employer scrutiny",
        "main_threat": "firms may manipulate headcount around the threshold",
    },
    {
        "project_id": "P05",
        "title": "Nonbinary identity signals and callback heterogeneity",
        "domain": "identity_hiring",
        "labor_object": "callbacks and employer screening",
        "mechanism": "employer response to visible gender-identity signals",
        "comparison_group": "randomized nonbinary identity signal vs otherwise identical resumes",
        "key_margin": "callback probability",
        "data_source": "correspondence audit with pre-registered identity signals",
        "method": "randomized audit experiment",
        "welfare_object": "access to interviews and screening-stage discrimination",
        "portability_claim": "portable as evidence on screening of a disclosed signal, not all nonbinary workers",
        "main_threat": "resume signal may not represent disclosure or perceived identity in real workplaces",
    },
    {
        "project_id": "P06",
        "title": "Reproductive-health access and early-career job continuity",
        "domain": "health_reproduction",
        "labor_object": "early-career employment continuity",
        "mechanism": "reproductive autonomy changes timing, job search, and attachment",
        "comparison_group": "cohorts differentially exposed to clinic access changes by county and age",
        "key_margin": "employment, hours, and job-to-job transitions",
        "data_source": "administrative earnings panel linked to reproductive-health access measures",
        "method": "event study with cohort-by-county exposure",
        "welfare_object": "timing autonomy, earnings, and job continuity",
        "portability_claim": "portable where reproductive timing changes labor-market attachment",
        "main_threat": "clinic access changes may track other county-level policy shifts",
    },
    {
        "project_id": "P07",
        "title": "AI scheduling tools and gendered hours volatility",
        "domain": "technology_ai",
        "labor_object": "hours volatility",
        "mechanism": "algorithmic scheduling changes control over work timing",
        "comparison_group": "stores adopting scheduling software at different rollout dates",
        "key_margin": "hours, schedule predictability, quits, and earnings",
        "data_source": "retail payroll schedules linked to software rollout",
        "method": "staggered rollout event study",
        "welfare_object": "income risk, schedule control, and retention",
        "portability_claim": "portable to low-wage settings where scheduling technology governs hours",
        "main_threat": "software adoption may be chosen by stores with worsening staffing problems",
    },
    {
        "project_id": "P08",
        "title": "Representation in local councils and enforcement of workplace protections",
        "domain": "political_economy",
        "labor_object": "enforcement and reporting",
        "mechanism": "representation changes enforcement priorities and worker reporting beliefs",
        "comparison_group": "close-election municipalities with different representation outcomes",
        "key_margin": "complaints, inspections, and labor-force attachment",
        "data_source": "local election returns linked to enforcement and employment records",
        "method": "close-election regression discontinuity",
        "welfare_object": "legal protection, reporting costs, and employment security",
        "portability_claim": "portable where representation affects enforcement credibility",
        "main_threat": "complaints measure reporting behavior as well as underlying violations",
    },
]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    write_csv(OUTFILE, IDEAS)
    print(f"Wrote {len(IDEAS)} candidate project ideas to {OUTFILE}")


if __name__ == "__main__":
    main()
