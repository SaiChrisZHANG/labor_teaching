# Code Lab 11: Technology, Automation, AI, and Labor Market

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 11 --- Technology, Automation, AI, and Labor Market  
**Associated chapter:** `11-technology-automation-ai-and-labor-market.md`  
**Lab slug:** `11-technology-automation-ai-and-labor-market`  
**Scope tier:** Heavy shock-and-adjustment week  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 1, 4, 6, and 10; comfort with grouped data, simple regressions, and the distinction between exposure and realized treatment  
**Core economic question:** When technology changes work, are we measuring supply-side, demand-side, or market-level effects; are we using exposure or actual adoption; and which labor-market margin is directly observed?  
**Primary source anchor:** `@aghionEtAl2025HowDifferentUsesAI`  
**Secondary / challenge anchor:** `@acemogluRestrepo2020RobotsJobs`  
**Optional extension anchor:** `@brynjolfssonLiRaymond2025GenerativeAIWork`

## Why this lab exists

Week 11 becomes blurry if students jump directly from “AI is important” to “AI helps or hurts jobs.” `@aghionEtAl2025HowDifferentUsesAI` is the right reproduction anchor because it forces the class to work with actual adoption categories inside firms rather than only exposure scores. `@acemogluRestrepo2020RobotsJobs` is the right challenge anchor because it flips the design to local-labor-market exposure and equilibrium incidence. `@brynjolfssonLiRaymond2025GenerativeAIWork` is the right optional extension because it makes worker learning and heterogeneity visible without pretending that a worker-productivity treatment already identifies market-wide labor outcomes.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded firm-level AI adoption exercise with heterogeneous labor-demand effects by use type;
2. state explicitly whether the design captures supply-side, demand-side, or market-level effects;
3. distinguish actual adoption from occupation-level exposure before interpreting any coefficient or plot;
4. identify the unit of observation, the observed labor-market margin, and the key equilibrium margin left offstage;
5. transfer one exposure idea to a bounded new setting using a small synthetic occupation-market panel.

## Scope rules

This lab is intentionally bounded.

- Reproduce one firm-level AI-use design from a local synthetic panel inspired by `@aghionEtAl2025HowDifferentUsesAI`.
- Diagnose the difference between actual adoption and exposure using the generated outputs.
- Transfer one exposure idea to a small synthetic occupation-market panel.
- Keep the smoke path fully local and synthetic.
- Do not require proprietary microdata, confidential firm records, or a full official replication package.

## Lab roadmap

1. **Reproduce** a bounded firm-level AI-use and labor-demand design.
2. **Diagnose** whether the technology object is actual adoption or predicted exposure.
3. **Transfer** one exposure idea to a small occupation-market panel.
4. **Challenge** yourself by comparing that transfer design to a robot-style local-labor-market exposure logic.

## Part 0. Setup and orientation

### First commands to run

```bash
conda run -n research python src/reproduce_ai_uses.py \
  --outdir output/reproduced

conda run -n research python src/transfer_technology_exposure.py \
  --reproduced output/reproduced/firm_ai_panel.csv \
  --outdir output/transfer
```

### Before you interpret anything

Write down four things for each stage of the lab.

1. Is the effect you are studying supply-side, demand-side, or market-level?
2. Is the technology object actual adoption or predicted exposure?
3. What is the unit of observation?
4. Which labor-market margin is observed directly, and which equilibrium margin remains offstage?

## Part I. Reproduce a bounded Aghion-et-al.-style adoption design

### Objective

Recover a small firm-quarter panel in which AI uses differ across firms and generate different labor-demand responses.

### Be explicit before you run anything

1. **Design family:** within-firm adoption design.
2. **Technology object:** actual AI adoption by use category.
3. **Primary effect family:** demand-side.
4. **Unit of observation:** firm-quarter.
5. **Observed labor-market margins:** employment growth, vacancy growth, routine-task employment share, and wage-bill growth.
6. **Key equilibrium margin left offstage:** labor reallocation across firms, occupations, and local markets.

### Student tasks

1. Run `src/reproduce_ai_uses.py`.
2. Inspect `output/reproduced/firm_ai_panel.csv`.
3. Inspect `output/reproduced/ai_use_summary.csv`.
4. Inspect `output/reproduced/ai_use_effects.csv`.
5. Open `output/reproduced/ai_use_labor_demand.png`.
6. Write a short note explaining why “AI adoption” is not a single treatment when uses differ.

### Required questions

- Which AI uses look closest to automation, and which look closest to augmentation?
- Which observed outcomes are demand-side margins rather than market-level incidence?
- What would you need to observe to say something stronger about worker welfare rather than firm labor demand?

## Part II. Diagnose adoption versus exposure

### Objective

Use the transfer outputs to separate descriptive exposure from realized adoption.

### Be explicit before you interpret the diagnosis outputs

1. **Design family:** occupation-market descriptive exposure design.
2. **Technology object:** predicted exposure score plus aggregated realized adoption share.
3. **Primary effect family:** descriptive bridge between demand-side and market-level objects.
4. **Unit of observation:** occupation-market cell.
5. **Observed labor-market margins:** employment change, wage growth, vacancy skill intensity.
6. **Key equilibrium margin left offstage:** full general-equilibrium adjustment across places and industries.

### Student tasks

1. Run `src/transfer_technology_exposure.py`.
2. Inspect `output/transfer/exposure_vs_adoption_panel.csv`.
3. Inspect `output/transfer/exposure_vs_adoption_summary.csv`.
4. Open `output/transfer/exposure_vs_adoption.png`.
5. Explain why a high exposure score is not the same thing as observing treatment.

### Minimum output

- one paragraph distinguishing exposure from adoption;
- one paragraph explaining what the occupation-market panel can and cannot identify;
- one short note on which labor-market margin is actually being measured.

## Part III. Transfer one exposure idea to a bounded new setting

### Objective

Move one Week 11 measurement idea to a small synthetic occupation-market design.

### Concrete transfer exercise

Recompute the synthetic AI exposure measure using only routine cognitive task weights instead of the full task bundle, then compare how that alternative exposure score relates to employment change and wage growth in the occupation-market panel.

### Why this is the transfer exercise

It is narrow, reproducible, and disciplined. Students are not asked to “do something with AI.” They are asked to move one exposure construction idea to a new but bounded setting and compare the resulting labor-market patterns.

### Be explicit before you interpret the transfer outputs

1. **Design family:** descriptive exposure transfer.
2. **Technology object:** alternative exposure index.
3. **Primary effect family:** market-level descriptive comparison with some demand-side content.
4. **Unit of observation:** occupation-market cell.
5. **Observed labor-market margins:** employment change and wage growth.
6. **Key equilibrium margin left offstage:** worker mobility and firm entry/exit.

### Student tasks

1. Inspect `output/transfer/alternative_exposure_results.csv`.
2. Compare the baseline and alternative exposure summaries.
3. Explain whether the alternative index looks more like a routine-automation measure than a broad AI-complementarity measure.
4. State whether this transfer exercise is closer to exposure measurement or causal adoption evidence.

## Part IV. Challenge extension: robot-style local-market logic

### Objective

Contrast the within-firm AI adoption design with a market-level exposure design inspired by `@acemogluRestrepo2020RobotsJobs`.

### Be explicit before you interpret the challenge outputs

1. **Design family:** local labor-market shift-share exposure.
2. **Technology object:** predicted robot exposure, not realized treatment for each worker.
3. **Primary effect family:** market-level equilibrium incidence.
4. **Unit of observation:** commuting-zone-year cell.
5. **Observed labor-market margins:** employment-to-population change and wage change.
6. **Key equilibrium margin left offstage:** national product-demand and price adjustments.

### Student tasks

1. Inspect `output/transfer/robot_market_challenge.csv`.
2. Compare the robot-style exposure object to the AI adoption object from Part I.
3. Write two sentences on why the market-level design answers a different question from the firm-level design.

## Limitations relative to the original papers

Students should say these plainly.

1. The reproduction path uses synthetic firm-quarter data rather than the original French adoption environment in `@aghionEtAl2025HowDifferentUsesAI`.
2. The transfer path uses a public-like synthetic occupation-market panel rather than real vacancy, firm, or worker microdata.
3. The challenge path mimics a local-labor-market exposure design but does not reproduce the full institutional and data structure in `@acemogluRestrepo2020RobotsJobs`.
4. None of the bounded paths identify full general equilibrium, long-run diffusion, or welfare incidence across all workers.

## Deliverables checklist

- [ ] reproduced firm-level AI panel and summary table  
- [ ] figure on heterogeneous labor-demand responses by AI use  
- [ ] diagnosis note on exposure versus adoption  
- [ ] occupation-market transfer outputs  
- [ ] alternative exposure comparison results  
- [ ] short challenge note contrasting within-firm and market-level designs  

## Instructor notes

- The largest payoff comes from forcing students to label the technology object before interpreting results.
- The second largest payoff comes from making students compare within-firm adoption evidence to market-level exposure evidence without pretending they are interchangeable.
- The bounded path is intentionally local and synthetic so the Week 11 concepts are reproducible without confidential microdata.
