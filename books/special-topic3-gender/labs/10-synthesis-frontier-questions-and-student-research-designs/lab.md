# Code Lab 10: Synthesis, Frontier Questions, And Student Research Designs

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 10 -- synthesis, frontier questions, and student research designs  
**Associated chapter:** `10-synthesis-frontier-questions-and-student-research-designs.md`  
**Lab slug:** `10-synthesis-frontier-questions-and-student-research-designs`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 90 minutes core + 45 minutes memo revision  

## Why This Lab Exists

The final week does not need a heavy replication package. It needs a disciplined way to turn project ideas into credible research designs. The bounded path uses a deterministic idea bank to practice three moves:

1. **Reproduce** a structured design table from candidate gender-and-labor project ideas.
2. **Diagnose** identification threats, data fit, portability, and welfare interpretation.
3. **Design** a short research memo for one selected project.

The lab is a teaching analog. It does not require confidential microdata or an official replication archive.

## Learning Objectives

By the end of the lab, students should be able to:

1. classify candidate ideas by labor-market object, mechanism, comparison group, margin, data source, method, and welfare object;
2. diagnose whether a project has a credible counterfactual rather than only an important topic;
3. compare candidate ideas on labor focus, mechanism clarity, data fit, identification credibility, portability, and welfare relevance;
4. map outcomes to methods without overclaiming what the data observe;
5. produce a short research memo scaffold that can become a seminar proposal.

## Local Structure

```text
labs/10-synthesis-frontier-questions-and-student-research-designs/
  lab.md
  smoke.sh
  src/
    build_project_idea_bank.py
    reproduce_design_table.py
    diagnose_project_ideas.py
    design_research_memo.py
  original/
    reduced/
  output/
    reproduced/
    diagnosed/
    design/
```

## First Commands

```bash
conda run -n research python src/build_project_idea_bank.py

conda run -n research python src/reproduce_design_table.py \
  --input original/reduced/week10_candidate_project_ideas.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_project_ideas.py \
  --input original/reduced/week10_candidate_project_ideas.csv \
  --outdir output/diagnosed

conda run -n research python src/design_research_memo.py \
  --ideas original/reduced/week10_candidate_project_ideas.csv \
  --scores output/diagnosed/project_scores.csv \
  --outdir output/design
```

## Part I. Reproduce

Run the builder and reproduction script. Inspect:

- `output/reproduced/research_design_table.csv`
- `output/reproduced/object_method_counts.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which ideas begin with a labor object rather than a broad population or policy label?
- Which methods require event timing, randomization, worker mobility, policy rollout, survey variation, or linked data?
- Which ideas have clear welfare or distributional objects?

## Part II. Diagnose

Run the diagnosis script. Inspect:

- `output/diagnosed/project_scores.csv`
- `output/diagnosed/identification_threats.csv`
- `output/diagnosed/method_fit_diagnostics.csv`
- `output/diagnosed/diagnosis_note.txt`

Write a short diagnostic paragraph for two ideas:

1. **Strongest design:** Explain why the comparison group, data, and margin fit together.
2. **Weakest design:** Explain what additional variation or data would be needed.

## Part III. Design

Run the memo script. It selects the highest-scoring idea unless you pass `--project-id`.

Inspect:

- `output/design/research_memo_scaffold.md`
- `output/design/memo_fields.csv`

Revise the memo scaffold by hand. The finished memo should include:

1. research question;
2. labor-market object;
3. mechanism;
4. comparison group or counterfactual;
5. key labor margin;
6. data source;
7. identification strategy;
8. main threats;
9. portability and broad relevance;
10. welfare or distributional object;
11. contribution.

## Deliverables Checklist

- [ ] reproduced design table
- [ ] project-score diagnostics
- [ ] one short diagnostic paragraph comparing two ideas
- [ ] memo scaffold for one selected project
- [ ] revised contribution sentence

## Reflection Prompt

Take the selected project and write one sentence in this form:

> This project uses `[variation]` in `[setting]` to identify how `[mechanism]` changes `[labor object]`, with implications for `[welfare or distributional object]`.

If the sentence is vague, the design is not ready yet.
