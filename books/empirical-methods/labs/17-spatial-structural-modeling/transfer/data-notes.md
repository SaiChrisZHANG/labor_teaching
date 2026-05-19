# Transfer Data Notes

The transfer task is inspired by Greaney, Parkhomenko, and Van Nieuwerburgh on dynamic urban economics [@GreaneyParkhomenkoVanNieuwerburgh2025].

The synthetic policy file contains:

- `shock_location_id`: the location receiving the productivity shock;
- `productivity_multiplier`: the size of the shock;
- `periods`: the number of transition periods;
- `migration_adjustment_speed`: how quickly residence and workplace allocation move toward the long-run equilibrium;
- `housing_adjustment_speed`: how quickly rents move toward the long-run equilibrium.

The exercise is intentionally modest. It compares a static long-run equilibrium with a transition path. A frontier dynamic model would add forward-looking households, tenure, durable housing, investment, expectations, and a richer state space.
