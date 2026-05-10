# Code Lab 10: Synthesis, Welfare, and Student Research Designs

**Course:** Behavioral Labor  
**Module / Week:** Week 10 -- Synthesis, Welfare, and Student Research Designs  
**Associated chapter:** `10-synthesis-welfare-and-student-research-designs.md`  
**Lab slug:** `10-synthesis-welfare-and-student-research-designs`  
**Scope tier:** Capstone proposal studio  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 workshop hour  
**Primary lab logic:** Reproduce -> Diagnose -> Transfer  
**Capstone artifact:** structured behavioral-labor research-design memo

## Why This Lab Exists

Week 10 turns the course into a project studio. The bounded path is memo-first rather than estimation-heavy because the capstone skill is design discipline: moving from a labor-market puzzle to a behavioral wedge, setting, identification strategy, method, welfare interpretation, and contribution.

The lab does not reproduce confidential or proprietary data. Instead, it reverse-engineers the research logic of an anchor menu and produces a memo scaffold that students revise into an original behavioral-labor project idea.

## Learning Objectives

By the end of the lab, students should be able to:

1. diagnose the question, wedge, setting, design, method, and welfare claim in an anchor paper;
2. distinguish a treatment effect from a behavioral parameter, welfare object, and equilibrium response;
3. transfer a design logic to a new labor-market setting without overclaiming;
4. state the benchmark action or normative criterion used for welfare interpretation;
5. write a concise research-design memo that can seed a field paper, second-year paper, or dissertation idea.

## Anchor Menu

Students choose one or two anchors:

1. [@muellerSpinnewijnTopa2021] for job-search beliefs, repeated expectations, and unemployment duration;
2. [@dellaVignaListMalmendierRao2022] for social preferences, gift exchange, and workplace effort;
3. [@bhargavaManoli2015] for psychological frictions, take-up, implementation, and administrative design;
4. [@bernheimFradkinPopov2015] for defaults, retirement saving, and welfare under passive choice.

## Local Structure

```text
labs/10-synthesis-welfare-and-student-research-designs/
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
  --anchor muellerSpinnewijnTopa2021 \
  --outdir output/studio
```

## Optional Comparison Override

```bash
conda run -n research python src/research_design_studio.py \
  --anchor bhargavaManoli2015 \
  --comparison bernheimFradkinPopov2015 \
  --outdir output/studio
```

## Part I. Reproduce

### Objective

Reverse-engineer one anchor paper's research architecture.

### Student Tasks

1. Run `src/research_design_studio.py` with your chosen anchor.
2. Inspect `output/studio/anchor_menu.csv`.
3. Inspect `output/studio/selected_anchor_diagnostic.csv`.
4. Open `output/studio/research_design_memo.md`.
5. Rewrite the memo's mechanism section in your own words.

### Required Diagnosis Questions

- What is the labor-market fact or puzzle?
- What behavioral wedge is being studied?
- What institution or environment makes the wedge economically relevant?
- What variation identifies the object?
- Is the main estimate a treatment effect, behavioral parameter, welfare-relevant wedge, or equilibrium-adjusted response?

## Part II. Diagnose

### Objective

Separate what the anchor identifies from what students may be tempted to infer.

### Student Tasks

Write five short paragraphs:

1. **Behavioral object:** Name the wedge and one standard alternative explanation.
2. **Labor margin:** State the outcome and unit of observation.
3. **Design:** Explain the identifying variation and econometric method.
4. **Welfare:** Define the benchmark action or state why the paper does not settle welfare.
5. **External validity:** Name the firm, market, policy, or learning response that may change interpretation.

## Part III. Transfer

### Objective

Build a mini-project memo that applies the anchor logic to a new setting.

### Required Memo Sections

Your final memo should contain:

1. puzzle or fact;
2. behavioral mechanism;
3. labor-market setting;
4. outcome and unit of observation;
5. identifying variation;
6. econometric method;
7. welfare or policy interpretation;
8. contribution relative to the frontier.

### Student Tasks

1. Edit `output/studio/research_design_memo.md`.
2. Replace the starter project question with your own bounded question.
3. Add one sentence explaining what the design identifies.
4. Add one sentence explaining what it does not identify.
5. Add one sentence naming the welfare benchmark or explicitly declining a welfare claim.

## Workshop Prompts

1. Is the behavioral wedge narrower than the labor-market question?
2. Does the setting make the wedge first-order, or is the wedge decorative?
3. Does the method match the estimand?
4. Would reduced-form evidence be enough, or is a structural or calibrated object required?
5. What firm, market, or policy response could alter external validity?
6. What would make this project a contribution rather than a rerun?

## Deliverables Checklist

- [ ] selected anchor and optional comparison anchor  
- [ ] anchor diagnostic table  
- [ ] one-page research-design memo  
- [ ] explicit statement of what the design identifies  
- [ ] explicit statement of the welfare benchmark or welfare limitation  
- [ ] one-paragraph frontier contribution  

## Limitations Of The Bounded Path

The local script is a teaching scaffold. It does not reproduce the original papers' data, estimation routines, or full institutional detail. Its purpose is to make research-design choices visible and to help students draft a proposal that is behavioral, labor-relevant, empirically credible, and appropriately bounded.
