Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib
- @books/special-topic6-health-population/README.md if it exists

If helpful, also inspect:
- nearby weeks from other special topics only for structure comparison
- the week pack files under:
  - `special_topic6_health_population_week1_edit_pack/source/`
  - `special_topic6_health_population_week1_edit_pack/bibliography/`
  - `special_topic6_health_population_week1_edit_pack/tables/`

Goal: create or refresh Week 1 of the Labor Market, Health, and Population course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic6-health-population/01-health-risk-and-labor-markets-core-frameworks-and-measurement.md`
- `books/special-topic6-health-population/slides/week1/01-health-risk-and-labor-markets-core-frameworks-and-measurement.tex`
- `books/special-topic6-health-population/labs/01-health-risk-and-labor-markets-core-frameworks-and-measurement/`

Use these as the intellectual source of truth:
1. the week source markdown if available:
   `special_topic6_health_population_week1_edit_pack/source/01-health-risk-and-labor-markets-core-frameworks-and-measurement.md`
2. the week-specific bibliography if available:
   `special_topic6_health_population_week1_edit_pack/bibliography/01-health-risk-and-labor-markets-core-frameworks-and-measurement.bib`
3. the week tables if available:
   `special_topic6_health_population_week1_edit_pack/tables/*.md`

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 1 identity:
- This is the opening labor-health lecture.
- It must remain a labor-economics chapter, not a generic health-economics or epidemiology introduction.
- It must define health as:
  1. work capacity / human capital,
  2. a source of labor-market risk and heterogeneity,
  3. a determinant of the feasible set for work,
  4. a worker-side and firm-side margin.
- It must foreground measurement as a first-order open problem:
  - self-reported health
  - diagnosis and biomarker/objective measures
  - disability status and administrative definitions
  - mortality risk and severe health shocks
  - mental health and latent conditions
  - insurance coverage / treatment access
  - reverse causality, omitted socioeconomic status, and dynamic selection
- It should set up the rest of the course by showing how health affects:
  labor supply, job choice, productivity, mobility, wages, amenities, worker welfare, and firm behavior.

Special-topics defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only:
  `books/special-topic6-health-population/references.bib`
- if you merge week-specific bibliography entries into `references.bib`, deduplicate repeated BibTeX entries

Required structure:
1. Opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading Ladder And References
7. Exercises And Discussion Prompts
8. Reproducibility And Code Lab Note
9. Slide Companion Note
10. Bridge Forward

Required Week 1 content:
A. Health as a labor object: work capacity, productivity, feasible set, and welfare
B. Measurement problems and why they matter for causal interpretation
C. Dynamic selection, reverse causality, and socioeconomic confounding
D. Worker-side vs firm-side health channels
E. A field map for the rest of the course
F. Research Lab

Slides requirements:
- create the Week 1 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week1/01-health-risk-and-labor-markets-core-frameworks-and-measurement.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on health as human capital / work capacity
  - one slide on measurement choices
  - one slide on reverse causality and dynamic selection
  - one slide on worker-side vs firm-side channels
  - one slide on the research field map
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week1/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose one primary anchor paper that is central to health measurement / labor-supply identification
- choose one challenge / extension paper that deepens the measurement or causal-design discussion
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
- keep the week labor-focused
- do not let the opener collapse into a generic “health matters” essay
- make the measurement discussion explicit and teachable
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 1 slides from the canonical path
3. if a bounded Week 1 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 1 slides compile from the canonical path
5. whether the Week 1 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points