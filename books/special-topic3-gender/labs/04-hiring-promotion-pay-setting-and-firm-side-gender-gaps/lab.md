# Code Lab 4: Hiring, Promotion, Pay-Setting, And Firm-Side Gender Gaps

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 4 -- Hiring, promotion, pay-setting, and firm-side gender gaps  
**Associated chapter:** `04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.md`  
**Lab slug:** `04-hiring-promotion-pay-setting-and-firm-side-gender-gaps`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@cullenPerezTruglia2023oldBoysClub]  
**Secondary / challenge anchor:** [@goldinRouse2000blindAuditions]  
**Optional extension anchor:** [@blundellDuchiniSimionTurrell2025payTransparency] or [@bensonLiShue2026potentialPromotionGap]  

## Why This Lab Exists

Week 4 teaches students to distinguish sorting into firms from what firms do after workers arrive. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a within-firm manager-access and promotion exercise.
2. **Diagnose** whether outputs speak to sorting, personnel processes, pay-setting, or retention.
3. **Transfer** the same margin discipline to a blind-screening entry design.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require personnel records, confidential wage data, or audit microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce grouped promotion and wage-growth summaries for a manager-access design;
2. distinguish informal manager access from general worker sorting;
3. state the identifying variation and observed margin in a within-firm personnel design;
4. transfer the same logic to a blind-screening design where the observed margin is advancement at entry;
5. explain why pay transparency or potential-rating evidence would require different data and outcomes.

## Local Structure

```text
labs/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps/
  lab.md
  smoke.sh
  src/
    build_week4_synthetic_data.py
    reproduce_old_boys_club.py
    transfer_blind_auditions.py
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
conda run -n research python src/build_week4_synthetic_data.py

conda run -n research python src/reproduce_old_boys_club.py \
  --input original/reduced/cullen_perez_truglia_old_boys_club_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_blind_auditions.py \
  --input transfer/data/goldin_rouse_blind_auditions_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/manager_access_balance.csv`
- `output/reproduced/promotion_effects.csv`
- `output/reproduced/mechanism_diagnostics.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the source of variation in manager access?
- What is the observed margin: informal interaction, promotion, wage growth, or retention?
- Does the design identify sorting into firms?
- What additional data would be needed to distinguish mentoring, sponsorship, information, favoritism, and exclusion?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** State whether the design measures sorting, within-firm personnel treatment, pay-setting, or retention.
2. **Variation:** State the manager-access comparison and why it is useful.
3. **Margin:** State the outcomes observed and why they are internal career margins.
4. **Limitation:** State why a one-firm personnel design needs caution on external validity and hidden mechanisms.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/screening_balance.csv`
- `output/transfer/blind_screen_advancement.csv`
- `output/transfer/transfer_diagnostics.csv`
- `output/transfer/transfer_note.txt`

Use the blind-screening exercise inspired by [@goldinRouse2000blindAuditions] to explain why an entry-stage screen is a different empirical object from a within-firm promotion design. State the identifying variation, observed margin, and what downstream outcomes remain unobserved.

## Optional Frontier Prompt

Choose one extension:

- Use pay transparency evidence [@blundellDuchiniSimionTurrell2025payTransparency] to ask whether a firm policy changes wage compression, raises, retention, or sorting.
- Use subjective potential ratings [@bensonLiShue2026potentialPromotionGap] to ask whether promotion gaps arise from performance measurement, potential ratings, or leadership-pipeline rules.

Do not estimate either extension in the bounded path. State the observed margin, identifying variation, and the main threat to interpretation.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced manager-access summaries
- [ ] one-page design memo
- [ ] blind-screening transfer summaries
- [ ] paragraph distinguishing entry screening from internal promotion
- [ ] optional transparency or potential-rating prompt
