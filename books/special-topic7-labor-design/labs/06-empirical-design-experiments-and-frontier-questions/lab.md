# Week 6 Lab: Empirical Design, Experiments, And Frontier Questions

## Purpose

This capstone lab turns the course into a student-facing research-design workflow. It does not replicate official estimates in Agarwal or Davis, Greenberg, and Jones. Instead, it uses deterministic synthetic teaching data to practice how labor economists move from a matching or assignment mechanism to an empirical object, a counterfactual, an equilibrium diagnosis, and a welfare claim.

Primary anchor: Agarwal on empirical evaluation of the medical match [@agarwal2015].

Challenge anchor: Davis, Greenberg, and Jones on deferred acceptance in Army officer labor markets [@davisGreenbergJones2026].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/matching_counterfactual_summary.csv`.

The script creates a small professional-entry matching dataset with:

- applicants with preferences, ability, service orientation, location preferences, outside options, and risk exposure;
- programs with capacity, training value, shortage pressure, location type, and priority weights;
- a deferred-acceptance-style assignment rule;
- a decentralized early-offer rule;
- predicted match quality, worker welfare, program staffing value, and shortage-site assignment.

The object to reproduce is a reduced counterfactual comparison:

```{math}
\Delta \bar y =
\bar y_{\text{deferred acceptance}}
-
\bar y_{\text{early offers}}.
```

The exercise is pedagogical. It reproduces the design logic of a matching counterfactual, not the official structural estimates from the anchor paper.

### Diagnose

Open `output/diagnosed/mechanism_counterfactual_diagnostics.csv` and `output/diagnosed/equilibrium_portability_diagnostics.csv`.

For each diagnostic, classify whether the observed difference most likely reflects:

- direct assignment effects;
- worker ranking or strategic response;
- program priority alignment;
- shortage-site staffing;
- congestion and reallocation across applicants;
- outside options and acceptance behavior;
- a welfare object that is partly modeled rather than directly observed.

Answer four questions:

1. Which objects are observed directly in the synthetic data?
2. Which objects would require confidential administrative, platform, or survey data in a real project?
3. When does a better assigned rank fail to imply higher welfare?
4. What equilibrium response would most threaten portability to another labor market?

### Transfer

Open `output/transfer/frontier_research_designs.csv`. The transfer exercise asks students to move the same architecture to neighboring labor-market design settings:

- platform ranking and wage disclosure;
- recruiting timing and exploding-offer rules;
- pay transparency or compensation-history policies;
- teacher and public-service placement;
- internal assignment and promotion markets;
- AI-assisted screening and recommendations.

Write a short memo answering:

- What rule changed?
- What mechanism does the rule move?
- What labor margin captures the effect?
- What counterfactual rule is needed?
- What data are required?
- What spillovers or equilibrium responses matter?
- What welfare object makes the project a labor-economics paper?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing deferred acceptance and early offers on assigned rank, top-three assignment, priority alignment, match quality, shortage staffing, program value, and worker welfare;
- one paragraph explaining why the same assignment improvement may have different welfare interpretations for workers, programs, and public agencies;
- one paragraph diagnosing direct effects, behavioral response, and equilibrium adjustment;
- one transfer memo naming the rule, mechanism, labor margin, counterfactual, data requirement, spillover threat, welfare object, and portability argument.
