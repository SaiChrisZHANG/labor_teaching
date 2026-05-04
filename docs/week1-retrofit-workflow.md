# Week 1 retrofit workflow

## What to edit first

For intellectual changes, edit:
- `books/labor-i/sources/01-labor-market-facts.md`

For direct content changes after the scholarly draft exists, edit only:
- `books/labor-i/01-labor-market-facts.md`
- `books/labor-i/slides/week1/01-labor-market-facts.tex`
- `books/labor-i/labs/01-labor-market-facts/lab.md`
- `books/labor-i/labs/01-labor-market-facts/src/*.py`

Do not edit:
- `_build/`
- generated PDFs
- generated lab outputs

## One-pass retrofit sequence

1. Review and adjust `books/labor-i/sources/01-labor-market-facts.md`.
2. Open the Week 1 retrofit prompt in `prompts/codex-week1-retrofit.md`.
3. Run the prompt in Codex from the repo root.
4. Review the rewritten chapter first.
5. If the chapter looks right, accept the synced slide and lab changes.
6. Validate locally.

## Local validation

From the repo root:

```bash
conda run -n research python books/labor-i/assets/scripts/generate_week1_facts.py   # if internet is available
make build BOOK=labor-i ENV=research
make slides BOOK=labor-i WEEK=01-labor-market-facts ENV=research
make lab-smoke BOOK=labor-i WEEK=01-labor-market-facts ENV=research
```

For live preview:

```bash
cd books/labor-i
conda run -n research --live-stream jupyter book start
```

## Minimum acceptance criteria

A Week 1 retrofit is acceptable only if:
- the chapter has real citations;
- the chapter has at least two labeled equations;
- the chapter includes at least one figure and two tables;
- slides reflect the revised chapter;
- the lab handout names the anchor paper and the transfer exercise;
- strict build, slide compile, and lab smoke all pass.
