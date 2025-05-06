# Aufgabe 3: Erstellen einer kleinen Klasse für API-Daten (OOP)

# Ziel: Eine Klasse erstellen, die Daten von einer API abruft und in einer benutzerfreundlichen Art und Weise darstellt. Die Antwort wird als Pandas DataFrame gespeichert.

# Aufgabe:

    # Erstelle eine Klasse APIClient, die folgende Attribute/Methoden hat:
    # getData(url): Sendet eine GET-Anfrage an die übergebene URL und speichert die Antwort (= response)
    # getDict(): Gibt die Antwort im Dictionary-Format zurück, falls die Anfrage erfolgreich war.
    # getStatusCode(): Gibt den Statuscode der Antwort zurück.
    # showStructure(): Gibt die Struktur der Antwort im Textformat aus, damit du sehen kannst, wie der Aufbau der Daten strukturiert ist (Tipp: response.text).
    # dataFrame: Gibt die Antwortdaten als Pandas DataFrame zurück (Tipp: property verwenden).

    # Erstelle eine Instanz der Klasse und rufe die Methoden mit der URL https://jsonplaceholder.typicode.com/posts auf, um die Daten und den Statuscode zu erhalten.
    # Gib die Antwort im Dictionary-Format aus und zeige den Statuscode der Anfrage.
    # Nutze die Methode showStructure(), um die Struktur der Daten in der Konsole darzustellen.
    # Speichere die Antwort als Pandas DataFrame und gib die ersten 5 Zeilen des DataFrames aus.
    # Hinweis: Achte darauf, Fehler zu behandeln, falls die Anfrage fehlschlägt (z.B. durch den Statuscode 404 oder 500).

import requests
import pandas as pd

class APIClient:

    def __init__(self, url_ein):
        try:
            self.__url = url_ein
            self.__response = None # = null / Null / nil
        except Exception as e:
            print("Fehler:", {e})
    
    def getData(self):
        self.__response = requests.get(self.__url)

    def showStructure(self):
        if self.statusCode == 200:
            print(self.__response.text)
        else:
            print("Anfrage an Server nicht erfolgreich!")

    @property
    def responseDict(self):
        if self.statusCode == 200:
            return self.__response.json()
        else:
            return {}
    
    @property
    def responseDf(self):
        return pd.DataFrame(self.responseDict)

    @property
    def statusCode(self):
        return self.__response.status_code
    
client = APIClient(url_ein="https://jsonplaceholder.typicode.com/posts")
client.getData()
print("Antwort im dict-Format:", client.responseDict)
print("Status Code:", client.statusCode)
print("####################################################")
client.showStructure()
print("####################################################")
df = client.responseDf
print(df.head())