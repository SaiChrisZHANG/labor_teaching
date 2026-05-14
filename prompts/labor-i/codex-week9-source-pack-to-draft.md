Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/09-discrimination-measurement-and-sorting.md, @books/labor-i/assets/tables/09-mechanism-map.md, @books/labor-i/assets/tables/09-identification-map.md, @books/labor-i/assets/tables/09-sorting-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 9 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 9
- Canonical chapter path: `books/labor-i/09-discrimination-measurement-and-sorting.md`
- Canonical slide path: `books/labor-i/slides/week9/09-discrimination-measurement-and-sorting.tex`
- Canonical lab path: `books/labor-i/labs/09-discrimination-measurement-and-sorting/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/09-discrimination-measurement-and-sorting.md`
2. `books/labor-i/slides/week9/09-discrimination-measurement-and-sorting.tex`
3. `books/labor-i/labs/09-discrimination-measurement-and-sorting/lab.md`
4. `books/labor-i/labs/09-discrimination-measurement-and-sorting/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 9 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week9/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week9/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must emphasize concepts and identification, not a single identity category.
- It must include at least:
  - one raw-versus-conditional gap object,
  - one Oaxaca--Blinder style decomposition,
  - one taste-based employer-profit object,
  - one statistical-discrimination decision rule,
  - one audit-study treatment-effect object,
  - one sorting/segmentation object,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge to Week 8 inequality and Week 10 mobility.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@bertrandMullainathan2004`.
- Secondary / challenge anchor: `@klineRoseWalters2024`.
- Optional extension anchor: `@hurstRubinsteinShimizu2024`.
- The student-facing bounded path should be runnable locally without requiring students to run a real field experiment or access restricted employer microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. Week 8 to Week 9 bridge,
  3. what is a discrimination object?,
  4. taste-based discrimination,
  5. statistical discrimination,
  6. decomposition logic and bad-controls warning,
  7. audit/correspondence identification,
  8. sorting and segmentation,
  9. firm report cards / frontier measurement,
  10. bridge to Week 10.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 9 slides compile from the canonical path
4. Week 9 lab smoke test passes

Important implementation notes:
- If you add Week 9 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
