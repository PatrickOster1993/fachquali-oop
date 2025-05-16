
# Einführung in APIs

## Was ist eine API?

Eine **API (Application Programming Interface)** ist eine Sammlung von Regeln und Definitionen, die es Softwareanwendungen ermöglichen, miteinander zu kommunizieren. Sie dient als **Schnittstelle, über die Programme miteinander Daten austauschen** oder bestimmte Funktionen anfordern können, ohne die interne Funktionsweise der anderen Anwendung zu kennen.

## Beispiel einer API

Stell dir vor, eine API ist wie ein Kellner in einem Restaurant. Du gibst deine Bestellung (Anfrage) an den Kellner (API), der diese Anfrage an die Küche (Server) weitergibt und dir das Essen (Antwort) zurückbringt. Der Kellner weiß nicht genau, wie das Essen zubereitet wird, aber er bringt dir genau das, was du bestellt hast.

## Funktionen und Arten von APIs

APIs ermöglichen den Zugriff auf verschiedene Dienste und Funktionen, darunter:

- **Datenabruf**: API-Endpunkte können Daten von einer Webanwendung oder einer Datenbank zurückgeben.
- **Steuerung von Hardware**: Einige APIs bieten Funktionen zur Steuerung von Geräten oder Maschinen.
- **Verbindung zu externen Diensten**: APIs verbinden Webanwendungen mit externen Plattformen (z.B. Zahlungsabwicklungsdienste, soziale Netzwerke).

## HTTP-Methoden in APIs

APIs verwenden oft HTTP-Methoden, um zu definieren, welche Aktion auf einem Endpunkt ausgeführt werden soll:

- **GET**: Abrufen von Daten.
- **POST**: Erstellen von neuen Daten.
- **PUT**: Aktualisieren von bestehenden Daten.
- **DELETE**: Löschen von Daten.

## API-Antworten

Die Antworten einer API sind in der Regel in einem strukturierten Format wie **JSON** oder **XML** enthalten. Die Antwort enthält entweder die angeforderten Daten oder eine Statusmeldung, die den Erfolg oder Fehler der Anfrage angibt.


## Arbeiten mit APIs in Python

In Python kannst du das Modul `requests` verwenden, um HTTP-Anfragen an eine API zu senden. Dies ermöglicht dir, Daten zu extrahieren und zu verarbeiten. `requests` ist eine benutzerfreundliche Bibliothek, die das Arbeiten mit APIs vereinfacht.

### Senden einer GET-Anfrage

Eine der häufigsten Methoden zum Interagieren mit einer API ist das Senden einer **GET-Anfrage**. Diese Anfrage dient zum Abrufen von Daten von einem API-Endpunkt. 

### Statuscodes und ihre Bedeutung

Jede Antwort einer API enthält einen **Statuscode**, der den Erfolg oder Misserfolg der Anfrage angibt. Ein Statuscode ist eine dreiziffrige Zahl, die Teil der HTTP-Antwort ist. Die gängigsten Statuscodes sind:

- **200 OK**: Die Anfrage war erfolgreich, und die Antwort enthält die angeforderten Daten.
- **201 Created**: Die Anfrage war erfolgreich, und ein neuer Datensatz wurde erstellt (meist bei POST-Anfragen).
- **400 Bad Request**: Die Anfrage war fehlerhaft, z.B. durch ungültige Parameter.
- **401 Unauthorized**: Die Anfrage erfordert eine Authentifizierung, die jedoch nicht bereitgestellt wurde.
- **404 Not Found**: Der angeforderte Endpunkt oder die Ressource wurde nicht gefunden.
- **500 Internal Server Error**: Der Server hat einen Fehler festgestellt, der die Anfrage nicht verarbeiten konnte.

### Das `response`-Objekt

Das **`response`-Objekt** enthält alle Informationen über die API-Antwort. Neben dem Statuscode enthält es auch den Text der Antwort, Header-Informationen und andere nützliche Daten. Wichtige Eigenschaften des `response`-Objekts:

- **`status_code`**: Der HTTP-Statuscode der Antwort.
- **`text`**: Der Antwortinhalt als Text (z.B. HTML, JSON oder XML).
- **`content`**: Die Antwort als Rohdaten (z.B. für Binärdaten wie Bilder).
- **`headers`**: Die Header-Informationen der Antwort.
- **`json()`**: Wandelt den Antwortinhalt, der im JSON-Format vorliegt, in ein Python-Objekt um (z.B. ein Dictionary).

#### Erklärung der verschiedenen Antwortmethoden:

- **`json()`**: Diese Methode wird verwendet, um die Antwort in ein Python-Objekt zu konvertieren, wenn die API-Antwort im JSON-Format vorliegt. JSON (JavaScript Object Notation) ist ein weit verbreitetes Datenformat, das von vielen APIs verwendet wird. Diese Methode gibt in der Regel ein Dictionary zurück (= gut zuer Weiterverarbeitung der Daten).
```python
import requests

# Senden einer GET-Anfrage an die API
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Verarbeiten der Antwort, falls erfolgreich
    print("Die Anfrage war erfolgreich!")
    print(response.json())
```
- **`text`**: Gibt den Antwortinhalt als Zeichenkette zurück. Dies ist nützlich, wenn die Antwort im Textformat vorliegt, beispielsweise HTML oder einfacher Text (aber auch gut für Debugging, da Struktur innerhalb der Console ersichtlich).
```python
text_data = response.text
print(text_data)
```
- **`content`**: Diese Methode gibt die Antwort als Rohdaten (Bytes) zurück. Sie eignet sich besonders für die Verarbeitung von Binärdaten wie Bilder, Audiodateien oder andere nicht-textuelle Formate.
```python
binary_data = response.content
print(binary_data)
```
- **`raise_for_status()`**: Diese Methode überprüft den Statuscode der Antwort und wirft eine Ausnahme (`HTTPError`), wenn der Statuscode einen Fehler anzeigt (z.B. 404 oder 500). Dies kann nützlich sein, um Fehler direkt zu erkennen und zu behandeln.
```python
try:
    response.raise_for_status()
    print("Die Anfrage war erfolgreich.")
except requests.exceptions.HTTPError as err:
    print(f"Ein Fehler ist aufgetreten: {err}")
```
### Fazit

APIs sind eine grundlegende Technologie, um mit externen Datenquellen oder Diensten zu interagieren. Sie bieten eine standardisierte Möglichkeit, auf Daten zuzugreifen und diese zu verarbeiten. In Python wird die Arbeit mit APIs durch die `requests`-Bibliothek vereinfacht, die es ermöglicht, HTTP-Anfragen zu senden und Antworten in verschiedenen Formaten zu verarbeiten. Das `response`-Objekt liefert alle wichtigen Informationen über die Antwort und bietet Methoden zur Verarbeitung der Daten, die von der API zurückgegeben werden.

> Tipp: Mittels dem header-Argument können Sie erweiterte Einstellungen vornehmen, wie etwas das Setzen eines **user-agent** oder die für eine **Authentifizierung** erforderlichen Daten (z. B. API-KEY).

```python
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'User-Agent': 'YourApp/1.0'
}
url = 'https://api.example.com/data'

response = requests.get(url, headers=headers)
```