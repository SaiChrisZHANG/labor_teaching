# Source Notes

The reduced source file is a deterministic synthetic job-posting dataset inspired by applied economics work that uses vacancy text to construct remote-work and task-related economic measures [@hansenRemoteWorkAcross2023; @gentzkowKellyTaddy2019].

It is not an official replication file. It does not contain proprietary vacancy data, platform records, hand labels, or paper-specific replication inputs.

The teaching target is `remote_label`, a binary label indicating whether a posting is designed to represent a job that can be performed remotely or in a hybrid remote arrangement. The model may use posting text, sector, region, job family, year, and firm size. The column `future_remote_badge` is intentionally included as a leakage example and should be excluded because it is generated after the intended measurement point.
