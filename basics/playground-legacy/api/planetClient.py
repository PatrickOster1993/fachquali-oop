# Nutze die Planeten-API:
# https://api.le-systeme-solaire.net/rest/bodies/

# Klasse: PlanetClient

## Methoden
### fetchData(): Lädt die Planeteninformationen von der API.
### filterPlanets(): Filtert nur die echten Planeten aus den Daten.
### plotPlanetRadii(): Erstellt ein Balkendiagramm der Radii der Planeten.

## Property
### dataFrame: Gibt die heruntergeladenen Daten als Pandas DataFrame zurück.

####################################################################################
# Instanziere die Klasse und lade die Daten mit fetchData().
# Gib die Daten als DataFrame aus.
# Filtere die Planeten mit filterPlanets() und zeige die gefilterten Daten an.
# Visualisiere die Radii der Planeten mit plotPlanetRadii().
####################################################################################

import requests
import pandas as pd
import matplotlib.pyplot as plt

class PlanetClient:

    def __init__(self, url_ein):
        self.__url = url_ein
        self.__data = {}
        self.filteredPlanets = pd.DataFrame()

    def fetchData(self):
        response = requests.get(self.__url)
        code = response.status_code

        if code == 200:
            self.__data = response.json()["bodies"]
        else:
            print(f"Request fehlgeschlagen mit Code {code}!")

    def filterPlanets(self):
        filter_bedingung = self.dataFrame["isPlanet"] == True
        self.filteredPlanets = self.dataFrame[filter_bedingung]

    def plotPlanetRadii(self):
        plt.bar(self.filteredPlanets["englishName"], self.filteredPlanets["meanRadius"])
        plt.title("Durchschnittlicher Radius der Planeten")
        plt.xlabel("Planet")
        plt.ylabel("Radius / km")
        plt.show()

    @property
    def dataFrame(self):
        return pd.DataFrame(self.__data)
    
my_planets = PlanetClient("https://api.le-systeme-solaire.net/rest/bodies/")
my_planets.fetchData()
my_planets.filterPlanets()
print(my_planets.filteredPlanets)
my_planets.plotPlanetRadii()