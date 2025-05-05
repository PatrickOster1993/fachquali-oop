# Hier testen wir die in "api.md" vermittelten Inhalte aus!
import requests

# Senden einer GET-Anfrage an die API
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Verarbeiten der Antwort, falls erfolgreich
    print("STATUS_CODE: Die Anfrage war erfolgreich!")
    # print(response.json()) # bessere Weiterverarbeitung (Python dict)
    print(response.text) # bessere Lesbarkeit (für Konsole)
    # print(response.content) # für Verarbeitung von nicht-textellen Daten / Binärdaten (z. B. Bilder / Audios)

# Alternatives Abfangen von Fehlern / gescheiterten Anfragen
# für mich persönlich präferierte Variante, da über echtes Exception-Handling!
# try:
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"Ein Fehler ist aufgetreten: {err}")
# else:
#     print(response.text)
#     print("RAISE_FOR_STATUS: Die Anfrage war erfolgreich!")