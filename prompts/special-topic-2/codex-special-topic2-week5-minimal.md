Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/05-culture-norms-and-labor-market-allocation.md`
- `bibliography/05-culture-norms-and-labor-market-allocation.bib`
- `tables/05-norms-categories-map.md`
- `tables/05-mechanisms-and-labor-outcomes-map.md`
- `tables/05-measurement-and-identification-map.md`
- `tables/05-frontier-and-reading-map.md`

Goal: draft the canonical Week 5 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 5
- Canonical chapter path: `books/special-topic2-institutions/05-culture-norms-and-labor-market-allocation.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week5/05-culture-norms-and-labor-market-allocation.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/05-culture-norms-and-labor-market-allocation/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/05-culture-norms-and-labor-market-allocation.bib` into `books/special-topic2-institutions/references.bib`.
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
- Week 5 is about norms around work, family, reputation, competition, leadership-entry, and acceptable labor-market conduct.
- Week 5 is NOT the week for full treatment of caste, race, ethnicity, migrant status, or institutionalized hierarchy. Those should be reserved for Week 6.
- Categories may appear in Week 5 only insofar as they carry expectations about conduct or acceptable work.
- The chapter must make this Week 5 / Week 6 distinction explicit so the course remains cohesive.

Required chapter structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references block
7. bridge to Week 6

Narrative backbone:
Use the wide-range paper set in this source pack explicitly, including:
- `[@guisoSapienzaZingales2006]`
- `[@alesinaGiulianoNunn2013]`
- `[@fernandezFogli2009]`
- `[@jayachandran2021]`
- `[@carvalho2013]`
- `[@floryLeibbrandtList2015]`
- `[@delfino2024]`
- `[@cullenPerezTruglia2023]`
- `[@clark2003]`
- `[@brezaKaurKrishnaswamy2019]`
- `[@eugsterLaliveSteinhauerZweimuller2017]`

Substantive requirements:
The chapter must include:
1. an explicit explanation of why norms are labor-market mechanisms rather than residual explanations;
2. a broad taxonomy of norms, covering:
   - family and gender-role norms,
   - religion and reputation norms,
   - competition and self-promotion norms,
   - networking and leadership-entry norms,
   - work ethic, unemployment, and wage-acceptance norms;
3. a clear distinction between Week 5 conduct/role norms and Week 6 structural hierarchy;
4. a mechanism section connecting norms to labor supply, search, occupational entry, entrepreneurship, migration, promotions, and wage acceptance;
5. a measurement section showing how economists identify norms;
6. a frontier section that points to how norms interact with firms, communities, and changing labor markets.

Formal / conceptual requirements:
Include at least one compact conceptual object, such as:
```{math}
:label: eq:norm-allocation-week5
U_{ij} = w_{ij} - c_{ij} - s_{ij}(a_{ij}, n_i) + \varepsilon_{ij},
```

Methods requirements:
Explicitly distinguish:
- inherited-culture identification,
- historical persistence designs,
- job-entry field experiments,
- workplace networking / promotion evidence,
- local social-environment evidence,
- market-level labor-supply norm experiments.

Make clear what each design identifies and what it does not identify.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary anchor: `[@fernandezFogli2009]`
- Secondary / challenge anchor: `[@floryLeibbrandtList2015]`
- Religion extension: `[@carvalho2013]`
- Leadership/networking extension: `[@cullenPerezTruglia2023]`
- Work-norm extension: `[@brezaKaurKrishnaswamy2019]`
- The bounded pedagogical path must run locally without confidential data.
- The lab should help students diagnose:
  - when a proxy is measuring norms rather than prices,
  - when a design identifies cultural transmission rather than current pressure,
  - how conduct norms differ from structural hierarchy.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. central question and bridge from Week 4
  2. norms as labor-market mechanisms
  3. Week 5 vs Week 6 boundary
  4. family and gender-role norms
  5. religion, reputation, and acceptable work
  6. competition, self-promotion, and leadership-entry norms
  7. work ethic, unemployment, and wage-acceptance norms
  8. measurement and empirical strategies
  9. frontier questions and bridge to Week 6

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 5 slides compile from the canonical path.
4. Week 5 lab smoke test passes.

Important implementation notes:
- If you add Week 5 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week5/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
