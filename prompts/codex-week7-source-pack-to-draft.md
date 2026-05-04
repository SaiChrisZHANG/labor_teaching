Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/07-job-amenities-compensating-differentials.md, @books/labor-i/assets/tables/07-amenity-taxonomy.md, @books/labor-i/assets/tables/07-design-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 7 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 7
- Canonical chapter path: `books/labor-i/07-job-amenities-compensating-differentials.md`
- Canonical slide path: `books/labor-i/slides/week7/07-job-amenities-compensating-differentials.tex`
- Canonical lab path: `books/labor-i/labs/07-job-amenities-compensating-differentials/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/07-job-amenities-compensating-differentials.md`
2. `books/labor-i/slides/week7/07-job-amenities-compensating-differentials.tex`
3. `books/labor-i/labs/07-job-amenities-compensating-differentials/lab.md`
4. `books/labor-i/labs/07-job-amenities-compensating-differentials/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 7 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week7/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week7/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one worker utility / indirect-utility object over wages and amenities,
  - one worker-side equalizing-differentials condition,
  - one firm-side amenity-cost or profit object,
  - one modern discrete-choice / willingness-to-pay object,
  - three figures,
  - two tables,
  - a real reading ladder with citations,
  - a clear bridge to Week 8 inequality and Week 9 discrimination/segmentation.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@masPallais2017`.
- Secondary / challenge anchor: `@maestasMullenPowellVonWachterWenger2023`.
- Optional extension anchor: `@sorkin2018`.
- The student-facing bounded path should be runnable locally without requiring proprietary or restricted administrative microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. Week 6 to Week 7 bridge,
  3. jobs as wage-plus-amenity bundles,
  4. Rosen hedonic equilibrium and equalizing differentials,
  5. why hedonic wage regressions can fail,
  6. modern willingness-to-pay evidence,
  7. amenity taxonomy table,
  8. empirical design map table,
  9. amenities, sorting, and inequality,
  10. bridge to Week 8 and Week 9.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 7 slides compile from the canonical path
4. Week 7 lab smoke test passes

Important implementation notes:
- If you add Week 7 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
