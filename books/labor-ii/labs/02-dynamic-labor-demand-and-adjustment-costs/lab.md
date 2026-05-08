# Code Lab 02: Dynamic Labor Demand, Adjustment Paths, and Policy Timing

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 2 — Dynamic labor demand and adjustment costs  
**Associated chapter:** `02-dynamic-labor-demand-and-adjustment-costs.md`  
**Lab slug:** `02-dynamic-labor-demand-and-adjustment-costs`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 1 module, basic command-line work, introductory `pandas`, comfort reading time paths and event-study style figures  
**Core economic question:** How do economists learn about adjustment frictions from dynamic response paths rather than from one-shot employment elasticities?  
**Primary source anchor:** [@dibiasiMikoschSarferaz2025]  
**Challenge anchor:** [@caballeroEngelHaltiwanger1997]  
**Optional extension anchor:** [@saezSchoeferSeim2019]

## Why this lab exists

Week 2 should not stop at saying that employment is persistent. [@dibiasiMikoschSarferaz2025] is a strong teaching anchor because it keeps firm beliefs, uncertainty, and timing in view. The local bounded path therefore teaches students to read target-versus-actual gaps, adjustment speeds, and hours-headcount differences rather than treating a single employment slope as the whole story.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a compact dynamic-adjustment summary from a local synthetic firm panel;
2. diagnose the difference between target employment, actual employment, and the observed response path;
3. explain how uncertainty and margin choice can slow measured headcount adjustment;
4. transfer the Week 2 framework to convex versus nonconvex adjustment scenarios;
5. explain why policy incidence should be read over horizons rather than at one date only.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact dynamic-adjustment pattern from the synthetic firm panel.
- Diagnose the dynamic object, identifying variation, and observed margin.
- Transfer the logic to a small scenario file with convex, nonconvex, and policy-timing cases.
- Do not turn the lab into a full structural estimation exercise or a confidential firm-data replication.
- Keep the smoke test on the synthetic teaching path only.

## Lab roadmap

1. **Reproduce** a reduced target-versus-actual employment pattern from the synthetic firm panel.
2. **Diagnose** what the measured closure rate does and does not identify.
3. **Transfer** the Week 2 logic to convex and nonconvex adjustment scenarios.
4. **Reflect** on the link from dynamic labor demand to policy timing and later personnel choices.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for [@dibiasiMikoschSarferaz2025]. It is a synthetic teaching workflow inspired by the paper's design logic: firm beliefs, uncertainty, and adjustment paths. The goal is to practice Week 2 reasoning cleanly, not to ship the full data environment of the published paper.

### First commands to run

```bash
conda run -n research python src/reproduce_dibiasi_adjustment.py \
  --input original/reduced/dibiasi_adjustment_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_dynamic_adjustment.py \
  --input transfer/data/dynamic_adjustment_scenarios.csv \
  --outdir output/transfer
```

## Part I. Reproduce a bounded dynamic object

### Objective

Recover a compact target-versus-actual adjustment path, then compare gap-closing behavior across uncertainty groups.

### Student tasks

1. Read `original/source-notes.md`.
2. Run `src/reproduce_dibiasi_adjustment.py`.
3. Inspect `output/reproduced/dibiasi_adjustment_event_path.csv`.
4. Open `output/reproduced/dibiasi_adjustment_paths.png`.
5. Read `output/reproduced/dibiasi_adjustment_summary.csv`.
6. Write a short note explaining why the estimated closure rate is not yet a deep structural adjustment-cost parameter.

### Required questions

- What varies in the bounded reproduction path?
- Which outcome margins are observed directly?
- Why can a small contemporaneous headcount response still coexist with substantial short-run labor-demand adjustment?
- What would you need to observe to move from a reduced-form closure rate to a stronger structural interpretation?

## Part II. Diagnose the design

### Objective

Move from "employment adjusts slowly" to "I know what this dynamic object means."

### Student tasks

1. State the identifying variation in one sentence.
2. Name the observed margin in one sentence.
3. Explain the difference between target employment and actual employment in the bounded panel.
4. Explain whether the synthetic design is closer to policy timing evidence, uncertainty evidence, or structural estimation.
5. Say what the challenge paper [@caballeroEngelHaltiwanger1997] adds that the bounded path does not.

### Minimum output

- one short design memo;
- one annotated summary table;
- one paragraph interpreting short-run, medium-run, and long-run responses separately.

## Part III. Transfer the Week 2 logic

### Objective

Use the Week 2 framework on a small scenario file that compares convex adjustment, nonconvex adjustment, and policy timing.

### Student tasks

1. Run `src/transfer_dynamic_adjustment.py`.
2. Inspect `output/transfer/dynamic_adjustment_paths.csv`.
3. Open `output/transfer/dynamic_adjustment_transfer.png`.
4. Compare how the same target shift can produce different headcount paths under convex versus nonconvex costs.
5. Explain why the payroll-tax scenario is the natural bridge to [@saezSchoeferSeim2019].

### Acceptable transfer interpretations

- hours can absorb more of the immediate response than headcount;
- a fixed inaction band can generate delayed but larger headcount jumps;
- short-run and long-run policy incidence can differ because adjustment margins are sequenced.

## Part IV. Optional extensions

Use one extension only.

1. Read [@caballeroEngelHaltiwanger1997] and explain why micro-level lumpiness can coexist with smoother aggregate adjustment.
2. Read [@saezSchoeferSeim2019] and explain why a payroll-tax reform should be interpreted over event time rather than at one horizon only.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced event-path table and figure  
- [ ] one-page diagnose memo  
- [ ] transfer path table and figure  
- [ ] short bridge note to [@caballeroEngelHaltiwanger1997]  
- [ ] final reflection memo

## Instructor notes

- The bounded path is for local execution and smoke testing.
- The biggest classroom payoff comes from forcing students to separate a reduced-form adjustment speed from a structural cost parameter.
- Students should not treat the synthetic closure rate as a publishable estimate.
