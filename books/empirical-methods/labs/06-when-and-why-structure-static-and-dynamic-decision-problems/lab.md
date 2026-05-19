# Code Lab 06: When And Why Structure? Static And Dynamic Decision Problems

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 6 - structural estimation, static and dynamic decision problems  
**Associated chapter:** `06-when-and-why-structure-static-and-dynamic-decision-problems.md`  
**Lab slug:** `06-when-and-why-structure-static-and-dynamic-decision-problems`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** discrete choice, basic likelihood logic, dynamic programming intuition, basic `pandas`  
**Core economic question:** What does structure buy when the object of interest is latent, dynamic, or outside observed support?  
**Core design / estimator:** dynamic discrete choice, conditional choice probabilities, likelihood-style fit, model diagnostics, and a bounded policy counterfactual  
**Source paper spine:** Rust [@rust1987optimal], Hotz and Miller [@hotz1993conditional], Keane and Wolpin [@keane1997career], Todd and Wolpin [@todd2006assessing], and Keane [@keane2010structural]

## Why This Lab Exists

The lecture argues that structure is useful when the research object is not directly observed. This lab makes that concrete. Students first work with a synthetic replacement panel inspired by Rust. They observe states and choices, but they do not observe replacement costs, continuation values, or the value of waiting. A simple dynamic model maps those latent objects into replacement probabilities.

Students then transfer the same logic to a small career-choice setting inspired by dynamic human-capital models. The transfer is deliberately bounded. The goal is not to estimate a production-grade lifecycle model. The goal is to make students name states, actions, expectations, transition rules, and policy-counterfactual limits.

## Learning Objectives

By the end of this lab, students should be able to:

1. compute empirical conditional choice probabilities by state;
2. solve a small dynamic logit replacement model;
3. estimate structural parameters with a likelihood-style objective;
4. compare static choice fit with dynamic-choice fit;
5. explain what observed state transitions discipline and what remains assumed;
6. run a replacement-cost counterfactual and interpret its support;
7. transfer the same logic to a simplified schooling/work career-choice setting.

## Required Local Structure

```text
labs/06-when-and-why-structure-static-and-dynamic-decision-problems/
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
      replacement_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      career_choice_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_dynamic_choice.py
    transfer_career_choice.py
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
python src/reproduce_dynamic_choice.py --input original/reduced/replacement_synthetic.csv --outdir output/reproduced
python src/transfer_career_choice.py --input transfer/data/career_choice_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce Dynamic Replacement Logic

### Objective

Estimate a small dynamic discrete-choice model in which a manager chooses whether to continue operating a capital good or replace it.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/replacement_state_ccps.csv`.
4. Open `output/reproduced/replacement_estimates.csv`.
5. Inspect `output/reproduced/replacement_fit.png`.
6. Write the interpretation sentence for the estimated replacement-cost parameter.

### Required Questions

- What is the state variable?
- What is the action set?
- What is observed by the econometrician?
- What is latent?
- Which moments discipline replacement cost?
- Which moments discipline maintenance cost?
- What does a static hazard miss?

### Minimum Output

- one paragraph describing the dynamic decision problem;
- one sentence interpreting the estimated replacement cost;
- one sentence explaining continuation value;
- one paragraph comparing empirical and model-implied replacement probabilities.

## Part II. Diagnose The Structural Model

### Objective

Evaluate whether the dynamic replacement model is credible enough for a bounded counterfactual.

### Student Tasks

1. Open `output/reproduced/state_support.csv`.
2. Open `output/reproduced/likelihood_surface.csv`.
3. Open `output/reproduced/counterfactual_replacement_cost.csv`.
4. Write a one-page Diagnose memo.

### Required Prompts

- Are high-mileage states well supported?
- Does the likelihood surface have a clear optimum or a flat region?
- Which assumptions are imposed by the transition matrices?
- What does the lower replacement-cost counterfactual change?
- Is the counterfactual close to the observed support?
- What would you want to validate in a real replacement or job-search paper?

### Minimum Output

- one state-support paragraph;
- one likelihood/fit paragraph;
- one counterfactual interpretation paragraph;
- one final sentence naming what the model can and cannot identify.

## Part III. Transfer To Career Choice

### Objective

Use the same structural vocabulary for a simplified schooling/work career-choice problem.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_career_choice.py`.
3. Open `output/transfer/career_choice_moments.csv`.
4. Open `output/transfer/career_choice_model.csv`.
5. Open `output/transfer/tuition_subsidy_counterfactual.csv`.
6. Write a short transfer memo.

### Required Prompts

- What are the states?
- What are the actions?
- What is the latent object?
- What does tuition variation discipline?
- What dynamic feedback is included?
- What dynamic feedback is missing?
- Why is this transfer path not a full Keane-Wolpin replication?

### Minimum Output

- career-choice moments table;
- one state/action paragraph;
- one tuition-subsidy counterfactual paragraph;
- one paragraph on model dependence and missing validation.

## Deliverables Checklist

- [ ] run log;
- [ ] replacement conditional choice probability table;
- [ ] dynamic parameter estimates;
- [ ] static-versus-dynamic fit comparison;
- [ ] state support diagnostics;
- [ ] replacement-cost counterfactual;
- [ ] dynamic replacement Diagnose memo;
- [ ] career-choice moments and fitted choice model;
- [ ] tuition-subsidy transfer counterfactual;
- [ ] final paragraph stating what structure identifies and what remains assumption-dependent.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| State/action/latent-object interpretation | 25 |
| Dynamic-choice and continuation-value logic | 20 |
| Likelihood and fit diagnostics | 20 |
| Counterfactual interpretation and support | 20 |
| Transfer to career-choice design | 10 |
| Code organization and communication | 5 |

## Instructor Notes

- The replacement data are synthetic so students can compare empirical behavior with a known small state space.
- The dynamic estimator fixes the discount factor and estimates a small number of primitives. This keeps the lab pedagogical.
- The transfer path is a simplified dynamic policy exercise, not a full lifecycle model.
- The lab should be evaluated on research-design interpretation, not on reproducing published magnitudes.
