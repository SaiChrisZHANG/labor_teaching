# Code Lab 07: Job Amenities, Willingness to Pay, and Working Conditions

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 7 --- Job amenities and compensating differentials  
**Associated chapter:** `07-job-amenities-compensating-differentials.md`  
**Lab slug:** `07-job-amenities-compensating-differentials`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 5--6, basic command-line use, introductory `pandas`, and comfort with regression-style design logic  
**Core economic question:** How much are workers willing to trade wages for nonwage job attributes, and how does broader job quality change the interpretation of wage inequality?  
**Core design / estimator:** bounded pairwise job-choice reproduction plus a synthetic working-conditions transfer exercise  
**Source paper for reproduction:** Mas, Alexandre, and Amanda Pallais. 2017. *Valuing Alternative Work Arrangements.* *American Economic Review* 107(12): 3722--3759.  
**Secondary / challenge anchor:** Maestas, Nicole, Kathleen J. Mullen, David Powell, Till von Wachter, and Jeffrey Wenger. 2023. *The Value of Working Conditions in the United States and Implications for the Structure of Wages.* *American Economic Review* 113(7): 2007--2047.  
**Optional extension anchor:** Sorkin, Isaac. 2018. *Ranking Firms Using Revealed Preference.* *Quarterly Journal of Economics* 133(3): 1331--1393.  

## Why this lab exists

Week 7 asks students to stop treating wages as the whole job and start treating wages as one component of a broader compensation bundle. The bounded lab makes that move concrete: students first estimate wage-equivalent values for explicit amenities in the spirit of [@masPallais2017], then transfer the same valuation logic to a broader working-conditions and inequality exercise in the spirit of [@maestasMullenPowellVonWachterWenger2023].

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce one bounded discrete-choice amenity valuation exercise using synthetic job-choice data;
2. interpret wage coefficients and amenity coefficients as a willingness-to-pay object rather than a hedonic wage slope;
3. diagnose why willingness to pay can differ across workers with different care or commute constraints;
4. transfer the workflow from named job attributes to a broader working-conditions bundle;
5. explain why value-adjusted job rankings can differ from wage-only rankings.

## Scope rules

This lab is intentionally bounded.

- Reproduce one synthetic pairwise job-choice design only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one synthetic working-conditions and inequality exercise only.
- Keep the smoke path fully local and synthetic.
- Treat worker-flow revealed preference as optional extension material, not as part of the core smoke path.

## Lab roadmap

1. **Reproduce** a synthetic job-choice amenity valuation exercise.
2. **Diagnose** what the willingness-to-pay estimates identify and what they leave out.
3. **Transfer** the workflow to broader working-conditions bundles and total job value.
4. **Reflect** on the bridge from amenities to inequality and segmentation.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship the official experimental files or the full working-conditions infrastructure from the published papers. Instead, it builds deterministic synthetic teaching files that preserve the logic of pairwise job choice and broader working-conditions valuation.

### Required local structure

```text
labs/07-job-amenities-compensating-differentials/
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
      mas_pallais_job_choice_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      maestas_working_conditions_synthetic.csv
  src/
    build_week7_synthetic_data.py
    reproduce_mas_pallais_wtp.py
    transfer_working_conditions_value.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week7_synthetic_data.py

conda run -n research python src/reproduce_mas_pallais_wtp.py \
  --input original/reduced/mas_pallais_job_choice_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_working_conditions_value.py \
  --input transfer/data/maestas_working_conditions_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded willingness-to-pay object for explicit job amenities using pairwise job choices.

### Student tasks

1. Run `src/build_week7_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/mas_pallais_job_choice_synthetic.csv`.
4. Inspect the willingness-to-pay output table and the figure in `output/reproduced/`.
5. Write a short note on why these estimates are closer to marginal valuations of named amenities than a simple wage-amenity slope from a cross-sectional wage regression.

### Required questions

- Which job attributes are explicitly varied in the bounded design?
- Why is the wage coefficient necessary for turning attribute effects into money-metric willingness to pay?
- Which workers appear to value predictable schedules or remote options more in the synthetic data?
- Why is this reproduction closer to a discrete-choice willingness-to-pay object than to a Rosen hedonic slope?

### Minimum output

- one reproduced figure;
- one willingness-to-pay CSV;
- one subgroup-summary CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "workers value amenities" to a disciplined statement about which valuation object the bounded design identifies.

### Student tasks

1. Explain why the bounded design is about choosing between explicitly described offers rather than observing equilibrium wage bundles in the wild.
2. Distinguish a marginal willingness-to-pay estimate from a cross-sectional hedonic wage differential.
3. State two reasons why willingness to pay may vary across workers even when the same amenity is described identically.
4. Explain which broader job-quality features remain outside the bounded reproduction step.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on heterogeneity;
- one paragraph on external-validity limits.

## Part III. Transfer

### Objective

Use the same valuation logic on a broader working-conditions bundle tied to inequality accounting.

### Bounded transfer path

Run `src/transfer_working_conditions_value.py` on the synthetic accepted-job file and compare wage-only rankings with value-adjusted rankings that add the monetized value of predictability, remote work, low risk, autonomy, and commute burden.

### Student tasks

1. Produce one main value-adjustment figure.
2. Save the group summary table.
3. Save the rank-change table.
4. Write a short paragraph explaining why value-adjusted rankings can differ from wage-only rankings.
5. State whether the transfer step is better suited to measuring welfare inequality, wage inequality, or both.

### Scope constraints

- Keep the same Week 7 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on job quality, ranking, and distributional interpretation.

## Part IV. Optional extension

Use [@sorkin2018] to write a short note on how worker flows or job-to-job mobility could recover latent firm value when the researcher does not directly observe a full amenity bundle. The goal is not to estimate a full revealed-preference model here. The goal is to connect Week 7's explicit-attribute logic to broader firm ranking and sorting.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 7?
2. What would still be missing before claiming to know the full contribution of working conditions to inequality in a labor market?
3. How does the lab change the way you will read Week 8 inequality decompositions or Week 9 discrimination evidence?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced willingness-to-pay figure  
- [ ] reproduced willingness-to-pay CSV  
- [ ] subgroup summary  
- [ ] design memo  
- [ ] transfer figure and rank-change summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from separating direct willingness-to-pay estimates from equilibrium hedonic wage slopes.
- Use the optional extension only if the course wants an explicit bridge from named job attributes to worker-flow revealed preference.
