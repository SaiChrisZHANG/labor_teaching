Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/14-llm-workflows-for-applied-research.md if it exists
- @books/empirical-methods/15-curating-maps-and-spatial-data.md if it exists

If helpful, also inspect:
- nearby empirical-methods lectures to match structure and tone
- the Lecture 15 source pack if it exists in the repo
- the Lecture 15 slide file if it exists
- the Lecture 15 lab folder if it exists

Goal: create or refresh Lecture 15 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/15-curating-maps-and-spatial-data.md`
- `books/empirical-methods/slides/week15/15-curating-maps-and-spatial-data.tex`
- `books/empirical-methods/labs/15-curating-maps-and-spatial-data/`

Use these as the intellectual source of truth if they exist locally:
- `empirical_methods_lecture15_edit_pack/source/15-curating-maps-and-spatial-data.md`
- `empirical_methods_lecture15_edit_pack/bibliography/15-curating-maps-and-spatial-data.bib`
- all markdown files under `empirical_methods_lecture15_edit_pack/tables/`

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

This lecture’s intellectual requirements:
1. Teach spatial data curation as a conceptual and empirical-design problem, not as clerical GIS work.
2. Make explicit that geography choice, exposure definition, crosswalks, and travel-cost construction shape the estimand.
3. Include the key equations/objects where helpful:
   - generalized commuting / access cost, e.g. `c_{ij} = \tau t_{ij}`
   - exposure measures, e.g. `E_i = \sum_j w_{ij} s_j`
   - distance-decay or kernel-weighted exposure logic
   - basic net-value / spatial-equilibrium object when useful
4. Cover the main spatial data objects:
   - points
   - polygons
   - rasters
   - networks
   - panel geographies over time
5. Cover the practical operations:
   - geocoding
   - projections and coordinate systems
   - spatial joins
   - buffers
   - distance and travel-time construction
   - boundary crosswalks
   - aggregation to commuting zones / tracts / counties / labor markets
   - confidentiality and disclosure control
6. Be explicit about the main pitfalls:
   - MAUP / arbitrary unit choice
   - geocoding error
   - temporal mismatch between outcomes and geography
   - endogenous boundary choice
   - ecological fallacy / aggregation bias
   - edge effects
   - support and comparability problems
7. Include a practical section with “rules of thumb” for defensible spatial-data work.
8. Keep the lecture tied closely to economics research papers rather than a generic GIS tutorial.
9. Use important applied papers as anchors, for example:
   - local labor market definition / commuting zones
   - neighborhood exposure / tract-level work
   - commuting and migration adjustment
   - job-access / job suburbanization / spatial mismatch
   You may refine the exact paper mix, but keep the lecture labor-oriented.
10. Avoid vague method descriptions: major tools should come with usable implementation details and caveats.
11. Make clear where spatial curation ends and spatial causal inference begins; the latter is previewed here but belongs mainly in the next lecture.

Slides requirements:
- create the Lecture 15 slide deck under the canonical path:
  `books/empirical-methods/slides/week15/15-curating-maps-and-spatial-data.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the lecture structure
- include:
  - one slide on why spatial data are economic objects, not clerical inputs
  - one slide on spatial objects (point/polygon/raster/network)
  - one slide on geographies and estimands
  - one slide on core operations (joins, buffers, distances, crosswalks)
  - one slide on practical pitfalls
  - one slide on recommended workflow / rules of thumb
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week15/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary paper where spatial curation is central to the empirical design (e.g., commuting zones, tract exposure, or job-access measurement)
- use one challenge/extension paper that pushes on finer geography, boundary choice, or access measures
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
- the main learning goal is that students understand what it means to make places, borders, distances, and exposures into empirical objects
- where useful, mention practical tools/resources (e.g., `sf`, `geopandas`, `terra`, routing/travel-time APIs, raster handling), but do not turn the lecture into software documentation
- include a concise “good spatial workflow” checklist
- use equations to clarify the mapping from geography to empirical object, not to overload the lecture

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 15 slides from the canonical path
3. if a bounded Lecture 15 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key spatial objects/equations are present
5. whether the lecture is tied clearly to economics research papers
6. whether the practical rules/pitfalls are explicit and concrete
7. whether the Lecture 15 slides compile from the canonical path
8. whether the Lecture 15 lab folder now exists and follows the standard structure
9. whether the strict build passes
10. any manual follow-up points
