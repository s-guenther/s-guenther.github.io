---
title: "Hybrid energy storage systems"
subheadline: "Sizing combined storage systems"
summary: "When does it pay to combine two storage technologies, and how large must they be? I investigated this question independently of a specific application: with optimisation models, simulation and parameter studies across more than 1,000 load profiles."
weight: 20
---

Hybrid storage systems combine two technologies, for example one for large
amounts of energy and one for high power. Their benefit had mostly been
shown in individual case studies. A general, application-independent
assessment was missing.

- **Setting:** Leibniz University Hannover, Institute of Electric Power
  Systems, Electrical Energy Storage Systems group
- **Status:** dissertation submitted and graded, defence at the end of
  November 2026
- **Tools:** Python, Pyomo, GLPK, IPOPT, pygmo, computing cluster with SLURM

### Content

- Theoretical sizing limits: when a hybrid storage system can be smaller
  than a single one
- A benchmark set of representative load profiles for unbiased comparisons
  (ESTSS)
- Representative energy management strategies derived from a meta-review
- Comparison of four strategy classes (filter, deadzone, MPC and fuzzy
  logic based) in about 10,000 configurations: typically 3 to 10 %
  oversizing compared with a reference with perfect forecast. Sizing and
  strategy design can be separated with little loss
- Effect of efficiency and self-discharge in more than 800,000 parameter
  configurations: compared with a loss-equivalent single storage system,
  sizing gains rarely exceed 3 %, while losses are often reduced by more
  than 20 %. Statistically, both are best explained by the coefficient of
  variation of the load profile (correlation ≈ 0.9)

### Outcome

- Dissertation: *Hybrid energy storage systems: a generalized quantitative
  analysis with a focus on system sizing*
- Six journal articles as first author, open-source software and data: see
  [About]({{< ref "about" >}})
