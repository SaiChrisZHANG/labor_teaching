Read these files first:
- `@AGENTS.md`
- `@books/labor-i/sources/01-labor-market-facts.md`
- `@shared/bibliography/references.bib`
- `@books/labor-i/01-labor-market-facts.md`
- `@books/labor-i/slides/week1/01-labor-market-facts.tex`
- `@books/labor-i/labs/01-labor-market-facts/lab.md`
- `@books/labor-i/labs/01-labor-market-facts/original/source-notes.md`
- `@books/labor-i/assets/tables/01-measurement-map.md`
- `@books/labor-i/assets/tables/01-roadmap-table.md`
- `@books/labor-i/assets/scripts/generate_week1_facts.py`

Goal: retrofit Week 1 from scaffold mode into source-first scholarly mode.

What to change:
1. Rewrite `books/labor-i/01-labor-market-facts.md` into a graduate-level chapter that follows the source pack.
2. Add frontmatter pointing to `../../shared/bibliography/references.bib`.
3. Use real citations from the existing BibTeX file only. Do not invent new bibliographic entries.
4. Add at least two labeled equations:
   - the labor-market accounting identity;
   - the composition decomposition linked to the Week 1 lab.
5. Insert at least:
   - one empirical figure;
   - two tables.
6. Use these table sources where helpful:
   - `books/labor-i/assets/tables/01-measurement-map.md`
   - `books/labor-i/assets/tables/01-roadmap-table.md`
7. If internet access is available locally, run `books/labor-i/assets/scripts/generate_week1_facts.py` and include the resulting figure in the chapter with a caption and label.
8. Update `books/labor-i/slides/week1/01-labor-market-facts.tex` so the slides reflect the revised chapter rather than the old scaffold.
9. Update `books/labor-i/labs/01-labor-market-facts/lab.md` so the lab handout explicitly names Daly and Hobijn, explains the reproduce/transfer logic, and aligns terminology with the revised chapter.
10. Do not redesign the repo structure.

Quality constraints:
- Preserve the Bridge / Field Core / Research Lab architecture.
- Make the prose concrete and field-like, not generic.
- Prefer fewer stronger claims with citations over many weak uncited claims.
- Keep Week 1 introductory, but unmistakably PhD-level.
- Distinguish measurement, description, mechanism, and identification clearly.
- In markdown, use valid MyST inline math syntax by default: prefer `{math}`...``, allow `$...$` when simpler, and never use `\(...\)`.

Validation:
1. Run the local asset-generation script if possible.
2. Run the strict book build from `books/labor-i`.
3. Compile the Week 1 slides.
4. Run the Week 1 lab smoke path.
5. Report files changed, outputs created, and any remaining warnings.
