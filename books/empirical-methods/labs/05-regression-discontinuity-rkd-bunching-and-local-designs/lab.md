# Code Lab 05: Regression Discontinuity, RKD, Bunching, And Local Designs

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 5 - regression discontinuity, RKD, bunching, and local designs  
**Associated chapter:** `05-regression-discontinuity-rkd-bunching-and-local-designs.md`  
**Lab slug:** `05-regression-discontinuity-rkd-bunching-and-local-designs`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, basic regression, local linear estimation, basic `pandas`  
**Core economic question:** When does a threshold create a credible local counterfactual, and what does the resulting estimate identify?  
**Core design / estimator:** sharp RD, local polynomial estimation, bandwidth and kernel sensitivity, covariate continuity, density diagnostics, robust-bias-correction-style and honest-inference-style diagnostics, and bunching around a kink  
**Source paper spine:** Lee [@lee2008], Calonico, Cattaneo, and Titiunik [@calonicoCattaneoTitiunik2014], Armstrong and Kolesar [@armstrongKolesar2020], Gelman and Imbens [@gelmanImbens2019], Saez [@saez2010], and Kleven [@kleven2016]

## Why This Lab Exists

The lecture argues that RD-style methods are local design logic, not a collection of commands. This lab makes that concrete. Students first reproduce a Lee-style close-election RD on a deterministic synthetic dataset. They estimate the local jump at the winning threshold, inspect bandwidth and kernel choices, check predetermined covariates, and diagnose the density of the running variable near zero.

Students then transfer the local-design logic to bunching around a tax kink. The transfer path estimates excess mass relative to a counterfactual density and maps it into a stylized elasticity. The key lesson is that bunching is not model-free: the estimate depends on the counterfactual density and an optimization model.

The lab does not reproduce official published magnitudes. It reproduces design decisions: what the threshold does, what the local estimand is, what can go wrong, and what the estimate means.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate and interpret a local linear sharp RD;
2. explain how bandwidth and kernel choices change the effective comparison;
3. diagnose covariate continuity and running-variable density near a cutoff;
4. explain why high-order global polynomials are not a preferred RD strategy;
5. distinguish conventional, robust-bias-correction-style, and honest-inference-style diagnostics;
6. estimate excess mass around a tax kink relative to a counterfactual density;
7. explain why bunching elasticities depend on behavioral assumptions.

## Required Local Structure

```text
labs/05-regression-discontinuity-rkd-bunching-and-local-designs/
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
      close_election_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      tax_kink_bunching_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_rd_design.py
    transfer_bunching_design.py
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
python src/reproduce_rd_design.py --input original/reduced/close_election_synthetic.csv --outdir output/reproduced
python src/transfer_bunching_design.py --input transfer/data/tax_kink_bunching_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce The RD Logic

### Objective

Estimate the local effect of barely winning an election on next-election vote share.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/rd_estimates.csv`.
4. Open `output/reproduced/bandwidth_kernel_sensitivity.csv`.
5. Inspect `output/reproduced/close_election_rd_plot.png`.
6. Write the interpretation sentence for the local RD estimate.

### Required Questions

- What is the running variable?
- What is the cutoff?
- What is the treatment?
- What is the outcome?
- Why is the estimand local?
- What does the estimate not identify?

### Minimum Output

- one paragraph describing the local comparison;
- one sentence interpreting the RD estimate at the threshold;
- one sentence explaining what the estimate does not identify;
- one bandwidth sensitivity note.

## Part II. Diagnose The RD Design

### Objective

Evaluate whether the local comparison is credible.

### Student Tasks

1. Open `output/reproduced/covariate_continuity.csv`.
2. Open `output/reproduced/density_check.csv`.
3. Open `output/reproduced/density_bins_near_cutoff.csv`.
4. Open `output/reproduced/global_polynomial_pitfall.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Are predetermined covariates smooth at the cutoff?
- Is there evidence of bunching or sorting in the running variable?
- How does the estimate move when the bandwidth changes?
- Why is the global fourth-order polynomial included only as a warning?
- What is the difference between the local-quadratic bias diagnostic and production `rdrobust`?
- What smoothness assumption is being made in the honest-interval teaching diagnostic?
- At what level would inference be clustered in a real close-election design?

### Minimum Output

- one covariate-continuity paragraph;
- one density/manipulation paragraph;
- one bandwidth and kernel paragraph;
- one inference paragraph;
- one final interpretation sentence naming the estimand.

## Part III. Transfer To Bunching

### Objective

Use threshold logic to estimate behavioral response around a tax kink.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_bunching_design.py`.
3. Open `output/transfer/bunching_estimates.csv`.
4. Open `output/transfer/bunching_sensitivity.csv`.
5. Inspect `output/transfer/tax_kink_bunching_plot.png`.
6. Write a short transfer memo.

### Required Prompts

- Is the threshold a kink or a notch?
- What is the counterfactual density?
- Which bins are excluded when fitting the counterfactual?
- How sensitive is excess mass to bin width and polynomial degree?
- What behavioral assumptions are needed to interpret the elasticity?
- What would change if the response reflected reporting rather than real earnings behavior?

### Minimum Output

- bunching estimates table;
- one counterfactual-density paragraph;
- one elasticity interpretation paragraph;
- one paragraph on model dependence and fragility.

## Deliverables Checklist

- [ ] run log;
- [ ] RD estimates table;
- [ ] bandwidth and kernel sensitivity table;
- [ ] covariate continuity table;
- [ ] density check;
- [ ] RD Diagnose memo;
- [ ] bunching estimates and sensitivity tables;
- [ ] bunching transfer memo;
- [ ] final paragraph stating what each design identifies and what it does not.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| RD estimand and local interpretation | 25 |
| Bandwidth, kernel, and polynomial discipline | 20 |
| Covariate continuity and density diagnostics | 20 |
| Inference and modern RD diagnostic interpretation | 15 |
| Bunching counterfactual density and elasticity logic | 15 |
| Code organization and communication | 5 |

## Instructor Notes

- The RD data are synthetic so students can see the true cutoff effect after estimating it. In real projects the true effect is never observed.
- The robust-bias-correction-style and honest-interval rows are deliberately pedagogical. They teach the logic but do not replace production `rdrobust` or `rdhonest` implementations.
- The bunching transfer is intentionally bounded. The goal is to make model dependence visible, not to turn Week 5 into a full tax bunching paper.
