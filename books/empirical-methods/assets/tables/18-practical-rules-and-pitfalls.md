### Practical rules and pitfalls

#### Practical rules
1. Begin from the economic mechanism, then define the graph.
2. State node, edge, direction, weight, timing, and boundary choices explicitly.
3. Show at least one robustness check to alternative network definitions.
4. Prefer the raw bipartite object when it is closer to the economic process.
5. Distinguish “missing link” from “zero link” wherever possible.
6. Keep privacy constraints explicit; network anonymization is harder than row-level anonymization.

#### Main pitfalls
- **Boundary choice**: your graph may be truncated by school, city, firm, or survey frame.
- **Projection error**: one-mode projections can inflate density and create artificial exposure.
- **Dynamic mismatch**: outcome timing and link timing may not align.
- **Selection**: networks are often jointly determined with outcomes.
- **Over-interpretation**: degree or centrality are descriptive until the mechanism is defended.
