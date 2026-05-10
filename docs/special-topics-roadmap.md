# Special Topics Teaching Portfolio Roadmap

## Purpose

The special-topics portfolio extends the core labor sequence into a set of job-market-facing and advanced elective courses that can stand alone, travel well in teaching packets, and remain compatible with the repository's standard book, slides, and lab workflow.

The portfolio is meant to do two things at once:

- deepen areas that naturally branch out of Labor I and Labor II without overloading the core sequence;
- create a visible family of polished field and advanced-elective offerings that can be built incrementally over time.

## Portfolio design

The family contains seven courses.

Three are **10-week flagship courses**:

1. `books/special-topic1-behavioral/` — Behavioral Labor
2. `books/special-topic2-institutions/` — Labor Markets and Political/Cultural Institutions
3. `books/special-topic3-gender/` — Gender Study

Four are **6-week compact advanced electives**:

1. `books/special-topic4-urban/` — Urban and Labor
2. `books/special-topic5-technology/` — Technology, Innovation, and Labor
3. `books/special-topic6-health-population/` — Labor Market, Health, and Population
4. `books/special-topic7-labor-design/` — Labor Market Design, Contracting, and Mechanism Design

## Why 10 weeks vs. 6 weeks

The 10-week courses are designed as flagship offerings because they can support a full quarter-length seminar with a strong public teaching identity. They are broad enough to anchor a job-market teaching portfolio, rich enough to sustain a layered Bridge / Field Core / Research Lab structure, and close enough to existing labor-field demand that they justify deeper week-by-week buildout.

The 6-week courses are designed as compact electives because they work best as advanced topical bursts. They are narrower, easier to slot into a department's rotating elective menu, and useful for focused teaching demonstrations or short-format graduate reading courses without pretending to be full-semester survey fields.

## Priority order for buildout

Recommended build priority:

1. Behavioral Labor
2. Labor Markets and Political/Cultural Institutions
3. Gender Study
4. Technology, Innovation, and Labor
5. Urban and Labor
6. Labor Market, Health, and Population
7. Labor Market Design, Contracting, and Mechanism Design

This order puts the three flagship, job-market-facing courses first. Among the compact electives, technology should come earliest because it connects directly to existing Labor II material; urban and health/population provide strong thematic extensions of worker and place-based labor questions; labor design is the most specialized and can remain compact longer without weakening the public portfolio.

## Bibliography policy

Each special-topics course must maintain its own course-local bibliography file:

- `books/<course-slug>/references.bib`

This is a hard architecture rule for the special-topics family.

- Do not use the large shared labor-series bibliography as the main bibliography for these courses.
- Future weekly reading packs, minimal source packs, and course-specific anchor references should merge into the course-local `references.bib`.
- Labor I and Labor II keep their current bibliography architecture in this task; no refactor is implied.

## Common course template

Every special-topics course should begin with the same structural shell:

- `index.md` — polished syllabus-style landing page and public-facing front door
- `myst.yml` — standalone MyST/Jupyter Book configuration
- `OUTLINE.md` — internal planning outline with the full weekly structure
- `README.md` — short build and workflow note
- `references.bib` — course-local bibliography
- `sources/` — source-pack or chapter-source staging area
- `slides/` — canonical slide root using `slides/weekN/<week-slug>.tex`
- `labs/` — future lab directories
- `assets/figures/`, `assets/tables/`, `assets/scripts/` — reusable course assets

Until real week chapters exist, the live reading sequence should expose the landing page and keep the rest of the scaffolding out of the visible book navigation unless there is a concrete reason to surface it.

## Chapter defaults

Every special-topics chapter should include a visible **Core points** box near the top, after the opening orientation and before the layered sections. Extension boxes are optional rather than default. Frontier, advanced, or optional material should usually live inside **Field Core** or **Research Lab**, where it can be tied directly to the labor question, evidence, and open research margins.

In prose markdown, citations must use linked citation syntax, such as `[@citekey]`. Bare citation keys like `@citekey` and backticked citation keys like `` `@citekey` `` should survive only in true code or example contexts.

## Relationship to Labor I and Labor II

The special-topics family is not a replacement for the labor sequence. Labor I and Labor II remain the core spine:

- Labor I supplies the worker-side foundations.
- Labor II supplies the firm, friction, institution, and shock architecture.

The special-topics books should be treated as structured extensions:

- some deepen a specific margin already introduced in the labor sequence, such as behavioral frictions or gendered labor outcomes;
- some cut across both semesters, such as institutions, technology, or labor design;
- all should remain legible as follow-on electives for students who already know where the topic sits in the broader labor field.

## Portfolio positioning

The first three books are the flagship, job-market-facing courses and should read like credible standalone teaching offerings from the start. The latter four are compact advanced electives: polished, clearly scoped, and intentionally narrower.

That distinction should remain visible in their front pages, outlines, and eventual build order.
