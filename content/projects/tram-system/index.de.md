---
title: "Straßenbahnnetz mit Schwungradspeichern"
slug: "strassenbahn"
subheadline: "Projekt [TODO: Rahmen]"
summary: "Simulation eines Straßenbahnnetzes in Matlab/Simulink und Optimierung von Lage und Größe von Schwungradspeichern."
weight: 50
---

**Rahmen:** **[TODO]** · **Zeitraum:** **[TODO]** · **Werkzeuge:**
Matlab, Simulink, SimPowerSystems, XML

Ziel war, den Energiebedarf eines Straßenbahnnetzes zu senken, indem
Bremsenergie in Schwungradspeichern zwischengespeichert wird.

Ich habe ein modulares Simulationsmodell des elektrischen Netzes aufgebaut.
Strecken- und Netzdaten werden in XML beschrieben, daraus erzeugt das
Programm das Simulink-Modell automatisch. Fahrpläne, Höhen- und
Kurvenprofile sowie die Lage der Unterwerke gehen in die Berechnung ein.
Lage und Größe der Speicher wurden mit externen evolutionären Algorithmen
optimiert, die über XML an das Modell angebunden sind.
