# Run Log

Use this file to record local lab runs.

## Smoke Test

Command:

```bash
ENV_NAME=research bash smoke.sh
```

Expected result:

- synthetic original data are written under `original/reduced/`;
- synthetic transfer data are written under `transfer/data/`;
- reproduce outputs are written under `output/reproduced/`;
- transfer outputs are written under `output/transfer/`.
