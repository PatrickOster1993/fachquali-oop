
# **Aufgabe: Planeten-API mit Visualisierung**

## **Ziel**  
Erstelle eine Klasse, die Planeteninformationen von einer API abruft und die Daten visuell darstellt.

## **API**  
Nutze die Planeten-API:  
[https://api.le-systeme-solaire.net/rest/bodies/](https://api.le-systeme-solaire.net/rest/bodies/)

---

## **Klasse: `PlanetClient`**

1. **`fetchData()`**  
   - Lädt die Planeteninformationen von der API.  

2. **`dataFrame` (Property)**  
   - Gibt die heruntergeladenen Daten als Pandas DataFrame zurück.  

3. **`filterPlanets()`**  
   - Filtert nur die echten Planeten aus den Daten.
   >Tipp: Schauen Sie sich hierzu zunächst den Aufbau der Daten an! Wonach müssen Sie filtern?

4. **`plotPlanetRadii()`**  
   - Erstellt ein Balkendiagramm der Radii der Planeten. 
   >Tipp: Nutzen Sie **plt.bar()**

---

## **Praktische Schritte**

1. Instanziere die Klasse und lade die Daten mit `fetchData()`.  
2. Gib die Daten als DataFrame aus.  
3. Filtere die Planeten mit `filterPlanets()` und zeige die gefilterten Daten an.  
4. Visualisiere die Radii der Planeten mit `plotPlanetRadii()`.