Read @AGENTS.md, @README.md, @docs/labor-i-v0-freeze.md, @docs/github-publish-labor-i-v0.md, @books/labor-i/index.md, @books/labor-i/README.md, @books/labor-i/myst.yml, and the current Labor I files.

Goal: prepare the repository for a clean public Labor I version-0 freeze.

Tasks:
1. Verify that the Labor I landing page is concise and public-facing.
2. Check that generated artifacts such as `_build/` and LaTeX auxiliary files are ignored.
3. Summarize what is included in Labor I version 0.
4. If the repo is not already a git repository, initialize it.
5. Stage the repository and create a commit with message:
   `Freeze Labor I version 0`
6. Create an annotated git tag:
   `labor-i-v0`
7. Do **not** attempt to push unless GitHub credentials are already configured locally.
8. If GitHub CLI (`gh`) is available and authenticated, report the exact command needed to publish this repo publicly.
9. Report:
   - git status
   - latest commit hash
   - whether the tag exists
   - whether any files should be excluded before publishing

Constraints:
- Do not rewrite course content.
- Keep changes minimal and reviewable.
- Do not fabricate authentication or remote configuration.
