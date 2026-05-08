# Code Lab 10: Mobility, Migration, and Intergenerational Transmission

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 10 --- Mobility, migration, and intergenerational transmission  
**Associated chapter:** `10-mobility-migration-intergenerational-transmission.md`  
**Lab slug:** `10-mobility-migration-intergenerational-transmission`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 5, 8, and 9; grouped summaries; simple regression intuition; and comfort reading event-style figures  
**Core economic question:** How do labor economists separate constrained mobility from chosen mobility, and how do lottery and exposure designs reveal the labor-market effects of movement across places and jobs?  
**Core design / estimator:** bounded lottery reproduction plus a synthetic reform-exposure transfer exercise  
**Source paper for reproduction:** Van Doornik, Bernardus, Armando Gomes, David Schoenherr, and Janis Skrastins. 2024. *Financial Access and Labor Market Outcomes: Evidence from Credit Lotteries.* *American Economic Review* 114(6): 1854--1881.  
**Secondary / challenge anchor:** Beerli, Andreas, Jan Ruffner, Michael Siegenthaler, and Giovanni Peri. 2021. *The Abolition of Immigration Restrictions and the Performance of Firms and Workers: Evidence from Switzerland.* *American Economic Review* 111(3): 976--1012.  
**Optional frontier extension anchors:** Haeck, Catherine, and Jean-William Lalibert{\'e}. 2025. *Careers and Intergenerational Income Mobility.* *American Economic Journal: Applied Economics* 17(1): 431--458; and Fujita, Shigeru, Giuseppe Moscarini, and Fabien Postel-Vinay. 2024. *Measuring Employer-to-Employer Reallocation.* *American Economic Journal: Macroeconomics* 16(3): 1--51.  

## Why this lab exists

Week 10 is the course's mobility-architecture week. The bounded lab turns that architecture into a local workflow. Students first reproduce a lottery-based mobility design in the spirit of [@vanDoornikGomesSchoenherrSkrastins2024], then diagnose what relaxing a credit friction identifies, and finally transfer the logic to a reform-exposure design in the spirit of [@beerliRuffnerSiegenthalerPeri2021].

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce an intention-to-treat mobility effect from a bounded credit-lottery dataset;
2. distinguish the causal effect of relaxing one mobility friction from the general return to moving;
3. compare moving, employer-switching, and wage-growth responses inside the same design;
4. estimate a compact exposure-design effect for labor-market reallocation after a migration reform;
5. explain why linked-data and intergenerational-mobility questions require richer data than the bounded teaching path ships locally.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact credit-lottery factbook only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one migration-reform exposure exercise only.
- Keep the smoke path fully local and synthetic.
- Treat the intergenerational and measurement-correction extensions as conceptual unless the instructor assigns more advanced work.

## Lab roadmap

1. **Reproduce** a synthetic credit-lottery mobility summary.
2. **Diagnose** what randomized credit access identifies.
3. **Transfer** the workflow to a synthetic migration-reform exposure panel.
4. **Reflect** on how firms, places, and families sustain inequality persistence.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship restricted credit-bureau files, linked employer-employee microdata, or tax-based parent-child panels. Instead, it builds deterministic synthetic teaching files that preserve the logic of lottery-based mobility estimation and reform-exposure labor-market analysis.

### Required local structure

```text
labs/10-mobility-migration-intergenerational-transmission/
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
      van_doornik_credit_lottery_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      beerli_open_border_synthetic.csv
  src/
    build_week10_synthetic_data.py
    reproduce_van_doornik_credit_lottery.py
    transfer_beerli_migration_exposure.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week10_synthetic_data.py

conda run -n research python src/reproduce_van_doornik_credit_lottery.py \
  --input original/reduced/van_doornik_credit_lottery_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_beerli_migration_exposure.py \
  --input transfer/data/beerli_open_border_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded mobility factbook from a synthetic credit-lottery dataset.

### Student tasks

1. Run `src/build_week10_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/van_doornik_credit_lottery_synthetic.csv`.
4. Inspect the moving, employer-switching, wage-growth, and heterogeneity outputs in `output/reproduced/`.
5. Write a short note on why the reproduced effect is the effect of relaxing one mobility friction rather than the unconditional return to migration.

### Required questions

- What is the treatment variation in the bounded credit-lottery design?
- Why is the move effect not the same as the average gain from moving among observed movers?
- How do local opportunity gaps change the labor interpretation of an average move effect?
- Which outcomes suggest employer mobility rather than geography alone is doing part of the work?

### Minimum output

- one reproduced figure;
- one mobility summary CSV;
- one heterogeneity CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "credit access raises mobility" to a disciplined statement about what the design actually identifies.

### Student tasks

1. Distinguish a lottery-based mobility effect from a mover-stayer wage comparison.
2. Explain why the same move effect can combine geographic relocation, employer switching, and occupational upgrading.
3. State one way in which housing or family constraints could still limit external validity.
4. Explain why the design says little by itself about intergenerational persistence.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on what remains outside the design;
- one paragraph linking the design to Week 11 worker policy.

## Part III. Transfer

### Objective

Use the same Week 10 logic on a synthetic migration-reform exposure panel.

### Bounded transfer path

Run `src/transfer_beerli_migration_exposure.py` on the synthetic regional panel and estimate compact exposure-design effects for employer-to-employer reallocation, employment, and wage growth.

### Student tasks

1. Produce one main transfer figure.
2. Save the difference-in-differences summary table.
3. Save the exposure-group event table.
4. Write a short paragraph explaining why exposure designs identify reduced-form market responses rather than one pure channel.
5. State how the transfer step broadens the Week 10 conversation from one friction to market-level reallocation.

### Scope constraints

- Keep the same Week 10 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on exposure, reallocation, and interpretation.

## Part IV. Optional frontier extension

Use [@haeckLaliberte2025] to write a short note on how career structure mediates intergenerational mobility. Use [@fujitaMoscariniPostelVinay2024] to explain why a mismeasured employer-to-employer series can distort the very object students think they are interpreting. The goal is not to estimate a structural model or use restricted data here. The goal is to recognize which parts of Week 10 remain outside the bounded path.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 10?
2. What would still be missing before claiming to measure the full labor-market return to mobility?
3. How does the lab change the way you will read Week 11 worker-policy evidence?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced mobility figure  
- [ ] mobility summary CSV  
- [ ] design memo  
- [ ] transfer figure and reform-exposure summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from teaching students to separate mobility objects from causal designs.
- Use the transfer step to make labor-market reallocation and policy relevance concrete before Week 11.
