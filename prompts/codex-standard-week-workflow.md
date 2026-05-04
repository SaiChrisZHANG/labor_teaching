# Codex prompt: generate a new weekly module and wire it into the repo workflow

Use this prompt inside the Codex VS Code extension after replacing the placeholders.

```text
Read @AGENTS.md, @docs/repo-workflow.md, @shared/templates/code-lab-template.md, @books/{{BOOK}}/OUTLINE.md, and the existing files for nearby weeks.

Goal: create Week {{N}} for {{BOOK}} and wire it into the standard repo workflow.

Week metadata:
- book: {{BOOK}}
- week slug: {{WEEK_SLUG}}
- chapter title: {{CHAPTER_TITLE}}
- slide title: {{SLIDE_TITLE}}
- core economic question: {{QUESTION}}
- code lab paper or package: {{PAPER_OR_PACKAGE}}
- lab scope tier: {{Lite|Standard|Stretch}}

Constraints:
- Preserve the Bridge / Field Core / Research Lab structure.
- Do not invent citations or bibliography metadata.
- Use Python as the default lab language unless there is a strong reason otherwise.
- Keep slide content shorter than the chapter.
- Create the slide folder `books/{{BOOK}}/slides/week{{N}}/` before writing the deck.
- In markdown, use valid MyST inline math syntax by default: prefer `{math}`...``, allow `$...$` when simpler, and never use `\(...\)`.
- The lab must include a bounded reduced-data or synthetic-data pathway if the official package is heavy.
- Do not leave workflow wiring incomplete.

Required outputs:
1. `books/{{BOOK}}/{{WEEK_SLUG}}.md`
2. `books/{{BOOK}}/slides/week{{N}}/{{WEEK_SLUG}}.tex`
3. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/lab.md`
4. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/README.md`
5. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/run-log.md`
6. `books/{{BOOK}}/labs/{{WEEK_SLUG}}/smoke.sh`
7. bounded starter files under `original/`, `transfer/`, `src/`, `output/`, and `environment/`
8. updates to `books/{{BOOK}}/myst.yml`
9. updates to `books/{{BOOK}}/index.md`

Validation steps:
1. from `books/{{BOOK}}`, run `conda run -n research jupyter book build --html --strict`
2. from `books/{{BOOK}}`, run `conda run -n research --live-stream jupyter book start` and confirm that preview prints a `localhost` URL
3. from `books/{{BOOK}}`, run `conda run -n research latexmk -cd -pdf -interaction=nonstopmode slides/week{{N}}/{{WEEK_SLUG}}.tex`
4. from `books/{{BOOK}}/labs/{{WEEK_SLUG}}`, run `ENV_NAME=research bash smoke.sh`
5. summarize files changed and any remaining issues

Do not stop after drafting content. Finish the workflow wiring and validate all four checks before considering the week complete.
```
