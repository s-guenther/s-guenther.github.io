---
title: "Straßenbahnnetz mit Schwungradspeichern"
slug: "strassenbahn"
subheadline: "Bahnnetz-Simulation und Optimierung"
summary: "Ich habe ein modulares Simulationsmodell für Straßenbahnnetze aufgebaut, mit dem sich Lage und Größe von Schwungradspeichern optimieren lassen."
weight: 50
---

Straßenbahnen bremsen elektrisch und erzeugen dabei Energie. Nimmt kein
anderes Fahrzeug sie auf, wird sie in Bremswiderständen in Wärme
umgewandelt. Speicher an der Strecke können sie aufnehmen. Wo sie stehen
und wie groß sie sein sollten, hängt von Fahrplan und Netz ab.

- **Rahmen:** Forschung und Entwicklung bei der TII Energy GmbH & Co. KG
  (Schwungradspeicher)
- **Werkzeuge:** Matlab, Simulink, SimPowerSystems, XML

### Mein Beitrag

- Modulares Simulationsmodell des elektrischen Bahnnetzes
- Automatische Erzeugung des Simulink-Modells aus Strecken- und Netzdaten
  in XML
- Energiebedarf je Streckenabschnitt aus Höhen- und Kurvenprofil
- Fahrpläne und Lastzyklen in Tabellenform, Lage der Unterwerke und
  Fahrtrichtung auf beiden Gleisen als Eingangsgrößen
- Einstellbare Rechengenauigkeit, automatisierte Auswertung der
  Simulationsdaten
- Optimierung von Lage und Größe der Speicher mit evolutionären
  Algorithmen, über XML an das Modell gekoppelt

### Ergebnis

- Simulationswerkzeug, das sich auf andere Netze übertragen lässt, etwa auf
  Gleich- oder Wechselstromnetze in Industrieanlagen
