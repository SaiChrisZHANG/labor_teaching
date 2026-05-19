Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/18-curating-network-data-and-descriptive-statistics.md if it exists
- @books/empirical-methods/19-causal-inference-with-network-data.md if it exists
- @books/empirical-methods/20-structural-modeling-with-network-data.md if it exists

If helpful, also inspect:
- the Lecture 20 source pack if it exists in the repo
- the Lecture 20 slide file if it exists
- the Lecture 20 lab folder if it exists

Goal: create or refresh Lecture 20 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established workflow used for earlier empirical-methods lectures.

Canonical output files:
- `books/empirical-methods/20-structural-modeling-with-network-data.md`
- `books/empirical-methods/slides/week20/20-structural-modeling-with-network-data.tex`
- `books/empirical-methods/labs/20-structural-modeling-with-network-data/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists
2. if available, the lecture pack files under:
   - `empirical_methods_lecture20_edit_pack/source/`
   - `empirical_methods_lecture20_edit_pack/bibliography/`
   - `empirical_methods_lecture20_edit_pack/tables/`

This is a sync-and-complete task, not a fresh rewrite unless required.

Course conventions to enforce:
- Core points box required near the top
- linked citations only in prose markdown
- use the course-local bibliography only:
  `books/empirical-methods/references.bib`
- preserve the established empirical-methods chapter architecture

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

Lecture 20 identity to preserve:
- structural peer-effects models
- endogenous network formation
- referral/search networks
- diffusion and equilibrium behavior on networks
- policies that change links, information flows, or matching opportunities
- stronger assumptions and validation burdens when links are endogenous

Additional requirement for this lecture:
- because this is the last lecture of the Network Methods block, include a short explicit **Network Block Summary** component that points students to:
  - where the literature is now
  - what the key open questions are
  - what future research opportunities look like
- this should be an extra component and should not replace the main structural-modeling material

Slides requirements:
- create the Lecture 20 slide deck under the canonical path:
  `books/empirical-methods/slides/week20/20-structural-modeling-with-network-data.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on when reduced-form network methods are not enough
  - one slide on network formation vs behavior
  - one slide on search/referral and labor-market applications
  - one slide on estimation / computation / validation
  - one slide on the Network Methods block summary
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week20/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper central to structural network modeling
- use one secondary / challenge paper that pushes into labor-market referrals, matching, or endogenous formation
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
- gravity-style or flow-style network models can appear as subfamilies, but the lecture should remain centered on network formation / network-mediated behavior / network counterfactuals
- keep the lecture methods-oriented and research-oriented, not a generic graph theory lecture
- preserve the distinction between:
  (i) network definition/data,
  (ii) causal identification with networks,
  (iii) structural modeling and counterfactuals
- emphasize where structural network models add value beyond Lectures 18 and 19

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 20 slides from the canonical path
3. if the Lecture 20 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 20 slides compile from the canonical path
5. whether the Lecture 20 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. how the Network Block Summary was incorporated
8. any manual follow-up points
