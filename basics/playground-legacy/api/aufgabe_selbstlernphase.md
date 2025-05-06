
# Aufgabe: Wetterdaten-API mit Visualisierung

**Ziel:** Erstelle eine Klasse, die Wetterdaten von einer API abruft, benutzerfreundlich darstellt und diese Daten visuell aufbereitet.

---

## Aufgabenbeschreibung

Erstelle eine Klasse `WeatherClient`, die folgende Attribute und Methoden besitzt:

### Attribute/Methoden

1. **`fetchData(city)`**
   - Sendet eine Anfrage an die Wetter-API mit dem übergebenen Stadtnamen.
   - Die Daten werden in einem internen Attribut gespeichert.
   - *Nutze z. B. die API:*
     ```
     https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max&timezone=auto
     ```
     *(für Berlin)*

2. **`dataDict`** (Property)
   - Gibt die Antwortdaten im Dictionary-Format zurück.

3. **`status`** (Property)
   - Gibt den HTTP-Statuscode der Anfrage zurück.

4. **`showWeather()`**
   - Gibt die Temperaturdaten (z. B. die maximalen Tagestemperaturen der nächsten Woche) im Konsolenformat aus.

5. **`dataFrame`** (Property)
   - Gibt die Daten als Pandas DataFrame zurück.

6. **`plotWeather()`**
   - Visualisiert die Temperaturdaten als Liniendiagramm (z. B. Temperatur über die Zeit mit Matplotlib).

---

## Praktische Schritte

1. **Instanziere die Klasse** und führe die folgenden Schritte aus:
   - Rufe die Methode `fetchData()` für Berlin auf.
   - Gib die Wetterdaten im Dictionary-Format und den Statuscode aus.
   - Nutze `showWeather()`, um die Daten in der Konsole anzuzeigen.
   - Erstelle den DataFrame und gib die ersten Zeilen aus.
   - Erstelle eine Visualisierung der Temperaturen mit `plotWeather()`.

---

## Hinweis

- Achte darauf, Fehler zu behandeln, falls die Anfrage fehlschlägt (z. B. bei Statuscodes 404 oder 500).
- Nutze Bibliotheken wie `requests`, `pandas` und `matplotlib`.
- Falls ihr mehrere Städte vergleichen möchtet, könnt ihr später eine Methode `compareWeather(city1, city2)` hinzufügen.

---

## Erwartete Visualisierung

Das Diagramm sollte die Tagesdaten auf der X-Achse und die maximalen Temperaturen auf der Y-Achse zeigen. Beschrifte die Achsen und füge einen passenden Titel hinzu (z. B. "Maximale Temperaturen in Berlin").

---

## Zusatzaufgabe (optional)

1. Füge die Möglichkeit hinzu, Wetterdaten für mehrere Städte abzurufen und diese in einem Diagramm zu vergleichen.
2. Speichere das Diagramm mit `plt.savefig()` als Bilddatei.