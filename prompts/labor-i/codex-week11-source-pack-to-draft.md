Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/11-public-policy-targeting-workers.md, @books/labor-i/assets/tables/11-policy-toolkit-map.md, @books/labor-i/assets/tables/11-identification-map.md, @books/labor-i/assets/tables/11-research-frontier-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 11 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 11
- Canonical chapter path: `books/labor-i/11-public-policy-targeting-workers.md`
- Canonical slide path: `books/labor-i/slides/week11/11-public-policy-targeting-workers.tex`
- Canonical lab path: `books/labor-i/labs/11-public-policy-targeting-workers/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/11-public-policy-targeting-workers.md`
2. `books/labor-i/slides/week11/11-public-policy-targeting-workers.tex`
3. `books/labor-i/labs/11-public-policy-targeting-workers/lab.md`
4. `books/labor-i/labs/11-public-policy-targeting-workers/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 11 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week11/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week11/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course capstone with a strong empirical-methods backbone.
- It must remain labor-focused and not drift into generic public economics or political economy.
- It must explicitly synthesize the worker-side logic of Weeks 2--10.
- It must include at least:
  - one policy-adjusted budget or participation object,
  - one extensive/intensive margin decomposition,
  - one dynamic insurance or benefit-timing object,
  - one take-up condition,
  - one causal-design estimand,
  - one welfare or sufficient-statistics object,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge from Week 10 mobility to Week 12 frictions.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Methods requirements:
- The chapter must have an explicit empirical-design section that teaches students how labor economists evaluate worker-targeted policies.
- It should explain the logic of:
  - kink and bunching designs,
  - randomized field experiments and encouragement designs,
  - reform/event-study or difference-in-differences designs,
  - judge or examiner assignment IV,
  - difference-in-knowledge or exposure designs,
  - and why design choice must match the policy margin and institutional setting.
- Do not present policy results without stating the identifying variation.

Synthesis requirements:
- The opening should explicitly map previous weeks into policy-relevant margins.
- The take-up section should do real conceptual work and serve as a bridge to Week 12.
- The conclusion should end with a researcher's checklist for worker-side policy evaluation.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@chettyFriedmanSaez2013`.
- Secondary / challenge anchors: `@linosProhofskyRameshRothsteinUnrath2022` and `@lindnerReizer2020`.
- Optional extension anchors: `@frenchSong2014`, `@autorKostolMogstadSetzler2019`, `@manoliWeber2016`, `@wheelerGarlickJohnsonShawGargano2022`, and `@verhoHamalainenKanninen2022`.
- The bounded student path must run locally without restricted administrative microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why this is the worker-side policy capstone,
  2. Week 2--10 to Week 11 policy map,
  3. unified framework: incentives, constraints, frictions, insurance, investment,
  4. EITC and in-work support,
  5. UI, benefit timing, and search assistance,
  6. training and skill policy,
  7. family-support and time-allocation policy,
  8. disability and retirement incentives,
  9. take-up, salience, and administrative burden,
  10. empirical design toolkit,
  11. welfare and design interpretation,
  12. research checklist and bridge to Week 12.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 11 slides compile from the canonical path
4. Week 11 lab smoke test passes

Important implementation notes:
- If you add Week 11 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
