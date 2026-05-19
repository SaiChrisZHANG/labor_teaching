# Transfer Data Notes

`transfer/data/synthetic_control_city.csv` is created by `src/make_synthetic_data.py`.

The unit is a city-year. `Bay City` is treated beginning in 2016. Other cities form the donor pool. The outcome is a synthetic employment-placement index. The data are designed so that a weighted donor combination fits Bay City well before treatment and diverges after treatment.

This is a teaching path, not an official replication package. Students should focus on design questions:

- Is the donor pool credible?
- Does the synthetic path fit before treatment?
- Are post-treatment gaps large relative to placebo gaps?
- What population, if any, can this single-city estimate speak for?
