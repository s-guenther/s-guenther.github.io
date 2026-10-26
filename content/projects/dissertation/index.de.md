---
title: "Hybride Energiespeichersysteme"
slug: "promotion"
subheadline: "Auslegung kombinierter Speicher"
summary: "Wann lohnt es sich, zwei Speichertechnologien zu kombinieren, und wie groß müssen sie sein? Ich habe diese Frage anwendungsunabhängig untersucht: mit Optimierungsmodellen, Simulation und Parameterstudien über mehr als 1.000 Lastprofile."
weight: 20
---

Hybride Speicher verbinden zwei Technologien, etwa eine für viel Energie und
eine für hohe Leistung. Ihr Nutzen wurde bisher meist an Einzelfällen
gezeigt. Eine allgemeine, anwendungsunabhängige Bewertung fehlte.

- **Rahmen:** Leibniz Universität Hannover, Institut für Elektrische
  Energiesysteme, Fachgebiet Elektrische Energiespeichersysteme
- **Stand:** Dissertation eingereicht und begutachtet, Disputation Ende
  November 2026
- **Werkzeuge:** Python, Pyomo, GLPK, IPOPT, pygmo, Rechencluster mit SLURM

### Inhalt

- Theoretische Auslegungsgrenzen: wann ein Hybridspeicher kleiner ausfallen
  kann als ein Einzelspeicher
- Benchmark-Satz repräsentativer Lastprofile für unverzerrte Vergleiche
  (ESTSS)
- Repräsentative Energiemanagementstrategien, abgeleitet aus einer
  Meta-Review
- Vergleich von vier Strategieklassen (filter-, totband-, MPC- und
  Fuzzy-basiert) in rund 10.000 Konfigurationen: gegenüber einer Referenz
  mit perfekter Vorhersage typischerweise 3 bis 10 % Überdimensionierung.
  Auslegung und Strategieentwurf lassen sich mit geringem Verlust trennen
- Einfluss von Wirkungsgrad und Selbstentladung in über 800.000
  Parameterkonfigurationen: gegenüber einem verlustäquivalenten
  Einzelspeicher selten mehr als 3 % Größenvorteil, aber oft über 20 %
  weniger Verluste. Beides lässt sich statistisch am besten durch den
  Variationskoeffizienten des Lastprofils erklären (Korrelation ≈ 0,9)

### Ergebnis

- Dissertation: *Hybrid energy storage systems: a generalized quantitative
  analysis with a focus on system sizing*
- Sechs Fachartikel als Erstautor, quelloffene Software und Daten: siehe
  [Über mich]({{< ref "about" >}})
