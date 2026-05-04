# Run Log

- Environment: `research`
- Default smoke path:
  1. `python src/build_week10_synthetic_data.py`
  2. `python src/reproduce_van_doornik_credit_lottery.py --input original/reduced/van_doornik_credit_lottery_synthetic.csv --outdir output/reproduced`
  3. `python src/transfer_beerli_migration_exposure.py --input transfer/data/beerli_open_border_synthetic.csv --outdir output/transfer`
