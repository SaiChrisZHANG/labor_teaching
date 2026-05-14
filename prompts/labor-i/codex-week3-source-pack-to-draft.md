Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/03-dynamic-labor-supply.md, @books/labor-i/assets/tables/03-shock-taxonomy.md, @books/labor-i/assets/tables/03-design-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 3 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 3
- Canonical chapter path: `books/labor-i/03-dynamic-labor-supply.md`
- Canonical slide path: `books/labor-i/slides/week3/03-dynamic-labor-supply.tex`
- Canonical lab path: `books/labor-i/labs/03-dynamic-labor-supply/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/03-dynamic-labor-supply.md`
2. `books/labor-i/slides/week3/03-dynamic-labor-supply.tex`
3. `books/labor-i/labs/03-dynamic-labor-supply/lab.md`
4. `books/labor-i/labs/03-dynamic-labor-supply/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 3 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week3/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week3/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like a PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one dynamic optimization problem,
  - one intratemporal condition/frisch interpretation object,
  - one persistence or adjustment-cost object,
  - two figures,
  - two tables,
  - a real reading ladder with citations,
  - a clear bridge to Week 4 human capital.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.

Lab requirements:
- Build the week around the standard Reproduce → Diagnose → Transfer structure.
- Primary lab anchor: `@fehrGoette2007`.
- Secondary/optional lifecycle anchor: `@attanasioLowSanchezMarcos2008`.
- The student-facing bounded path should be runnable locally without requiring heavyweight external restricted data.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. dynamic problem,
  3. temporary vs permanent wage changes,
  4. Frisch elasticity interpretation,
  5. lifecycle profile figure,
  6. empirical design map,
  7. persistence / adjustment costs,
  8. bridge to Week 4.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as “localhost URL printed”; then stop the server cleanly.
3. Week 3 slides compile from the canonical path
4. Week 3 lab smoke test passes

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
