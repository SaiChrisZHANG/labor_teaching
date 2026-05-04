WEEK ?= 01-labor-market-facts
WEEK_NUM := $(shell printf '%s\n' "$(WEEK)" | sed -E 's/^0*([1-9][0-9]*)[-_].*/\1/')

preview:
	conda run -n research --live-stream jupyter book start

build:
	conda run -n research jupyter book build --html --strict

clean:
	conda run -n research jupyter book clean --templates --cache -y

slides:
	conda run -n research latexmk -cd -pdf -interaction=nonstopmode slides/week$(WEEK_NUM)/$(WEEK).tex
