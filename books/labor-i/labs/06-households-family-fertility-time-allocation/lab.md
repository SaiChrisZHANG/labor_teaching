# Code Lab 06: Households, Fertility, Child Penalties, and Time Allocation

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 6 --- Households, family, fertility, and time allocation  
**Associated chapter:** `06-households-family-fertility-time-allocation.md`  
**Lab slug:** `06-households-family-fertility-time-allocation`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 2--5, basic command-line use, introductory `pandas`, and comfort reading grouped summaries and event-study style plots  
**Core economic question:** How do fertility and care shocks move labor-market outcomes once the relevant decision-making unit is the household rather than the isolated worker?  
**Core design / estimator:** bounded IVF-style fertility-IV reproduction plus a synthetic child-penalty event-study transfer exercise  
**Source paper for reproduction:** Lundborg, Petter, Erik Plug, and Astrid W{\"u}rtz Rasmussen. 2017. *Can Women Have Children and a Career? IV Evidence from IVF Treatments.* *American Economic Review* 107(6): 1611--1637.  
**Secondary / challenge anchor:** Kleven, Henrik, Camille Landais, and Jakob Egholt S{\o}gaard. 2019. *Children and Gender Inequality: Evidence from Denmark.* *American Economic Journal: Applied Economics* 11(4): 181--209.  
**Optional policy extension:** Gelbach, Jonah B. 2002. *Public Schooling for Young Children and Maternal Labor Supply.* *American Economic Review* 92(1): 307--322; Cort{\'e}s, Patricia and Jos{\'e} Tessada. 2011. *Low-Skilled Immigration and the Labor Supply of Highly Skilled Women.* *American Economic Journal: Applied Economics* 3(3): 88--123.  

## Why this lab exists

Week 6 asks students to stop treating children as a regression control and start treating fertility and caregiving as labor-market shocks that reallocate time inside the household. The bounded lab makes that move concrete: students first estimate a causal fertility effect in the spirit of [@lundborgPlugRasmussen2017], then trace dynamic child-penalty paths in the spirit of [@klevenLandaisSogaard2019].

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce one bounded fertility-IV design using synthetic IVF-style data;
2. interpret a first stage, a reduced form, and a Wald estimand in household-labor language;
3. diagnose which labor margin is moving after fertility and which margins are left outside the bounded design;
4. transfer the workflow to a dynamic child-penalty event-study setting;
5. explain how childcare, schooling, or household-service substitutes could change the same family-allocation problem.

## Scope rules

This lab is intentionally bounded.

- Reproduce one IVF-style fertility effect only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one synthetic child-penalty event study only.
- Keep the smoke path fully local and synthetic.
- Treat the policy extension as optional and conceptual unless the instructor assigns more data work.

## Lab roadmap

1. **Reproduce** a synthetic IVF-style fertility-IV comparison.
2. **Diagnose** what the local fertility effect identifies and what it does not.
3. **Transfer** the workflow to a dynamic child-penalty event study.
4. **Reflect** on how childcare, school entry, or outsourcing could move the same margins.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship the official microdata or administrative event-study files. Instead, it builds deterministic synthetic teaching files that preserve the logic of IVF-generated fertility variation and post-birth dynamic outcome paths.

### Required local structure

```text
labs/06-households-family-fertility-time-allocation/
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
      lundborg_ivf_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      kleven_child_penalty_synthetic.csv
  src/
    build_week6_synthetic_data.py
    reproduce_lundborg_ivf.py
    transfer_child_penalty_event_study.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week6_synthetic_data.py

conda run -n research python src/reproduce_lundborg_ivf.py \
  --input original/reduced/lundborg_ivf_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_child_penalty_event_study.py \
  --input transfer/data/kleven_child_penalty_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded causal fertility effect on labor-market outcomes using IVF-style variation.

### Student tasks

1. Run `src/build_week6_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/lundborg_ivf_synthetic.csv`.
4. Inspect the first-stage and Wald-estimate tables and the output figure in `output/reproduced/`.
5. Write a short note on why IVF success changes the fertility margin for a local group rather than identifying the effect of parenthood for every family.

### Required questions

- What is the instrument in the bounded IVF design?
- Why is the first stage a fertility object rather than a labor-supply object?
- Which labor outcomes move most in the local data: participation, hours, or earnings?
- Why is a local fertility effect not the same as a descriptive motherhood penalty?

### Minimum output

- one reproduced figure;
- one summary CSV;
- one Wald-estimate CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "fertility matters" to a disciplined statement about which causal family-labor margin the bounded design identifies.

### Student tasks

1. Explain which couples are closest to compliers in an IVF-style design.
2. Distinguish the causal effect of an additional child from a descriptive gap between parents and non-parents.
3. State two reasons the IVF design and the child-penalty event study answer different questions even when both are about family labor supply.
4. Explain which long-run career margins remain outside the reproduction step even if annual earnings move.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on external-validity limits;
- one paragraph on which labor margins remain unmeasured.

## Part III. Transfer

### Objective

Use the same workflow in a dynamic child-penalty environment centered on years relative to first birth.

### Bounded transfer path

Run `src/transfer_child_penalty_event_study.py` on the synthetic panel file and compare mothers and fathers from five years before first birth to ten years after.

### Student tasks

1. Produce one main event-study figure.
2. Save the penalty summary table.
3. Save the event-time panel summary.
4. Write a short paragraph explaining why an event-study path is a dynamic object rather than a single treatment coefficient.
5. State whether the transfer step is better suited to measuring timing, persistence, composition, or all three.

### Scope constraints

- Keep the same family-labor empirical family.
- Produce one main figure and one compact summary table.
- Do not add formal inference or external data pulls.
- Keep the transfer discussion focused on persistence, margin decomposition, and interpretation.

## Part IV. Optional policy extension

Use [@gelbach2002], [@cortesTessada2011], or [@klevenLandaisPoschSteinhauerZweimueller2024] to write a short note on how a cheaper care substitute or a family-policy expansion could move the same household-allocation problem. The goal is not to estimate a full policy model here. The goal is to translate Week 6 theory into a clean comparative-static or design memo.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 6?
2. What would still be missing before claiming to know the full contribution of children to gender inequality in a labor market?
3. How does the lab change the way you will read Week 7 amenities or Week 8 inequality decompositions?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced figure  
- [ ] reproduced summary CSV  
- [ ] Wald-estimate CSV  
- [ ] design memo  
- [ ] transfer figure and penalty summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from separating a causal fertility margin from a dynamic post-birth earnings path.
- Use the optional policy extension only if the course wants an explicit bridge to childcare, leave, or outsourcing evidence.
