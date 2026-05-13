# Transfer Notes

The transfer step is inspired by Notowidigdo on local labor-demand incidence. It uses synthetic data and does not claim to reproduce official estimates.

Run:

```bash
conda run -n research python src/transfer_notowidigdo_incidence.py
```

The script reads `transfer/data/local_demand_shocks_synthetic.csv` and writes outputs under `output/transfer/`.

