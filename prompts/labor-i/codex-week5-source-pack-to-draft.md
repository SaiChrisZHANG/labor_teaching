Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/05-wage-determination-returns-to-skill.md, @books/labor-i/assets/tables/05-returns-parameter-map.md, @books/labor-i/assets/tables/05-wage-dispersion-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 5 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 5
- Canonical chapter path: `books/labor-i/05-wage-determination-returns-to-skill.md`
- Canonical slide path: `books/labor-i/slides/week5/05-wage-determination-returns-to-skill.tex`
- Canonical lab path: `books/labor-i/labs/05-wage-determination-returns-to-skill/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/05-wage-determination-returns-to-skill.md`
2. `books/labor-i/slides/week5/05-wage-determination-returns-to-skill.tex`
3. `books/labor-i/labs/05-wage-determination-returns-to-skill/lab.md`
4. `books/labor-i/labs/05-wage-determination-returns-to-skill/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 5 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week5/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week5/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one Mincer benchmark equation,
  - one formal selection or heterogeneous-returns object,
  - one IV/LATE interpretation object,
  - one worker--firm or worker--place decomposition object,
  - three figures,
  - two tables,
  - a real reading ladder with citations,
  - a clear bridge to Week 6 households and to Week 8 inequality.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@oreopoulos2006`.
- Secondary / challenge anchor: `@stephensYang2014`.
- Optional sorting anchor: `@engbomMoser2017` or `@diamond2016`.
- The student-facing bounded path should be runnable locally without requiring restricted matched employer--employee data.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. Week 4 to Week 5 bridge,
  3. Mincer benchmark,
  4. selection and heterogeneous gains,
  5. OLS versus IV/LATE figure,
  6. worker--firm or worker--place sorting figure,
  7. parameter map table,
  8. bridge to Week 6 and Week 8.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 5 slides compile from the canonical path
4. Week 5 lab smoke test passes

Important implementation notes:
- If you add Week 5 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
