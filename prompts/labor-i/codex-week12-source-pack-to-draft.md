Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-i/OUTLINE.md, @books/labor-i/sources/12-behavioral-frictions-introduction-to-behavioral-labor.md, @books/labor-i/assets/tables/12-behavioral-taxonomy-map.md, @books/labor-i/assets/tables/12-identification-map.md, @books/labor-i/assets/tables/12-welfare-policy-map.md, and the generated figures under @books/labor-i/assets/figures/.

Goal: turn the Week 12 source pack into a polished Labor I chapter package that follows the established workflow and passes local validation.

Week identity:
- Course: Labor I
- Week: 12
- Canonical chapter path: `books/labor-i/12-behavioral-frictions-introduction-to-behavioral-labor.md`
- Canonical slide path: `books/labor-i/slides/week12/12-behavioral-frictions-introduction-to-behavioral-labor.tex`
- Canonical lab path: `books/labor-i/labs/12-behavioral-frictions-introduction-to-behavioral-labor/`
- Local conda environment: `research`

Required outputs:
1. `books/labor-i/12-behavioral-frictions-introduction-to-behavioral-labor.md`
2. `books/labor-i/slides/week12/12-behavioral-frictions-introduction-to-behavioral-labor.tex`
3. `books/labor-i/labs/12-behavioral-frictions-introduction-to-behavioral-labor/lab.md`
4. `books/labor-i/labs/12-behavioral-frictions-introduction-to-behavioral-labor/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-i/myst.yml` or `books/labor-i/index.md` needed to wire Week 12 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-i/slides/week12/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-i/slides/week12/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The chapter must follow the established Bridge / Field Core / Research Lab structure.
- It must read like an advanced PhD labor field-course introduction to Behavioral Labor.
- It must remain labor-focused and not drift into generic behavioral economics examples.
- It must use DellaVigna's taxonomy—nonstandard preferences, nonstandard beliefs, nonstandard decision-making—as the main organizing framework.
- It must explicitly explain responses by firms, managers, and policymakers, and the conditions under which markets or experience attenuate or amplify behavioral frictions.
- It must include at least:
  - one benchmark worker-choice object,
  - one quasi-hyperbolic or intertemporal inconsistency object,
  - one reference-dependent or fairness-augmented effort object,
  - one subjective-belief or distorted-return object,
  - one incentive-perception / complexity object,
  - one welfare object distinguishing positive response from normative evaluation,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - explicit bridge language back to Weeks 3, 7, and 11 and forward to a stand-alone Behavioral Labor course.
- Use the generated figures and tables if they fit; if you improve labels or captions, keep paths stable.
- Treat this as a full 3-hour core chapter with an optional extension block, not a short note.

Methods requirements:
- The chapter must have an explicit methods section on how behavioral labor is identified.
- It should explain the logic of:
  - field experiments on effort, gifts, and incentive design,
  - expectation-based and survey designs,
  - quasi-experimental identification of behavioral channels,
  - structural behavioral estimation,
  - and welfare analysis under behavioral departures from revealed preference.
- Do not present behavioral claims without stating what standard alternative is being ruled out.
- Use DellaVigna (2018) to frame the role of structural estimation, heterogeneity, identification, and sensitivity.

Synthesis requirements:
- The opening should explain why this lecture is an introduction to Behavioral Labor, not a list of biases.
- The chapter should repeatedly map behavioral mechanisms onto labor objects: hours, effort, search, job choice, training, take-up, and contract design.
- The conclusion should end with a compact field map for a future Behavioral Labor course.

Lab requirements:
- Build the week around the standard Reproduce -> Diagnose -> Transfer structure.
- Primary lab anchor: `@abelerHuffmanRaymond2025`.
- Secondary / challenge anchors: `@dellaVignaListMalmendierRao2022` and `@royerStehrSydnor2015`.
- Optional extension anchors: `@oh2023`, `@dellaVignaPaserman2005`, and `@dellaVignaPope2018`.
- The bounded student path must run locally without proprietary employer data.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why this is an introduction to Behavioral Labor,
  2. DellaVigna taxonomy adapted to labor,
  3. benchmark labor choice and behavioral wedges,
  4. nonstandard preferences in labor,
  5. nonstandard beliefs in labor,
  6. nonstandard decision-making in labor,
  7. employers, managers, and policy responses,
  8. empirical design toolkit,
  9. welfare and behavioral policy interpretation,
  10. field map and bridge to a full Behavioral Labor course.

Validation requirements:
After drafting, validate locally using the actual repo workflow.

At minimum:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 12 slides compile from the canonical path
4. Week 12 lab smoke test passes

Important implementation notes:
- If you add Week 12 to `index.md` or `myst.yml`, do so in the same style as existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-i/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
