Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/06-identity-social-hierarchy-and-labor-market-institutions.md`
- `bibliography/06-identity-social-hierarchy-and-labor-market-institutions.bib`
- `tables/06-category-hierarchy-map.md`
- `tables/06-institutional-channels-map.md`
- `tables/06-identification-and-evidence-map.md`
- `tables/06-frontier-and-reading-map.md`

Goal: draft the canonical Week 6 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 6
- Canonical chapter path: `books/special-topic2-institutions/06-identity-social-hierarchy-and-labor-market-institutions.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week6/06-identity-social-hierarchy-and-labor-market-institutions.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/06-identity-social-hierarchy-and-labor-market-institutions/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/06-identity-social-hierarchy-and-labor-market-institutions.bib` into `books/special-topic2-institutions/references.bib`.
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

Topic boundary:
- Week 6 is about category-based hierarchy and labor-market institutions.
- It should not collapse into a generic discrimination lecture.
- It should not collapse into a generic identity lecture.
- It should show how caste, race, ethnicity, gender, religion, migrant status, and related categories become labor-market institutions through:
  - employer beliefs,
  - networks and referrals,
  - credential recognition,
  - occupation boundaries,
  - public rules,
  - local governance,
  - spatial sorting.
- Keep the contrast with Week 5 visible: Week 5 studied conduct norms; Week 6 studies durable structural hierarchy.

Required chapter structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references block
7. bridge to Week 7

Narrative backbone:
Use the paper set in this source pack explicitly, including:
- `[@bertrandMullainathan2004]`
- `[@munshiRosenzweig2006]`
- `[@hsiehHurstJonesKlenow2019]`
- `[@oreopoulos2011]`
- `[@lowe2021]`
- `[@anejaXu2020]`
- `[@darity2022]`

Substantive requirements:
The chapter must include:
1. a clear opening explanation of when a social category becomes a labor-market institution;
2. explicit treatment of employer beliefs and differential treatment;
3. explicit treatment of networks, referrals, and occupation persistence;
4. explicit treatment of occupational boundaries and talent misallocation;
5. explicit treatment of public rules, state action, or local governance;
6. a section on contact/integration as an institutional margin;
7. a clear contrast between norms of conduct (Week 5) and durable hierarchy (Week 6);
8. frontier questions connecting micro barriers to broader labor allocation.

Formal / conceptual requirements:
Include at least one compact conceptual object, for example:
```{math}
:label: eq:hierarchy-access-week6
P(\text{access}_{ij}) = f(x_i, q_i, B_j, N_i, L_i, H_i),
```

and/or a compact allocation-loss decomposition.

Methods requirements:
Explicitly distinguish:
- audit studies,
- credential / resume experiments,
- network and migration designs,
- historical/public-rule shocks,
- contact experiments,
- macro or structural misallocation frameworks.

Make clear what each design identifies and what it does not identify.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary anchor: `[@bertrandMullainathan2004]`
- Secondary / challenge anchor: `[@oreopoulos2011]`
- Network / caste extension: `[@munshiRosenzweig2006]`
- Contact / hierarchy extension: `[@lowe2021]`
- Public-rule extension: `[@anejaXu2020]`
- Misallocation extension: `[@hsiehHurstJonesKlenow2019]`
- The bounded pedagogical path must run locally without confidential data.
- The lab should help students diagnose:
  - whether a barrier is belief-based, network-based, legal, or spatial,
  - whether evidence is micro, meso, or macro,
  - how hierarchy differs from conduct norms.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. central question and bridge from Week 5
  2. Week 5 vs Week 6 boundary
  3. when social categories become labor-market institutions
  4. employer beliefs and differential treatment
  5. networks, referrals, and occupation persistence
  6. occupational boundaries and talent misallocation
  7. public rules, segregation, and local governance
  8. identification and empirical strategies
  9. frontier questions and bridge to Week 7

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 6 slides compile from the canonical path.
4. Week 6 lab smoke test passes.

Important implementation notes:
- If you add Week 6 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week6/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
