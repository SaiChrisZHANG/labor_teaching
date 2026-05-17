# Week 1 Lab: Matching, Market Design, And Labor Allocation

## Purpose

This lab turns the opening matching lecture into a student-facing research-design workflow. It does not replicate official estimates in Roth and Peranson or Agarwal. Instead, it uses deterministic synthetic data to practice how labor economists move from matching theory to an empirical design about professional entry labor markets, staffing, timing, priorities, fairness, and welfare.

Primary anchor: Roth and Peranson on the redesign of the medical residency match [@rothPeranson1999].

Challenge anchor: Agarwal on empirical and policy analysis in the medical match [@agarwal2015; @agarwal2017].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/assignment_comparison.csv` and `output/reproduced/match_summary.csv`.

The script creates a small professional-entry matching market with:

- applicants with region preferences, service commitments, quality measures, and risk aversion;
- programs with capacities, priorities, training styles, regions, and rural-service missions;
- applicant preferences over programs;
- program priorities over applicants.

The object to reproduce is a simplified centralized many-to-one matching rule:

```{math}
\mu(i) \in P \cup \{\emptyset\},
\qquad
|\mu(p)| \leq q_p.
```

The smoke path implements an applicant-proposing deferred-acceptance rule and compares it with a stylized decentralized exploding-offer process. The exercise is pedagogical: it reproduces design logic, not official NRMP estimates.

### Diagnose

Open `output/diagnosed/design_diagnostics.csv`. For each diagnostic, classify whether the observed difference most likely reflects:

- stability pressure;
- congestion and timing;
- applicant-side welfare;
- program priority or staffing;
- fairness and service placement;
- data requirements for an empirical design.

Answer three questions:

1. Which outcomes improve under centralized matching, and which remain ambiguous?
2. Which diagnostics require preference or priority data rather than match outcomes alone?
3. What labor-market welfare object is missing if the researcher observes only the final assignment?

### Transfer

Open `output/transfer/professional_market_design_transfer.csv`. The transfer exercise asks students to move the same architecture to neighboring professional labor markets:

- clinical psychology;
- specialist fellowships;
- judicial clerkships;
- rural public-service placement;
- platform-mediated professional projects.

Write a short memo answering:

- What is the institution?
- What is the failure mode?
- What data would reveal preferences, priorities, timing, matches, or outcomes?
- What counterfactual design should be compared?
- What welfare or fairness object matters?
- What is the main remaining threat?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing centralized matching and decentralized exploding offers;
- one paragraph explaining which diagnostics speak to stability, timing, and congestion;
- one paragraph explaining why stability is not the same as welfare;
- one transfer memo naming the institution, failure mode, data, counterfactual, welfare or fairness object, and main threat.
