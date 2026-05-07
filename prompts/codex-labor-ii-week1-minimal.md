Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/01-labor-demand-and-production.md, @books/labor-ii/assets/tables/01-elasticity-taxonomy.md, @books/labor-ii/assets/tables/01-design-map.md, @books/labor-ii/assets/tables/01-policy-incidence-map.md, and the generated figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 1 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 1
- Canonical chapter path: `books/labor-ii/01-labor-demand-and-production.md`
- Canonical slide path: `books/labor-ii/slides/week1/01-labor-demand-and-production.tex`
- Canonical lab path: `books/labor-ii/labs/01-labor-demand-and-production/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/01-labor-demand-and-production.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/01-labor-demand-and-production.md`
2. `books/labor-ii/slides/week1/01-labor-demand-and-production.tex`
3. `books/labor-ii/labs/01-labor-demand-and-production/lab.md`
4. `books/labor-ii/labs/01-labor-demand-and-production/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 1 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week1/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week1/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on static labor demand and production; do not drift into dynamic adjustment, search, bargaining, or monopsony.
- Include at least:
  - one production-function object,
  - one cost-minimization / conditional-demand derivation,
  - one explicit scale/substitution decomposition,
  - one Hicks--Marshall discussion,
  - one policy-incidence application,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Labor I and forward to Week 2.
- Use the generated figures and tables if they fit; if you improve captions or labels, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Methods requirements:
- Explicitly distinguish:
  - conditional vs total labor demand,
  - short-run vs long-run elasticities,
  - payroll-tax or labor-cost reforms,
  - city-industry demand shocks,
  - product-market cost shocks,
  - matched employer-employee rent-sharing evidence.
- Do not present empirical results without naming the identifying variation and the margin observed.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@beaudryGreenSand2018`.
- Secondary / challenge anchor: `@saezSchoeferSeim2019`.
- Optional extension anchor: `@buttersSacksSeo2022`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course reorientation,
  2. Labor I to Labor II bridge,
  3. production and the static firm problem,
  4. cost minimization and conditional labor demand,
  5. unconditional demand and scale effects,
  6. Hicks--Marshall laws,
  7. payroll taxes, cost shocks, and incidence,
  8. empirical designs and what they identify,
  9. bridge to Week 2 dynamic adjustment.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 1 slides compile from the canonical path
4. Week 1 lab smoke test passes

Important implementation notes:
- If you add Week 1 to `index.md` or `myst.yml`, do so in the same style that Labor I uses.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
