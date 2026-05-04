# Code Lab 13: Synthesis, Student Research Designs, and the Bridge to Labor II

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 13 -- Synthesis, student research designs, and the bridge to Labor II  
**Associated chapter:** `13-synthesis-and-research-designs.md`  
**Lab slug:** `13-synthesis-and-research-designs`  
**Scope tier:** Bounded research-design studio  
**Primary language:** Python  
**Estimated student time:** 3 core hours + optional workshop time  
**Prerequisites:** Weeks 1--12, especially Weeks 4, 5, 8, 9, 11, and 12  
**Core economic question:** How do students move from a Labor I topic to a labor research question with one mechanism, one estimand, one feasible design, and one explicit statement about where Labor II begins?  
**Core design / estimator:** local anchor-paper packet plus a structured proposal workflow  
**Anchor-paper menu:** Card (1999); Autor, Katz, and Kearney (2008); Card et al. (2018); Neumark (2018); DellaVigna (2009)  

## Why this lab exists

Week 13 is not a new heavy replication. It is a research-design studio. The purpose of the lab is to help students convert a semester of worker-side labor economics into a feasible first paper idea. The bounded local path uses a deterministic anchor-paper packet, a compact reproduced design map, and an anchor-specific memo template so students can focus on economic discipline instead of on data access barriers.

## Learning objectives

By the end of this lab, students should be able to:

1. generate a local Week 13 anchor-paper packet from a deterministic teaching script;
2. reproduce a compact summary of how different anchor papers map into objects, mechanisms, designs, and Labor II bridge needs;
3. diagnose whether an idea is weak because the object is vague, the mechanism is underspecified, the design is weak, or the contribution is unclear;
4. draft a 2--3 page memo from one selected anchor paper;
5. state clearly whether the proposed extension remains partial equilibrium or already requires Labor II tools.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact anchor-paper map only.
- Diagnose the mechanism, data, estimand, and hidden equilibrium issue.
- Propose one extension memo only.
- Keep the smoke path fully local.
- Do not pull outside datasets or attempt a full official replication package.

## Lab roadmap

1. **Reproduce** a deterministic anchor-paper packet and a compact design-map figure.
2. **Diagnose** the object, mechanism, estimand, design, and Labor II boundary for one anchor.
3. **Propose** a 2--3 page memo using the generated anchor-specific template.

## Part 0. Setup and orientation

### Required local structure

```text
labs/13-synthesis-and-research-designs/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      week13_anchor_papers.csv
  transfer/
    README.md
    data-notes.md
    templates/
      research-memo-template.md
  src/
    build_week13_research_studio_packet.py
    reproduce_week13_anchor_map.py
    propose_week13_extension_memo.py
  output/
    reproduced/
    proposed/
```

### First commands to run

```bash
conda run -n research python src/build_week13_research_studio_packet.py

conda run -n research python src/reproduce_week13_anchor_map.py \
  --input original/reduced/week13_anchor_papers.csv \
  --outdir output/reproduced

conda run -n research python src/propose_week13_extension_memo.py \
  --input original/reduced/week13_anchor_papers.csv \
  --template transfer/templates/research-memo-template.md \
  --anchor card1999 \
  --outdir output/proposed
```

## Part I. Reproduce

### Objective

Build a compact Week 13 studio packet and reproduce the anchor-paper bridge map.

### Student tasks

1. Run `src/build_week13_research_studio_packet.py`.
2. Read `original/source-notes.md`.
3. Run `src/reproduce_week13_anchor_map.py`.
4. Inspect the generated bridge-map figure and design-family summary in `output/reproduced/`.
5. Write 5--7 sentences explaining why the same labor field can contain descriptive, quasi-experimental, matched worker--firm, and behavioral-design anchor papers.

### Required questions

- What is the primary object in each anchor paper?
- Which mechanism is being tested or organized?
- Which design family carries the identification burden?
- Which anchor is already closest to Labor II, and why?

### Minimum output

- one anchor-paper CSV;
- one reproduced figure;
- one design-family summary CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Turn one anchor paper into a disciplined diagnosis of object, mechanism, data, design, and contribution.

### Student tasks

1. Choose one anchor from the menu.
2. State the paper's main object in one sentence.
3. State the mechanism in one sentence.
4. Name the strongest alternative interpretation.
5. Explain whether the project is still worker-side or whether firm behavior, search, or wage-setting has already become central.

### Minimum output

- one one-page diagnosis memo;
- one paragraph on the estimand;
- one paragraph on the best design diagnostic;
- one paragraph on the Labor I / Labor II boundary.

## Part III. Propose

### Objective

Use the anchor-specific template to draft a feasible Week 13 extension memo.

### Student tasks

1. Run `src/propose_week13_extension_memo.py` with one anchor.
2. Fill in the generated memo template in `output/proposed/`.
3. Keep one primary estimand only.
4. Keep one mechanism only.
5. End with one explicit sentence on whether the project remains partial equilibrium.

### Scope constraints

- Do not propose three papers inside one memo.
- Do not use "important topic" as a contribution.
- Do not hide the firm or equilibrium issue.
- Do not turn the memo into a literature review.

## Part IV. Optional frontier extension

Strong students can take the same memo and add a final paragraph titled `Why Labor II may be necessary`. That paragraph should say whether the next step would require a worker--firm dataset, a search framework, a wage-setting model, a personnel-economics mechanism, or an institutional labor-demand margin.

## Reflection prompts

1. Which anchor paper was easiest to extend, and why?
2. Which proposal failure mode was most tempting in your own first draft?
3. What makes a strong worker-side paper idea different from a good broad seminar question?

## Deliverables checklist

- [ ] run log  
- [ ] local anchor-paper packet  
- [ ] reproduced bridge-map figure  
- [ ] diagnosis memo  
- [ ] generated proposal template  
- [ ] completed 2--3 page research memo  
- [ ] explicit Labor I / Labor II boundary statement  

## Instructor notes

- The lab is strongest when students commit to one anchor and one estimand early.
- The smoke path should stay narrow and local.
- The main teaching payoff is not the figure; it is the discipline of moving from topic to mechanism, data, design, and contribution.

