# Standard repo workflow

This repository uses one standard workflow for every weekly module. The point is to make new weeks predictable for both humans and Codex.

## Core rule

Every new week should be a complete package with four connected pieces:

1. a book chapter in `books/<book>/<week-slug>.md`
2. a Beamer deck in `books/<book>/slides/weekN/<week-slug>.tex`
3. a code lab in `books/<book>/labs/<week-slug>/`
4. a smoke test in `books/<book>/labs/<week-slug>/smoke.sh`

For example, Week 1 for Labor I uses:

- source: `books/labor-i/slides/week1/01-labor-market-facts.tex`
- compiled PDF: `books/labor-i/slides/week1/01-labor-market-facts.pdf`

In addition, every new week must be wired into the book navigation by updating:

- `books/<book>/myst.yml`
- `books/<book>/index.md`

## Standard commands

The standalone Jupyter Book root for each course is `books/<book>`.

Canonical local build and preview commands should use the `research` conda environment. Run them from the book folder unless a wrapper says otherwise.

### Preview the book locally

```bash
cd books/labor-i
conda run -n research --live-stream jupyter book start
```

The preview check passes when the server starts and prints a `localhost` URL.

### Build the book with strict checks

```bash
cd books/labor-i
conda run -n research jupyter book build --html --strict
```

### Clean template and cache state

```bash
cd books/labor-i
conda run -n research jupyter book clean --templates --cache -y
```

### Compile one week's slides

Slide compilation depends on a local TeX toolchain with `latexmk`.

```bash
cd books/labor-i
conda run -n research latexmk -cd -pdf -interaction=nonstopmode slides/week2/02-static-labor-supply.tex
```

The `-cd` flag is the canonical safeguard: it makes `latexmk` compile from the slide source directory so the `.pdf`, `.aux`, `.nav`, `.log`, and related artifacts stay in `books/<book>/slides/weekN/` next to the `.tex` source instead of spilling into `books/<book>/`.

### Run one week's lab smoke test

Every weekly lab must include `smoke.sh`.

```bash
cd books/labor-i/labs/01-labor-market-facts
ENV_NAME=research bash smoke.sh
```

### Run the full weekly quality check

You can still use the repository `Makefile` wrappers from the repo root when convenient:

```bash
make week-check BOOK=labor-i WEEK=01-labor-market-facts ENV=research
```

## What each command is expected to do

- `preview` starts the local Jupyter Book preview server for the selected book and should print a `localhost` URL.
- `build` runs a strict HTML build for the selected book.
- `clean` clears cached template and web-response state when preview/build behavior gets weird.
- `slides` compiles the selected week's Beamer source with `latexmk` from the local TeX installation.
- Markdown inline math in chapter, source-pack, and lab handout `.md` files should use valid MyST syntax: prefer `{math}`...``, allow `$...$` when simpler, and never use `\(...\)`.
- `lab-smoke` runs the lab's reduced-data or synthetic-data pathway.
- `week-check` runs `build`, `slides`, and `lab-smoke` in sequence.

Non-fatal Node or font warnings may be acceptable during preview, build, or slide compilation if the required outputs are still produced successfully.

## Week-level file contract

Each weekly lab folder should contain at least:

```text
books/<book>/labs/<week-slug>/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
  transfer/
    README.md
    data-notes.md
  src/
    reproduce_*.py|R|do
    transfer_*.py|R|do
  output/
    reproduced/
    transfer/
```

The smoke test should only verify the bounded teaching path. It should not require proprietary data or a full official replication package unless the course explicitly ships those files.

## Notes on environment handling

The canonical local environment is `research`.

If you are running direct commands, prefer `conda run -n research ...`.

If you already activated the environment manually, document that explicitly and keep using the same environment consistently:

```bash
conda activate research
cd books/labor-i
jupyter book build --html --strict
```

The repository shell wrappers and `make` targets also default to `ENV=research` and fall back to `conda run` automatically when the active environment does not match.

## When Codex creates a new week

A new weekly module is not done until Codex has:

1. created the chapter file
2. created the slide deck
3. created the lab folder
4. added `smoke.sh`
5. updated `myst.yml`
6. updated `index.md`
7. placed the slide source at `books/<book>/slides/weekN/<week-slug>.tex`
8. run a strict HTML build from `books/<book>`
9. start preview from `books/<book>` and confirm a printed `localhost` URL
10. run slide compilation for the week
11. run `smoke.sh` for the week's lab
12. reported any remaining issues clearly
