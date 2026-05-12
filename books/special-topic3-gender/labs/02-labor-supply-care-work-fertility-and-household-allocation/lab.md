# Code Lab 2: Labor Supply, Care Work, Fertility, And Household Allocation

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 2 -- Labor supply, care work, fertility, and household allocation  
**Associated chapter:** `02-labor-supply-care-work-fertility-and-household-allocation.md`  
**Lab slug:** `02-labor-supply-care-work-fertility-and-household-allocation`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@klevenLandaisPoschSchmidtSogaard2019]  
**Secondary / challenge anchor:** [@lundborgPlugRasmussen2017]  
**Optional policy anchor:** [@bjorvatnFerrisJayachandran2025]  

## Why This Lab Exists

Week 2 teaches students to keep family-labor empirical objects separate. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a child-penalty event-time exercise.
2. **Diagnose** what the child-penalty path shows and what it does not identify alone.
3. **Transfer** the same design discipline to a causal fertility setting.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential administrative or microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce event-time child-penalty summaries for employment, hours, earnings, and job quality;
2. distinguish dynamic child penalties from causal fertility effects;
3. diagnose whether a margin is extensive, intensive, earnings-based, job-quality-based, or care-time-based;
4. compute a bounded IVF-style Wald estimand and explain its local interpretation;
5. transfer the same logic to childcare and policy evidence without overstating the design.

## Local Structure

```text
labs/02-labor-supply-care-work-fertility-and-household-allocation/
  lab.md
  smoke.sh
  src/
    build_week2_synthetic_data.py
    reproduce_child_penalties.py
    transfer_fertility_design.py
  original/
    reduced/
  transfer/
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week2_synthetic_data.py

conda run -n research python src/reproduce_child_penalties.py \
  --input original/reduced/kleven_child_penalty_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_fertility_design.py \
  --input transfer/data/lundborg_ivf_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/event_time_profiles.csv`
- `output/reproduced/child_penalty_summary.csv`
- `output/reproduced/margin_diagnostics.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the event-time object?
- Which outcomes are extensive-margin, intensive-margin, earnings, job-quality, and care-time margins?
- How large is the mother-father divergence five years after first birth?
- Why is this dynamic path not automatically a causal fertility effect?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** State whether the design measures a child penalty, a fertility effect, a childcare-policy effect, or a bargaining shift.
2. **Margins:** Separate participation, hours, earnings, job quality, and care time.
3. **Mechanism:** Name at least two mechanisms that could generate the child-penalty path.
4. **Evidence needed:** State what extra variation would distinguish childcare constraints, bargaining shifts, employer flexibility, and norms.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/fertility_design_summary.csv`
- `output/transfer/wald_estimates.csv`
- `output/transfer/transfer_note.txt`

Use the IVF-style exercise inspired by [@lundborgPlugRasmussen2017] to explain why a fertility shifter answers a different question from a child-penalty event study. State the first stage, the reduced form, and the Wald estimand for employment, hours, and earnings.

## Optional Policy Prompt

Use [@bjorvatnFerrisJayachandran2025] to write a short note on how childcare availability could change the same household allocation problem. Do not estimate a policy effect in the bounded path. State which margin the policy could move: care time, participation, hours, earnings, firm choice, job quality, or business development.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced child-penalty summaries
- [ ] one-page design memo
- [ ] IVF-style fertility transfer summaries
- [ ] paragraph distinguishing child penalties from fertility effects
- [ ] optional childcare-policy margin note
