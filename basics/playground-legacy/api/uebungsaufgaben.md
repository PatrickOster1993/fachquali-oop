
# Aufgaben zur Vertiefung des Wissens über APIs und `requests`

## Aufgabe 1: Senden einer einfachen GET-Anfrage

**Ziel:** Deine erste Anfrage an eine API senden und den Statuscode der Antwort auswerten.

**Aufgabe:**
1. Sende eine GET-Anfrage an die URL: `https://jsonplaceholder.typicode.com/posts/1`.
2. Überprüfe den Statuscode der Antwort und gib eine Nachricht aus, die anzeigt, ob die Anfrage erfolgreich war oder nicht (Nutze `response.status_code`).

**Hinweis:** Eine erfolgreiche Antwort hat den Statuscode **200**.

---
## Aufgabe 2: Arbeiten mit JSON-Daten und Pandas

**Ziel:** Eine API anfragen und die Antwortdaten mit Pandas in ein DataFrame umwandeln.

**Aufgabe:**
1. Sende eine GET-Anfrage an die URL: `https://jsonplaceholder.typicode.com/users`.
2. Verarbeite die Antwort mit `response.json()`, um die Daten in ein Python-Dictionary zu konvertieren.
3. Verwende `pandas`, um die JSON-Daten in ein DataFrame umzuwandeln (nur **id**-, **name**-, **username**- und **email**-Spalten erforderlich)
4. Gib das DataFrames in der Konsole aus, um die Struktur der erhaltenen Daten zu überprüfen.
---


## Aufgabe 3: Erstellen einer kleinen Klasse für API-Daten (OOP)

**Ziel:** Eine Klasse erstellen, die Daten von einer API abruft und in einer benutzerfreundlichen Art und Weise darstellt. Die Antwort wird als Pandas DataFrame gespeichert.

**Aufgabe:**
1. Erstelle eine Klasse `APIClient`, die folgende Attribute/Methoden hat:
   - **`getData(url)`**: Sendet eine GET-Anfrage an die übergebene URL und speichert die Antwort (= response)
   - **`getDict()`**: Gibt die Antwort im **Dictionary-Format** zurück, falls die Anfrage erfolgreich war.
   - **`getStatusCode()`**: Gibt den Statuscode der Antwort zurück.
   - **`showStructure()`**: Gibt die Struktur der Antwort im **Textformat** aus, damit du sehen kannst, wie der Aufbau der Daten strukturiert ist (Tipp: response.text).
   - **`dataFrame`**: Gibt die Antwortdaten als **Pandas DataFrame** zurück (Tipp: property verwenden).
2. Erstelle eine Instanz der Klasse und rufe die Methoden mit der URL `https://jsonplaceholder.typicode.com/posts` auf, um die Daten und den Statuscode zu erhalten.
3. Gib die Antwort im **Dictionary-Format** aus und zeige den Statuscode der Anfrage.
4. Nutze die Methode `showStructure()`, um die Struktur der Daten in der Konsole darzustellen.
5. Speichere die Antwort als Pandas DataFrame und gib die ersten 5 Zeilen des DataFrames aus.

>**Hinweis:** Achte darauf, Fehler zu behandeln, falls die Anfrage fehlschlägt (z.B. durch den Statuscode 404 oder 500).
---