ENV ?= research
BOOK ?= labor-i
WEEK ?= 01-labor-market-facts

.PHONY: help preview build clean slides lab-smoke week-check

help:
	@echo "Usage: make <target> BOOK=<book-slug> WEEK=<week-slug> ENV=<conda-env>"
	@echo ""
	@echo "Targets:"
	@echo "  preview    Start the local Jupyter Book preview server"
	@echo "  build      Build the selected book with strict checks"
	@echo "  clean      Clean cached Jupyter Book templates and responses"
	@echo "  slides     Compile the selected week's Beamer slides"
	@echo "  lab-smoke  Run the selected week's lab smoke test"
	@echo "  week-check Run build + slides + lab smoke in sequence"
	@echo ""
	@echo "Example: make week-check BOOK=labor-i WEEK=01-labor-market-facts ENV=research"

preview:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/book_preview.sh

build:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/book_build_strict.sh

clean:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/book_clean.sh

slides:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/slides_build.sh

lab-smoke:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/lab_smoke.sh

week-check:
	@ENV_NAME=$(ENV) BOOK=$(BOOK) WEEK=$(WEEK) bash scripts/week_check.sh
