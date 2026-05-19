Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/15-curating-maps-and-spatial-data.md if it exists
- @books/empirical-methods/16-causal-inference-with-spatial-data.md if it exists

If helpful, also inspect:
- nearby empirical-methods lectures to match structure and tone
- the Lecture 16 source pack if it exists in the repo
- the Lecture 16 slide file if it exists
- the Lecture 16 lab folder if it exists

Goal: create or refresh Lecture 16 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/16-causal-inference-with-spatial-data.md`
- `books/empirical-methods/slides/week16/16-causal-inference-with-spatial-data.tex`
- `books/empirical-methods/labs/16-causal-inference-with-spatial-data/`

Use these as the intellectual source of truth if they exist locally:
- `empirical_methods_lecture16_edit_pack/source/16-causal-inference-with-spatial-data.md`
- `empirical_methods_lecture16_edit_pack/bibliography/16-causal-inference-with-spatial-data.bib`
- all markdown files under `empirical_methods_lecture16_edit_pack/tables/`

This is a lecture-drafting / sync task using the established empirical-methods conventions.

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only:
  `books/empirical-methods/references.bib`
- preserve the established chapter architecture:
  1. Opening Orientation
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. Methods Box
  7. Reading Ladder And References
  8. Exercises And Discussion Prompts
  9. Reproducibility And Code Lab Note
  10. Slide Companion Note
  11. Bridge Forward

Lecture 16 identity to preserve:
- this lecture is about **identification problems with spatial data**
- each key issue should be taught through a high-quality paper students can actually use as a template
- the main issues must include:
  A. spatial clustering and inference
  B. spillovers / interference / exposure mappings
  C. border designs and spatial RD
  D. shift-share and place-based designs
  E. sorting, MAUP, and correlated local shocks
- the lecture must explain whether geography is:
  - the source of identification,
  - a threat to inference,
  - or the mechanism itself
- methods must come with usable implementation details and caveats, not just textual description

Equations / formal objects that should appear:
- spatial exposure mapping:
  `Y_i = Y_i(D_i, E_i)`
- exposure measure:
  `E_i = \sum_{j \neq i} w_{ij} D_j`
- Conley-style variance logic:
  a formula or notation showing distance-weighted covariance adjustment
- spatial RD / boundary-discontinuity specification:
  treatment or outcome as a function of signed distance to a border
- shift-share exposure:
  `Z_\ell = \sum_s w_{\ell s} g_s`

Paper anchors to use if helpful:
- Conley on spatial dependence / inference
- Miguel and Kremer on treatment externalities / interference
- Black on school-district boundaries
- Dell on the mita boundary
- Dube, Lester, and Reich on contiguous border comparisons
- Borusyak, Hull, and Jaravel on shift-share instruments
- Goldsmith-Pinkham, Sorkin, and Swift on shift-share diagnostics
- Chetty, Hendren, and Katz or another strong neighborhood exposure / mover design paper
- one place-based policy application if useful

Slides requirements:
- create the Lecture 16 slide deck under the canonical path:
  `books/empirical-methods/slides/week16/16-causal-inference-with-spatial-data.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the lecture structure
- include:
  - one slide on geography as source / threat / mechanism
  - one slide on spatial clustering and Conley-style inference
  - one slide on spillovers / exposure mapping
  - one slide on border designs and spatial RD
  - one slide on shift-share and place-based designs
  - one slide on design diagnostics / checklist
  - one slide on the Research Lab design
- do not create duplicate slide files outside `slides/week16/`

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper where spatial identification is central
- use one challenge/extension paper with a different spatial logic (e.g. border vs shift-share vs exposure)
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
- keep the lecture methods-focused but still applied-economics oriented
- the key pedagogical goal is to show how a solid design attacks spatial identification problems
- each major issue should be tied to a paper and a practical implementation lesson
- make clear that Conley-style inference solves a variance problem, not necessarily a bias problem
- make clear that place definitions, interference structure, and estimand choice are part of identification
- use equations to clarify the mapping from geography to causal object, not to overload the lecture

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 16 slides from the canonical path
3. if a bounded Lecture 16 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key spatial equations are present
5. whether each major identification issue is tied to a paper and practical caveat
6. whether the Lecture 16 slides compile from the canonical path
7. whether the Lecture 16 lab folder now exists and follows the standard structure
8. whether the strict build passes
9. any manual follow-up points
