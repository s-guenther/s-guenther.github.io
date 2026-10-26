---
title: "Tram network with flywheel storage"
subheadline: "Rail simulation and optimisation"
summary: "Braking trams feed back energy that is often lost without storage. A modular simulation model for tram networks makes it possible to optimise the location and size of flywheel storage units."
weight: 50
---

- **Setting:** research and development at TII Energy GmbH & Co. KG
  (flywheel storage)
- **Tools:** Matlab, Simulink, SimPowerSystems, XML

### Implementation

- A modular simulation model of the electrical rail network
- Automatic generation of the Simulink model from track and network data in
  XML
- Timetables, elevation and curve profiles and substation locations as
  inputs
- Optimisation of storage location and size with evolutionary algorithms,
  coupled to the model via XML

### Outcome

- A simulation tool that transfers to other networks, such as AC or DC
  networks in industrial plants
