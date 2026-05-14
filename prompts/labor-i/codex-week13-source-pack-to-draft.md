Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/13-synthesis-and-research-designs.md, @books/labor-i/assets/tables/13-research-idea-template.md, @books/labor-i/assets/tables/13-labor-i-to-labor-ii-bridge-map.md, @books/labor-i/assets/tables/13-common-failure-modes.md, @books/labor-i/assets/tables/13-anchor-paper-menu.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 13 source pack into a polished Labor I capstone package that synthesizes the first semester, helps students develop a research idea of their own, and explicitly bridges into Labor II.

Week identity:
- Course: Labor I
- Week: 13
- Canonical chapter path: `books/labor-i/13-synthesis-and-research-designs.md`
- Canonical slide path: `books/labor-i/slides/week13/13-synthesis-and-research-designs.tex`
- Canonical lab path: `books/labor-i/labs/13-synthesis-and-research-designs/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/13-synthesis-and-research-designs.md`
2. `books/labor-i/slides/week13/13-synthesis-and-research-designs.tex`
3. `books/labor-i/labs/13-synthesis-and-research-designs/lab.md`
4. `books/labor-i/labs/13-synthesis-and-research-designs/smoke.sh`
5. any minimal `src/` or template files needed for the bounded research-design studio path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 13 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week13/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week13/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course capstone and research-design studio.
- It must synthesize Weeks 1--12 and show how the worker-side topics fit into modern labor economics.
- It must explicitly foreshadow Labor II: firms, labor demand, search, wage-setting, monopsony, organizations, institutions, and aggregate adjustment.
- It must include at least:
  - one unified worker-side choice problem,
  - one human-capital accumulation object,
  - one job-value or amenity object,
  - one causal estimand,
  - one assignment / sorting object,
  - one bridge-to-Labor-II object,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a concrete student research-memo assignment.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional research-workshop extension, not a short review note.

Research-design requirements:
- The chapter must teach students how to move from topic -> question -> mechanism -> data -> design -> contribution.
- It must distinguish strong labor research questions from weak or overbroad ideas.
- It must explain common failure modes and how to improve them.
- It must provide several example research templates drawn from different weeks in Labor I.
- It must clearly indicate when a worker-side idea remains partial-equilibrium and when Labor II tools become necessary.

Labor-II bridge requirements:
- The chapter must make the bridge to Labor II explicit rather than decorative.
- It should show how worker-side questions change once firms, search frictions, wage-setting, personnel economics, or institutions are added.
- The final section should leave students with a map of where Labor II begins.

Lab requirements:
- Build Week 13 as a research-design studio rather than a heavy new replication.
- Use the standard Reproduce -> Diagnose -> Propose structure.
- The bounded student path must run locally without restricted data.
- The lab should give students a small menu of anchor papers from earlier topics and then help them draft an extension memo.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. why Week 13 is a synthesis and research-design week,
  2. the full Labor I architecture,
  3. unified worker-side framework,
  4. what makes a good labor research question,
  5. mechanism--data--design--contribution pipeline,
  6. example research templates,
  7. common failure modes,
  8. the bridge to Labor II,
  9. the student memo template,
  10. where Labor I fits inside modern labor economics.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 13 slides compile from the canonical path
4. Week 13 lab smoke test passes

Important implementation notes:
- If you add Week 13 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
