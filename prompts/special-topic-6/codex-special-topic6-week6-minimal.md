Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib
- @books/special-topic6-health-population/01-health-risk-and-labor-markets-core-frameworks-and-measurement.md if it exists
- @books/special-topic6-health-population/02-disability-chronic-conditions-labor-supply-and-job-choice.md if it exists
- @books/special-topic6-health-population/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.md if it exists
- @books/special-topic6-health-population/04-mental-health-stress-workplace-productivity-and-worker-welfare.md if it exists
- @books/special-topic6-health-population/05-disease-exposure-environmental-health-demographic-change-and-labor-market-adjustment.md if it exists

Use these as the intellectual source of truth for Week 6 if they exist:
- `special_topic6_health_population_week6_edit_pack/source/06-synthesis-frontier-questions-and-student-research-designs.md`
- `special_topic6_health_population_week6_edit_pack/bibliography/06-synthesis-frontier-questions-and-student-research-designs.bib`
- all markdown files under `special_topic6_health_population_week6_edit_pack/tables/`

Goal: create or refresh Week 6 of the Labor Market, Health, and Population course as a fully synchronized capstone week with canonical chapter, slides, and lab outputs, matching the established special-topic workflow.

Canonical output files:
- `books/special-topic6-health-population/06-synthesis-frontier-questions-and-student-research-designs.md`
- `books/special-topic6-health-population/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
- `books/special-topic6-health-population/labs/06-synthesis-frontier-questions-and-student-research-designs/`

This is a sync-and-draft task for a capstone week, not a generic recap.

Non-negotiable week identity:
- This is the synthesis / frontier / student-research-design week.
- It must remain a labor-economics capstone, not a generic health-economics or demography recap.
- It must teach students how to turn health and population questions into research designs about labor supply, job choice, disability, caregiving, mental health, productivity, disease exposure, demographic change, firm response, inequality, and welfare.
- It must make explicit where the literature currently is, where the main open questions are, and how students can enter the field with credible projects.
- It must help students distinguish labor-focused health/population research from generic health economics, epidemiology, or demography.

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

Required Week 6 content:
A. Synthesis of the course into a research architecture:
   - health/population mechanism
   - labor outcome
   - relevant worker / household / firm / aggregate margin
   - timing/exposure logic
   - dynamic selection concerns
   - welfare/distributional object

B. Where the literature is:
   - health as human capital, work capacity, and risk
   - disability / chronic conditions and labor supply / job choice
   - fertility, caregiving, and lifecycle allocation
   - mental health, productivity, and worker welfare
   - disease/environment/demography and labor-market adjustment
   - what is measured well and what is still poorly measured

C. Where the literature is going:
   - biomarkers, administrative linkage, and better work-capacity measurement
   - mental-health treatment, stigma, and workplace design
   - aging, retirement, caregiving, and older-worker flexibility
   - climate, disease exposure, and migration/incidence
   - health inequality, within-country heterogeneity, and global evidence
   - firm response to worker health constraints and accommodations

D. Research design guidance:
   - how to formulate a labor question rather than a generic health question
   - how to define exposure/timing/onset
   - how to choose the relevant unit (worker, household, firm, establishment, place, cohort)
   - how to think about counterfactuals and timing
   - what makes a design persuasive
   - common failure modes in this literature

E. A research opportunities section:
   - concrete project directions students could plausibly pursue
   - should include both empirical and measurement contributions
   - should clearly indicate which questions are saturated vs still open
   - should explicitly say why this field is worth investing in as a labor economist

Slides requirements:
- create the Week 6 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the health/population → labor research architecture
  - one slide on where the literature is
  - one slide on frontier directions
  - one slide on research design choices
  - one slide on common failure modes
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week6/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose a primary anchor that is central to the field and feasible for a bounded teaching reproduction
- choose a challenge/transfer anchor that pushes to a newer frontier (for example mental health, disease exposure, or demographic change)
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
- This week should help students launch projects.
- Keep the language practical and research-facing.
- Be explicit about how to make a health/population-and-labor paper broadly interesting.
- Distinguish clearly between:
  - health/population mechanism
  - exposure/timing/onset
  - labor outcome
  - firm/household response
  - equilibrium incidence
  - welfare object
- Include a short section on why this field matters for labor economists and what contributions are still missing.

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 6 slides from the canonical path
3. if a bounded Week 6 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 6 slides compile from the canonical path
5. whether the Week 6 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
