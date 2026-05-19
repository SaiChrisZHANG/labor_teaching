Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib

If helpful, also inspect:
- the Week 1 source pack if it exists in the repo
- the Week 1 slide file if it exists
- the Week 1 lab folder if it exists

Goal: create or refresh Week 1 of the Labor Market Design, Contracting, and Mechanism Design course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic7-labor-design/01-matching-market-design-and-labor-allocation.md`
- `books/special-topic7-labor-design/slides/week1/01-matching-market-design-and-labor-allocation.tex`
- `books/special-topic7-labor-design/labs/01-matching-market-design-and-labor-allocation/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists:
   `books/special-topic7-labor-design/01-matching-market-design-and-labor-allocation.md`
2. if available, the week pack files under:
   - `special_topic7_labor_design_week1_edit_pack/source/`
   - `special_topic7_labor_design_week1_edit_pack/bibliography/`
   - `special_topic7_labor_design_week1_edit_pack/tables/`

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

Week 1 identity to preserve:
- this is a theory-heavy labor-market-design opening week, but it must always connect theory to empirical applied research design
- matching stability, thickness, congestion, timing, priority rules, strategy-proofness, fairness, and welfare are central objects
- professional entry labor markets (medical residents, psychologists, lawyers, etc.) should be the labor anchor, not generic school choice
- the lecture should teach students how to translate matching theory into an empirical labor-market design project

Required theory-to-empirics bridge:
- The lecture must not stop at theory exposition.
- It must explicitly show how a matching-design question becomes an applied research project:
  - institutional detail
  - market failure / design object
  - data on preferences, priorities, matches, timing, or outcomes
  - counterfactual design or policy comparison
  - welfare / fairness / allocation object
- Include a clear subsection in Field Core on “From theory to empirical design” or equivalent.

Slides requirements:
- create the Week 1 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week1/01-matching-market-design-and-labor-allocation.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on why centralized matching appears in labor markets
  - one slide on stability, thickness, congestion, and timing
  - one slide on strategy-proofness, priorities, and fairness
  - one slide on professional-entry labor markets as the empirical anchor
  - one slide on the theory-to-empirical bridge
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week1/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to labor-market matching design with feasible public materials if available
- use one challenge / extension paper that illustrates an empirical policy-analysis or market-culture angle
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
- primary: Roth and Peranson on the redesign of the medical residency match
- secondary / challenge: Agarwal on empirical/policy analysis of the medical match, or Niederle–Roth on exploding offers and market culture, depending on local feasibility and pedagogical fit

Implementation notes:
- keep the chapter labor-focused
- do not drift into generic market-design theory without a labor-market mechanism
- preserve the distinction between:
  (i) why centralized matching arises,
  (ii) what design properties matter,
  (iii) how researchers identify the effects of design changes
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
2. compile the Week 1 slides from the canonical path
3. if the Week 1 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 1 slides compile from the canonical path
5. whether the Week 1 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points