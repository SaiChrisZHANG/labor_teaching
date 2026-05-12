# Code Lab 3: Education, Skills, Aspirations, And Occupational Sorting

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 3 -- Education, skills, aspirations, and occupational sorting  
**Associated chapter:** `03-education-skills-aspirations-and-occupational-sorting.md`  
**Lab slug:** `03-education-skills-aspirations-and-occupational-sorting`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@porterSerra2020femaleRoleModelsMajor]  
**Secondary / challenge anchor:** [@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices]  
**Optional extension anchor:** [@fadlonLyngseNielsen2022earlyCareerSetbacks] or [@lepageLiZafar2025anticipatedDiscrimination]  

## Why This Lab Exists

Week 3 teaches students to separate early-choice mechanisms from later-adjustment frictions. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a reduced-form role-model intervention for major choice.
2. **Diagnose** the identifying variation, margin, and limitation of the reduced form.
3. **Transfer** the same diagnostic discipline to competitiveness and track choice.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential administrative or microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce treatment-control major-choice summaries for a role-model intervention;
2. distinguish a field-choice intervention from a later-career outcome design;
3. diagnose whether a result speaks to information, aspirations, belonging, competitiveness, or anticipated discrimination;
4. compute a bounded track-choice comparison by competitiveness and gender;
5. transfer the same logic to anticipated-discrimination or early-career-inertia evidence without overstating the design.

## Local Structure

```text
labs/03-education-skills-aspirations-and-occupational-sorting/
  lab.md
  smoke.sh
  src/
    build_week3_synthetic_data.py
    reproduce_role_models.py
    transfer_competitiveness.py
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
conda run -n research python src/build_week3_synthetic_data.py

conda run -n research python src/reproduce_role_models.py \
  --input original/reduced/porter_serra_role_models_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_competitiveness.py \
  --input transfer/data/buser_competitiveness_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/role_model_balance.csv`
- `output/reproduced/major_choice_effects.csv`
- `output/reproduced/mechanism_diagnostics.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the treatment?
- What is the observed margin?
- Does the intervention identify later wages, promotion, or occupational persistence?
- Which mechanisms are consistent with the result: information, belonging, role-model exposure, expected returns, or anticipated discrimination?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** State whether the design measures early choice, entry sorting, later adjustment, or a bundled sequence.
2. **Variation:** State the treatment or comparison group.
3. **Margin:** State the observed outcome and why it is a field-choice margin.
4. **Limitation:** State what additional data would be needed to connect the field-choice result to later labor-market outcomes.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/competitiveness_summary.csv`
- `output/transfer/track_choice_diagnostics.csv`
- `output/transfer/transfer_note.txt`

Use the competitiveness exercise inspired by [@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices] to explain why a behavioral measure linked to track choice is different from a randomized role-model intervention. State whether the object is a preference, a belief, an aspiration, or a reduced-form predictor of later sorting.

## Optional Frontier Prompt

Choose one extension:

- Use [@lepageLiZafar2025anticipatedDiscrimination] to ask how expected treatment could enter major choice before employer treatment is observed.
- Use [@fadlonLyngseNielsen2022earlyCareerSetbacks] to ask how an early-career shock could reveal later-adjustment frictions after initial choices are made.

Do not estimate either extension in the bounded path. State the observed margin, identifying variation, and the main threat to interpretation.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced role-model intervention summaries
- [ ] one-page design memo
- [ ] competitiveness transfer summaries
- [ ] paragraph distinguishing early-choice evidence from later-adjustment evidence
- [ ] optional anticipated-discrimination or early-career-inertia prompt
