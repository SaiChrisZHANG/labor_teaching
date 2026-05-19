# Transfer Data Notes

The transfer dataset is a stylized place-by-sector shift-share design.

- `shift_share_places.csv` contains places, regions, baseline growth, treatment intensity, outcome growth, and baseline sector shares.
- `sector_shocks.csv` contains national sector shocks.
- The shift-share instrument is `sum_s share_{place,s} * shock_s`.

The synthetic design deliberately gives some places concentrated exposure and lets baseline shares correlate with pre-period growth. Students should therefore treat the exercise as a diagnostic task, not as a clean causal estimate.
