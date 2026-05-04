Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/06-households-family-fertility-time-allocation.md, @books/labor-i/assets/tables/06-household-model-map.md, @books/labor-i/assets/tables/06-policy-margin-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 6 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 6
- Canonical chapter path: `books/labor-i/06-households-family-fertility-time-allocation.md`
- Canonical slide path: `books/labor-i/slides/week6/06-households-family-fertility-time-allocation.tex`
- Canonical lab path: `books/labor-i/labs/06-households-family-fertility-time-allocation/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/06-households-family-fertility-time-allocation.md`
2. `books/labor-i/slides/week6/06-households-family-fertility-time-allocation.tex`
3. `books/labor-i/labs/06-households-family-fertility-time-allocation/lab.md`
4. `books/labor-i/labs/06-households-family-fertility-time-allocation/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 6 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week6/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week6/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one household time-allocation object,
  - one household-production or resource problem,
  - one collective or bargaining object,
  - one event-study child-penalty object,
  - three figures,
  - two tables,
  - a real reading ladder with citations,
  - a clear bridge to Week 7 amenities and Week 8 inequality.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@lundborgPlugRasmussen2017`.
- Secondary / challenge anchor: `@klevenLandaisSogaard2019`.
- Optional policy or outsourcing extension: `@gelbach2002`, `@cortesTessada2011`, or `@klevenLandaisPoschSteinhauerZweimueller2024`.
- The student-facing bounded path should be runnable locally without requiring restricted administrative microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. Week 5 to Week 6 bridge,
  3. household time-allocation problem,
  4. unitary versus collective models,
  5. fertility and childbirth as labor-market shocks,
  6. child-penalty event-study figure,
  7. household-model map table,
  8. policy-margin map table,
  9. bridge to Week 7 and Week 8.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 6 slides compile from the canonical path
4. Week 6 lab smoke test passes

Important implementation notes:
- If you add Week 6 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
