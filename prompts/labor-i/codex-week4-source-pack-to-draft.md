Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/04-human-capital-skill-formation.md, @books/labor-i/assets/tables/04-human-capital-taxonomy.md, @books/labor-i/assets/tables/04-design-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 4 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 4
- Canonical chapter path: `books/labor-i/04-human-capital-skill-formation.md`
- Canonical slide path: `books/labor-i/slides/week4/04-human-capital-skill-formation.tex`
- Canonical lab path: `books/labor-i/labs/04-human-capital-skill-formation/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/04-human-capital-skill-formation.md`
2. `books/labor-i/slides/week4/04-human-capital-skill-formation.tex`
3. `books/labor-i/labs/04-human-capital-skill-formation/lab.md`
4. `books/labor-i/labs/04-human-capital-skill-formation/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 4 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week4/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week4/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter, not a generic AI summary.
- It must include at least:
  - one Ben-Porath-style law of motion,
  - one wage/earnings relation linked to human capital,
  - one investment tradeoff or first-order condition,
  - one skill-production function,
  - at least two figures and two tables,
  - a real reading ladder with citations,
  - a clear distinction between core material and optional extension material,
  - a clear bridge to Week 5 wage determination and returns to skill.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Because Week 4 is intentionally heavier, it is acceptable for the chapter to be longer than Weeks 2--3.
- Make the chapter usable in three ways:
  1. as a full long-form chapter,
  2. as a 3-hour core lecture,
  3. as a core lecture plus optional extension block.

Lab requirements:
- Build the week around the standard Reproduce → Diagnose → Transfer structure.
- Primary lab anchor: `@attanasioEtAl2020HumanCapital`.
- Secondary/optional reduced-form anchor: `@walters2015`.
- Optional theory/finance extension: `@lochnerMongeNaranjo2011`.
- The student-facing bounded path should be runnable locally without requiring heavyweight restricted data.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. why Week 3 is not enough,
  3. Ben-Porath law of motion,
  4. lifecycle human-capital and wage profiles,
  5. schooling versus training as accumulation margins,
  6. general versus specific training,
  7. self-productivity and dynamic complementarity,
  8. empirical design map,
  9. frictions / finance / policy,
  10. core versus extension material,
  11. bridge to Week 5.
- Put the optional extension material in appendix-style slides if needed.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as “localhost URL printed”; then stop the server cleanly.
3. Week 4 slides compile from the canonical path
4. Week 4 lab smoke test passes

Important implementation notes:
- If you add Week 4 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
