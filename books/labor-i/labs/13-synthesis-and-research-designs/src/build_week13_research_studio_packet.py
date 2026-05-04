from __future__ import annotations

import csv
from pathlib import Path


ANCHORS = [
    {
        "anchor_slug": "card1999",
        "anchor_label": "Card (1999)",
        "citation_key": "card1999",
        "week_origin": "Week 5: Wage determination and returns to skill",
        "labor_object": "causal returns to schooling and wage determination",
        "mechanism": "human-capital accumulation, selection, and skill pricing",
        "data_unit": "worker",
        "design_family": "IV / quasi-experimental returns design",
        "primary_estimand": "causal return to schooling for a clearly defined margin",
        "labor_ii_bridge": "This idea begins on the worker side, but firm complementarity, task demand, and wage-setting become central once heterogeneity across employers matters.",
        "bridge_score": "1",
        "extension_prompt": "How do heterogeneous worker beliefs, training design, or firm complementarity change the measured return to schooling or post-school skill investment?",
    },
    {
        "anchor_slug": "autor-katz-kearney-2008",
        "anchor_label": "Autor, Katz, and Kearney (2008)",
        "citation_key": "autorKatzKearney2008",
        "week_origin": "Week 8: Inequality and wage dispersion",
        "labor_object": "changes in wage inequality across the distribution",
        "mechanism": "skill demand, composition, and dispersion across workers and jobs",
        "data_unit": "worker or percentile cell",
        "design_family": "descriptive decomposition",
        "primary_estimand": "distributional change in percentile gaps or components",
        "labor_ii_bridge": "A descriptive inequality project can stay in Labor I, but it moves into Labor II once firm wage premia, labor demand, or institutions are central propagation mechanisms.",
        "bridge_score": "2",
        "extension_prompt": "How does adding amenities, firms, or local labor-demand exposure change the descriptive architecture of inequality for a specific worker group?",
    },
    {
        "anchor_slug": "card-et-al-2018",
        "anchor_label": "Card et al. (2018)",
        "citation_key": "cardCardosoHeiningKline2018",
        "week_origin": "Weeks 5 and 8: Wage determination, sorting, and inequality",
        "labor_object": "worker and firm components of wages",
        "mechanism": "sorting, firm wage premia, and heterogeneity in wage-setting",
        "data_unit": "worker--firm match",
        "design_family": "matched worker--firm decomposition",
        "primary_estimand": "variance shares and wage components attributable to workers and firms",
        "labor_ii_bridge": "This anchor already sits on the Labor I / Labor II boundary because firm heterogeneity and wage-setting are part of the core object.",
        "bridge_score": "3",
        "extension_prompt": "How do amenities, internal mobility, or worker search frictions alter the interpretation of firm wage premia and sorting patterns?",
    },
    {
        "anchor_slug": "neumark2018",
        "anchor_label": "Neumark (2018)",
        "citation_key": "neumark2018",
        "week_origin": "Week 9: Discrimination, measurement, and sorting",
        "labor_object": "causal discrimination in labor-market outcomes",
        "mechanism": "unequal treatment, sorting, and differential employer response",
        "data_unit": "worker, application, or employer",
        "design_family": "audit / quasi-experimental discrimination design",
        "primary_estimand": "treatment effect of group identity on callbacks, hiring, or wages",
        "labor_ii_bridge": "A worker-side discrimination question quickly becomes Labor II once firms, occupations, search channels, and institutions determine where discrimination propagates.",
        "bridge_score": "2",
        "extension_prompt": "How does discrimination interact with firm heterogeneity, search channels, or task assignment for a specific worker margin?",
    },
    {
        "anchor_slug": "dellavigna2009",
        "anchor_label": "DellaVigna (2009)",
        "citation_key": "dellavigna2009",
        "week_origin": "Week 12: Behavioral frictions and Behavioral Labor",
        "labor_object": "worker response under behavioral wedges",
        "mechanism": "nonstandard preferences, beliefs, or decision-making",
        "data_unit": "worker or job-seeker",
        "design_family": "mechanism map / behavioral design",
        "primary_estimand": "behavioral treatment effect on effort, search, training, or take-up",
        "labor_ii_bridge": "Behavioral worker-side questions remain in Labor I at first pass, but employer contract design and policy implementation quickly bring firms and institutions into the analysis.",
        "bridge_score": "2",
        "extension_prompt": "How do salience, complexity, or present bias change labor-market response for one worker-side object, and when would employer design become part of the treatment?",
    },
]


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    out_dir = lab_dir / "original" / "reduced"
    out_dir.mkdir(parents=True, exist_ok=True)
    (lab_dir / "output" / "reproduced").mkdir(parents=True, exist_ok=True)
    (lab_dir / "output" / "proposed").mkdir(parents=True, exist_ok=True)

    output_path = out_dir / "week13_anchor_papers.csv"
    fieldnames = list(ANCHORS[0].keys())
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ANCHORS)

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

