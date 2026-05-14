Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/08-unions-collective-bargaining-and-worker-voice.md, @books/labor-ii/assets/tables/08-collective-bargaining-concepts-map.md, @books/labor-ii/assets/tables/08-union-takeup-coverage-and-spillovers-map.md, @books/labor-ii/assets/tables/08-identification-and-political-economy-bridge.md, and any existing Week 8 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 8 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 8
- Canonical chapter path: `books/labor-ii/08-unions-collective-bargaining-and-worker-voice.md`
- Canonical slide path: `books/labor-ii/slides/week8/08-unions-collective-bargaining-and-worker-voice.tex`
- Canonical lab path: `books/labor-ii/labs/08-unions-collective-bargaining-and-worker-voice/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/08-unions-collective-bargaining-and-worker-voice.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/08-unions-collective-bargaining-and-worker-voice.md`
2. `books/labor-ii/slides/week8/08-unions-collective-bargaining-and-worker-voice.tex`
3. `books/labor-ii/labs/08-unions-collective-bargaining-and-worker-voice/lab.md`
4. `books/labor-ii/labs/08-unions-collective-bargaining-and-worker-voice/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 8 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week8/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week8/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on unions, collective bargaining, worker voice, union takeup, bargaining coverage, spillovers onto non-union workers, and a brief political-economy bridge; do not drift into the later labor-regulation/enforcement lecture or into a general history-of-labor survey.
- This should be one of the heavier institution weeks in Labor II: a full 3-hour core chapter with a substantial optional 60-90 minute extension block.
- Include at least:
  - one clean distinction between union membership, collective-bargaining coverage, bargaining regimes, and worker voice,
  - one collective-bargaining or rent-sharing framework,
  - one section on union takeup / organizing / certification and who gets organized,
  - one section on coverage effects, selection, and wage compression,
  - one section on spillovers or threat effects for non-union workers,
  - one brief but explicit section on the political-economy link of unions,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 7 and forward to Week 9.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Keep the lecture cleanly structured even though it spans institutions, wage-setting, spillovers, organizing, and political economy.

Methods requirements:
- Explicitly distinguish:
  - union membership vs collective-bargaining coverage,
  - firm-level bargaining vs sectoral bargaining vs extension regimes,
  - direct effects on covered workers vs spillovers onto uncovered workers,
  - certification-election RD designs vs matched employer-employee designs,
  - time-series / distributional decompositions vs policy-shock/event-study designs,
  - private-sector unionization vs public-sector or education-sector collective bargaining if the latter are mentioned.
- Do not present empirical results without naming the identifying variation, the unit of observation, the margin observed, and the key unobserved object.
- Be explicit that disagreement in the literature can come from:
  - different objects (coverage vs membership, wages vs employment vs survival),
  - different institutional settings,
  - selection into organizing,
  - and different notions of spillover.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@farberHerbstKuziemkoNaidu2021`.
- Secondary / challenge anchor: `@dinardoLee2004`.
- Optional extension anchor: `@fortinLemieuxLloyd2021`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. whether the object is union membership, union coverage, or an organizing/certification margin,
  2. whether the effect is direct, spillover, or threat-based,
  3. what the main identification challenge is,
  4. how to transfer the design to a small public CPS/Unionstats panel, certification-election panel, or synthetic coverage/inequality panel.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 7 to Week 8 bridge,
  3. what unions and collective bargaining change in the labor market,
  4. membership vs coverage vs bargaining regime,
  5. union takeup, organizing, and certification,
  6. direct effects on covered workers: premia, compression, and selection,
  7. spillovers and threat effects on non-union workers,
  8. empirical designs and what they identify,
  9. political-economy bridge,
  10. bridge to Week 9 labor regulation, enforcement, and insurance.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 8 slides compile from the canonical path
4. Week 8 lab smoke test passes

Important implementation notes:
- If you add Week 8 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1-7 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/08-membership-vs-coverage-distinction.png`
  - `assets/figures/08-collective-bargaining-regimes.png`
  - `assets/figures/08-union-wage-compression-and-spillovers.png`
  - `assets/figures/08-certification-to-coverage-pipeline.png`
  - `assets/figures/08-political-economy-bridge.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
