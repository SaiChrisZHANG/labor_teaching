# Code Lab 05: Wage Determination, Returns to Schooling, and Local Causal Objects

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 5 --- Wage determination and returns to skill  
**Associated chapter:** `05-wage-determination-returns-to-skill.md`  
**Lab slug:** `05-wage-determination-returns-to-skill`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 4 human capital, basic command-line use, introductory `pandas`, comfort reading grouped summaries and simple plots  
**Core economic question:** What does a measured return to schooling actually represent, and how do compulsory-schooling designs change the object relative to a descriptive Mincer coefficient?  
**Core design / estimator:** bounded OLS-versus-IV comparison with a trend-sensitivity transfer exercise  
**Source paper for reproduction:** Oreopoulos, Philip. 2006. *Estimating Average and Local Average Treatment Effects of Education when Compulsory Schooling Laws Really Matter.* *American Economic Review* 96(1): 152--175.  
**Secondary / challenge anchor:** Stephens, Melvin, Jr. and Dou-Yan Yang. 2014. *Compulsory Education and the Benefits of Schooling.* *American Economic Review* 104(6): 1777--1792.  
**Optional sorting extension:** Engbom, Niklas and Christian Moser. 2017. *Returns to Education through Access to Higher-Paying Firms.* *American Economic Review: Papers and Proceedings* 107(5): 374--378.  

## Why this lab exists

Week 5 is where wage coefficients stop being self-explanatory. The bounded lab is designed to make that discipline operational. Students first compare a descriptive Mincer return with a compulsory-schooling IV return in the spirit of [@oreopoulos2006], then test how sensitive a familiar schooling instrument can be to cohort-trend assumptions in the spirit of [@stephensYang2014].

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce one bounded compulsory-schooling design with both OLS and IV estimates;
2. explain why those two estimates target different empirical objects;
3. diagnose the role of first-stage strength, cohort trends, and policy margins in returns-to-schooling work;
4. transfer the same workflow to a trend-sensitivity exercise;
5. explain how sorting into firms or places could mediate an observed education premium even when the bounded lab does not use restricted matched data.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compulsory-schooling return comparison only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one trend-sensitivity comparison only.
- Keep the smoke path fully local and synthetic.
- Treat the sorting extension as conceptual unless the instructor assigns a public-data add-on.

## Lab roadmap

1. **Reproduce** a synthetic Mincer-versus-IV comparison.
2. **Diagnose** what the IV estimate changes and what it still does not identify.
3. **Transfer** the same workflow to a trend-sensitive design environment.
4. **Reflect** on how worker-firm or worker-place sorting could mediate measured returns.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship the full official replication packages. Instead, it builds deterministic synthetic teaching files that preserve the logic of compulsory-schooling variation and trend sensitivity.

### Required local structure

```text
labs/05-wage-determination-returns-to-skill/
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
      oreopoulos_schooling_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      stephens_yang_trends_synthetic.csv
  src/
    build_week5_synthetic_data.py
    reproduce_oreopoulos_returns.py
    transfer_schooling_trends.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week5_synthetic_data.py

conda run -n research python src/reproduce_oreopoulos_returns.py \
  --input original/reduced/oreopoulos_schooling_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_schooling_trends.py \
  --input transfer/data/stephens_yang_trends_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded comparison between a descriptive Mincer return and a compulsory-schooling IV return.

### Student tasks

1. Run `src/build_week5_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/oreopoulos_schooling_synthetic.csv`.
4. Inspect the return-estimate table and output figure in `output/reproduced/`.
5. Write a short note on why the IV estimate is not just a "corrected" OLS estimate, but a different return object.

### Required questions

- Why is the Mincer coefficient descriptive even when it controls for experience?
- What is the first stage in the bounded compulsory-schooling design?
- Why does the IV estimate speak to a local schooling margin rather than a universal return?

### Minimum output

- one reproduced figure;
- one summary CSV;
- one return-estimate CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "IV is more causal" to a disciplined statement about what the design identifies.

### Student tasks

1. Explain which workers are most likely to be compliers in a compulsory-schooling setting.
2. Distinguish a descriptive wage premium from a local return for law-induced schooling changes.
3. State two reasons OLS and IV can differ even when both are internally consistent for their own targets.
4. Explain why the same return estimate could still be incomplete if schooling affects access to better firms or places.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on first-stage credibility;
- one paragraph on what remains outside the design.

## Part III. Transfer

### Objective

Use the same workflow in a trend-sensitive compulsory-schooling environment.

### Bounded transfer path

Run `src/transfer_schooling_trends.py` on the synthetic trend file and compare the pooled IV estimate with the group-trend-adjusted IV estimate.

### Student tasks

1. Produce one main figure showing cohort profiles and the two IV estimates.
2. Save the specification summary table.
3. Save the cohort-profile table.
4. Write a short paragraph explaining why trend adjustment changes the interpretation of the same instrument.
5. State whether the transfer exercise changes the treatment margin, the identifying assumptions, or both.

### Scope constraints

- Keep the same compulsory-schooling empirical family.
- Produce one main figure and one compact summary table.
- Do not add formal inference or external data pulls.
- Keep the transfer discussion focused on trend sensitivity and estimand discipline.

## Part IV. Optional sorting extension

Use [@engbomMoser2017] or [@diamond2016] to write a short note on how an education premium might be mediated by better firms or better cities rather than only by within-job pay. The goal is not to estimate a full worker-firm or spatial model here. The goal is to make explicit what the bounded IV design still leaves outside the wage-determination problem.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 5?
2. What would still be missing before claiming to know the policy-relevant return to schooling in a new setting?
3. How does the lab change the way you will read Week 8 inequality decompositions?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced figure  
- [ ] reproduced summary CSV  
- [ ] return-estimate CSV  
- [ ] design memo  
- [ ] transfer figure and specification summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmark  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from separating design credibility from target-parameter credibility.
- Use the optional sorting extension only if the course wants an explicit bridge into worker-firm or worker-place decomposition work.
