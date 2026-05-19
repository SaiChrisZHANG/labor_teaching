# Transfer Data Notes

The transfer data mimic a stylized metro area with residential tracts and workplace centers.

Generated files:

- `residential_tracts_synthetic.csv`: residential tract coordinates, resident counts, transit-dependence indicators, demographic composition, and geocoding-quality fields.
- `workplace_centers_synthetic.csv`: workplace center coordinates, job counts, sector labels, and whether the center is suburban or outside the study-area frame.

The travel-time object in the transfer script is a deterministic teaching surrogate:

```text
travel time = fixed cost + distance slope + transit penalty + suburban penalty
```

In a real project, the researcher would need to record routing source, route mode, departure time, network vintage, API version, missing-route rules, and whether travel times correspond to the period of the outcome.
