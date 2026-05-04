# {{ lab-title }}

**Course:** {{ course-name }}  
**Module / Week:** {{ module-name }}  
**Associated chapter:** `{{ chapter-file }}`  
**Lab slug:** `{{ lab-slug }}`  
**Scope tier:** {{ Lite | Standard | Stretch }}  
**Primary language:** {{ Python | R | Stata }}  
**Companion languages (optional):** {{ none | R | Stata | Python }}  
**Estimated student time:** {{ x }} core hours + {{ y }} optional hours  
**Prerequisites:** {{ prerequisites }}  
**Core economic question:** {{ one-sentence question }}  
**Core design / estimator:** {{ DID / IV / RDD / structural / event study / causal forest / etc. }}  
**Source paper for reproduction:** {{ citation placeholder }}  
**Replication package source:** {{ DOI / repository / URL placeholder }}  
**Transfer dataset source:** {{ public dataset placeholder or 'to be specified' }}

## Why this lab exists

{{ 1 short paragraph explaining why this lecture benefits from a code lab and why the selected paper/design is pedagogically useful. }}

## Learning objectives

By the end of this lab, students should be able to:

1. recover at least one headline empirical result from a published paper;
2. explain the paper's estimand, identification logic, and main implementation choices;
3. read and navigate a real replication package rather than only toy code;
4. transfer one empirical design or estimator to a bounded new dataset;
5. compare the original and transferred exercises without overstating external validity;
6. document code and data decisions clearly enough for another student to reproduce them.

## Scope rules

This template is designed to keep each lab ambitious but bounded.

- Use **one source paper** and **one main identification strategy or estimator**.
- Reproduce **one to two headline outputs** at most.
- The transfer exercise should use **one small new dataset** or **one clearly defined extension sample**.
- No IRB-dependent original human-subject data collection.
- The transfer exercise should yield **one main table or one main figure**, not a full paper.
- Students may acquire, construct, or collect a small dataset, but the acquisition burden should normally stay within a few hours.
- If the original package is computationally heavy, provide a reduced pedagogical pathway.

## Lab roadmap

This lab has four parts:

1. **Reproduce** a core result from the original paper.  
2. **Diagnose** the code and research design.  
3. **Transfer** the estimator or design to a new dataset or setting.  
4. **Reflect** on what carries over and what does not.

## Part 0. Setup and orientation

### Files and environment

- Create a working directory for the lab.
- Record package versions, software dependencies, and operating-system notes.
- Read the replication README before running any code.
- Identify the code path that produces the chosen table or figure.

### Required student setup

- `README.md` with run instructions
- `environment.yml` or `requirements.txt` for Python when relevant
- `renv.lock` notes for R when relevant
- Stata version note when relevant
- a short run log (`run-log.md`) that records what worked, what failed, and what was changed

### Repo structure for the lab

```text
labs/{{ lab-slug }}/
  README.md
  lab.md
  run-log.md
  original/
    README.md
    source-notes.md
  transfer/
    README.md
    data-notes.md
  src/
    reproduce_01.*
    transfer_01.*
    utils.*
  output/
    reproduced/
    transfer/
  environment/
```

## Part I. Reproduce a headline result

### Objective

Recover one or two central outputs from the source paper using the provided package.

### Student tasks

1. Download or access the official replication package.
2. Identify the file(s) that generate the target result.
3. Run the minimal code path needed to reproduce it.
4. Save the reproduced result in `output/reproduced/`.
5. Document any divergence from the published output.

### Required questions

- What is the precise estimand behind the reproduced result?
- What sample restrictions are being used?
- Where in the code are the treatment, outcome, and controls defined?
- Where are standard errors or inference choices specified?
- Which preprocessing or cleaning steps are most consequential?

### Minimum output

- one reproduced table, figure, or coefficient set;
- one short note describing whether the result matched exactly, approximately, or not at all;
- one code map showing which files matter for the target result.

## Part II. Diagnose the code and the design

### Objective

Move from "I can run it" to "I understand what it is doing."

### Student tasks

1. Write a short design memo explaining the paper's question, estimand, and identification logic.
2. Map the code workflow from raw data to final result.
3. Identify at least two design choices that are substantive rather than cosmetic.
4. Identify one fragility, ambiguity, or portability issue in the original package.

### Required prompts

- Which identifying variation does the paper rely on?
- Under what assumptions does the estimate have a causal interpretation?
- Which implementation choices appear tightly linked to the institutional setting?
- Which parts of the workflow look portable to another dataset?
- What would be the first robustness check you would add?

### Minimum output

- `design-memo.md` or equivalent section in the submission;
- a workflow diagram or bullet map from data to result;
- one paragraph on package portability and reproducibility quality.

## Part III. Guided transfer exercise

### Objective

Apply the same empirical logic to a bounded new dataset or adjacent setting.

### Acceptable transfer sources

Choose **one**:

- a public dataset newly downloaded by the student;
- a new time period from the same source;
- a new geography;
- a subsample with a clearly justified research reason;
- a small hand-built dataset from public documents;
- a matched dataset built from two public files;
- a re-coded or extended version of the original data with a new variable construction.

### Transfer design note

Students must specify:

- the new research question;
- the new data source and why it is appropriate;
- what stays fixed from the original design;
- what changes and why;
- what the transferred estimate can and cannot be interpreted as.

### Scope constraints

- Use the **same broad design family** as the original paper whenever possible.
- Do not introduce multiple new estimators.
- Do not attempt a full-scale new research project.
- Prefer one clean adaptation over many weak extensions.

### Student tasks

1. Acquire or construct the transfer dataset.
2. Write a concise data note describing provenance, units, and key variables.
3. Adapt the estimator or workflow from the original package.
4. Produce one main result.
5. Compare the transferred result to the original design in a disciplined way.

### Required prompts

- Why is this transfer informative rather than arbitrary?
- Which assumptions remain credible in the new setting?
- Which assumptions are weaker or stronger than in the original paper?
- What part of the original code could be reused directly?
- What had to be rewritten from scratch?

### Minimum output

- `data-notes.md` for the transfer dataset;
- one estimation script;
- one main table or one main figure in `output/transfer/`;
- one paragraph comparing the original and transferred exercises.

## Part IV. Reflection and communication

### Objective

Convert coding activity into research judgment.

### Student prompts

1. What did you learn by reading the original package that a cleaned textbook example would not teach?
2. Was the original package easy to reproduce? Why or why not?
3. Did the transfer exercise feel like a robustness check, a replication, or an application? Explain.
4. What would be the most credible next extension if you had one more week?

### Final memo

Students submit a short memo that contains:

- the reproduced result;
- a design diagnosis;
- the transfer exercise;
- one main takeaway about identification or implementation;
- one limitation of the transfer.

## Deliverables checklist

A complete submission should include:

- [ ] reproducibility run log
- [ ] reproduced table/figure
- [ ] code map or workflow note
- [ ] design memo
- [ ] transfer data note
- [ ] transfer script
- [ ] one transfer table or figure
- [ ] final memo
- [ ] clean README with run order

## Suggested grading rubric

| Component | Weight |
|---|---:|
| Reproduction completeness and accuracy | 25 |
| Understanding of design and identification | 25 |
| Quality of transfer exercise | 25 |
| Code organization and reproducibility | 15 |
| Interpretation and communication | 10 |

## Instructor notes

### When to assign this lab

Use this lab when the lecture has:

- a strong paper with a usable public replication package;
- a method or design students should see in real code;
- a natural adjacent dataset for transfer;
- a manageable compute burden.

### When to downgrade to Lite scope

Choose `Lite` when:

- the package is difficult to run;
- the lecture is conceptually dense already;
- the transfer data are harder to acquire;
- the teaching goal is mainly reproducibility and code reading.

In `Lite` mode, require Parts I, II, and a very small transfer plan, but not a full transfer estimate.

### When to upgrade to Stretch scope

Choose `Stretch` when:

- students already know the method well;
- the package is stable and lightweight;
- a strong public extension dataset exists;
- the lab can naturally support student research ideas.

In `Stretch` mode, allow one additional robustness check or heterogeneity exercise, but keep the lab within the same design family.

## Notes on language choice

- Run the original package in the author's native language when that minimizes friction.
- Prefer **Python** for the public teaching version of the transfer exercise unless there is a strong pedagogical reason to use R or Stata.
- If R or Stata are used, provide a brief note explaining why that language is the best fit for this lab.
- Do not create full parallel implementations in all three languages by default.

## Citation and provenance placeholders

- **Paper citation:** {{ fill manually }}
- **Replication package citation:** {{ fill manually }}
- **Data citation for transfer exercise:** {{ fill manually }}
- **Software/package citations:** {{ fill manually }}

## Lecture-specific customization checklist

Before using this template for a specific lecture, fill in:

- [ ] course and module metadata
- [ ] source paper and replication package
- [ ] target reproduced result
- [ ] transfer dataset source
- [ ] scope tier
- [ ] language choice
- [ ] student time budget
- [ ] deliverable due date
- [ ] any lecture-specific warnings about computation or data access
