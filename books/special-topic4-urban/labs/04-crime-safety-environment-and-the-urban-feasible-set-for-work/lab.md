# Week 4 Lab: Crime, Safety, Environment, And The Urban Feasible Set For Work

## Purpose

This lab turns Week 4 into a bounded empirical workflow. It does not replicate confidential microdata or official estimates. Instead, it uses deterministic synthetic data to practice the design objects behind displacement-to-crime and environment-to-productivity research.

Primary anchor: Khanna, Medina, Nyshadham, and Tamayo on job loss, credit, and crime in Colombia [@khannaMedinaNyshadhamTamayo2021].

Transfer anchors: Hanna and Oliva on pollution and labor supply, Graff Zivin and Neidell on pollution and worker productivity, and Chang, Graff Zivin, Gross, and Neidell on pollution and call-center productivity [@hannaOliva2015; @graffZivinNeidell2012; @changGraffZivinGrossNeidell2019].

## Workflow

### Reproduce

Run the synthetic displacement path and inspect `output/reproduced/displacement_crime_event_study.csv`.

The script creates a small panel of displaced and comparison workers around an event date. It computes formal earnings, a legal-opportunity index, credit stress, and a crime-risk index. The object is an event-study-style comparison:

```{math}
Y_{it}
=
\alpha_i
+ \lambda_t
+ \sum_{k \neq -1} \beta_k
\mathbf{1}\{t - T_i = k\} \times \text{Displaced}_i
+ \varepsilon_{it}.
```

The exercise asks whether the post-displacement pattern is consistent with the labor-opportunity-to-crime channel. It also asks what else changed: earnings, credit stress, local risk, household liquidity, and reporting or enforcement.

### Diagnose

Open `output/diagnosed/risk_mechanism_diagnosis.csv`. For each claim, classify whether it is about:

- risk changing labor supply;
- labor opportunity changing crime or risky activity;
- workplace harassment or violence;
- environmental exposure and productivity;
- sorting and capitalization;
- welfare rather than nominal wages.

Answer four questions for each row:

1. What is the labor-market object?
2. What is the counterfactual?
3. Which data source would measure the mechanism directly?
4. What is the main interpretation threat?

### Transfer

Open `output/transfer/environment_productivity_transfer.csv`. The transfer exercise uses worker-day observations with heat, pollution, and noise exposure. It computes predicted hours and output under different exposure conditions. Interpret the result as an exposure-to-productivity design, not as a wage equation.

Then open `output/transfer/risk_adjusted_job_ranking.csv`. Compare the nominal wage ranking with the risk-adjusted value ranking:

```{math}
V_{ijr}
=
w_j
- R_r
- \tau_{ijr}
- \rho^S_{ijr}
- \rho^E_{ijr}
+ A_r.
```

The goal is to see why wages alone can misstate welfare when risk and exposure differ.

## Bounded Extension

Add a commute-safety shock to the synthetic job ranking. Hold wages fixed, raise route risk for late shifts, and recompute the risk-adjusted value of each job. Write a short memo explaining whether the shock changes employment, feasible shifts, search radius, or welfare.

Keep the extension bounded. Do not turn it into a full crime model unless you can name the source of variation, the affected labor margin, and the counterfactual.

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs the complete bounded exercise and checks that the core output files were written. No confidential data or external downloads are required.

## Submission Checklist

- one table describing event-time changes in earnings, legal opportunity, credit stress, and crime risk;
- one paragraph distinguishing opportunity-cost mechanisms from credit, reporting, and enforcement mechanisms;
- one table describing heat, pollution, noise, hours, and productivity;
- one table comparing nominal wage rankings with risk-adjusted job rankings;
- one design memo naming the mechanism, counterfactual, geography, data source, and welfare object.
