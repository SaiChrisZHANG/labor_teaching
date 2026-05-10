# Codex prompt: generate a special-topics weekly module

Use this prompt inside Codex after replacing the placeholders.

```text
Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, @books/{{BOOK}}/OUTLINE.md, @books/{{BOOK}}/index.md, @books/{{BOOK}}/myst.yml, @books/{{BOOK}}/references.bib, and any existing source pack, tables, figures, or nearby week files for Week {{N}}.

Goal: create Week {{N}} for the special-topics book {{BOOK}} and wire it into the standard repo workflow without changing the course scope.

Week metadata:
- book: {{BOOK}}
- week slug: {{WEEK_SLUG}}
- chapter title: {{CHAPTER_TITLE}}
- central labor question: {{QUESTION}}
- canonical chapter path: `books/{{BOOK}}/{{WEEK_SLUG}}.md`
- canonical slide path: `books/{{BOOK}}/slides/week{{N}}/{{WEEK_SLUG}}.tex`
- canonical lab path: `books/{{BOOK}}/labs/{{WEEK_SLUG}}/`
- local conda environment: `research`

Non-negotiable special-topics conventions:
- Follow the Bridge / Field Core / Research Lab structure.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do not include an Extension / Optional Extension box by default.
- If frontier or optional material is genuinely useful, surface it inside **Field Core** or **Research Lab** unless a separate extension box is specifically warranted.
- Use real citation keys from `books/{{BOOK}}/references.bib`.
- In prose markdown, use linked citation syntax only: `[@citekey]`.
- Do not use bare prose citations like `@citekey` or backticked prose citations like `` `@citekey` `` outside true code/example contexts.
- Do not invent citations or bibliography metadata.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Keep edits minimal and reviewable.

Required outputs:
1. `books/{{BOOK}}/{{WEEK_SLUG}}.md`
2. `books/{{BOOK}}/slides/week{{N}}/{{WEEK_SLUG}}.tex`
3. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/lab.md`
4. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/README.md`
5. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/run-log.md`
6. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/smoke.sh`
7. bounded starter files under `original/`, `transfer/`, `src/`, `output/`, and `environment/` as needed
8. updates to `books/{{BOOK}}/myst.yml`
9. updates to `books/{{BOOK}}/index.md`

Validation steps:
1. from `books/{{BOOK}}`, run `conda run -n research jupyter book build --html --strict`
2. from `books/{{BOOK}}`, run `conda run -n research --live-stream jupyter book start` and confirm that preview prints a `localhost` URL
3. from `books/{{BOOK}}`, run `conda run -n research latexmk -cd -pdf -interaction=nonstopmode slides/week{{N}}/{{WEEK_SLUG}}.tex`
4. from `books/{{BOOK}}/labs/{{WEEK_SLUG}}`, run `ENV_NAME=research bash smoke.sh`
5. summarize files changed and any remaining issues
```
