Read @AGENTS.md, @docs/repo-workflow.md, @books/labor-i/OUTLINE.md, @books/labor-i/sources/02-static-labor-supply.md, @shared/bibliography/references.bib, @books/labor-i/assets/tables/02-elasticity-taxonomy.md, @books/labor-i/assets/tables/02-policy-margin-map.md, and @books/labor-i/assets/scripts/generate_week2_static_figures.py.

Goal: create the full Week 2 package for Labor I as a scholarly field-course module on static labor supply.

Create or update these canonical files:
- `books/labor-i/02-static-labor-supply.md`
- `books/labor-i/slides/week2/02-static-labor-supply.tex`
- `books/labor-i/labs/02-static-labor-supply/lab.md`
- `books/labor-i/labs/02-static-labor-supply/README.md`
- `books/labor-i/labs/02-static-labor-supply/smoke.sh`
- `books/labor-i/labs/02-static-labor-supply/src/*` as needed
- any figure files generated under `books/labor-i/assets/figures/`

Constraints:
- Use the Week 2 source pack as the intellectual source of truth.
- Write in a graduate field-course voice, not generic textbook prose.
- Preserve the Bridge / Field Core / Research Lab structure.
- Use real citations from `shared/bibliography/references.bib`.
- Include at least three cross-referenced formal objects (e.g. equations).
- Include at least two figures and two tables, with labels and references.
- Put slides only under `books/labor-i/slides/week2/`.
- In markdown, use valid MyST inline math syntax by default: prefer `{math}`...``, allow `$...$` when simpler, and never use `\(...\)`.
- Use the conda environment `research` for local Python/Jupyter workflow commands.
- Do not leave placeholder citations.
- If a lab paper requires an external replication package, provide a bounded reduced teaching path and document exactly what external files are still needed.

Required content decisions:
1. The chapter should explain the static benchmark, nonlinear budget sets, extensive vs intensive margins, and policy interpretation.
2. The chapter should use the EITC literature as the main applied bridge.
3. The primary lab anchor should be `@saez2010`, with `@chettyFriedmanSaez2013` allowed as a secondary or optional extension.
4. The chapter should explicitly connect to Week 1 measurement objects and preview Weeks 3, 11, and 12.

Required workflow steps:
1. Run the Week 2 figure-generation script if useful and wire resulting figures into the chapter/slides.
2. Wire the new chapter into the Labor I book navigation if needed.
3. Validate locally with the repo workflow after drafting.

Validation targets:
- strict HTML build for Labor I
- Week 2 slide compilation from `books/labor-i/slides/week2/02-static-labor-supply.tex`
- Week 2 lab smoke test using the bounded teaching path

Use these commands where appropriate:
- `conda run -n research python books/labor-i/assets/scripts/generate_week2_static_figures.py`
- `conda run -n research jupyter book build --html --strict`
- slide compile using the repo workflow or `conda run -n research latexmk -cd -pdf -interaction=nonstopmode`
- lab smoke using the repo workflow or the week-local `smoke.sh`

At the end, report:
- files created or changed
- exact validation commands used
- whether build / slides / lab smoke passed
- any remaining external-data requirements for the primary replication lab
