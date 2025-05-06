# Aufgabe 2: Arbeiten mit JSON-Daten und Pandas

# Ziel: Eine API anfragen und die Antwortdaten mit Pandas in ein DataFrame umwandeln.

# Aufgabe:

# Sende eine GET-Anfrage an die URL: https://jsonplaceholder.typicode.com/users.
# Verarbeite die Antwort mit response.json(), um die Daten in ein Python-Dictionary zu konvertieren.
# Verwende pandas, um die JSON-Daten in ein DataFrame umzuwandeln (nur id-, name-, username- und email-Spalten erforderlich)
# Gib das DataFrames in der Konsole aus, um die Struktur der erhaltenen Daten zu überprüfen.

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response_dict = response.json()

response_df = pd.DataFrame(response_dict, columns=["id", "name", "username", "email"])

print(response_df)

