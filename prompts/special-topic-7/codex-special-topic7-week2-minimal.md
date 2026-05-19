Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib
- @books/special-topic7-labor-design/01-matching-market-design-and-labor-allocation.md if it exists
- @books/special-topic7-labor-design/02-recruiting-congestion-timing-and-unraveling.md if it exists

If helpful, also inspect:
- the Week 2 source pack if it exists in the repo
- the Week 2 slide file if it exists
- the Week 2 lab folder if it exists

Goal: create or refresh Week 2 of the Labor Market Design, Contracting, and Mechanism Design course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic7-labor-design/02-recruiting-congestion-timing-and-unraveling.md`
- `books/special-topic7-labor-design/slides/week2/02-recruiting-congestion-timing-and-unraveling.tex`
- `books/special-topic7-labor-design/labs/02-recruiting-congestion-timing-and-unraveling/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists:
   `books/special-topic7-labor-design/02-recruiting-congestion-timing-and-unraveling.md`
2. if available, the week pack files under:
   - `special_topic7_labor_design_week2_edit_pack/source/`
   - `special_topic7_labor_design_week2_edit_pack/bibliography/`
   - `special_topic7_labor_design_week2_edit_pack/tables/`

This is a sync-and-complete task, not a fresh rewrite unless required.

Special-topics defaults to enforce:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only:
  `books/special-topic7-labor-design/references.bib`
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

Week 2 identity to preserve:
- this is a theory-heavy and empirically active lecture on recruiting-process frictions in decentralized labor markets
- the key labor objects are congestion, timing, exploding offers, early contracting, interview bottlenecks, vacancy yields, recruiting intensity, and within-vacancy margins
- the lecture must make clear that many “matching” failures arise inside the recruiting process rather than from worker or firm fundamentals alone
- this is one of the most active current literatures in labor and job search, so the week should be a bit longer than average
- the lecture must explicitly connect theory to empirical applied research design

Non-negotiable intellectual additions:
1. Within-vacancy margins
- The lecture must emphasize that the action is often within vacancies:
  applicant pools, interview bottlenecks, recruiting intensity, hiring standards, wage transparency, offer timing, and yield conversion from vacancy to hire.
- These margins should not be treated as residual details.

2. Unraveling
- Keep labor-market unraveling as a serious topic.
- Include the classic theoretical and institutional papers, but also bring in empirical or descriptive labor-market evidence wherever possible.
- Markets like gastroenterology fellows, law firms, clerkships, and other professional entry markets are acceptable labor anchors.

3. Empirical design bridge
- There must be a clear subsection in Field Core on how a recruiting-design question becomes an empirical labor paper.
- This should include:
  - what is the frictive object
  - what margin is observed
  - what data are needed
  - what counterfactual is meaningful
  - how design interventions or natural variation can identify the effect

Slides requirements:
- create the Week 2 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week2/02-recruiting-congestion-timing-and-unraveling.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on recruiting frictions vs worker/firm fundamentals
  - one slide on congestion, vacancy yields, and within-vacancy margins
  - one slide on exploding offers, early contracting, and unraveling
  - one slide on empirical/descriptive evidence from professional labor markets
  - one slide on modern data from vacancies / applications / job posts
  - one slide on the theory-to-empirical bridge
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week2/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to recruiting congestion / within-vacancy margins with feasible public or reproducible teaching materials if available
- use one challenge / extension paper that illustrates unraveling, centralized clearing, or timing design
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

Suggested empirical anchors:
- recruiting / within-vacancy primary anchor: Carrillo-Tudela et al. on recruitment policies, job-filling rates, and matching efficiency; or a comparable within-vacancy/recruiting-intensity paper if the repo already points to one
- unraveling / timing challenge anchor: Niederle and Roth on centralized clearinghouses / unraveling in medical markets, Roth and Xing on timing of transactions, or an equivalent labor-market timing paper
- if a more practical teaching path is needed, a reduced teaching exercise can use synthetic vacancy-yield or application-congestion data inspired by these papers

Implementation notes:
- keep the chapter labor-focused
- do not drift into generic market-design theory without a labor-market mechanism
- preserve the distinction between:
  (i) recruiting-process frictions,
  (ii) decentralized-timing failures,
  (iii) centralized or coordinated design responses
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
2. compile the Week 2 slides from the canonical path
3. if the Week 2 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 2 slides compile from the canonical path
5. whether the Week 2 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
