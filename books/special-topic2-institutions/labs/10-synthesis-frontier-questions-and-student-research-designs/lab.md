# Code Lab 10: Synthesis, Frontier Questions, and Student Research Designs

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 10 -- Synthesis, Frontier Questions, and Student Research Designs  
**Associated chapter:** `10-synthesis-frontier-questions-and-student-research-designs.md`  
**Lab slug:** `10-synthesis-frontier-questions-and-student-research-designs`  
**Scope tier:** Capstone proposal studio  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 workshop hour  
**Primary lab logic:** Reproduce -> Diagnose -> Transfer  
**Primary anchor:** [@dell2010Mita]  
**Challenge anchor:** [@naiduYuchtman2013CoerciveContractEnforcement]  
**Optional extension anchor:** [@beerliPeriRuffnerSiegenthaler2021]  

## Why This Lab Exists

Week 10 turns the course into a project studio. The bounded path is memo-first because the capstone skill is research design: moving from a labor outcome to an institutional mechanism, counterfactual, data source, identification strategy, portability claim, and welfare or distributional object.

The lab does not reproduce confidential or proprietary data. Instead, it reverse-engineers the design architecture of anchor papers and generates a memo scaffold that students revise into an original institutions-and-labor project idea.

## Learning Objectives

By the end of the lab, students should be able to:

1. diagnose the labor outcome, institutional mechanism, comparison, data, design, welfare object, and portability claim in an anchor paper;
2. distinguish institutional detail from an institutional mechanism;
3. explain what a setting-specific paper identifies and what it does not identify;
4. transfer a design logic to a new labor-market setting without overclaiming external validity;
5. write a concise project memo that can seed a field paper, second-year paper, or dissertation idea.

## Anchor Menu

Students begin with three required design roles:

1. [@dell2010Mita] as the primary Reproduce anchor for historical coercive labor institutions and persistence;
2. [@naiduYuchtman2013CoerciveContractEnforcement] as the Diagnose challenge for contract enforcement, mobility, and bargaining power;
3. [@beerliPeriRuffnerSiegenthaler2021] as the optional Transfer extension for modern migration regimes and portability.

The local script also includes [@distelhorstHainmuellerLocke2017] as a global supply-chain governance alternative.

## Local Structure

```text
labs/10-synthesis-frontier-questions-and-student-research-designs/
  lab.md
  smoke.sh
  src/
    research_design_studio.py
  output/
    studio/
```

## First Command

```bash
conda run -n research python src/research_design_studio.py \
  --anchor dell2010Mita \
  --challenge naiduYuchtman2013CoerciveContractEnforcement \
  --extension beerliPeriRuffnerSiegenthaler2021 \
  --outdir output/studio
```

## Optional Extension Override

```bash
conda run -n research python src/research_design_studio.py \
  --anchor dell2010Mita \
  --challenge naiduYuchtman2013CoerciveContractEnforcement \
  --extension distelhorstHainmuellerLocke2017 \
  --outdir output/studio
```

## Part I. Reproduce

### Objective

Reverse-engineer the research architecture in [@dell2010Mita].

### Student Tasks

1. Run `src/research_design_studio.py` with the default anchors.
2. Inspect `output/studio/anchor_menu.csv`.
3. Inspect `output/studio/selected_anchor_diagnostic.csv`.
4. Open `output/studio/research_design_memo.md`.
5. Rewrite the Dell mechanism in your own words.

### Required Diagnosis Questions

- What is the labor outcome?
- What is the historical institutional mechanism?
- What comparison creates leverage?
- What data source observes the institutional exposure and labor margin?
- What is the main portability claim?
- What welfare or distributional object does the paper speak to?

## Part II. Diagnose

### Objective

Separate what the anchor identifies from what students may be tempted to infer.

Use [@naiduYuchtman2013CoerciveContractEnforcement] as the challenge case. Write five short paragraphs:

1. **Labor mechanism:** Explain how coercive contract enforcement changes worker exit, employer discipline, or bargaining power.
2. **Labor margin:** State the outcome and unit of observation.
3. **Design:** Explain the identifying variation and why it is credible.
4. **Portability:** Say what travels beyond nineteenth-century Britain and what does not.
5. **Welfare:** Name the distributional object and one welfare claim the design cannot settle alone.

## Part III. Transfer

### Objective

Build a mini-project memo that applies the same architecture to a new institutions-and-labor setting.

### Required Memo Sections

Your final memo should contain:

1. labor outcome;
2. institutional mechanism;
3. setting and leverage;
4. counterfactual;
5. data source;
6. identification strategy;
7. portability claim;
8. welfare or distributional object;
9. main threats.

### Student Tasks

1. Edit `output/studio/research_design_memo.md`.
2. Replace the starter project language with your own bounded question.
3. Add one sentence explaining what the design identifies.
4. Add one sentence explaining what it does not identify.
5. Add one sentence naming the welfare or distributional object.

## Workshop Prompts

1. Is the labor outcome narrower than the institutional story?
2. Does the mechanism do real work, or is the setting doing all the persuasion?
3. Does the comparison group match the mechanism?
4. What institutional detail sharpens identification?
5. Which data limitation would a skeptical reader notice first?
6. What travels: mechanism, estimate, design logic, or caution?
7. Who gains, who loses, and on what welfare margin?

## Deliverables Checklist

- [ ] selected anchor and challenge diagnostic table  
- [ ] one-page research-design memo  
- [ ] explicit statement of the labor outcome  
- [ ] explicit statement of the institutional mechanism  
- [ ] explicit statement of the comparison group and identifying variation  
- [ ] explicit statement of what travels and what remains local  
- [ ] explicit welfare or distributional object  
- [ ] one-paragraph frontier contribution  

## Limitations Of The Bounded Path

The local script is a teaching scaffold. It does not reproduce the original papers' data, estimation routines, archival work, or administrative records. Its purpose is to make research-design choices visible and to help students draft a project that is labor-relevant, institutionally precise, empirically credible, and appropriately bounded.
