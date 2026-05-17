Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib

If helpful, also inspect:
- the Week 4 source pack if it exists in the repo
- the Week 4 slide file if it exists
- the Week 4 lab folder if it exists

Goal: draft Week 4 of the Health, Population, and Labor course as a fully synchronized week with canonical chapter, slides, and lab outputs, using the existing special-topics workflow.

Canonical output files:
- `books/special-topic6-health-population/04-mental-health-stress-workplace-productivity-and-worker-welfare.md`
- `books/special-topic6-health-population/slides/week4/04-mental-health-stress-workplace-productivity-and-worker-welfare.tex`
- `books/special-topic6-health-population/labs/04-mental-health-stress-workplace-productivity-and-worker-welfare/`

Use these week-pack files as the intellectual source of truth:
- `special_topic6_health_population_week4_edit_pack/source/04-mental-health-stress-workplace-productivity-and-worker-welfare.md`
- `special_topic6_health_population_week4_edit_pack/bibliography/04-mental-health-stress-workplace-productivity-and-worker-welfare.bib`
- all markdown files under `special_topic6_health_population_week4_edit_pack/tables/`

Week identity to preserve:
- mental health as a labor-market force, not an individual residual
- depression, anxiety, stress, pain, and substance use as labor-relevant conditions
- absenteeism, presenteeism, productivity, retention, supervision, job quality, safety, and welfare
- stigma around mental health and treatment-seeking
- the two-way relationship between labor-market choices and mental health
- a methods/data box that is honest about the causal limitations of the literature

Special-topics defaults to enforce:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only:
  `books/special-topic6-health-population/references.bib`

Required chapter structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading Ladder And References
7. Exercises And Discussion Prompts
8. Reproducibility And Code Lab Note
9. Slide Companion Note
10. Bridge Forward

Required content additions:
A. Stigma, disclosure, and treatment
- make stigma against mental health and treatment a named labor-market mechanism
- show how stigma affects disclosure, help-seeking, treatment access, accommodations, attendance, and career choices

B. Work causing mental health outcomes
- include a section on how jobs, supervision, workload, autonomy, conflict, isolation, and meaning of work contribute to mental health
- connect mental health to job quality and worker welfare, not just productivity loss

C. Methods and measurement
- include a dedicated methods/data section or box that covers:
  - survey measures (PHQ-9, GHQ, CES-D, K6, self-reported distress)
  - administrative proxies (prescriptions, claims, sick leave, disability claims, treatment episodes)
  - workplace measures (absenteeism, presenteeism, performance, quits, accommodations)
  - key identification challenges:
    reverse causality, dynamic selection, diagnosis intensity, treatment selection, co-morbidity, SES confounding, and differential reporting
- be explicit that credible causal work is still limited in many areas, and that this is an open field
- include frontier causal strategies where relevant:
  treatment access shocks, waiting-time shocks, pandemic and workplace shocks, job-loss shocks, policy changes, and structural/job-search approaches

D. Research frontier emphasis
- keep the lecture labor-focused and research-facing
- make the open empirical gaps legible to students

Slides requirements:
- create the Week 4 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week4/04-mental-health-stress-workplace-productivity-and-worker-welfare.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on measurement and causal challenges
  - one slide on stigma/treatment/disclosure
  - one slide on mental health as a productivity and welfare object
  - one slide on how labor conditions shape mental health
  - one slide on frontier methods and research opportunities
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week4/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- pick one primary anchor paper with a feasible empirical object (e.g. Bubonya et al. on productivity or a comparable paper with tractable measures)
- use one challenge/extension paper on stigma, treatment, or job-design/meaning if useful
- keep the lab student-facing and concrete
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `smoke.sh`
  - `src/`
  - `output/reproduced/`
  - `output/transfer/`
  - reduced or synthetic teaching-path data if needed
- do not invent replication packages
- be conservative if replication availability is uncertain

Implementation notes:
- treat the source markdown as the intellectual source of truth
- keep the week labor-focused, not a general clinical-mental-health lecture
- be explicit when evidence is correlational or structurally identified rather than cleanly causal
- preserve the distinction between:
  (i) mental health affecting work,
  (ii) work affecting mental health,
  (iii) treatment and stigma,
  (iv) measurement and welfare

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 4 slides from the canonical path
3. if the Week 4 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 4 slides compile from the canonical path
5. whether the Week 4 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
