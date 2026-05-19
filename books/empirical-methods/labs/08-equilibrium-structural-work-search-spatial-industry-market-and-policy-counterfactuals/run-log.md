# Week 8 lab run log

This file records the intended local run path for the Week 8 lab.

```bash
ENV_NAME=research bash smoke.sh
```

Expected stages:

1. `src/make_synthetic_data.py` writes deterministic spatial and market teaching data.
2. `src/reproduce_spatial_equilibrium.py` solves the spatial-equilibrium reproduce/diagnose path.
3. `src/transfer_market_equilibrium.py` runs the market-equilibrium transfer path.

The generated outputs are teaching artifacts and should not be interpreted as published replication magnitudes.
