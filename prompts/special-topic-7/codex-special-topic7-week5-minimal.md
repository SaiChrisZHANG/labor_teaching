Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib
- @books/special-topic7-labor-design/04-assignment-wages-platforms-and-pricing-rules.md if it exists
- @books/special-topic7-labor-design/05-professional-labor-markets-and-public-sector-design.md if it exists

If helpful, also inspect:
- the Week 5 source pack if it exists in the repo
- the Week 5 slide file if it exists
- the Week 5 lab folder if it exists

Goal: create or refresh Week 5 of the Labor Market Design, Contracting, and Mechanism Design course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic7-labor-design/05-professional-labor-markets-and-public-sector-design.md`
- `books/special-topic7-labor-design/slides/week5/05-professional-labor-markets-and-public-sector-design.tex`
- `books/special-topic7-labor-design/labs/05-professional-labor-markets-and-public-sector-design/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists:
   `books/special-topic7-labor-design/05-professional-labor-markets-and-public-sector-design.md`
2. if available, the week pack files under:
   - `special_topic7_labor_design_week5_edit_pack/source/`
   - `special_topic7_labor_design_week5_edit_pack/bibliography/`
   - all markdown files under `special_topic7_labor_design_week5_edit_pack/tables/`

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 5 identity:
- The week must remain a labor-economics lecture, not a generic public administration or mechanism-design theory lecture.
- It should connect structured professional markets, public-sector assignment, and career ladders to labor allocation, worker welfare, fairness, and staffing needs.
- It must explicitly include:
  1. internal job ladders, promotions, and within-system mobility
  2. training and on-the-job search within structured labor markets
  3. “in and out” of the public sector from a mechanism-design perspective
  4. military / army labor markets as a structured assignment system
  5. teacher / public-service allocation as an empirical design laboratory
- It should keep institutional detail central: the same matching or priority rule can behave differently when outside options, service obligations, wage rigidity, staffing targets, and public objectives differ.

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

Required Week 5 content:
A. professional labor markets as design laboratories
B. staffing, fairness, transparency, and public objectives
C. internal job ladders, promotions, and training within structured systems
D. public/private outside options and movement into and out of the public sector
E. military labor markets and branch/assignment design
F. methods / data layer
G. Research Lab

Slides requirements:
- create the Week 5 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week5/05-professional-labor-markets-and-public-sector-design.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on professional/public-sector design principles
  - one slide on teacher/public-service assignment
  - one slide on internal ladders / training / on-the-job search
  - one slide on army / military assignment design
  - one slide on methods / data
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week5/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to labor-market design in a professional/public-sector setting
- use one challenge/extension paper that pushes into internal assignment / military / teacher / public-sector margins
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
- keep the chapter labor-focused
- do not let the week become just “school choice for workers”
- make clear where job-ladder dynamics, training, and public-sector exit/entry change the design problem
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily
- use theory to sharpen the applied question, not to dominate the chapter

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
2. compile the Week 5 slides from the canonical path
3. if a bounded Week 5 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 5 slides compile from the canonical path
5. whether the Week 5 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
