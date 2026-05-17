Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib
- @books/special-topic6-health-population/04-mental-health-stress-workplace-productivity-and-worker-welfare.md if it exists
- @books/special-topic6-health-population/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment.md if it exists

If helpful, also inspect:
- the Week 5 source pack if it exists in the repo
- the Week 5 slide file if it exists
- the Week 5 lab folder if it exists

Goal: create or refresh Week 5 of the Health, Population, and Labor course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic6-health-population/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment.md`
- `books/special-topic6-health-population/slides/week5/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment.tex`
- `books/special-topic6-health-population/labs/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists
2. the week pack files under:
   - `special_topic6_health_population_week5_edit_pack/source/`
   - `special_topic6_health_population_week5_edit_pack/bibliography/`
   - all markdown files under `special_topic6_health_population_week5_edit_pack/tables/`

This is a sync-and-complete task, not a fresh rewrite unless required.

Special-topics defaults to enforce:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only:
  `books/special-topic6-health-population/references.bib`
- preserve the established special-topics chapter architecture

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

Week 5 identity to preserve:
- scale the course up from individual and household mechanisms to disease, environmental exposure, demographic change, and aggregate labor-market adjustment
- treat historical epidemics (plague, tuberculosis, HIV/AIDS) and COVID as part of a unified labor-market incidence literature
- include health inequality and unequal exposure as central objects, not side notes
- connect disease/environmental shocks to migration, spatial sorting, labor reallocation, and worker welfare
- include population aging and demographic composition as labor-market adjustment forces

Required content additions:
A. Historical health episodes and long-run labor effects
- include a substantive section comparing plague / Black Death, tuberculosis / early public health, HIV/AIDS, and COVID-era labor-market evidence
- show how contemporary COVID work fits inside a longer labor-market history of disease shocks
- distinguish short-run disruption, medium-run reallocation, and long-run institutional or distributional effects

B. Health inequality, migration, and labor choices
- include a section on unequal exposure and unequal capacity to adjust
- connect health inequality to migration decisions, immobility, sorting, and labor-market choices
- include global and development evidence where possible

C. Demographic change
- include aging, fertility decline, dependency structure, and demographic composition as labor-market adjustment forces
- connect demographic change to wages, labor shortages, technology adoption, migration, and retirement/late-career margins

D. Methods / data layer
- include a stronger methods-and-data section than the average week
- students should leave this week with a sense of what kinds of empirical designs exist and what data are commonly used

Slides requirements:
- create the Week 5 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week5/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include at minimum:
  - one slide on disease/environment/demography as labor-market shocks
  - one slide on historical health episodes and labor outcomes
  - one slide on COVID in historical perspective
  - one slide on health inequality, migration, and labor adjustment
  - one slide on aging/demographic change
  - one slide on methods/data
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week5/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose one primary anchor paper from the disease/environment/demography literature with a plausible bounded pedagogical reproduction
- choose one challenge / transfer paper that pushes toward long-run historical or migration / health inequality themes
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
- be conservative about official replication availability
- if no official replication data are locally available, create a bounded synthetic pedagogical path

Implementation notes:
- keep the lecture labor-focused, not generic epidemiology or demography
- health inequality should be about labor-market incidence, adjustment, and welfare
- historical episodes should be used to structure labor questions, not just as interesting stories
- if the chapter already exists, treat it as the canonical source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 5 slides from the canonical path
3. if the Week 5 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 5 slides compile from the canonical path
5. whether the Week 5 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points