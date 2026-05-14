Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/08-inequality-and-wage-dispersion.md, @books/labor-i/assets/tables/08-inequality-concepts-map.md, @books/labor-i/assets/tables/08-mechanism-map.md, @books/labor-i/assets/tables/08-empirical-toolkit-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 8 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 8
- Canonical chapter path: `books/labor-i/08-inequality-and-wage-dispersion.md`
- Canonical slide path: `books/labor-i/slides/week8/08-inequality-and-wage-dispersion.tex`
- Canonical lab path: `books/labor-i/labs/08-inequality-and-wage-dispersion/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/08-inequality-and-wage-dispersion.md`
2. `books/labor-i/slides/week8/08-inequality-and-wage-dispersion.tex`
3. `books/labor-i/labs/08-inequality-and-wage-dispersion/lab.md`
4. `books/labor-i/labs/08-inequality-and-wage-dispersion/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 8 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week8/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week8/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one percentile/distribution object,
  - one between/within variance decomposition,
  - one residual-inequality wage equation,
  - one AKM-style worker-firm decomposition,
  - one wage-versus-total-job-value bridge object,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge from Week 7 amenities to Week 8 inequality and from Week 8 to Week 9 discrimination/segmentation.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@autorKatzKearney2008`.
- Secondary / challenge anchors: `@songPriceGuvenenBloomVonWachter2019` and `@cardCardosoHeiningKline2018`.
- Optional frontier extension anchor: `@haanwinckel2025`.
- The student-facing bounded path should be runnable locally without requiring proprietary or restricted administrative microdata.
- A good bounded path is a small inequality factbook from public/synthetic CPS-style wage data plus a simple synthetic worker-firm decomposition.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- Because this week is heavier, the deck can be somewhat longer than a standard week.
- It should include, at minimum:
  1. central question and why this week is heavier,
  2. bridge from Weeks 5--7,
  3. inequality objects and measurement choices,
  4. percentile gaps and distribution summaries,
  5. between/within decomposition,
  6. canonical distributional facts,
  7. supply-demand and skill-premium logic,
  8. tasks and polarization,
  9. institutions and the lower tail,
  10. firms, rents, and sorting,
  11. wage inequality versus total labor-market value,
  12. empirical toolkit map,
  13. bridge to Week 9.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 8 slides compile from the canonical path
4. Week 8 lab smoke test passes

Important implementation notes:
- If you add Week 8 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
