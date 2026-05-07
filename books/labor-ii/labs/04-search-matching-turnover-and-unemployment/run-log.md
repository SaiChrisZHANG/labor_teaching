# Run log

- Environment: `research`
- Date: `2026-05-05`
- Reproduction command:
  `conda run -n research python src/reproduce_hall_schulhofer_wohl.py --input original/reduced/hall_schulhofer_wohl_synthetic.csv --outdir output/reproduced`
- Transfer command:
  `conda run -n research python src/transfer_job_ladder_search.py --input transfer/data/job_ladder_scenarios.csv --outdir output/transfer`
- Smoke command:
  `ENV_NAME=research bash smoke.sh`
- Key outputs created:
  `output/reproduced/hall_schulhofer_wohl_decomposition.csv`,
  `output/reproduced/hall_schulhofer_wohl_matching.png`,
  `output/reproduced/hall_schulhofer_wohl_summary.csv`,
  `output/transfer/job_ladder_transition_summary.csv`,
  `output/transfer/job_ladder_market_summary.csv`,
  `output/transfer/job_ladder_transfer.png`
- Notes:
  bounded teaching path only; no confidential data required.
