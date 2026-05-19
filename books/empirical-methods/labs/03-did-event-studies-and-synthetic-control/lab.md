# Code Lab 03: DID, Event Studies, And Synthetic Control As Panel Designs

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 3 - DID, event studies, and synthetic control  
**Associated chapter:** `03-did-event-studies-and-synthetic-control.md`  
**Lab slug:** `03-did-event-studies-and-synthetic-control`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, fixed effects, basic regression, basic `pandas`  
**Core economic question:** Which observed path can credibly stand in for treated units' missing untreated path?  
**Core design / estimator:** 2x2 DID, event-study support, staggered-adoption group-time ATT, imputation-style DID, clustered inference, and synthetic control  
**Source paper spine:** Card and Krueger [@cardKrueger1994], Bertrand, Duflo, and Mullainathan [@bertrandDufloMullainathan2004], Goodman-Bacon [@goodmanBacon2021], Callaway and Sant'Anna [@callawaySantAnna2021], Sun and Abraham [@sunAbraham2021], Borusyak, Jaravel, and Spiess [@borusyakJaravelSpiess2024], and Abadie, Diamond, and Hainmueller [@abadieDiamondHainmueller2010]

## Why This Lab Exists

The lecture argues that DID, event studies, and synthetic control are counterfactual panel designs, not just regression formats. This lab makes that argument executable. Students work through a classical 2x2 DID, then diagnose why staggered timing and heterogeneous effects can make naive TWFE misleading, then transfer the same missing-path logic to synthetic control.

The lab does not reproduce official published magnitudes. It reproduces design logic: what comparison is being made, what it identifies, what can go wrong, and how inference choices affect credibility.

## Learning Objectives

By the end of this lab, students should be able to:

1. compute the canonical 2x2 DID contrast and match it to a regression coefficient;
2. state what the 2x2 DID identifies under parallel trends and no anticipation;
3. diagnose staggered-adoption timing, event-time support, and forbidden-comparison risk;
4. compare naive TWFE, group-time ATT, and imputation-style ATT estimates;
5. explain why clustering at the policy-assignment level changes inference;
6. build a small synthetic-control counterfactual and interpret donor weights, pre-fit, post-treatment gaps, and placebo gaps.

## Required Local Structure

```text
labs/03-did-event-studies-and-synthetic-control/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      card_krueger_synthetic.csv
      staggered_minimum_wage_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      synthetic_control_city.csv
  src/
    make_synthetic_data.py
    reproduce_did_event_study.py
    transfer_synthetic_control.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs three steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_did_event_study.py --card-input original/reduced/card_krueger_synthetic.csv --staggered-input original/reduced/staggered_minimum_wage_synthetic.csv --outdir output/reproduced
python src/transfer_synthetic_control.py --input transfer/data/synthetic_control_city.csv --outdir output/transfer
```

## Part I. Reproduce The Classical DID Logic

### Objective

Estimate what a Card-Krueger-style two-state, two-period DID identifies.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path and open `output/reproduced/card_krueger_did_estimates.csv`.
3. Compare the treated pre-post change, comparison pre-post change, DID contrast, and regression coefficient.
4. Open `output/reproduced/card_krueger_state_paths.csv` and inspect the plotted path in `card_krueger_paths.png`.
5. Write the interpretation sentence as an ATT under parallel trends.

### Required Questions

- What was treated?
- What is the comparison group?
- What untreated potential-outcome path is missing?
- What does the second difference replace?
- Why are state-level clusters the relevant warning even though the data contain many restaurants?

### Minimum Output

- `output/reproduced/card_krueger_did_estimates.csv`;
- one paragraph describing the 2x2 estimand;
- one sentence interpreting the DID estimate as an ATT;
- one sentence explaining why inference is fragile with very few policy clusters.

## Part II. Diagnose Staggered Adoption

### Objective

Move from a familiar TWFE regression to modern DID design logic.

### Student Tasks

1. Open `output/reproduced/modern_did_comparison.csv`.
2. Open `output/reproduced/group_time_att.csv`.
3. Open `output/reproduced/imputation_event_time_att.csv`.
4. Open `output/reproduced/event_time_support.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Which cohorts adopt early, late, or never?
- Why can already-treated cohorts be bad controls?
- Is the TWFE estimate close to the group-time or imputation-style estimate?
- Which event times have broad cohort support, and which rely on only a few cohorts?
- What clustering level is most defensible in this synthetic county panel?

### Minimum Output

- one comparison table;
- one event-time support paragraph;
- one estimator-choice paragraph;
- one inference paragraph;
- one final interpretation sentence that names the estimand.

## Part III. Transfer To Synthetic Control

### Objective

Use donor construction to build a counterfactual path for one treated city.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_synthetic_control.py`.
3. Open `output/transfer/synthetic_control_weights.csv`.
4. Open `output/transfer/synthetic_control_gaps.csv`.
5. Open `output/transfer/placebo_summary.csv`.
6. Write a short design memo for a real-data version of the project.

### Required Prompts

- What is the treated unit?
- What is the donor pool?
- Does the synthetic control fit before treatment?
- How large are post-treatment gaps relative to placebo gaps?
- What spillover or donor-contamination risk would matter in a real city-level policy?

### Minimum Output

- donor weight table;
- pre-treatment fit statistic;
- post-treatment gap table;
- placebo comparison table;
- one design memo with treated unit, donor pool, estimand, pre-fit, and main threat.

## Deliverables Checklist

- [ ] run log;
- [ ] 2x2 DID estimates table;
- [ ] modern DID comparison table;
- [ ] group-time ATT and imputation-style ATT diagnostics;
- [ ] event-time support table;
- [ ] one-page Diagnose memo;
- [ ] synthetic-control weights, gaps, and placebo summary;
- [ ] transfer design memo;
- [ ] final paragraph that states which counterfactual path is most defensible and why.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Classical DID reproduction and interpretation | 20 |
| Staggered-adoption diagnosis | 25 |
| Modern DID estimator choice and estimand clarity | 20 |
| Inference and clustering discussion | 15 |
| Synthetic-control transfer memo | 15 |
| Code organization and communication | 5 |

## Instructor Notes

- The lab is intentionally synthetic so students can focus on design logic before wrestling with official replication-package details.
- The best class discussion asks whether the comparison path, not the estimator, is doing credible causal work.
- The transfer exercise should stay bounded. Students should not turn Week 3 into a full synthetic-control paper.
