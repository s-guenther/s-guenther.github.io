---
title: "Tram network with flywheel storage"
summary: "**[TODO: setting, year]**. Simulation of a tram network in Matlab/Simulink and optimisation of location and size of flywheel storage units."
weight: 50
---

**Setting:** **[TODO]** · **Period:** **[TODO]** · **Tools:** Matlab,
Simulink, SimPowerSystems, XML

The aim was to reduce the energy demand of a tram network by storing braking
energy in flywheel storage units.

I built a modular simulation model of the electrical network. Track and
network data are described in XML, from which the program generates the
Simulink model automatically. Timetables, elevation and curve profiles and
the location of substations enter the calculation. Location and size of the
storage units were optimised with external evolutionary algorithms coupled to
the model via XML.
