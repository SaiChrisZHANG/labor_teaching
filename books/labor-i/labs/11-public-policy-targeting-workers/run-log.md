# Run Log

- Environment: `research`
- Default smoke path:
  1. `python src/build_week11_synthetic_data.py`
  2. `python src/reproduce_chetty_friedman_saez.py --input original/reduced/chetty_friedman_saez_knowledge_synthetic.csv --outdir output/reproduced`
  3. `python src/transfer_linos_takeup.py --input transfer/data/linos_eitc_nudge_synthetic.csv --outdir output/transfer`
