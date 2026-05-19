Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/06-when-and-why-structure-static-and-dynamic-decision-problems.md if it exists
- @books/empirical-methods/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.md if it exists

If helpful, also inspect:
- the Week 8 source pack if it exists in the repo
- nearby empirical-methods lectures for chapter-structure consistency
- any existing slides/lab folders for naming conventions

Goal: create or refresh Lecture 8 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.md`
- `books/empirical-methods/slides/week8/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.tex`
- `books/empirical-methods/labs/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals/`

Use these as the intellectual source of truth:
1. the week pack files under:
   - `empirical_methods_lecture8_edit_pack/source/`
   - `empirical_methods_lecture8_edit_pack/bibliography/`
   - `empirical_methods_lecture8_edit_pack/tables/`
2. the existing canonical chapter file if it already exists

This is a week-drafting / sync task using the established empirical-methods conventions.

Non-negotiable lecture identity:
- This is the capstone lecture of Block 2.
- It must teach equilibrium structural work as a research choice for questions where individual decisions interact through markets, prices, firms, or locations.
- It must remain methods-focused and research-oriented, not a survey of macro or trade models.
- It must show students when equilibrium structure is worth the extra assumptions and when it is not.
- Gravity-style structural work may be included as one application/subfamily within spatial or flow equilibrium work if it helps clarify the method, but it should not dominate the lecture.

Core content to preserve:
A. Search and matching equilibrium
B. Spatial equilibrium
C. Industry/market equilibrium (IO-style structural)
D. Policy counterfactuals and welfare in equilibrium
E. Estimation/computation/identification burdens
F. Research Lab

Required chapter structure:
1. Opening Orientation
2. Core points
3. Bridge
4. Field Core
5. Research Lab
6. Methods Box
7. Reading Ladder And References
8. Exercises And Discussion Prompts
9. Reproducibility And Code Lab Note
10. Slide Companion Note
11. Bridge Forward

Required math/equations:
- search/matching equilibrium objects:
  - matching function and market tightness
  - free-entry or vacancy-zero-profit condition
  - wage/ surplus-sharing condition
- spatial equilibrium objects:
  - indirect utility / location-choice object
  - equilibrium equalization / market-clearing condition
  - commuting/migration or housing-cost incidence object
- industry/market equilibrium objects:
  - demand system
  - firm first-order condition / markup or pricing rule
  - equilibrium mapping from primitives to prices/quantities
- policy counterfactual object:
  - equilibrium fixed point or equilibrium correspondence
  - welfare object
- one short section on computational approaches:
  - nested fixed point
  - MPEC intuition
  - calibration/estimation hybrids
  - equilibrium simulation burden

Applied/research orientation:
- every method block must be anchored in actual papers
- students should learn:
  - when equilibrium structure is essential
  - what the model identifies
  - what assumptions are doing the work
  - how to interpret counterfactuals
  - what validation burden is required
  - what can go wrong empirically

Gravity-style note:
- If useful, include gravity-style structural work as an optional application within spatial/trade/migration equilibrium models.
- Do not force it if it dilutes the main lecture.
- If included, explain clearly what kind of object gravity models recover and how they fit into equilibrium structural work.

Slides requirements:
- create the slide deck under:
  `books/empirical-methods/slides/week8/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.tex`
- use the same professional beamer style already used elsewhere
- include:
  - one slide on “when do we need equilibrium structure?”
  - one slide each for search, spatial, and industry equilibrium
  - one slide on policy counterfactuals and welfare
  - one slide on computational/identification burdens
  - one slide on the Research Lab design
  - if used, one optional slide on gravity-style equilibrium models

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper with a real equilibrium counterfactual
- use one challenge / extension paper from a different equilibrium domain
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
- keep the lecture firmly methods-focused
- emphasize gains vs burdens of equilibrium modeling
- keep search/spatial/industry sections parallel so students can compare them
- do not let the lecture drift into pure theory without applied interpretation
- if gravity-style work is included, keep it concise and clearly subordinate to the main lecture

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 8 slides from the canonical path
3. if a bounded Lecture 8 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 8 slides compile from the canonical path
5. whether the Lecture 8 lab folder now exists and follows the standard structure
6. whether gravity-style structural work was included and how
7. whether the strict build passes
8. any manual follow-up points
