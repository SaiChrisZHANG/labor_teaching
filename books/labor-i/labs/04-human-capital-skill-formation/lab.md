# Code Lab 04: Human Capital, Skill Formation, and Dynamic Complementarity

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 4 --- Human capital and skill formation  
**Associated chapter:** `04-human-capital-skill-formation.md`  
**Lab slug:** `04-human-capital-skill-formation`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 3 dynamic labor supply, basic command-line use, introductory `pandas`, comfort reading grouped summaries and simple plots  
**Core economic question:** What can treatment-induced investment shifts teach us about human-capital production, and how does baseline preparedness or program quality change the observed return to later inputs?  
**Core design / estimator:** reduced-form treatment-effect summaries with bounded heterogeneity contrasts  
**Source paper for reproduction:** Attanasio, Orazio, Sarah Cattan, Emla Fitzsimons, Costas Meghir, and Marta Rubio-Codina. 2020. *Estimating the Production Function for Human Capital: Results from a Randomized Controlled Trial in Colombia.* *American Economic Review* 110(1): 48--85.  
**Secondary reduced-form anchor:** Walters, Christopher R. 2015. *Inputs in the Production of Early Childhood Human Capital: Evidence from Head Start.* *American Economic Journal: Applied Economics* 7(4): 76--102.  
**Optional finance extension:** Lochner, Lance J. and Alexander Monge-Naranjo. 2011. *The Nature of Credit Constraints and Human Capital.* *American Economic Review* 101(6): 2487--2529.  

## Why this lab exists

Week 4 is where productive capacity becomes an explicit state variable. The bounded lab is designed to keep that transition concrete. Students see one treatment-induced investment contrast in the spirit of `@attanasioEtAl2020HumanCapital`, then ask whether observed gains vary with baseline preparedness or program quality in the spirit of `@walters2015`.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce one bounded treatment-effect contrast for parental investments and child skill;
2. explain what that contrast identifies and what it leaves inside the production-function black box;
3. diagnose why baseline skill and input quality matter for interpreting intervention effects;
4. transfer the same workflow to a center-quality heterogeneity exercise;
5. explain how the same human-capital logic connects to schooling finance and later wage determination.

## Scope rules

This lab is intentionally bounded.

- Reproduce one treatment-effect summary only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one quality-heterogeneity comparison only.
- Do not turn the exercise into a full structural estimation project.
- Keep the smoke path fully local and synthetic.

## Lab roadmap

1. **Reproduce** a treatment-induced investment and endline-skill contrast.
2. **Diagnose** what that contrast identifies inside a broader human-capital model.
3. **Transfer** the same workflow to a center-quality environment.
4. **Reflect** on how early-childhood evidence changes the interpretation of later schooling and wage gaps.

## Part 0. Setup and orientation

### Official package reality

The source paper is the conceptual benchmark. The bounded course path does **not** ship the full official replication package. Instead, it builds deterministic synthetic teaching files that preserve the logic of randomized investment shifts and dynamic complementarity.

### Required local structure

```text
labs/04-human-capital-skill-formation/
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
      attanasio_parenting_rct_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      walters_center_quality_synthetic.csv
  src/
    build_week4_synthetic_data.py
    reproduce_attanasio_human_capital.py
    transfer_skill_formation.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week4_synthetic_data.py

conda run -n research python src/reproduce_attanasio_human_capital.py \
  --input original/reduced/attanasio_parenting_rct_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_skill_formation.py \
  --input transfer/data/walters_center_quality_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded treatment-effect contrast and relate it back to Week 4's investment and skill-formation logic.

### Student tasks

1. Run `src/build_week4_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/attanasio_parenting_rct_synthetic.csv`.
4. Inspect the summary table and output figure in `output/reproduced/`.
5. Write a short note on whether the observed treatment effect should be read as a treatment effect on outcomes, a direct estimate of the production function, or something in between.

### Required questions

- Why is a treatment-induced parental-investment shift informative for human-capital production?
- Why does a reduced-form skill gain still fall short of identifying the full production technology?
- What role does baseline skill play in interpreting the same treatment effect?

### Minimum output

- one reproduced figure;
- one summary CSV;
- one treatment-gap CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "treated children score higher" to a disciplined statement about what the estimate means.

### Student tasks

1. Explain which inputs are shifted directly by treatment and which outcomes are measured later.
2. Distinguish a treatment effect on endline skill from a structural estimate of dynamic complementarity.
3. State two reasons treatment effects could differ across baseline-skill groups.
4. Explain why the same evidence matters for later labor-market inequality even though no adult wages appear in the lab data.

### Minimum output

- a one-page design memo;
- one paragraph on identification;
- one paragraph on heterogeneity;
- one paragraph connecting the lab back to Week 5 returns to skill.

## Part III. Transfer

### Objective

Use the same skill-formation workflow in a program-quality environment.

### Bounded transfer path

Run `src/transfer_skill_formation.py` on the synthetic center-quality file and compare treatment gains across `low_quality`, `medium_quality`, and `high_quality` centers.

### Student tasks

1. Produce one grouped treatment-effect figure.
2. Save the summary table by treatment status and center quality.
3. Save the treatment-gap table by center quality.
4. Write a short paragraph explaining whether the treatment design changed or only the delivery environment changed.
5. State whether larger gains in high-quality centers are evidence of dynamic complementarity, better inputs, or both.

### Scope constraints

- Keep the same treatment-versus-control logic.
- Produce one main figure and one compact summary table.
- Do not add structural estimation.
- Keep the transfer discussion focused on heterogeneity in inputs and delivery quality.

## Part IV. Optional finance extension

Use `@lochnerMongeNaranjo2011` to write a short note on how the same investment logic changes when schooling must be financed under limited commitment. The goal is not to estimate a full credit model here. The goal is to explain why high-return investments can still be underprovided when borrowing or repayment is difficult.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 4?
2. What would still be missing before claiming to know the full skill-production technology?
3. How does this lab change the way you will read Week 5 wage-return estimates?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced figure  
- [ ] reproduced summary CSV  
- [ ] treatment-gap CSV  
- [ ] design memo  
- [ ] transfer figure and summary table  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official replication benchmark  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from separating treatment effects from technology parameters.
- Use the optional finance extension only if the course wants a direct bridge from early investment to schooling-credit frictions.
