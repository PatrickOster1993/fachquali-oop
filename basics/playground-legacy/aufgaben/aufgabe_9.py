import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class TemperatureAnalysis:
    def __init__(self, weeks=10):
        self.weeks = weeks
        self.days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        self.formerTemperature = np.random.uniform(low=9, high=17, size=(self.weeks, 7))

    @property
    def currentTemperature(self):
        return self._generateCurrentTemperature()

    @property
    def averageTemperatures(self):
        return self._calculateAverageTemperatures()

    @property
    def maxTemp(self):
        return np.max(self.averageTemperatures)

    @property
    def minTemp(self):
        return np.min(self.averageTemperatures)

    def _generateCurrentTemperature(self):
        current_temp = np.random.uniform(low=self.minTemp, high=self.maxTemp, size=7)
        today = datetime.now().weekday()  # 0 = Monday, 6 = Sunday
        if today < 6:
            current_temp[today + 1:] = np.nan
        return current_temp

    def _calculateAverageTemperatures(self):
        return np.mean(self.formerTemperature, axis=0)

    def createDataframe(self):
        df_dict = {
            "Tag": self.days,
            "Durchschnittstemperatur (°C)": self.averageTemperatures
        }
        return pd.DataFrame(df_dict)

    def plotTemperatures(self):
        df = self.createDataframe()

        plt.style.use('dark_background')
        plt.figure(figsize=(10, 5))
        plt.plot(df["Tag"], df["Durchschnittstemperatur (°C)"], label='Durchschnitt', color='#ABE4F9')
        plt.plot(df["Tag"], self.currentTemperature, label='Aktuelle Woche', color='#F9E7AB')

        plt.axhline(y=self.maxTemp, color='#ABF9E7', linestyle=':', label='Max. Temperatur')
        plt.axhline(y=self.minTemp, color='#F9ABBD', linestyle=':', label='Min. Temperatur')

        plt.xlabel("Wochentag", fontsize=12)
        plt.ylabel("Temperatur (°C)", fontsize=12)
        plt.title(f"Temperaturvorhersage basierend auf den letzten {self.weeks} Jahren", fontsize=16)

        plt.legend()
        plt.grid(axis='y', linewidth=0.5, alpha=0.25)

        plt.show()

############################ Beispiel mit ausführlicher Erklärung #############################

# 1. Objekt der Klasse TemperatureAnalysis erzeugen (Instanzierung)
#    Das Erzeugen eines Objekts einer Klasse wird als "Instanzierung" bezeichnet.
#    Hier rufen wir den Konstruktor (`__init__`) auf, um die Klasse `TemperatureAnalysis`
#    mit der Anzahl der Wochen (`weeks=52`) zu initialisieren.
analyzer = TemperatureAnalysis(weeks=10) # nun können wir sogar komplexe Datentypen (list, dict, ...) aus unserem Objekt erstellen:)
# 2. Attribute der Klasse (keine Logik dahinter, reine Datenspeicherung)
#    Attribute wie `days` oder `formerTemperature` sind **normale Variablen**,
#    die in der Klasse gespeichert werden und direkt ausgelesen werden können.
#    Sie haben keine Logik, sondern enthalten nur Daten.
days = analyzer.days  # Eine Liste der Wochentage ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
weeks = analyzer.weeks  # Die Anzahl der Wochen, die für die Analyse herangezogen werden
former_temps = analyzer.formerTemperature  # Eine Matrix mit Temperaturwerten der letzten Wochen

print(f"Die Temperaturen von {days[0]} bis {days[-1]} der aktuellen KW für die letzten {weeks} Jahre befinden sich als Matrix in former_temps!")

# 3. Properties (Props = Attribute mit Logik dahinter)
#    Properties sind spezielle Attribute, die mit der `@property`-Dekoration erstellt werden.
#    Sie sehen aus wie normale Attribute, enthalten aber Logik, die ausgeführt wird, wenn
#    auf das Property zugegriffen wird. So können dynamische Werte erzeugt werden.

#    a) currentTemperature: Liefert die aktuellen Temperaturen der Woche.
#       Diese werden dynamisch erzeugt und für die restlichen Tage der Woche (ab morgen)
#       mit `np.nan` aufgefüllt (wie gestern im Unterricht erwünscht).
current_temp = analyzer.currentTemperature

#    b) averageTemperatures: Berechnet den Durchschnitt der Temperaturen aus der Matrix
#       `formerTemperature` über alle Kalenderwochen.
mean_temp = analyzer.averageTemperatures

#    c) maxTemp: Findet den höchsten Wert aus den Durchschnittstemperaturen.
max_temp = analyzer.maxTemp

#    d) minTemp: Findet den niedrigsten Wert aus den Durchschnittstemperaturen.
min_temp = analyzer.minTemp

print(f"Max. Temperatur: {round(max_temp, 2)}°C | Min. Temperatur: {round(min_temp, 2)}°C")

# 4. Methoden (Aktionen oder Funktionen der Klasse)
#    Methoden sind Funktionen innerhalb der Klasse, die mit `def` definiert werden.
#    Sie führen bestimmte Aktionen aus oder geben Ergebnisse zurück.

#    a) createDataframe: Diese Methode erstellt ein Pandas-DataFrame-Objekt,
#       das die Wochentage und die Durchschnittstemperaturen in einer Tabelle zusammenfasst.
#       Das Ergebnis kann für Analysen oder Ausgaben verwendet werden.
mean_temp = analyzer.createDataframe()
print(mean_temp)

#    b) plotTemperatures: Diese Methode erzeugt eine grafische Darstellung (Plot)
#       der Daten. Sie zeigt die Durchschnittstemperaturen der letzten Wochen sowie
#       die aktuellen Temperaturen der laufenden Woche. Zusätzlich werden
#       horizontale Linien für die Maximal- und Minimaltemperaturen eingezeichnet.
analyzer.plotTemperatures()
###############################################################################################
