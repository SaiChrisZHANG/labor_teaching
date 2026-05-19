# Code Lab 02: Experiments And Field Experiments As Research Designs

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 2 - Experiments and field experiments  
**Associated chapter:** `02-experiments-and-field-experiments.md`  
**Lab slug:** `02-experiments-and-field-experiments`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, randomized assignment, basic regression, basic `pandas`  
**Core economic question:** What does a randomized design identify once take-up, spillovers, attrition, and scale are made explicit?  
**Core design / estimator:** ITT, first stage, Wald/LATE, clustered exposure, and saturation logic  
**Source paper spine:** Duflo and Saez [@dufloSaez2003], Crepon et al. [@creponEtAl2013], Pallais [@pallais2014], and field-experiment design references [@harrisonList2004; @atheyImbens2017]

## Why This Lab Exists

The lecture argues that experiments are a design for building a counterfactual, not a generic claim that "randomized" means "done." This lab makes that discipline concrete. Students work with a synthetic workplace retirement-seminar encouragement design inspired by Duflo and Saez. The dataset contains randomized encouragement, realized attendance, retirement-plan participation, baseline covariates, department membership, peer exposure, and a small amount of outcome attrition.

The lab does not reproduce official published magnitudes. It reproduces the design logic: assignment is randomized, receipt is not; ITT differs from treatment-on-the-treated intuition; first stages matter; peer exposure can be a mechanism; and attrition must be shown rather than assumed away.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate ITT effects on treatment receipt and outcomes;
2. compute a first stage and Wald/LATE-style ratio in a randomized encouragement design;
3. explain why a naive receipt contrast is not the same as an experimental effect;
4. diagnose baseline balance, take-up, attrition, and exposure patterns;
5. write a short memo distinguishing assignment, receipt, and spillover interpretations;
6. transfer the same logic to a labor-market saturation design.

## Required Local Structure

```text
labs/02-experiments-and-field-experiments/
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
      encouragement_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      saturation_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_experiment_design.py
    transfer_spillover_design.py
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
python src/reproduce_experiment_design.py --input original/reduced/encouragement_synthetic.csv --outdir output/reproduced
python src/transfer_spillover_design.py --input transfer/data/saturation_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce The Design Logic

### Objective

Estimate what randomized encouragement identifies in a workplace seminar setting.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path and open `output/reproduced/experimental_estimates.csv`.
3. Compare the ITT on attendance, ITT on retirement-plan participation, first stage, Wald/LATE-style ratio, and naive attendance contrast.
4. Write a short paragraph explaining why the naive attendance contrast is not the experimental estimand.

### Required Questions

- What was randomized?
- What treatment was actually received?
- Is the ITT or the Wald/LATE-style ratio more relevant for a policy that can only invite workers?
- Who are the likely compliers in this design?
- What does the naive receipt contrast require us to believe?

### Minimum Output

- `output/reproduced/experimental_estimates.csv`;
- one paragraph describing the assignment margin;
- one sentence interpreting the first stage;
- one sentence explaining the difference between ITT and LATE.

## Part II. Diagnose The Design

### Objective

Move from "the experiment was randomized" to "the design is interpretable."

### Student Tasks

1. Open `output/reproduced/balance_by_assignment.csv`.
2. Open `output/reproduced/takeup_by_assignment.csv`.
3. Open `output/reproduced/attrition_by_assignment.csv`.
4. Open `output/reproduced/exposure_summary.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Does assignment produce reasonable baseline balance?
- How large is the first stage for seminar attendance?
- Does outcome attrition differ by assignment status?
- Is peer exposure balanced enough to interpret spillovers?
- Which estimate would you present as the main policy-relevant estimate?

### Minimum Output

- one baseline-balance paragraph;
- one take-up paragraph;
- one attrition paragraph;
- one exposure/spillover paragraph;
- one final interpretation sentence.

## Part III. Transfer The Design

### Objective

Use the same logic in a labor-market saturation design inspired by displacement and platform experiments.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_spillover_design.py`.
3. Open `output/transfer/saturation_estimates.csv`.
4. Compare direct assignment effects, market-saturation exposure effects, and untreated-worker exposure patterns.
5. Write a short design memo for a real-data version of the project.

### Required Prompts

- What is the unit of randomization?
- What is the treatment receipt margin?
- What spillover or displacement channel is most plausible?
- Should the main estimand be individual, cluster-level, or market-level?
- What extra design feature would help separate direct effects from equilibrium response?

### Minimum Output

- one transfer estimates table;
- one transfer exposure table;
- one design memo with assignment unit, estimand, spillover channel, and scale concern.

## Deliverables Checklist

- [ ] run log;
- [ ] reproduce estimates table;
- [ ] balance, take-up, attrition, and exposure diagnosis;
- [ ] one-page Diagnose memo;
- [ ] transfer estimates and exposure diagnostics;
- [ ] transfer design memo;
- [ ] final interpretation paragraph that states the estimand and main remaining threat.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Reproduction estimates and run log | 20 |
| Correct ITT, first-stage, and LATE interpretation | 25 |
| Balance, attrition, and spillover diagnosis | 25 |
| Transfer design memo | 20 |
| Code organization and communication | 10 |

## Instructor Notes

- The lab is intentionally synthetic so students can focus on design logic before wrestling with official replication-package details.
- The best class discussion asks whether the policy question is about assignment, receipt, peer exposure, or market-level rollout.
- The transfer exercise should stay bounded. Students should not turn Week 2 into a full equilibrium paper.
