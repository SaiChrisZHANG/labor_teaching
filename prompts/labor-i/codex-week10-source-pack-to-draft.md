Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/10-mobility-migration-intergenerational-transmission.md, @books/labor-i/assets/tables/10-mobility-objects-map.md, @books/labor-i/assets/tables/10-methods-design-map.md, @books/labor-i/assets/tables/10-transmission-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 10 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 10
- Canonical chapter path: `books/labor-i/10-mobility-migration-intergenerational-transmission.md`
- Canonical slide path: `books/labor-i/slides/week10/10-mobility-migration-intergenerational-transmission.tex`
- Canonical lab path: `books/labor-i/labs/10-mobility-migration-intergenerational-transmission/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/10-mobility-migration-intergenerational-transmission.md`
2. `books/labor-i/slides/week10/10-mobility-migration-intergenerational-transmission.tex`
3. `books/labor-i/labs/10-mobility-migration-intergenerational-transmission/lab.md`
4. `books/labor-i/labs/10-mobility-migration-intergenerational-transmission/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 10 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course chapter with a strong empirical-methods backbone.
- It must remain labor-focused and not drift into generic public economics or political economy.
- It must include at least:
  - one transition-matrix or hazard object,
  - one migration-choice or Roy-style selection object,
  - one employer or occupation mobility wage-growth object,
  - one reform or exposure design,
  - one rank-rank mobility object,
  - one intergenerational transmission decomposition or mediation object,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge from Week 9 discrimination and to Week 11 worker-side policies.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Methods requirements:
- The chapter must have an explicit empirical-progress section that teaches students how the field improved its measurement and identification of mobility, migration, and intergenerational transmission.
- It should explain the logic of:
  - linked employer-employee data,
  - linked parent-child administrative data,
  - reform and border/exposure designs,
  - lottery-style designs,
  - rank-rank and transition-matrix approaches,
  - and measurement correction for employer-to-employer mobility.
- Do not present empirical results without clearly stating the identifying variation.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@vanDoornikGomesSchoenherrSkrastins2024`.
- Secondary / challenge anchor: `@beerliRuffnerSiegenthalerPeri2021`.
- Optional extension anchors: `@haeckLaliberte2025` and `@fujitaMoscariniPostelVinay2024`.
- The bounded student path must run locally without restricted linked employer-employee or tax microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and motivation,
  2. Week 9 to Week 10 bridge,
  3. mobility objects and measurement,
  4. worker mobility and sorting,
  5. migration as labor-market reallocation,
  6. credit, information, and moving frictions,
  7. intergenerational transmission of labor-market outcomes,
  8. empirical progress and causal designs,
  9. inequality persistence through firms/occupations/places,
  10. bridge to Week 11 policy.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add Week 10 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
