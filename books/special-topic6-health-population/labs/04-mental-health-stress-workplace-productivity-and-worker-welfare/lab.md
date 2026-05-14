# Week 4 Lab: Mental Health, Stress, Workplace Productivity, And Worker Welfare

## Purpose

This lab turns the Week 4 lecture into a bounded mental-health and workplace-productivity exercise. It does not replicate official estimates in Bubonya, Cobb-Clark, and Wooden or in the job-meaning and identity literature. Instead, it uses deterministic synthetic data to practice how labor economists connect mental-health measures to absenteeism, presenteeism, performance, quits, accommodations, treatment, stigma, job quality, and welfare.

Primary anchor: Bubonya, Cobb-Clark, and Wooden on mental health and productivity at work [@bubonyaCobbClarkWooden2017].

Challenge paper: Kranton and Thomas on meaning, identity, and employee mental health [@krantonThomas2025].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/mental_health_productivity_profile.csv`.

The script creates a small worker panel with:

- mental-health distress measured as a symptom index and an observed high-distress indicator;
- job conditions including strain, autonomy, conflict, isolation, supervision support, schedule volatility, meaning, and stigma;
- treatment access, treatment use, disclosure, and accommodation;
- labor outcomes including absenteeism, presenteeism, performance, quit risk, safety incidents, and a welfare index.

The object to reproduce is a compact Bubonya-style descriptive profile:

```{math}
Y_{it} =
\alpha + \beta MH_{it} + \gamma Q_{it} + X_{it}'\delta + \varepsilon_{it},
```

where {math}`MH_{it}` is observed distress and {math}`Q_{it}` is job quality. The lab reports grouped profiles rather than claiming a causal estimate.

### Diagnose

Open `output/diagnosed/mental_health_mechanism_diagnosis.csv`. For each outcome, classify whether the observed association most likely reflects:

- productivity loss;
- work causing mental health;
- reporting or measurement bias;
- stigma and nondisclosure;
- treatment selection;
- job-quality confounding;
- dynamic selection into quits or lower-strain jobs.

Answer three questions:

1. Which outcomes look like productivity margins, and which look like welfare margins?
2. Where would stigma or disclosure change the interpretation of the same observed coefficient?
3. What comparison would help separate mental health affecting work from work affecting mental health?

### Transfer

Open `output/transfer/mental_health_design_transfer.csv`. The transfer exercise asks students to move the same logic to six settings:

- treatment-access shock;
- waiting-time shock;
- job-loss event study;
- pandemic or workplace reorganization shock;
- disclosure or destigmatization intervention;
- structural job-search model with mental health and job quality.

Write a short memo answering:

- What is the latent mental-health object?
- What is the labor outcome?
- What identifies the design?
- What is the main remaining threat?
- What welfare margin would wages or employment miss?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing absenteeism, presenteeism, performance, quits, accommodations, and welfare by observed distress;
- one paragraph explaining why the profile is not automatically causal;
- one paragraph separating stigma, disclosure, and treatment selection;
- one paragraph on how job quality can cause mental-health outcomes;
- one transfer paragraph naming a labor outcome, identifying variation, main threat, and welfare object.
