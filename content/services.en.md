---
# Interim text; final wording in front (a), see todo_relaunch.md
title: "Services"
# Tiles on the home page ({{< tiles >}}): title, text, image (path in
# assets/), and the subheading on this page they link to (the {#...} ids
# below).
tiles:
  - title: "Research software"
    text: "Software for modelling, simulation and analysis that turns scientific methods into usable tools."
    image: "img/services/tile-research-software.jpg"
    anchor: "research-software"
  - title: "Scientific computing"
    text: "Models, simulations and optimisation for energy systems and energy storage, from sizing to the evaluation of large parameter studies."
    image: "img/services/banner.jpg"
    anchor: "scientific-computing"
  - title: "Hardware prototyping"
    text: "Design and construction of mechatronic prototypes and test rigs, including control and data acquisition."
    image: "img/services/tile-hardware-prototyping.jpg"
    anchor: "hardware-prototyping"
---

![Inside a computer: mainboard, processor and graphics card](img/services/banner.jpg)
{.sg-page-banner}

I apply methods from research to a company's concrete questions and deliver
the result as a usable tool: as software, as a calculation with a traceable
report, or as a working prototype. The three areas often work together: a
model becomes software, a simulation accompanies a prototype.

## Research software {#research-software}

Many technical questions are answered with spreadsheets, scripts or one-off
calculations that are hard to trace, extend or apply to new cases later. I
turn them into tools that make exactly this possible: I port existing Excel
or Matlab calculations to Python, implement models and algorithms from the
literature or from your own development, and use version control,
documentation and tests so the software can be maintained and handed over.

Examples: [storage sizing for wind farms]({{< ref "projects/wind-farm" >}})
and open-source software on hybrid energy storage (see
[About]({{< ref "about" >}})).

## Scientific computing {#scientific-computing}

I answer technical and economic questions with mathematical models: Which
storage size, technology and operating strategy suit a given load or
generation profile? How much load can be shifted in time, and what is it
worth? What do existing measurement, operating and time-series data show?
For this I formulate optimisation problems (linear and nonlinear), simulate
operating strategies and run parameter studies with many variants, on a
computing cluster if needed.

Examples: [assessing flexibility potential]({{< ref "projects/flexibility" >}}),
[hybrid energy storage systems]({{< ref "projects/dissertation" >}}),
[energy-plus neighbourhood]({{< ref "projects/residential-area" >}}).

## Hardware prototyping {#hardware-prototyping}

When an idea has to be tested on real hardware, I design and build
prototypes and test rigs: mechanical design with 3D model and drawings,
sizing of bearings, drives and gears, estimates of thermal behaviour and
rotor dynamics, motor control and automation of measurement sequences.

Examples: [flywheel storage prototype]({{< ref "projects/flywheel" >}}),
[NC rotary table for a laser scanning vibrometer]({{< ref "projects/rotary-table" >}}).

## Tools

Python (NumPy, Pyomo), mathematical optimisation (GLPK, IPOPT, pygmo),
Matlab/Simulink, statistics and time-series analysis, Git, Linux, computing
clusters with SLURM, 3D mechanical design. More detail under
[About]({{< ref "about" >}}).

## Two ways of working together {#zusammenarbeit}

**An assignment with a defined result.** We agree on question, scope and
deliverables up front. You receive report, source code and documentation,
so the results can be traced and reproduced.

**Support for your project team.** During workload peaks I join your team
temporarily, for an agreed period and scope.

## How it works

1. A short, non-binding conversation about the question.
2. An offer stating scope, deliverables and effort.
3. The work itself, with interim results.
4. Handover of results, source code and documentation.

## What I do not offer

Standard designs for which specialised providers exist, such as PV systems
for houses or air conditioning for office buildings.
