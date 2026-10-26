---
title: "Tram network with flywheel storage"
subheadline: "Rail simulation and optimisation"
summary: "I built a modular simulation model for tram networks that optimises the location and size of flywheel storage units."
weight: 50
aliases: ["../../projects/tram-system/"]   # old Jekyll URL
---

Trams brake electrically and generate energy in the process. If no other
vehicle takes it up, it is converted to heat in braking resistors. Storage
units along the line can absorb it. Where they should be placed and how
large they should be depends on the timetable and the network.

- **Setting:** research and development at TII Energy GmbH & Co. KG
  (flywheel storage)
- **Tools:** Matlab, Simulink, SimPowerSystems, XML

### My contribution

- A modular simulation model of the electrical rail network
- Automatic generation of the Simulink model from track and network data in
  XML
- Energy demand per track section from elevation and curve profiles
- Timetables and load cycles in tabular form, substation locations and the
  direction of travel on both tracks as inputs
- Adjustable simulation accuracy, automated evaluation of the simulation
  data
- Optimisation of storage location and size with evolutionary algorithms,
  coupled to the model via XML

### Outcome

- A simulation tool that transfers to other networks, such as AC or DC
  networks in industrial plants
