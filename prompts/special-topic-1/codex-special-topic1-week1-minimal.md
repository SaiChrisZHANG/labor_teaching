Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/sources/01-what-is-behavioral-labor.md, @books/special-topic1-behavioral/assets/tables/01-taxonomy-map.md, @books/special-topic1-behavioral/assets/tables/01-labor-domains-map.md, @books/special-topic1-behavioral/assets/tables/01-methods-and-welfare-map.md, and any generated figures under @books/special-topic1-behavioral/assets/figures/.

Goal: turn the Behavioral Labor Week 1 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: special-topic1-behavioral
- Week: 1
- Canonical chapter path: `books/special-topic1-behavioral/01-what-is-behavioral-labor.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week1/01-what-is-behavioral-labor.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/01-what-is-behavioral-labor/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/01-what-is-behavioral-labor.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/01-what-is-behavioral-labor.md`
2. `books/special-topic1-behavioral/slides/week1/01-what-is-behavioral-labor.tex`
3. `books/special-topic1-behavioral/labs/01-what-is-behavioral-labor/lab.md`
4. `books/special-topic1-behavioral/labs/01-what-is-behavioral-labor/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 1 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `books/special-topic1-behavioral/references.bib`.
- In prose markdown, use linked citation syntax only: `[@citekey]`.
- Do not use bare prose citations like `@citekey` or backticked prose citations like `` `@citekey` `` outside true code/example contexts.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do not include an Extension / Optional Extension box by default. If frontier or optional material is genuinely useful, surface it inside **Field Core** or **Research Lab** unless a separate box is specifically warranted.
- Slides must live only under `books/special-topic1-behavioral/slides/week1/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week1/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- This is an introductory Behavioral Labor lecture, not a bag of biases.
- Keep the week labor-focused and organized around a disciplined taxonomy:
  - nonstandard preferences
  - nonstandard beliefs
  - nonstandard decision-making / attention / complexity
  - firm, market, and policy responses
- Include at least:
  - one benchmark labor-choice object,
  - one explicit behavioral-wedge representation,
  - one welfare / internality discussion,
  - one taxonomy figure mapping behavioral wedges to labor domains,
  - one methods / identification figure,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Labor I Week 12 and forward to Week 2.
- Use the generated tables and any generated figures if they fit; if you improve captions or labels, keep paths stable.
- Treat this as a full 3-hour core chapter, not a short note.

Substantive requirements:
- Make clear why labor is a natural domain for behavioral economics:
  - repeated high-stakes decisions,
  - search frictions,
  - dynamic incentives,
  - household interactions,
  - contracts and workplace relationships,
  - policy design and take-up.
- Distinguish carefully between:
  - a reduced-form behavioral effect,
  - a structural behavioral model,
  - a welfare claim,
  - an equilibrium response by firms or markets.
- Explicitly explain why Behavioral Labor is not just “general behavioral economics applied to jobs.”
- Clarify where the lecture sits in the full series:
  - Labor I supplied worker-side foundations,
  - Labor II supplied firms, frictions, institutions, and shocks,
  - Behavioral Labor reorganizes both through behavioral wedges and design.

Methods requirements:
- Make students understand the main empirical strategies used in this literature:
  - field experiments and framed field experiments,
  - information/salience interventions,
  - administrative nudges and policy design,
  - observational designs with measured beliefs/preferences,
  - structural behavioral estimation.
- Do not present evidence without stating what margin is identified and what behavioral object is inferred.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: [@royerStehrSydnor2015].
- Secondary / challenge anchor: [@altmannFalkJaegerZimmermann2018].
- Optional frontier anchor: [@bertrandKamenicaPan2015].
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course reorientation,
  2. Behavioral Labor relative to Labor I and Labor II,
  3. benchmark labor model,
  4. DellaVigna taxonomy and labor wedges,
  5. labor domains where behavioral frictions matter,
  6. examples: workers, households, firms, policy,
  7. methods and identification,
  8. welfare and equilibrium cautions,
  9. bridge to Week 2 on nonstandard preferences.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 1 slides compile from the canonical path
4. Week 1 lab smoke test passes

Important implementation notes:
- If you add Week 1 to `index.md` or `myst.yml`, do so in the same style that Labor I and Labor II use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Keep the chapter introduction polished and job-market-facing.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
