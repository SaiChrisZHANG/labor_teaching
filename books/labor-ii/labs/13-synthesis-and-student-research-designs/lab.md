# Code Lab 13: Synthesis and Student Research Designs

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 13 --- Synthesis and Student Research Designs  
**Associated chapter:** `13-synthesis-and-student-research-designs.md`  
**Lab slug:** `13-synthesis-and-student-research-designs`  
**Scope tier:** Capstone studio week  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 optional hour  
**Prerequisites:** Weeks 1--12; comfort with distinguishing mechanism, unit, observed margin, and equilibrium scope  
**Core economic question:** How do we turn a labor-market mechanism into a research design that is sharp enough to be credible and bounded enough to be feasible?  
**Primary lab logic:** Diagnose -> Compare -> Design  
**Capstone artifact:** structured research-design memo scaffold

## Why this lab exists

Week 13 should not end with a vague "final reflection." The capstone skill in Labor II is learning how to move from a labor-market mechanism to a research design without skipping the hard middle steps. This lab exists to make those middle steps explicit.

The lab is memo-first rather than estimation-heavy. That is deliberate. Students have already spent twelve weeks learning the field's objects. Week 13 asks them to diagnose an anchor paper, compare it to a nearby design, and then build a bounded extension that could seed a field paper, second-year paper, or dissertation direction.

## Learning objectives

By the end of this lab, students should be able to:

1. diagnose the central mechanism in a major Labor II paper;
2. name the unit of treatment and the unit of observation separately;
3. distinguish the observed labor-market margin from the broader equilibrium or welfare object;
4. compare a policy-style design to a shock-style or measurement-style design without flattening them into one template;
5. produce a structured research-design memo that can be revised into a stronger project.

## Scope rules

This lab is intentionally bounded.

- Choose one anchor paper, or one tightly related pair, from the capstone menu.
- Use the local script to generate a memo scaffold and comparison table.
- Do not build a full new replication package.
- Do not claim a welfare or equilibrium contribution unless your design actually supports it.
- Keep the smoke path fully local and file-based.

## Anchor-paper menu

The required anchor menu spans the major Labor II blocks.

1. [@saezSchoeferSeim2019]
2. [@yehMacalusoHershbein2022]
3. [@cengizDubeLindnerZipperer2019]
4. [@jagerNaiduSchoefer2024]
5. [@acemogluRestrepo2020RobotsJobs]
6. [@autorDornHanson2013ChinaSyndrome]

## Lab roadmap

1. **Diagnose** one anchor paper.
2. **Compare** it to a nearby anchor that changes the unit, mechanism, or treatment family.
3. **Design** one bounded extension that names question, mechanism, unit, data, design, equilibrium concern, and contribution.

## Part 0. Setup and orientation

### First command to run

```bash
conda run -n research python src/research_design_studio.py \
  --anchor saezSchoeferSeim2019 \
  --outdir output/studio
```

### Optional comparison override

```bash
conda run -n research python src/research_design_studio.py \
  --anchor acemogluRestrepo2020RobotsJobs \
  --comparison autorDornHanson2013ChinaSyndrome \
  --outdir output/studio
```

### Before you interpret anything

Write down five things for the anchor you chose.

1. What is the central labor-market mechanism?
2. What is the unit of treatment?
3. What is the unit of observation?
4. What labor-market margin is directly observed?
5. What equilibrium concern remains offstage?

## Part I. Diagnose the anchor paper

### Objective

Make the paper's design legible before trying to extend it.

### Student tasks

1. Run `src/research_design_studio.py` with your chosen anchor.
2. Inspect `output/studio/anchor_menu.csv`.
3. Inspect `output/studio/selected_anchor_comparison.csv`.
4. Open `output/studio/research_design_memo.md`.
5. Rewrite the memo's mechanism section in your own words.

### Required diagnosis questions

- Is the anchor primarily descriptive, reduced-form, or structural?
- Does the anchor study a policy, a shock, or a measurement object?
- Which claim in the paper is strongest because it lines up tightly with the observed margin?
- Which larger claim would require more equilibrium structure than the anchor itself provides?

## Part II. Compare it to a nearby design

### Objective

Use a comparison anchor to make the design choice visible rather than accidental.

### Comparison logic

The comparison anchor should change at least one of these:

1. the treatment family, such as policy versus shock;
2. the unit of analysis, such as firm versus place;
3. the main observed margin, such as wages versus employment;
4. the equilibrium challenge, such as spillovers versus long-run adjustment.

### Student tasks

1. Compare the primary and comparison rows in `selected_anchor_comparison.csv`.
2. Write one paragraph on what stays constant across the two papers.
3. Write one paragraph on what changes in the interpretation because the unit or treatment family changes.

## Part III. Design a bounded extension

### Objective

Turn the comparison into a feasible project idea.

### Required memo sections

Your final memo should contain:

1. question,
2. mechanism,
3. treatment or exposure object,
4. unit of observation,
5. observed margin,
6. identifying variation or descriptive design,
7. key equilibrium concern,
8. proposed extension,
9. why the extension matters.

### Student tasks

1. Edit `output/studio/research_design_memo.md`.
2. Replace the starter question with your own bounded question.
3. Add one sentence explaining why your chosen unit is necessary.
4. Add one sentence stating what your design will not identify.
5. Add one sentence explaining why the extension is feasible.

## Part IV. Optional workshop extension

### Objective

Stress-test the memo before it becomes a project pitch.

### Workshop prompts

1. Is the mechanism narrower than the question, or wider?
2. Is the unit doing conceptual work, or is it just inherited from a familiar dataset?
3. Is the proposed extension a feasible next paper, or an entire dissertation in disguise?
4. Would a descriptive design already answer the question well enough?
5. If not, what stronger design feature is truly necessary?

## Limitations of the bounded path

Students should say these plainly.

1. The local script does not reproduce the original papers' estimation environments.
2. The artifact is a memo scaffold, not a finished project proposal.
3. The comparison file clarifies design choices, but it does not settle identification.
4. The bounded path is strongest as a design discipline exercise rather than as new evidence.

## Deliverables checklist

- [ ] selected anchor and comparison anchor  
- [ ] diagnosis of mechanism, treatment unit, observation unit, and observed margin  
- [ ] explicit statement of the main equilibrium concern  
- [ ] structured research-design memo with all nine sections  
- [ ] bounded extension idea that matches the proposed design  

## Instructor notes

- The highest-value move is forcing students to separate the observed margin from the broader welfare claim they are tempted to make.
- The second-highest-value move is making them compare designs that look similar rhetorically but differ in treatment family or unit.
- The memo-first format is a feature, not a compromise. It lets Week 13 end with real research discipline rather than loose synthesis language.
