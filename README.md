# Labor Teaching Starter

This starter kit is designed for a public labor-economics teaching platform built around Jupyter Book + LaTeX/Beamer slides, with Python as the backbone and R/Stata as companion languages.

## What is in this folder

- `AGENTS.md` — repository-wide instructions for Codex
- `PLANS.md` — planning template for any multi-step task
- `.codex/config.toml` — optional project-local Codex settings
- `docs/portfolio-charter.md` — course portfolio and build order
- `docs/repo-blueprint.md` — repository architecture and naming rules
- `shared/templates/module-template.md` — standard teaching module template
- `shared/templates/syllabus-template.md` — standard syllabus template
- `shared/templates/slide-outline-template.tex` — minimal Beamer structure
- `shared/style/code-policy.md` — language policy and code conventions
- `prompts/codex-prompt-pack.md` — reusable prompts for repo scaffolding and content generation
- `books/*/OUTLINE.md` — initial outlines for each course book

## Working philosophy

1. Build shared modules before full courses.
2. Keep one module structure across all books.
3. Use Python as the primary public teaching language.
4. Add R and Stata only when they add real teaching value.
5. Separate books from slides in the build pipeline.
6. Treat every public page as portfolio material.

## Immediate build order

1. Finalize the repository scaffold.
2. Build shared toolkit pages:
   - labor market facts and datasets
   - identification primer
   - reproducibility workflow
3. Build the first complete Labor I module.
4. Build the matching slide deck.
5. Build one executable Python lab.
6. Add optional R and Stata companion snippets where valuable.

## Recommended first Codex tasks

1. Read `AGENTS.md` and `PLANS.md`.
2. Scaffold the monorepo exactly as described in `docs/repo-blueprint.md`.
3. Create the first Jupyter Book shell for `books/labor-i/`.
4. Draft the first module using `shared/templates/module-template.md`.
5. Create a Beamer deck using `shared/templates/slide-outline-template.tex`.
6. Add GitHub Actions for book builds and link checks.
