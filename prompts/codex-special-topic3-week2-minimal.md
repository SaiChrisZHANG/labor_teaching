Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/02-labor-supply-care-work-fertility-and-household-allocation.md, @books/special-topic3-gender/assets/tables/02-household-allocation-map.md, @books/special-topic3-gender/assets/tables/02-identification-and-child-penalty-map.md, @books/special-topic3-gender/assets/tables/02-norms-bridge-map.md, and @books/special-topic3-gender/assets/tables/02-data-and-methods-map.md.

Goal: turn the Gender Study Week 2 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: special-topic3-gender
- Week: 2
- Canonical chapter path: `books/special-topic3-gender/02-labor-supply-care-work-fertility-and-household-allocation.md`
- Canonical slide path: `books/special-topic3-gender/slides/week2/02-labor-supply-care-work-fertility-and-household-allocation.tex`
- Canonical lab path: `books/special-topic3-gender/labs/02-labor-supply-care-work-fertility-and-household-allocation/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/02-labor-supply-care-work-fertility-and-household-allocation.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/02-labor-supply-care-work-fertility-and-household-allocation.md`
2. `books/special-topic3-gender/slides/week2/02-labor-supply-care-work-fertility-and-household-allocation.tex`
3. `books/special-topic3-gender/labs/02-labor-supply-care-work-fertility-and-household-allocation/lab.md`
4. `books/special-topic3-gender/labs/02-labor-supply-care-work-fertility-and-household-allocation/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 2 into the book

Special-topic conventions to preserve:
- include a clearly visible **Core points** box near the top
- do **not** add a default Extension box
- use linked citations only in prose markdown
- use the course-local bibliography
- keep edits minimal and reviewable

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Slides must live only under `books/special-topic3-gender/slides/week2/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week2/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established structure:
  1. short opening orientation,
  2. Core points box,
  3. Bridge,
  4. Field Core,
  5. Research Lab,
  6. reading ladder / references block.
- Keep the week focused on labor supply, care work, fertility, and household allocation.
- The chapter must explicitly foreshadow Week 5:
  domestic responsibility allocation partly stems from gender norms and traditions.
- The norms bridge should be clear but short; do not turn Week 2 into the norms lecture.
- Include at least:
  - one household production / time-allocation object,
  - one bargaining / control-over-resources discussion,
  - one child-penalty event-study object,
  - one causal fertility design discussion,
  - one childcare/policy section,
  - four tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 1 and forward to Weeks 3 and 5.

Methods requirements:
- Explicitly distinguish:
  - child penalties vs fertility effects,
  - descriptive event studies vs causal fertility designs,
  - bargaining shifts vs price/income effects,
  - care-time reallocation vs labor-market reallocation,
  - extensive-margin, hours, earnings, and job-quality margins.
- Make sure students can see which empirical setting maps to which econometric method.
- Use the tables to bridge empirical setting and method.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@klevenLandaisPoschSchmidtSogaard2019]`
- Secondary / challenge anchor: `[@lundborgPlugRasmussen2017]`
- Optional extension anchor: `[@bjorvatnFerrisJayachandran2025]`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and why this is labor economics,
  2. Week 1 -> Week 2 bridge,
  3. household production and time allocation,
  4. fertility and child penalties,
  5. bargaining and control over resources,
  6. childcare and policy constraints,
  7. empirical designs and what they identify,
  8. norms bridge to Week 5.

Implementation notes:
- If you add Week 2 to `index.md` or `myst.yml`, do so in the same style as the existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If any prose markdown still contains bare or backticked citations, normalize them to linked citations.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 2 slides compile from the canonical path.
4. Week 2 lab smoke test passes.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
