# Week 5 Lab: Disease Exposure, Environmental Health, Demographic Change, And Labor-Market Adjustment

## Purpose

This lab turns the Week 5 lecture into a bounded labor-incidence exercise. It does not replicate official estimates in Albanesi and Kim or Chicoine. Instead, it uses deterministic synthetic data to practice how labor economists connect disease exposure, environmental risk, demographic structure, occupation, care burden, migrant vulnerability, migration, firm response, and worker welfare.

Primary anchor: Albanesi and Kim on COVID labor-market incidence and unequal employment effects [@albanesiKim2021].

Challenge paper: Chicoine on HIV/AIDS mortality and labor-market outcomes in South Africa [@chicoine2012].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/labor_market_incidence_profile.csv`.

The script creates a local labor-market panel with:

- disease exposure, policy intensity, environmental exposure, aging share, dependency structure, and remote-work feasibility;
- worker-group indicators for frontline work, migrant vulnerability, care burden, older-worker concentration, and environmental risk;
- labor outcomes including employment, hours, wages, productivity, migration, automation adoption, remote work, and welfare loss.

The object to reproduce is a compact COVID-style incidence profile:

```{math}
\Delta Y_{rg} =
\alpha
+ \beta_1 Exposure_{rg}
+ \beta_2 RemoteFeasible_g
+ \beta_3 CareBurden_g
+ \beta_4 MigrantShare_g
+ \beta_5 Demography_r
+ u_{rg},
```

where {math}`Y_{rg}` is a labor outcome for worker group {math}`g` in region {math}`r`. The lab reports grouped profiles rather than claiming causal estimates.

### Diagnose

Open `output/diagnosed/adjustment_mechanism_diagnosis.csv`. For each pattern, classify whether the observed movement most likely reflects:

- direct disease risk;
- policy or demand collapse;
- caregiving constraint;
- occupational sorting;
- migration selection or immobility;
- firm reorganization or automation;
- environmental exposure;
- demographic pressure;
- hidden welfare incidence.

Answer three questions:

1. Which groups show the largest employment or hours losses during the shock?
2. Which groups show hidden welfare losses that are larger than their wage changes?
3. Which patterns would be hard to interpret without data on policy, demand, migration, or health risk?

### Transfer

Open `output/transfer/disease_environment_demography_design_transfer.csv`. The transfer exercise asks students to move the same logic to seven settings:

- Black Death labor scarcity;
- tuberculosis reporting laws and early public health;
- HIV/AIDS mortality and skill premia;
- pollution and worker productivity;
- heat and manufacturing labor supply;
- migrant vulnerability during epidemic shocks;
- aging, automation, and retirement.

Write a short memo answering:

- What is the shock?
- What is the labor outcome?
- What data would be needed?
- What comparison group or exposure gradient would identify the design?
- What is the main remaining threat?
- What welfare margin would wages or employment miss?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table comparing employment, hours, productivity, wages, migration, automation, and welfare across exposure groups;
- one paragraph explaining why a COVID-style labor estimate bundles health risk, policy, demand, and care constraints;
- one paragraph on migration as both adjustment and selection;
- one paragraph connecting environmental exposure to hidden productivity or welfare incidence;
- one transfer paragraph naming a shock, labor outcome, identifying variation, main threat, and welfare object.
