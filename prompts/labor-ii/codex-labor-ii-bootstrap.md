Read @AGENTS.md, @docs/repo-workflow.md, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-i/index.md, and the existing Labor I week-generation prompts.

Goal: bootstrap Labor II so it follows the same validated workflow as Labor I.

Tasks:
1. Verify that Labor II has the minimum standalone book structure.
2. If any standard directories are missing, create them:
   - `books/labor-ii/sources/`
   - `books/labor-ii/slides/`
   - `books/labor-ii/labs/`
   - `books/labor-ii/assets/figures/`
   - `books/labor-ii/assets/tables/`
   - `books/labor-ii/assets/scripts/`
3. Keep the same conventions:
   - slides live in `books/labor-ii/slides/weekN/`
   - local workflow uses the `research` conda environment
   - markdown uses valid MyST math syntax
4. Do not draft Week 1 yet.
5. End by reporting the exact file structure Labor II now has and what the next Week-1 source-pack prompt should build.

Constraints:
- Keep changes minimal.
- Do not rewrite the Labor II outline.
- Follow the Labor I workflow rather than inventing a new one.
