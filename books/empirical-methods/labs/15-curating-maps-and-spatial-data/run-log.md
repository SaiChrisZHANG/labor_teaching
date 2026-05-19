# Week 15 lab run log

Use this file to record local runs, outputs inspected, and any deviations from the bounded teaching path.

## Canonical smoke command

```bash
ENV_NAME=research bash smoke.sh
```

## Expected generated outputs

- `original/reduced/tract_sector_employment_synthetic.csv`
- `original/reduced/sector_trade_shocks_synthetic.csv`
- `original/reduced/boundary_crosswalk_synthetic.csv`
- `transfer/data/residential_tracts_synthetic.csv`
- `transfer/data/workplace_centers_synthetic.csv`
- `output/reproduced/cz_exposure.csv`
- `output/reproduced/tract_exposure_assignment.csv`
- `output/reproduced/county_vs_cz_exposure.csv`
- `output/reproduced/downstream_comparison.csv`
- `output/reproduced/maup_sensitivity.csv`
- `output/reproduced/crosswalk_weighting_sensitivity.csv`
- `output/reproduced/geocoding_jitter_sensitivity.csv`
- `output/reproduced/boundary_edge_audit.csv`
- `output/transfer/job_access_measures.csv`
- `output/transfer/access_group_comparison.csv`
- `output/transfer/buffer_vs_kernel_access.csv`
- `output/transfer/edge_effect_audit.csv`

## Notes

- The smoke path uses deterministic synthetic data.
- No live geocoding service, proprietary shapefile, or routing API is called.
- Treat non-fatal environment warnings as acceptable only if the required outputs are created.
