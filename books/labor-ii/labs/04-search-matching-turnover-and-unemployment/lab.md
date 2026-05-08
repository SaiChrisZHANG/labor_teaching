# Code Lab 04: Search, Matching, Worker Flows, and Job Ladders

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 4 — Search, matching, turnover, and unemployment  
**Associated chapter:** `04-search-matching-turnover-and-unemployment.md`  
**Lab slug:** `04-search-matching-turnover-and-unemployment`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 1--3, basic command-line work, introductory `pandas`, comfort reading transition rates and grouped summaries  
**Core economic question:** How do economists distinguish changes in the U-to-E job-finding hazard from changes in worker composition, and how do those objects differ from E-to-E job-ladder mobility?  
**Primary source anchor:** [@hallSchulhoferWohl2018]  
**Challenge anchor:** [@haltiwangerHyattKahnMcEntarfer2018]  
**Optional extension anchor:** [@huckfeldt2022]

## Why this lab exists

Week 4 introduces several objects that students often compress into "the unemployment rate." That is too coarse. [@hallSchulhoferWohl2018] is a strong teaching anchor because it forces the composition-versus-efficiency distinction into the measured job-finding rate. [@haltiwangerHyattKahnMcEntarfer2018] is the right challenge anchor because it shows that a large share of labor-market adjustment happens through E-to-E mobility and job ladders rather than only through unemployment transitions.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a compact U-to-E job-finding decomposition from a local synthetic panel;
2. name exactly which transition margin and hazard object the bounded reproduction path measures;
3. explain why the bounded reproduction is informative about composition and matching but not a full structural estimate of matching efficiency;
4. transfer Week 4 logic to a synthetic E-to-E job-ladder dataset;
5. articulate how a public CPS-style, JOLTS-style, or small linked synthetic dataset could extend the same design logic.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact U-to-E job-finding object from a synthetic seeker-by-month file.
- Diagnose the design with explicit attention to composition, hazards, and unobserved search objects.
- Transfer the logic to a synthetic job-ladder file where the measured margin is E-to-E mobility.
- Keep the smoke test on the local teaching path only.
- Do not turn the lab into a confidential microdata replication or a full structural search-estimation exercise.

## Lab roadmap

1. **Reproduce** a reduced Hall-Schulhofer-Wohl-style decomposition.
2. **Diagnose** what the bounded design identifies and what it leaves unobserved.
3. **Transfer** the Week 4 framework to a synthetic job-ladder setting.
4. **Extend** the interpretation to unemployment scarring and selective hiring.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for [@hallSchulhoferWohl2018]. It is a synthetic teaching workflow inspired by the paper's design logic: heterogeneous job seekers, aggregate job-finding rates, and composition-adjusted interpretation. The goal is to practice Week 4 reasoning cleanly, not to reproduce every data and modeling layer of the published paper.

### First commands to run

```bash
conda run -n research python src/reproduce_hall_schulhofer_wohl.py \
  --input original/reduced/hall_schulhofer_wohl_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_job_ladder_search.py \
  --input transfer/data/job_ladder_scenarios.csv \
  --outdir output/transfer
```

## Part I. Reproduce a bounded Week 4 object

### Objective

Recover the aggregate unemployment-to-employment hazard and compare it with a fixed-composition counterfactual.

### Be explicit before you run anything

1. **Transition margin being measured:** unemployment to employment, or U->E.
2. **Hazard or flow object being approximated:** the aggregate job-finding rate, {math}`f_t = M_t / U_t`.
3. **Observed unit in the bounded file:** seeker type by month.
4. **Identifying variation in the bounded path:** month-to-month changes in seeker composition and within-type match counts.

### Student tasks

1. Read `original/source-notes.md`.
2. Run `src/reproduce_hall_schulhofer_wohl.py`.
3. Inspect `output/reproduced/hall_schulhofer_wohl_decomposition.csv`.
4. Open `output/reproduced/hall_schulhofer_wohl_matching.png`.
5. Read `output/reproduced/hall_schulhofer_wohl_summary.csv`.
6. Read `output/reproduced/hall_schulhofer_wohl_seeker_shares.csv`.
7. Write a short note explaining when a falling aggregate U->E rate could reflect changing composition rather than a uniform collapse in within-type matching.

### Required questions

- Which margin is actually measured in this reproduction path?
- Which hazard object does the synthetic file approximate directly, and which objects remain unobserved?
- Why is the fixed-composition counterfactual useful?
- Why is this still not a full structural estimate of matching efficiency?

## Part II. Diagnose the design

### Objective

Move from "job finding changed" to "I know what changed in the measured object and what still needs theory."

### What the diagnosis must say explicitly

1. **Transition margin:** U->E only.
2. **Observed hazard object:** aggregate and type-specific job-finding rates.
3. **Most important limitation relative to the original paper:** the bounded path does not recover richer heterogeneity, market-level search technology, or the full structural object behind matching efficiency.
4. **Most important unobserved object:** the full opportunity set and search process connecting specific workers to specific vacancies.

### Student tasks

1. State the identifying variation in one sentence.
2. Name the unit of observation in one sentence.
3. Explain the difference between the observed aggregate rate and the fixed-composition rate.
4. State one reason the residual gap should not be over-interpreted as pure matching efficiency.
5. Explain what additional data you would want if you were trying to move toward the full logic of [@hallSchulhoferWohl2018].

### Minimum output

- one short design memo;
- one annotated decomposition table;
- one paragraph on what remains unobserved.

## Part III. Transfer the Week 4 logic

### Objective

Use a synthetic job-ladder file to shift from U->E hazards to E->E mobility and upgrading.

### Be explicit before you interpret the transfer file

1. **Transition margin being measured:** employment to employment, or E->E.
2. **Hazard or flow object being approximated:** the E→E mobility rate and the share of moves that upgrade job quality.
3. **Why this is a different Week 4 object:** it measures sorting and mobility among employed workers rather than reemployment from unemployment.
4. **Connection to the challenge anchor:** [@haltiwangerHyattKahnMcEntarfer2018] studies cyclical job ladders, which are invisible if we look only at unemployment transitions.

### Student tasks

1. Run `src/transfer_job_ladder_search.py`.
2. Inspect `output/transfer/job_ladder_transition_summary.csv`.
3. Inspect `output/transfer/job_ladder_market_summary.csv`.
4. Open `output/transfer/job_ladder_transfer.png`.
5. Compare upgrading from low- and middle-wage firms in tight versus loose markets.
6. Explain why a weak labor market can flatten job ladders even before all adjustment appears as unemployment.

### Transfer directions you are allowed to propose

- a public CPS-style month-to-month flow exercise focused on U->E and E->U;
- a JOLTS-style vacancy and hiring exercise focused on vacancy-filling and recruiting congestion;
- a small synthetic linked worker-firm panel focused on E→E upgrading and job ladders.

## Part IV. Optional extension

Use one extension only.

1. Read [@huckfeldt2022] and explain how recession timing changes post-unemployment job quality or scarring.
2. Propose a bridge from the Week 4 reproduction path to a public CPS/JOLTS-style teaching exercise, naming the observed unit, observed margin, and most important missing object.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path measures a synthetic U→E hazard and a simple composition decomposition, not the full search environment in [@hallSchulhoferWohl2018].
2. The bounded transfer path measures synthetic E→E mobility by firm tier, not the full administrative job-ladder structure in [@haltiwangerHyattKahnMcEntarfer2018].
3. Neither path identifies wages, reservation values, vacancy quality, or equilibrium spillovers directly.
4. Neither path can, on its own, distinguish reduced-form duration gradients from fully structural search behavior.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced decomposition table and figure  
- [ ] one-page diagnose memo  
- [ ] transfer summary tables and figure  
- [ ] short bridge note to [@haltiwangerHyattKahnMcEntarfer2018]  
- [ ] final reflection memo

## Instructor notes

- The bounded path is for local execution and smoke testing.
- The biggest classroom payoff comes from forcing students to name the transition margin and hazard object before they start interpreting results.
- The second biggest payoff comes from making students separate U→E evidence from E→E ladder evidence.
