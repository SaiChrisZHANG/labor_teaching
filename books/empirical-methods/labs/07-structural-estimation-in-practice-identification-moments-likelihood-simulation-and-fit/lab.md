# Code Lab 07: Structural Estimation In Practice

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 7 - structural estimation in practice  
**Associated chapter:** `07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.md`  
**Lab slug:** `07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** discrete choice, likelihood, GMM intuition, bootstrap basics, basic `pandas`  
**Core economic question:** How do researchers take a structural model to data credibly?  
**Core design / estimator:** likelihood, moments/GMM, simulated method of moments, targeted fit, bootstrap, and delta-method counterfactual uncertainty  
**Source paper spine:** Rust [@rust1987optimal], Pakes and Pollard [@pakes1989simulation], Gourieroux, Monfort, and Renault [@gourieroux1993indirect], Todd and Wolpin [@todd2006assessing], and Adda, Dustmann, and Stevens [@adda2017career]

## Why This Lab Exists

Lecture 7 argues that structural credibility comes from the full chain: identification -> estimation -> fit -> counterfactual discipline -> inference. This lab makes each link executable. Students first work with a reduced replacement panel inspired by Rust. The exercise compares likelihood and moments estimators, shows how weighting changes the moment criterion, reports targeted and untargeted fit, and uses bootstrap and delta-method logic for a counterfactual.

Students then transfer the same logic to a simplified schooling/work lifecycle model. The transfer is deliberately bounded. It uses simulated moments to show how a dynamic model can match schooling rates and lifecycle summaries before producing a tuition-subsidy counterfactual. It is not a full Todd-Wolpin or Adda-Dustmann-Stevens replication.

## Learning Objectives

By the end of this lab, students should be able to:

1. construct likelihood and moment criteria for a small structural model;
2. explain which moments identify replacement and maintenance primitives;
3. compare identity-weighted, diagonally weighted, and simulated moment estimates;
4. distinguish targeted fit from untargeted validation;
5. run a cluster bootstrap that respects unit histories;
6. use a numerical delta-method approximation for a counterfactual function;
7. diagnose simulation noise in an SMM criterion;
8. transfer the same implementation logic to a dynamic schooling/work example.

## Required Local Structure

```text
labs/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit/
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
      replacement_estimation_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      schooling_lifecycle_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_estimation_fit_inference.py
    transfer_smm_lifecycle.py
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
python src/reproduce_estimation_fit_inference.py --input original/reduced/replacement_estimation_synthetic.csv --outdir output/reproduced
python src/transfer_smm_lifecycle.py --input transfer/data/schooling_lifecycle_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce Estimation Logic

### Objective

Estimate a small replacement model using likelihood, GMM-style moments, and simulated moments.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/likelihood_estimates.csv`.
4. Open `output/reproduced/moment_estimates.csv`.
5. Compare `output/reproduced/targeted_moment_fit.csv` with `output/reproduced/untargeted_fit.csv`.
6. Inspect `output/reproduced/replacement_fit.png`.

### Required Questions

- What is observed?
- What is latent?
- Which observed variation disciplines replacement cost?
- Which moments are targeted?
- What changes when the weighting matrix changes?
- What does the likelihood criterion use that the moment criterion summarizes?
- Why is this not an official Rust replication?

### Minimum Output

- one paragraph mapping observed variation to latent primitives;
- one table or paragraph comparing likelihood, GMM, and SMM estimates;
- one paragraph explaining targeted and untargeted fit;
- one sentence naming the main implementation caveat.

## Part II. Diagnose Fit And Inference

### Objective

Evaluate whether the reduced model is credible enough for a bounded replacement-cost counterfactual.

### Student Tasks

1. Open `output/reproduced/weighting_sensitivity.csv`.
2. Open `output/reproduced/bootstrap_estimates.csv`.
3. Open `output/reproduced/counterfactual_uncertainty.csv`.
4. Open `output/reproduced/variance_summary.csv`.
5. Open `output/reproduced/simulation_noise.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Does weighting materially change the estimates?
- Are high-mileage states well supported?
- Does the bootstrap resample at the right level?
- How different are delta-method and bootstrap uncertainty for the counterfactual?
- Does simulation noise appear large relative to sampling uncertainty?
- What uncertainty is still not fully represented?

### Minimum Output

- one weighting paragraph;
- one targeted-versus-untargeted fit paragraph;
- one inference paragraph comparing bootstrap, delta method, and simulation checks;
- one final sentence stating whether the counterfactual is close to observed support.

## Part III. Transfer To A Lifecycle Schooling/Work Model

### Objective

Use simulated moments to estimate a reduced schooling/work model and run a tuition-subsidy counterfactual.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/smm_estimates.csv`.
3. Open `output/transfer/smm_moment_fit.csv`.
4. Open `output/transfer/policy_transfer_summary.csv`.
5. Inspect `output/transfer/schooling_counterfactual_paths.png`.
6. Write a short Transfer memo.

### Required Prompts

- What are the states?
- What are the actions?
- Which moments discipline tuition sensitivity?
- What does the simulated estimator hold fixed?
- What lifecycle features are missing?
- What validation evidence would a publishable paper need?

### Minimum Output

- one state/action paragraph;
- one simulated-moments fit paragraph;
- one tuition-subsidy counterfactual paragraph;
- one paragraph on why this transfer is pedagogical rather than a frontier replication.

## Deliverables Checklist

- [ ] run log;
- [ ] likelihood and moment estimates;
- [ ] targeted moment fit table;
- [ ] untargeted fit table;
- [ ] replacement fit figure;
- [ ] weighting sensitivity memo;
- [ ] bootstrap and delta-method inference memo;
- [ ] simulation-noise diagnostic;
- [ ] SMM transfer fit table;
- [ ] tuition-subsidy transfer counterfactual;
- [ ] final paragraph stating what the model identifies and what remains assumption-dependent.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Identification map and estimator comparison | 25 |
| Moment targeting, weighting, and fit interpretation | 25 |
| Inference and uncertainty discussion | 25 |
| Transfer to lifecycle SMM design | 15 |
| Code organization and communication | 10 |

## Instructor Notes

- The replacement panel is synthetic and intentionally small enough for local smoke testing.
- The bootstrap is a teaching cluster bootstrap: it resamples units and re-estimates a reduced-grid moment estimator.
- The delta-method calculation uses a numerical gradient and bootstrap covariance. This makes the approximation visible.
- The transfer model omits many objects that a publishable lifecycle paper would need, including borrowing constraints, fertility, occupations, expectations, and equilibrium wage response.
