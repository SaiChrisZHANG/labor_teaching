# Source Notes

The reproduce path is a bounded synthetic teaching analogue inspired by Bayer, Ross, and Topa [@bayerRossTopa2008]. The synthetic data contain workers, residential blocks, neighborhoods, employers, industries, tenure, wages, and next-period employment outcomes.

The raw economic object is a worker-employer and worker-neighborhood set of relations. The lab constructs local employer exposure by asking whether other workers in the same residential block or neighborhood work for the same employer. This is only a teaching object. It does not reproduce the confidential microdata, institutional setting, or estimates in the paper.

The data intentionally include:

- residential blocks nested in neighborhoods;
- employers with different sizes and industries;
- workers employed outside the observed local frame;
- group composition that creates homophily diagnostics;
- survey-response and missing-link-risk fields for measurement discussion;
- synthetic employment and wage outcomes that should be interpreted descriptively.

The lab's main lesson is that the same raw records support multiple plausible graphs. A worker-neighborhood-employer object, a worker-worker projection, and a neighborhood-employer bipartite table are related but not interchangeable.
