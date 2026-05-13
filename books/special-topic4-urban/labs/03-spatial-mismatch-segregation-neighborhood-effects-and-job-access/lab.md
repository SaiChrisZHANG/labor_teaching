# Week 3 Lab: Spatial Mismatch, Neighborhood Exposure, And Job Access

## Purpose

This lab turns Week 3 into a bounded empirical workflow. It does not replicate the confidential or full data in the anchor papers. Instead, it uses deterministic synthetic data to practice the objects behind age-at-move exposure designs and job-access shocks.

Primary anchor: Chetty, Hendren, and Katz on Moving to Opportunity [@chettyHendrenKatz2016MTO].

Challenge anchor: Miller on job suburbanization and Black employment [@millerWhenWorkMoves2023].

Optional frontier anchor: Bergman and coauthors on barriers to neighborhood choice [@bergmanChettyDeLucaEtAl2024].

## Workflow

### Reproduce

Run the synthetic exposure path and inspect `output/reproduced/exposure_timing_predictions.csv`.

The script creates a small set of families who move from a lower-opportunity origin to different destination neighborhoods at different child ages. It computes exposure as the share of childhood spent in the destination before age 18 and translates that exposure into a predicted adult labor outcome.

The object to reproduce is the chapter's exposure-timing logic:

```{math}
Y_i = \alpha + \theta \, \text{Exposure}_{ig} + \lambda_g + \varepsilon_i.
```

The exercise is deliberately small. Its goal is to make the age-at-move logic transparent: if neighborhood exposure is causal and timing is comparable, earlier movers should receive more of the destination treatment.

### Diagnose

Open `output/diagnosed/mechanism_diagnosis.csv`. For each claim, classify whether it is about:

- current job access;
- realized employment;
- residential sorting;
- school or institutional channels;
- referral networks;
- address stigma;
- broad neighborhood exposure.

Answer four questions for each row:

1. What is the labor-market object?
2. What is the counterfactual?
3. Which geography matters?
4. Which design family would isolate the mechanism most cleanly?

### Transfer

Open `output/transfer/job_suburbanization_access.csv`. The transfer exercise moves selected jobs from a central employment district to a suburban job center. It computes a simple access score before and after the shock:

```{math}
A_i = \sum_j v_j \exp\{-\kappa \tau_{ij}\}.
```

Interpret the result as an access shock, not as a realized-employment effect. Then write a short paragraph explaining:

- which residences gained or lost reachable vacancies;
- why the employment effect could differ from the access effect;
- what data would be needed to study networks or discrimination;
- how the same framework connects to Miller's job-suburbanization evidence [@millerWhenWorkMoves2023].

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs the complete bounded exercise and checks that the three output files were written. No confidential data or external downloads are required.

## Submission Checklist

- one table describing exposure timing and predicted adult outcomes;
- one paragraph distinguishing neighborhood exposure from residential sorting;
- one table describing access changes after job suburbanization;
- one paragraph distinguishing access from realized employment;
- one design memo naming a mechanism, counterfactual, geography, data source, and labor margin.
