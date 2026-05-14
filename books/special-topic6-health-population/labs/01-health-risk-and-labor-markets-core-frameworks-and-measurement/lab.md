# Week 1 Lab: Health Measures And Labor Supply Identification

## Purpose

This lab turns the Week 1 framework into a bounded measurement exercise. It does not replicate the official data or estimates in Blundell, Britton, Costa Dias, and French or Bound. Instead, it uses deterministic synthetic data to practice how labor economists compare health measures before interpreting a labor-supply or welfare estimate.

Primary anchor: Blundell, Britton, Costa Dias, and French on how health measurement changes employment estimates near retirement [@blundellBrittonCostaDiasFrench2023].

Measurement challenge: Bound's comparison of self-reported and objective health measures in retirement models [@bound1991].

## Workflow

### Reproduce

Run the synthetic measurement path and inspect `output/reproduced/health_measure_labor_gradient.csv`.

The script creates a small worker-level teaching data set with:

- latent work capacity;
- self-reported poor health;
- diagnosed condition severity;
- biomarker risk;
- administrative disability status;
- mortality-risk proxy;
- mental-health burden;
- insurance and treatment access;
- employment, hours, and feasible job counts.

The object to reproduce is the chapter's measurement discipline:

```{math}
Y_i =
\beta H_i
+ X_i'\Gamma
+ \varepsilon_i.
```

The lab compares estimates across health measures. It does not claim to recover a full structural model or official replication estimate.

### Diagnose

Open `output/diagnosed/measurement_bias_diagnostics.csv`. For each measure, compare:

- correlation with latent work capacity;
- correlation with socioeconomic status;
- whether the measure is subjective, clinical, administrative, severe-shock-based, latent-condition-sensitive, or institutionally mediated;
- the main threat to interpretation.

Answer three questions:

1. Which measure is closest to work capacity?
2. Which measure is most contaminated by labor-market status or program rules?
3. Which measure would you use for employment, hours, job choice, productivity, or worker welfare?

The diagnostic lesson is that "objective" does not automatically mean "better." A biomarker can be clinically clean but weakly tied to a job's feasible set. A self-report can be subjective but closer to pain, fatigue, or daily functioning.

### Transfer

Open `output/transfer/health_design_transfer.csv`. The transfer exercise asks students to move the same measurement logic to four settings:

- acute hospitalization;
- disability onset;
- mental-health treatment timing;
- insurance-linked treatment access.

Write a short memo answering:

- What is the labor outcome?
- What is the measured health object?
- What comparison group or timing variation would identify the design?
- What reverse-causality, omitted-SES, or dynamic-selection problem remains?
- What worker-side and firm-side channels might be mixed in the estimate?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing at least three health measures and their labor gradients;
- one paragraph explaining why health measurement changes the interpretation of a labor-supply coefficient;
- one paragraph diagnosing reverse causality, omitted socioeconomic status, and dynamic selection;
- one transfer paragraph linking a health measure to a labor margin and a feasible design.
