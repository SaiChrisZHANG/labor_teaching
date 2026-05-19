# Spatial Data Concepts Map

| Object | What it stores | Best for | Main risks |
|---|---|---|---|
| Point | Exact location of worker, firm, school, plant, event | Distance, routing, nearest-neighbor access, buffers | Geocoding error, confidentiality, false precision |
| Polygon | Tract, ZIP, county, municipality, school zone, commuting zone | Administrative linkage, policy exposure, neighborhood context | MAUP, ecological fallacy, arbitrary borders |
| Raster | Gridded surface like pollution, temperature, night lights, terrain | Environmental exposure, remote sensing, global comparability | Resolution mismatch, aggregation choice |
| Network | Roads, transit, commuting links, routes | Travel time, accessibility, bottlenecks, routing | Computational burden, mode assumptions, changing schedules |
| Panel geography | Repeated spatial units over time | Dynamic exposure, migration, policy timing | Boundary changes, crosswalk error, temporal mismatch |
