Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic6-health-population/index.md
- @books/special-topic6-health-population/OUTLINE.md
- @books/special-topic6-health-population/myst.yml
- @books/special-topic6-health-population/references.bib
- @books/special-topic6-health-population/README.md if it exists
- @books/special-topic6-health-population/01-health-risk-and-labor-markets-core-frameworks-and-measurement.md if it exists

If helpful, also inspect:
- nearby weeks from other special topics only for structure comparison
- the week pack files under:
  - `special_topic6_health_population_week2_edit_pack/source/`
  - `special_topic6_health_population_week2_edit_pack/bibliography/`
  - `special_topic6_health_population_week2_edit_pack/tables/`

Goal: create or refresh Week 2 of the Labor Market, Health, and Population course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic6-health-population/02-disability-chronic-conditions-labor-supply-and-job-choice.md`
- `books/special-topic6-health-population/slides/week2/02-disability-chronic-conditions-labor-supply-and-job-choice.tex`
- `books/special-topic6-health-population/labs/02-disability-chronic-conditions-labor-supply-and-job-choice/`

Use these as the intellectual source of truth:
1. the week source markdown if available:
   `special_topic6_health_population_week2_edit_pack/source/02-disability-chronic-conditions-labor-supply-and-job-choice.md`
2. the week-specific bibliography if available:
   `special_topic6_health_population_week2_edit_pack/bibliography/02-disability-chronic-conditions-labor-supply-and-job-choice.bib`
3. the week tables if available:
   `special_topic6_health_population_week2_edit_pack/tables/*.md`

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 2 identity:
- This week must remain a labor-economics lecture, not a generic disability-policy or medical lecture.
- It must study disability and chronic conditions as labor-market constraints that reshape labor-force attachment, hours, occupation, accommodations, job amenities, employer responses, and dynamic exits from employment.
- It must clearly separate:
  1. direct work-capacity effects,
  2. program incentives and benefit receipt,
  3. employer accommodation / workplace treatment,
  4. local labor-demand conditions,
  5. selection into disability status and program use.
- It must explicitly cover short-term versus long-term effects of disability and chronic conditions.
- It must include a discussion of whether treatment, accommodations, or return-to-work investments alter labor-market decisions.
- It must include a section on how disability and chronic conditions may generate monopsony power or inelastic labor supply through job lock, accommodation dependence, local scarcity, switching costs, and employer information advantages.
- It must include a frontier methods box on credible causal identification, including designs such as:
  - acute health-shock event studies
  - disability-onset administrative event studies
  - threshold / program-rule designs
  - twin / sibling comparisons where relevant
  - genetic / Mendelian-randomization style designs where relevant
  - matched employer-employee accommodation or firm-heterogeneity designs
  - treatment-access or reform designs

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

Required Week 2 content:
A. Disability and chronic conditions as dynamic labor-market constraints
B. Short-term versus long-term labor-market effects
C. Treatment, accommodation, and return-to-work investments
D. Disability, chronic conditions, and monopsony / inelastic labor supply
E. Frontier methods and identification
F. Research Lab

Slides requirements:
- create the Week 2 slide deck under the canonical path:
  `books/special-topic6-health-population/slides/week2/02-disability-chronic-conditions-labor-supply-and-job-choice.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on direct capacity effects vs program incentives
  - one slide on short-run vs long-run effects
  - one slide on accommodation / treatment / return-to-work
  - one slide on monopsony, job lock, and worker inelasticity
  - one slide on frontier methods
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week2/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic6-health-population/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose one primary anchor paper that is central to disability/chronic-condition labor-market dynamics
- choose one challenge / extension paper that sharpens the treatment/accommodation or identification discussion
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
- do not let the lecture collapse into a generic disability-policy survey
- emphasize dynamic incidence: employment, hours, occupation, accommodations, and exit may move on different horizons
- treat monopsony power as a labor-market mechanism, not just a legal aside
- use the methods box to help students think about what a strong causal design would actually look like in this area
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic6-health-population && conda run -n research jupyter book build --html --strict`
2. compile the Week 2 slides from the canonical path
3. if a bounded Week 2 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 2 slides compile from the canonical path
5. whether the Week 2 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
