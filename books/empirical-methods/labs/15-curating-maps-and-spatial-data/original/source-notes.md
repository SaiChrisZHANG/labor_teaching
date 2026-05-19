# Source Notes

The reproduce task is inspired by commuting-zone exposure work in applied labor economics, especially the logic of assigning industry shocks to functional local labor markets. The synthetic data are not an extract from a real replication package.

Generated files:

- `tract_sector_employment_synthetic.csv`: tract-level baseline sector employment, geography identifiers, coordinates, geocoding-quality fields, and a synthetic employment-growth outcome.
- `sector_trade_shocks_synthetic.csv`: sector-level shocks used to construct baseline-weighted local exposure.
- `boundary_crosswalk_synthetic.csv`: a many-to-many teaching crosswalk with area, population, and employment weights for selected split tracts.

Key teaching simplifications:

- Coordinates are planar synthetic coordinates, not latitude/longitude.
- Commuting zones and counties are stylized and intentionally imperfectly aligned.
- The outcome is generated from the synthetic exposure plus noise; it is included only so students can see how measurement choices affect downstream descriptive slopes.
- Crosswalk weights are synthetic and should be interpreted as examples of the logic, not official geography files.
