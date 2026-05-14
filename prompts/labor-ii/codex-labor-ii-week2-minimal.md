Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/02-dynamic-labor-demand-and-adjustment-costs.md, @books/labor-ii/assets/tables/02-adjustment-cost-taxonomy.md, @books/labor-ii/assets/tables/02-design-map.md, @books/labor-ii/assets/tables/02-observed-margins-map.md, and any existing Week 2 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 2 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 2
- Canonical chapter path: `books/labor-ii/02-dynamic-labor-demand-and-adjustment-costs.md`
- Canonical slide path: `books/labor-ii/slides/week2/02-dynamic-labor-demand-and-adjustment-costs.tex`
- Canonical lab path: `books/labor-ii/labs/02-dynamic-labor-demand-and-adjustment-costs/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/02-dynamic-labor-demand-and-adjustment-costs.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/02-dynamic-labor-demand-and-adjustment-costs.md`
2. `books/labor-ii/slides/week2/02-dynamic-labor-demand-and-adjustment-costs.tex`
3. `books/labor-ii/labs/02-dynamic-labor-demand-and-adjustment-costs/lab.md`
4. `books/labor-ii/labs/02-dynamic-labor-demand-and-adjustment-costs/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 2 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week2/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week2/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on dynamic labor demand and adjustment costs; do not drift into personnel economics, search, bargaining, or monopsony.
- Include at least:
  - one target-employment object linked back to Week 1,
  - one dynamic objective with adjustment costs,
  - one convex-cost / partial-adjustment result,
  - one fixed or nonconvex-cost / inaction discussion,
  - one explicit treatment of hours versus headcount or hiring versus firing margins,
  - one policy-timing application,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 1 and forward to Week 3.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Methods requirements:
- Explicitly distinguish:
  - target versus actual employment,
  - convex versus nonconvex adjustment costs,
  - hours versus headcount margins,
  - short-run versus medium-run versus long-run responses,
  - reduced-form speed-of-adjustment estimates versus structural cost parameters,
  - policy event studies versus dynamic structural inference.
- Do not present empirical results without naming the identifying variation and the margin observed.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@dibiasiMikoschSarferaz2025`.
- Secondary / challenge anchor: `@caballeroEngelHaltiwanger1997`.
- Optional extension anchor: `@saezSchoeferSeim2019`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and reorientation from static to dynamic labor demand,
  2. Week 1 to Week 2 bridge,
  3. target employment versus actual employment,
  4. dynamic objective and adjustment-cost intuition,
  5. convex costs and partial adjustment,
  6. fixed / nonconvex costs and inaction regions,
  7. hours, headcount, hiring, and firing margins,
  8. empirical designs and what they identify,
  9. policy timing and incidence over the adjustment path,
  10. bridge to Week 3 personnel economics.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 2 slides compile from the canonical path
4. Week 2 lab smoke test passes

Important implementation notes:
- If you add Week 2 to `index.md` or `myst.yml`, do so in the same style that Labor I and Labor II Week 1 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/02-target-vs-actual-employment.png`
  - `assets/figures/02-convex-vs-nonconvex-adjustment.png`
  - `assets/figures/02-hours-vs-headcount-adjustment.png`
  - `assets/figures/02-policy-incidence-over-time.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
