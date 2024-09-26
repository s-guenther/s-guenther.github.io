---
layout: page
header: no
subheadline: "A storage supported tram system simulation for energy savings"
title:  "Tram System"
teaser: "A simulation framework to optimize tram network energy use, incorporating energy storage. The program allows scalable modeling, detailed energy calculations, timetable creation, and integration with MATLAB/Simulink libraries. External data management, optimization algorithms, and flexible storage placement make this a robust tool for energy savings in tram systems."
# meta_teaser: "Meta-Teaser String"
# breadcrumb: true
categories:
    - projects
image:
    thumb: "projects/tram_thumb.jpg"
    title: "projects/tram_wide.jpg"
---

The project involves the development and optimization of a MATLAB/Simulink/SimPowerSystems
program to simulate electrical tram networks, which is adaptable to other
networks such as factories that either operate with either AC or DC power. The system
is designed with modularity in mind, allowing for easy scalability, detailed
calculation of route energy requirements (accounting for height and curve
profiles), and flexible integration of Simulink libraries and block-based
construction for adjustments and improvements. 

Key features include the ability to optimize the placement and sizing of
flywheel energy storage systems, which enhance energy savings by storing and
discharging energy at appropriate times. The simulation is highly customizable,
offering adjustable simulation accuracy, external model generation via XML, and
effective post-processing of simulation data. The simulation allows for precise
timetable and load cycle creation in a tabular format and considers the
influence of energy sources, including substation positioning and the direction
of tram movement on either track. 

The project utilizes MATLAB functions to generate train schedules, manage
simulation data, and control the flow of information between SimPowerSystems and
external modules. It also automates the block and model generation in
Simulink/SimPowerSystems based on track and network data provided via XML,
ensuring seamless integration of electrical and mechanical models. This
high-level markup file approach simplifies the customization of complex track
systems. 

The placement and sizing of energy storage systems along the tram network are
optimized using external genetic and evolutionary algorithms, which interface
with MATLAB through XML. This design allows for flexible modifications and
enhancements, making the program a powerful tool for energy management in tram
systems. 

---

{% include next-previous-in-projects %}