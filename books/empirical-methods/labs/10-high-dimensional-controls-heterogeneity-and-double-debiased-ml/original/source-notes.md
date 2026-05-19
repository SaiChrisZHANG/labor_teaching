# Source Notes

The reduced online labor file is a deterministic synthetic dataset inspired by applied economics work on online labor markets and double machine learning [@dubeMonopsonyOnlineLabor2020; @chernozhukovDoubleDebiasedMachine2018].

It is not an official replication file. It does not contain platform data, worker records, client identities, proprietary wage data, or paper-specific replication inputs.

The teaching target is the effect of `high_client_concentration` on `log_hourly_wage`. The pre-treatment controls include worker experience, completed tasks, rating, prior wages, market thickness, local unemployment, occupation, region, skill score, and repeat-client share. The column `future_client_rating` is intentionally included as a leakage example and should be excluded because it is realized after the treatment environment and wage outcome.
