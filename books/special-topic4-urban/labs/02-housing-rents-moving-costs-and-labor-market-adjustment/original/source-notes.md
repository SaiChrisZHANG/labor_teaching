# Source Notes

## Verified Anchor

- **Article:** Hsieh, Chang-Tai and Enrico Moretti. 2019. "Housing Constraints and Spatial Misallocation." *American Economic Journal: Macroeconomics* 11(2): 1-39.
- **Course citation:** [@hsiehMoretti2019HousingConstraints]
- **Replication source status:** The course manual review identifies a public openICPSR package for the Hsieh-Moretti paper. The package itself is not included in this repository.

## Reduced Teaching Object

The reduced reproduction approximates a city-level adjustment object:

```{math}
\Delta Y_\ell =
\left(
\Delta w_\ell,\,
\Delta R_\ell,\,
\Delta N_\ell,\,
\Delta E_\ell,\,
\Delta C_\ell,\,
\Delta P_\ell
\right).
```

The local CSV is designed to help students classify whether a productive place mainly adjusts through rents and prices, population and employment, commuting, or reduced real access. It is useful for teaching the paper architecture, not for recovering published numerical estimates.

## What The Full Official Package Would Add

The official package would conceptually add the paper's actual data construction, calibration or quantitative steps, exact sample definitions, official code order, robustness checks, and publication tables. Students should use the local path first to understand the objects, then use the official materials only when the course wants a closer replication.

## Cautions

- The reduced data are synthetic pedagogical placeholders.
- The output magnitudes should not be cited as evidence about actual cities.
- The local Python path preserves the logic of housing constraints and misallocation, not the full structural model.
- Any closer replication should document package version, run order, software requirements, and divergences from published results.
