Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib
- @books/special-topic7-labor-design/05-professional-labor-markets-and-public-sector-design.md if it exists
- @books/special-topic7-labor-design/06-empirical-design-experiments-and-frontier-questions.md if it exists

If helpful, also inspect:
- the Week 6 source pack if it exists in the repo
- the Week 6 slide file if it exists
- the Week 6 lab folder if it exists

Goal: create or refresh Week 6 of the Labor Market Design, Contracting, and Mechanism Design course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic7-labor-design/06-empirical-design-experiments-and-frontier-questions.md`
- `books/special-topic7-labor-design/slides/week6/06-empirical-design-experiments-and-frontier-questions.tex`
- `books/special-topic7-labor-design/labs/06-empirical-design-experiments-and-frontier-questions/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists:
   `books/special-topic7-labor-design/06-empirical-design-experiments-and-frontier-questions.md`
2. if available, the week pack files under:
   - `special_topic7_labor_design_week6_edit_pack/source/`
   - `special_topic7_labor_design_week6_edit_pack/bibliography/`
   - all markdown files under `special_topic7_labor_design_week6_edit_pack/tables/`

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 6 identity:
- The week must remain a labor-economics capstone on empirical design, not a generic econometrics lecture.
- It should teach students how to turn matching, recruiting, contracting, platform, and public-sector design questions into empirical research projects.
- It must explicitly cover:
  1. mechanism-first design: what object the intervention moves
  2. counterfactuals and welfare in labor-market design
  3. field experiments, audits, institutional pilots, administrative data, and structural evaluation
  4. equilibrium response and external validity
  5. frontier research opportunities in labor-market design
- The course should end with students able to outline a strong theory-backed applied project.

Special-topics defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only
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

Required Week 6 content:
A. what a credible labor-market design evaluation looks like
B. theory-to-empirical translation: mechanism, margin, and counterfactual
C. field experiments, audits, and institutional pilots
D. administrative data, platform data, and structural matching models
E. welfare, equilibrium response, and portability
F. frontier questions and student research designs
G. Research Lab

Slides requirements:
- create the Week 6 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week6/06-empirical-design-experiments-and-frontier-questions.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on mechanism-first empirical design
  - one slide on experiments / audits / pilots
  - one slide on administrative and platform data
  - one slide on structural matching / equilibrium evaluation
  - one slide on welfare and portability
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week6/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to empirical evaluation in labor-market design
- use one challenge/extension paper that pushes into experiments, platforms, or public-sector design
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
- keep the week research-oriented and labor-focused
- students should leave the course able to formulate a publishable applied design question with a strong theory backbone
- keep the week tied to the earlier course themes:
  matching, recruiting, contracts, platforms, and public-sector assignment
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
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
