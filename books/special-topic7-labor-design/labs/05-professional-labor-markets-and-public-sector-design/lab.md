# Week 5 Lab: Professional Labor Markets And Public-Sector Design

## Purpose

This lab turns the professional/public-sector lecture into a student-facing empirical design workflow. It does not replicate official estimates in Davis, Greenberg, and Jones; Davis; Sonmez and Switzer; or any Army, school, public-service, or civil-service assignment system. Instead, it uses deterministic synthetic data to practice how labor economists move from a structured assignment rule to observable staffing, match-quality, training, retention, internal-mobility, and outside-option margins.

Primary anchor: Davis, Greenberg, and Jones on deferred acceptance in Army officer labor markets [@davisGreenbergJones2026].

Challenge anchor: Davis on matching Teach For America teachers to schools [@davis2024tfa]. Internal-market and recruitment extensions can use Cowgill et al. and Leaver et al. [@cowgillDavisMontagnesPerkowski2025; @leaverOzierSerneelsSabarwal2021].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/army_assignment_summary.csv`.

The script creates a small structured labor-market dataset with:

- officers with preferences, performance, leadership, mission commitment, mobility preferences, and public/private outside options;
- branch capacities, hard-to-staff indicators, and training intensity;
- a deferred-acceptance-style assignment rule;
- a manager-directed assignment rule with stronger staffing weights;
- predicted training value, internal mobility, retention, promotion readiness, and worker welfare.

The object to reproduce is a reduced mechanism comparison:

```{math}
\Delta \bar y =
\bar y_{\text{deferred acceptance}}
-
\bar y_{\text{manager directed}}.
```

The exercise is pedagogical. It reproduces the design logic of a structured assignment comparison, not official estimates from the anchor paper.

### Diagnose

Open `output/diagnosed/design_diagnostics.csv`, `output/diagnosed/ladders_training_mobility.csv`, and `output/diagnosed/public_sector_entry_exit_diagnostics.csv`.

For each diagnostic, classify whether the observed difference most likely reflects:

- worker preference alignment;
- branch or site priority alignment;
- staffing of hard-to-serve units or schools;
- training and career-ladder value;
- internal mobility and on-the-job search;
- retention and exit risk;
- public/private outside options;
- a public objective that may differ from worker welfare.

Answer four questions:

1. Which margins are observed directly in the synthetic data?
2. Which hidden objects remain latent even after the rule comparison?
3. When does a better match rank fail to imply better public-service staffing?
4. What welfare object changes the interpretation: worker utility, training value, retention, service output, fairness, or public staffing?

### Transfer

Open `output/transfer/public_service_design_transfer.csv`. The transfer exercise asks students to move the same architecture to neighboring labor settings:

- Army or military branching;
- teacher or public-service placement;
- public-sector recruitment contracts;
- internal talent markets;
- civil-service entry and exit;
- public/private outside-option margins.

Write a short memo answering:

- What rule changed?
- What labor margin captures the effect?
- What counterfactual rule is needed?
- What data are required?
- What worker-welfare object matters?
- What public objective matters?
- What is the main remaining threat?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing deferred-acceptance-style and manager-directed assignment on preference rank, top-three assignment, priority alignment, hard-to-staff assignment, retention, training, and worker welfare;
- one paragraph explaining why worker preference rank is not enough for public-sector welfare;
- one paragraph explaining how internal ladders, training, and on-the-job search change the interpretation of initial assignment;
- one transfer memo naming the rule, labor margin, counterfactual, data requirement, worker-welfare object, public objective, and main threat.
