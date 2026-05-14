Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib
- @books/special-topic6-health-population/02-disability-chronic-conditions-labor-supply-and-job-choice.md if it exists
- @books/special-topic6-health-population/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.md if it exists

If helpful, also inspect:
- the Week 3 source pack if it exists in the repo
- the Week 3 slide file if it exists
- the Week 3 lab folder if it exists

Goal: create or refresh Week 3 of the Labor Market, Health, and Population course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic6-health-population/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.md`
- `books/special-topic6-health-population/slides/week3/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.tex`
- `books/special-topic6-health-population/labs/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation/`

Use these as the intellectual source of truth:
1. the week-specific minimal pack files if they exist locally under:
   - `special_topic6_health_population_week3_edit_pack/source/`
   - `special_topic6_health_population_week3_edit_pack/bibliography/`
   - `special_topic6_health_population_week3_edit_pack/tables/`
2. the current chapter file if it already exists at the canonical path.

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 3 identity:
- The week must remain a labor-economics lecture, not a generic demography or retirement lecture.
- It must start with a brief theoretical framework for lifecycle labor allocation.
- It must explicitly cover:
  1. fertility timing and child penalties as lifecycle labor-allocation shocks,
  2. mortality risk and severe family health shocks,
  3. caregiving burdens and household reallocation,
  4. aging, retirement timing, pensions, and retirement savings,
  5. post-retirement work / flexible late-life work / rehire or bridge-job margins,
  6. global evidence on aging societies.
- It should keep timing and persistence central:
  current shocks can move future wages, occupations, savings, mobility, retirement, and welfare.

Special-topics defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only
- if you merge week-specific bibliography entries into `references.bib`, deduplicate repeated BibTeX entries

Required chapter structure:
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

Required Week 3 content:
A. A brief lifecycle labor-allocation framework
- introduce the worker/household problem over the lifecycle
- make clear how fertility timing, caregiving, mortality risk, aging, and retirement enter dynamic labor allocation

B. Fertility timing, children, and dynamic career effects
- child penalties
- fertility timing
- dynamic earnings and occupational effects
- distinguish timing effects from permanent specialization effects

C. Severe health shocks, mortality risk, and family labor supply
- how households adjust labor when severe illness or death changes resources and time needs
- short-run vs medium-run responses

D. Caregiving and reallocation
- informal caregiving burdens
- parent care / spouse care / elder care
- interactions with paid leave or care arrangements where relevant

E. Aging, pensions, retirement timing, and late-life work
- retirement incentives and pension design
- flexibility of late-life work
- post-retirement work / bridge-job / rehire or part-time transition margins
- why aging societies make these margins more important

F. Global aging and comparative evidence
- make clear what is global and why it matters for labor economics
- distinguish labor-market relevance from purely macro population-aging discussions

Slides requirements:
- create the Week 3 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week3/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the lifecycle labor-allocation framework
  - one slide on fertility timing and child penalties
  - one slide on family responses to severe health shocks
  - one slide on caregiving and household reallocation
  - one slide on aging / pensions / retirement / post-retirement work
  - one slide on global aging evidence
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week3/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to lifecycle labor allocation
- use one challenge/extension paper that pushes into aging / retirement / caregiving / comparative evidence
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
- keep the lecture labor-focused
- use the lifecycle framework as an organizing device, not a full technical derivation
- make aging and pensions central rather than an afterthought
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 3 slides from the canonical path
3. if a bounded Week 3 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 3 slides compile from the canonical path
5. whether the Week 3 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
