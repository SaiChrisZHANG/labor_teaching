Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/15-curating-maps-and-spatial-data.md if it exists
- @books/empirical-methods/16-causal-inference-with-spatial-data.md if it exists
- @books/empirical-methods/17-spatial-structural-modeling.md if it exists

If available locally in the repo or current workspace, also use:
- `empirical_methods_lecture18_edit_pack/source/18-curating-network-data-and-descriptive-statistics.md`
- `empirical_methods_lecture18_edit_pack/bibliography/18-curating-network-data-and-descriptive-statistics.bib`
- all markdown files under `empirical_methods_lecture18_edit_pack/tables/`

Goal: create Lecture 18 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/18-curating-network-data-and-descriptive-statistics.md`
- `books/empirical-methods/slides/week18/18-curating-network-data-and-descriptive-statistics.tex`
- `books/empirical-methods/labs/18-curating-network-data-and-descriptive-statistics/`

Lecture identity to preserve:
- This is the opening lecture of the optional Network Methods block.
- It should mirror Lecture 15 conceptually: students should understand what it means to use network data, what the advantages and limitations are, what can go wrong, what the main opportunities are, and what the practical rules are.
- This is not yet the causal-identification lecture; the focus is on curation, definition, and descriptive structure.
- The lecture must stay research-oriented and tied to economics papers.

Core conceptual requirements:
1. Define nodes, edges, weighted links, directed links, bipartite networks, and multilayer/relational settings.
2. Make clear that network definition is a substantive economic choice, not clerical preprocessing.
3. Explain why network data are useful for labor economics:
   - referrals
   - information transmission
   - coworker exposure
   - neighborhood/job information networks
   - learning and diffusion
   - bargaining and inequality
4. Discuss the main risks and limitations:
   - missing links
   - endogenous network formation
   - boundary/specification choices
   - homophily versus influence
   - privacy/confidentiality
   - time aggregation and dynamic network mismatch
5. Give students practical rules for building defensible network data.
6. Use actual papers to anchor the lecture, not just generic network theory.

Required chapter structure:
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

Required content inside the lecture:
- a concise notation section for adjacency / incidence / bipartite representation
- a “what a network variable means economically” section
- a “descriptive statistics are theory-laden” section
- a practical section on data sources and construction
- a practical section on common mistakes and diagnostic checks

Suggested anchor papers (use if they fit the source pack and bibliography):
- Autor (2001), “Wiring the Labor Market”
- Bayer, Ross, and Topa on residential labor market networks
- Beaman and Magruder on referrals
- Barwick et al. on job referrals and inequality
- Hellerstein et al. on labor market networks / recovery / neighborhoods
- Ioannides and Loury / related survey-style bridge if useful

Slides requirements:
- create the Lecture 18 slide deck under the canonical path:
  `books/empirical-methods/slides/week18/18-curating-network-data-and-descriptive-statistics.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on node/edge/bipartite concepts
  - one slide on substantive network definitions
  - one slide on practical data sources and construction
  - one slide on descriptive statistics / common metrics
  - one slide on pitfalls / privacy / missing links
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week18/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- this lecture’s lab should remain bounded and primarily about building/diagnosing network data
- use one primary labor-network paper as the reproduction anchor
- use one contrast/extension paper if helpful
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
- if no official replication data are locally available, create a bounded synthetic pedagogical path

Methods Box requirements:
- should summarize commonly used network data sources and descriptive statistics:
  degree, weighted degree/strength, centrality, clustering, components, assortativity/homophily, bipartite projections
- it should explain what each object is good for, and what caveats matter

Implementation notes:
- keep the lecture conceptually parallel to Lecture 15, but network-specific
- keep the lecture economics-facing, not a generic graph-theory lecture
- do not overclaim causal interpretation at this stage
- do not drift heavily into causal-interference methods; preview them only as a bridge to Lecture 19
- preserve linked citations only in prose markdown

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 18 slides from the canonical path
3. if the Lecture 18 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 18 slides compile from the canonical path
5. whether the Lecture 18 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
