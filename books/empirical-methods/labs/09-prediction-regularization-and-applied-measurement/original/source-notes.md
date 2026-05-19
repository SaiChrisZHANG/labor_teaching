# Source Notes

The reduced posting file is a deterministic synthetic dataset inspired by applied economics work that uses machine learning to structure job postings and related text data [@dahlhausFromOnlineJob2025; @turrellTransformingNaturallyOccurring2019].

It is not an official replication file. It does not contain proprietary posting data, platform data, hand labels, or paper-specific replication inputs.

The teaching target is `technology_intensive`, a binary label indicating whether a posting is designed to represent a technology-intensive vacancy. The model may use posting text, year, sector, region, firm size, and a contemporaneous remote-signal variable. The column `future_verified_skill_tag` is intentionally included as a leakage example and should be excluded from prediction features because it is post-outcome verification metadata.
