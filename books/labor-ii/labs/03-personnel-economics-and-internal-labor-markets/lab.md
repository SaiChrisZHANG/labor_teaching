# Code Lab 03: Team Incentives, Promotions, and Internal Labor Markets

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 3 — Personnel economics and internal labor markets  
**Associated chapter:** `03-personnel-economics-and-internal-labor-markets.md`  
**Lab slug:** `03-personnel-economics-and-internal-labor-markets`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 1--2, basic command-line work, introductory `pandas`, comfort reading grouped summaries and simple reduced-form figures  
**Core economic question:** How do economists distinguish effort incentives, assignment, and promotion effects when studying internal labor markets?  
**Primary source anchor:** [@friebelHeinzKruegerZubanov2017]  
**Challenge anchor:** [@bensonLiShue2019]  
**Optional extension anchor:** [@emanuelHarrington2024]

## Why this lab exists

Week 3 should not stop at saying that firms use incentives and promotions. Students should practice saying what varies, what unit is observed, what margin is measured, and which interpretation is still too strong. [@friebelHeinzKruegerZubanov2017] is a strong teaching anchor because the variation is a clear firm-side incentive change. [@bensonLiShue2019] is a strong challenge anchor because it forces the assignment-versus-incentives distinction into the data.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a compact team-incentive result from a local synthetic panel;
2. diagnose whether the bounded evidence is closer to an effort effect, a selection effect, or a team-complementarity effect;
3. explain why promotions are not just rewards for current performance;
4. transfer Week 3 logic to a promotion-assignment scenario inspired by the Peter Principle;
5. articulate why remote-work estimates often require a separate selection-versus-treatment design.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact team-incentive pattern from a local synthetic panel.
- Diagnose the design using the Week 3 identification checklist.
- Transfer the logic to a synthetic promotion-assignment file.
- Keep the smoke test on the synthetic teaching path only.
- Do not turn the lab into a full confidential microdata replication.

## Lab roadmap

1. **Reproduce** a reduced team-incentive pattern using the synthetic retail panel.
2. **Diagnose** what the experiment identifies and what it does not.
3. **Transfer** the Week 3 logic to a promotion-assignment scenario.
4. **Extend** the interpretation to remote work as a selection-versus-treatment problem.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for [@friebelHeinzKruegerZubanov2017]. It is a synthetic teaching workflow inspired by the paper's design logic: team incentives, complementarity, and profits. The goal is to practice Week 3 reasoning cleanly, not to ship the full proprietary firm environment of the published study.

### First commands to run

```bash
conda run -n research python src/reproduce_friebel_team_incentives.py \
  --input original/reduced/friebel_team_incentives_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_personnel_assignment.py \
  --input transfer/data/personnel_assignment_scenarios.csv \
  --outdir output/transfer
```

## Part I. Reproduce a bounded personnel-economics object

### Objective

Recover a compact pre/post team-incentive pattern, then compare gains across higher- and lower-complementarity teams.

### Student tasks

1. Read `original/source-notes.md`.
2. Run `src/reproduce_friebel_team_incentives.py`.
3. Inspect `output/reproduced/friebel_team_incentives_event_path.csv`.
4. Open `output/reproduced/friebel_team_incentives_effects.png`.
5. Read `output/reproduced/friebel_team_incentives_summary.csv`.
6. Read `output/reproduced/friebel_team_incentives_heterogeneity.csv`.
7. Write a short note explaining why a within-firm team incentive result is closest to an effort-and-organization object rather than a long-run sorting estimate.

### Required questions

- What varies in the bounded reproduction path?
- Which outcome margins are observed directly?
- Why is profit a stronger Week 3 outcome than sales alone in this setting?
- What would you need to observe to make a stronger claim about selection or retention?

## Part II. Diagnose the design

### Objective

Move from "incentives improved performance" to "I know which personnel object this design identifies."

### Student tasks

1. State the identifying variation in one sentence.
2. Name the unit of observation in one sentence.
3. Name the observed outcome margins in one sentence.
4. Explain whether the bounded evidence is mostly about effort, selection, assignment, or team complementarities.
5. State one external-validity concern that would matter if another firm copied the same incentive plan.

### Minimum output

- one short design memo;
- one annotated summary table;
- one paragraph separating internal validity from external validity.

## Part III. Transfer the Week 3 logic

### Objective

Use the Week 3 framework on a synthetic promotion file that compares performance-first, balanced, and potential-first promotion rules.

### Student tasks

1. Run `src/transfer_personnel_assignment.py`.
2. Inspect `output/transfer/personnel_assignment_summary.csv`.
3. Open `output/transfer/personnel_assignment_tradeoff.png`.
4. Compare how the promoted group's current-job performance differs from its post-promotion output under each rule.
5. Explain why this transfer file is the natural bridge to [@bensonLiShue2019].

### Acceptable transfer interpretations

- a performance-first rule can maximize current-job incentives while making weaker next-job assignments;
- a potential-first rule can improve future-role fit while weakening the tournament signal for current effort;
- a balanced rule can improve assignment without fully giving up career incentives.

## Part IV. Optional extension

Use one extension only.

1. Read [@bensonLiShue2019] and explain how promotion data separate current performance from next-job fit.
2. Read [@emanuelHarrington2024] and explain why remote-work productivity estimates must separate who selects into remote work from what remote work does to comparable workers once assigned.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced event-path table and figure  
- [ ] one-page diagnose memo  
- [ ] transfer summary table and figure  
- [ ] short bridge note to [@bensonLiShue2019]  
- [ ] final reflection memo

## Instructor notes

- The bounded path is for local execution and smoke testing.
- The biggest classroom payoff comes from forcing students to separate effort effects from assignment and selection claims.
- Students should not treat the synthetic gains as publishable estimates or as evidence that one personnel policy transports cleanly across firms.
