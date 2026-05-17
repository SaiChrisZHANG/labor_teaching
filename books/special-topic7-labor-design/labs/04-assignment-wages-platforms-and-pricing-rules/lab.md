# Week 4 Lab: Assignment, Wages, Platforms, And Pricing Rules

## Purpose

This lab turns the platform and assignment lecture into a student-facing empirical design workflow. It does not replicate official estimates in Pallais, Barach and Horton, Horton, Johari, and Kircher, or any platform's internal experiment. Instead, it uses deterministic synthetic data to practice how labor economists move from a platform rule to observable assignment, wage, reputation, and worker-welfare margins.

Primary anchor: Pallais on information and entry-level online hiring [@pallais2014].

Challenge anchor: platform steering and guarantees in Barach and Horton [@barachHorton2019steering]. Wage-rule extensions can use compensation history, pay transparency, or platform minimum-wage designs [@barachHorton2021compensationHistory; @arnoldQuachTaska2025payTransparency; @horton2025minimumWage].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/visibility_information_summary.csv`.

The script creates a small platform-market panel with:

- inexperienced and experienced workers;
- a randomized public-signal and ranking-lift treatment for inexperienced workers;
- visibility scores, employer invitations, applications, hires, accepted wages, future jobs, and earnings risk;
- a separate steering and guarantee scenario for the transfer path.

The object to reproduce is a reduced information and visibility fact:

```{math}
\Delta \bar y =
\bar y_{\text{treated inexperienced workers}} -
\bar y_{\text{control inexperienced workers}}.
```

The exercise is pedagogical. It reproduces the design logic of a platform information experiment, not the official estimates of the anchor paper.

### Diagnose

Open `output/diagnosed/assignment_information_diagnostics.csv`, `output/diagnosed/rule_incidence_diagnostics.csv`, and `output/diagnosed/worker_welfare_components.csv`.

For each diagnostic, classify whether the observed difference most likely reflects:

- mechanical exposure from ranking or visibility;
- employer belief updating from a public signal;
- worker sorting or platform selection;
- wage bargaining or posted-price response;
- future reputation accumulation;
- earnings volatility and risk shifting;
- platform steering or governance.

Answer four questions:

1. Which margins are observed directly in the synthetic data?
2. Which hidden objects remain latent even after the rule change?
3. How much of the raw hiring difference should be interpreted as information rather than exposure?
4. What welfare object would change the interpretation: earnings, flexibility, risk, match quality, or future access to work?

### Transfer

Open `output/transfer/platform_rule_transfer.csv`. The transfer exercise asks students to move the same architecture to neighboring labor settings:

- platform guarantees or endorsements;
- search ranking or recommendation rules;
- compensation-history disclosure;
- wage transparency in job posts;
- platform wage floors or minimum pay rules;
- dynamic pricing and flexibility in ride-hailing;
- monitoring, dispute, or deactivation governance.

Write a short memo answering:

- What platform or intermediary rule changed?
- What labor margin captures the effect?
- What counterfactual rule is needed?
- What experimental or quasi-experimental variation identifies it?
- What competing mechanisms must be separated?
- What worker welfare object matters?
- What is the main remaining threat?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing treated and control inexperienced workers on invitations, hires, wages, future jobs, and risk;
- one paragraph separating exposure effects from information or belief effects;
- one paragraph explaining why average earnings are not enough for worker welfare;
- one transfer memo naming the rule, margin, counterfactual, identification strategy, welfare object, and main threat.
