Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/01-why-institutions-matter-for-labor-markets.md`
- `bibliography/01-why-institutions-matter-for-labor-markets.bib`
- `tables/01-institution-taxonomy-map.md`
- `tables/01-mechanism-map.md`
- `tables/01-domain-preview-map.md`
- `tables/01-empirical-strategies-map.md`

Goal: draft the canonical Week 1 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this revised source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 1
- Canonical chapter path: `books/special-topic2-institutions/01-why-institutions-matter-for-labor-markets.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week1/01-why-institutions-matter-for-labor-markets.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/01-why-institutions-matter-for-labor-markets/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/01-why-institutions-matter-for-labor-markets.bib` into `books/special-topic2-institutions/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key.
3. Do not duplicate citation keys.

Non-negotiable course conventions:
- Use valid MyST markdown syntax.
- All prose citations must render as linked citations like `[@citekey]`; do not leave bare `@citekey` or backticked citation keys in prose.
- Inline math in markdown should use `{math}`...`` if needed; do not use `\(...\)` in markdown.
- Include a visible **Core points** box near the top.
- Do NOT add a default Extension box.
- Keep the course labor-focused.
- Use the course-local bibliography as the primary bibliography for this course.

Content requirements:
- This is the fundamental framing lecture for the course.
- It must explain that labor-market institutions include both:
  1. formal institutions: labor law, regulation, contracts, enforcement, state capacity
  2. informal institutions: culture, norms, trust, family ties, hierarchy, networks, social status, beliefs about work and mobility
- Do not let culture collapse into a single gender application.
- Gender can appear as one application, but the broader point must be clear: culture is a wide class of informal institutions that shape labor supply, mobility, referrals, compliance, bargaining, occupational allocation, migration, and support for labor regulation.
- Keep the labor-market connection explicit at all times.

Narrative backbone:
- Use the revised framing anchors in this source pack:
  - Freeman on labor-market institutions in comparative perspective
  - MacLeod on labor law / employment contracts
  - Botero et al. on comparative institutional measurement
  - Guiso, Sapienza, and Zingales on culture as a measurable economic mechanism
  - Alesina, Algan, Cahuc, and Giuliano on family values and labor regulation
  - Munshi and Rosenzweig on networks, hierarchy, insurance, mobility, and labor misallocation
  - Clark on unemployment as a social norm
  - Fernández and Fogli may appear as one concrete application, but should not dominate the culture discussion

Required outputs:
1. `books/special-topic2-institutions/01-why-institutions-matter-for-labor-markets.md`
2. `books/special-topic2-institutions/slides/week1/01-why-institutions-matter-for-labor-markets.tex`
3. `books/special-topic2-institutions/labs/01-why-institutions-matter-for-labor-markets/lab.md`
4. `books/special-topic2-institutions/labs/01-why-institutions-matter-for-labor-markets/smoke.sh`
5. any minimal `src/` files needed for a bounded lab path
6. any minimal updates to `books/special-topic2-institutions/myst.yml` or `books/special-topic2-institutions/index.md` needed to wire Week 1 into the book

Chapter structure:
- opening orientation / why this week matters
- Core points box
- Bridge
- Field Core
- Research Lab
- reading ladder / references block
- forward bridge to Week 2

Week 1 content should include:
- an explicit taxonomy of institutions: formal vs informal
- a mechanism discussion: incentives, bargaining, enforcement, information, trust, insurance, sorting, mobility, compliance, political support for regulation
- a domain-preview section that foreshadows later weeks
- a short empirical-strategy section showing how researchers measure institutions and informal norms in labor settings
- a clear distinction between institutional objects, mechanisms, and outcomes
- at least one section that explains why informal institutions can persist even when formal rules change

Lab requirements:
- Keep the lab bounded and pedagogical.
- Use a “Reproduce -> Diagnose -> Transfer” structure.
- The lab can be lightweight and data-reduced for Week 1.
- A natural lab direction is a descriptive or reduced-form exercise connecting inherited culture / network structure / labor outcomes, but it must run locally without confidential data.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. course framing and why institutions matter
  2. formal vs informal institutions
  3. mechanism map
  4. comparative measurement
  5. culture as informal institution beyond gender
  6. networks / mobility / misallocation
  7. labor law / contracts / enforcement
  8. empirical strategies
  9. bridge to Week 2

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 1 slides compile from the canonical path
4. Week 1 lab smoke test passes

Important implementation notes:
- If you add Week 1 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week1/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
