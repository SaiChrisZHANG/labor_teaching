Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/03-informality-dualism-and-contract-enforcement.md`
- `bibliography/03-informality-dualism-and-contract-enforcement.bib`
- `tables/03-informality-dualism-map.md`
- `tables/03-worker-and-firm-margins-map.md`
- `tables/03-contract-enforcement-and-identification-map.md`
- `tables/03-frontier-questions-map.md`

Goal: draft the canonical Week 3 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 3
- Canonical chapter path: `books/special-topic2-institutions/03-informality-dualism-and-contract-enforcement.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week3/03-informality-dualism-and-contract-enforcement.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/03-informality-dualism-and-contract-enforcement/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/03-informality-dualism-and-contract-enforcement.bib` into `books/special-topic2-institutions/references.bib`.
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
- This week is about informality, dualism, and contract enforcement as labor-market institutions.
- It should treat informality as a two-sided worker–employer problem.
- It should not become a generic development-economics lecture.
- It should not collapse into a pure worker informality lecture.
- It should explicitly develop the firm-side angle: registration, payroll, contract form, compliance, productivity, and scale.
- It should keep the labor-market connection explicit throughout.

Content requirements:
- Follow the established structure:
  1. opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Make clear distinctions among:
  - informal workers vs informal firms,
  - extensive vs intensive margins of informality,
  - dualist vs competitive/equilibrium views,
  - formal contracts vs effective enforceability,
  - registration vs payroll reporting,
  - worker-side vs firm-side incidence.
- Keep the lecture centered on labor-market consequences rather than a generic informal-sector survey.

Narrative backbone:
Use this week’s anchor papers explicitly:
- Ulyssea, “Informality: Causes and Consequences for Development” `[@ulyssea2020]`
- La Porta and Shleifer, “Informality and Development” `[@laportaShleifer2014]`
- Ulyssea, “Firms, Informality, and Development: Theory and Evidence from Brazil” `[@ulyssea2018]`
- Meghir, Narita, and Robin, “Wages and Informality in Developing Countries” `[@meghirNaritaRobin2015]`
- Naidu and Yuchtman, “Coercive Contract Enforcement: Law and the Labor Market in Nineteenth Century Industrial Britain” `[@naiduYuchtman2013]`
- Samaniego de la Parra and Fernández Bujanda, “Increasing the Cost of Informal Employment: Evidence from Mexico” `[@samaniegoParraFernandezBujanda2024]`
- Optional policy extension: Gerard, “Informal Labor and the Efficiency Cost of Social Programs” `[@gerard2021]`

Formal / conceptual requirements:
The chapter must include at least:
1. a clear taxonomy of informality covering:
- unregistered firms,
- off-the-books workers in registered firms,
- informal wage employment,
- self-employment / own-account work,
- missing payroll or benefit compliance;

2. one explicit dualism vs equilibrium comparison;

3. one worker-side section covering:
- wages,
- benefits,
- risk,
- mobility,
- job ladders,
- sorting;

4. one firm-side section covering:
- registration,
- payroll reporting,
- compliance,
- productivity,
- firm scale,
- adaptation to enforcement;

5. one contract-enforcement section that explains why the enforceability of employment relationships is a central institutional margin;

6. one pedagogical equation or decomposition, for example:
```{math}
:label: eq:informal-contract-value-week3
V^{formal}_{ij} - V^{informal}_{ij}
= B_{ij} - C_{ij}(R,E,\tau) + X_{ij}(K,Q),
```
with explanation of what each component means and why it is useful pedagogically;

7. one equilibrium section explaining how worker and firm margins interact.

Methods requirements:
- Explicitly distinguish:
  - worker transition / panel designs,
  - inspection or enforcement-intensity designs,
  - matched worker–firm equilibrium models,
  - structural models of registration and payroll choices,
  - legal or policy discontinuities affecting formality,
  - historical labor-contract enforcement settings.
- Make clear what each design identifies:
  - worker sorting,
  - firm response,
  - wage-setting,
  - contract enforceability,
  - formalization,
  - welfare under policy change.
- Do not present results without naming the observed margin and the identifying variation.

Field Core requirements:
Move cleanly through:
1. why informality is an institutional labor-market object,
2. dualism vs competitive/equilibrium views,
3. worker-side margins,
4. firm-side margins,
5. contract enforcement and legal status,
6. equilibrium interactions,
7. empirical strategies and what they identify,
8. bridge to Week 4.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary anchor: `[@ulyssea2018]`
- Secondary / challenge anchor: `[@meghirNaritaRobin2015]`
- Optional modern enforcement extension: `[@samaniegoParraFernandezBujanda2024]`
- The bounded pedagogical path must run locally without confidential microdata.
- The lab should help students diagnose whether a paper identifies:
  - worker sorting,
  - firm compliance/registration,
  - wage-setting,
  - or equilibrium reallocation.
- Bounded transfer ideas:
  - compare worker-side and firm-side incidence in a compliance setting,
  - compare dualist vs equilibrium interpretations in one empirical setting,
  - adapt a worker-transition exercise to a firm-formalization setting.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. central question and bridge from Week 2
  2. what counts as informality?
  3. dualism vs equilibrium views
  4. worker-side margins
  5. firm-side margins
  6. contract enforcement and legal status
  7. equilibrium interactions
  8. empirical designs and what they identify
  9. bridge to Week 4

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 3 slides compile from the canonical path.
4. Week 3 lab smoke test passes.

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week3/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
