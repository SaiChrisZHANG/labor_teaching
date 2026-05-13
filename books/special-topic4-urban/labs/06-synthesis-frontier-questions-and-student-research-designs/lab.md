# Week 6 Lab: Synthesis, Frontier Questions, And Student Research Designs

## Purpose

This capstone lab is a design workshop. It does not reproduce confidential data or official estimates. Instead, it helps students turn a broad urban phenomenon into a one-page urban-labor research memo with a clear labor outcome, spatial mechanism, geography, counterfactual, incidence issue, and welfare object.

The lab synthesizes the course architecture: commuting and access, housing and rents, segregation and neighborhood exposure, safety and environment, migration, and local labor demand.

## Workflow

### Reproduce

Run the synthetic design path and inspect `output/reproduced/design_architecture_examples.csv`.

Each row starts from a broad topic and rewrites it as a labor research design. The exercise asks students to identify:

- the labor outcome;
- the spatial mechanism;
- the geography;
- the comparison or counterfactual;
- the incidence unit;
- the welfare object;
- why the mechanism matters beyond the focal city.

The point is to practice the Week 6 design template, not to estimate a coefficient.

### Diagnose

Open `output/diagnosed/failure_mode_checklist.csv`. For each design, classify the main risk:

- mechanism slippage;
- geography mismatch;
- ignoring equilibrium response;
- nominal-outcome bias;
- localism without mechanism;
- sorting versus treatment confusion;
- weak portability claim.

For each row, write one repair. A repair might be a better geography, a stronger comparison, a new adjustment-margin measure, a clearer welfare object, or a portability paragraph.

### Transfer

Open `output/transfer/frontier_project_scores.csv`. The transfer exercise scores frontier ideas on four dimensions:

1. labor focus;
2. mechanism clarity;
3. design plausibility;
4. external relevance.

The score is not a ranking of topics. It is a diagnostic for whether the project is ready to become a memo. A low-scoring topic may become strong after narrowing the outcome, identifying cleaner variation, or tracing incidence.

### Write

Open `output/transfer/one_page_research_memo_template.md` and fill it in for one project idea.

The memo should fit on one page:

```text
Title:
Research question:
Labor outcome:
Urban mechanism:
Unit of geography:
Population and incidence unit:
Counterfactual or identifying variation:
Expected adjustment margins:
Main empirical threats:
Welfare object:
Why this matters beyond one city:
```

## Bounded Extension

Choose one project from the frontier scores file and add one additional adjustment margin:

- rents;
- commuting;
- migration;
- firm entry or exit;
- neighborhood sorting;
- safety or environmental exposure;
- local service demand.

Write a short paragraph explaining whether the added margin changes the interpretation of the labor outcome.

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs a lightweight deterministic script and checks that the core outputs were written. No external data or downloads are required.

## Submission Checklist

- one completed one-page urban-labor research memo;
- one table mapping outcome, mechanism, geography, comparison, incidence, and welfare object;
- one paragraph explaining why the project matters beyond the focal city;
- one failure-mode diagnosis and repair;
- one short note on likely equilibrium adjustment.
