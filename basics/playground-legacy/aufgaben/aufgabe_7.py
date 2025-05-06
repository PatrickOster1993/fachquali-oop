import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Analyse der Temperaturen
temperatures = np.array([12, 15.13, 14, 10, 9.11, 13, 11])

# Statistische Berechnungen
mean = float(np.mean(temperatures))
max_temp = float(np.max(temperatures))
min_temp = float(np.min(temperatures))

# Konsolenausgaben
print(f"Durchschnittliche Temperatur: {round(mean, 2)}°C")
print(f"Max. Temperatur: {round(max_temp, 2)}°C")
print(f"Min. Temperatur: {round(min_temp, 2)}°C")

# DataFrame erstellen
wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
df_dict = {
    "Tag": wochentage,
    "Temperatur (°C)": temperatures
}
df = pd.DataFrame(df_dict)

# DataFrame in Konsole ausgeben
print("\nDataFrame:")
print(df)

# Plotten
plt.style.use('dark_background')
plt.figure()
plt.plot(df["Tag"], df["Temperatur (°C)"], label='Temperatur', color='#F9C0AB')

# Durchschnitt als horizontale Linie einzeichnen
plt.axhline(y=mean, color='#ABE4F9', linestyle=':', label='Durchschnittstemperatur')

# Achsenbeschriftung
plt.xlabel("Wochentag")
plt.ylabel("Temperatur (°C)")
plt.title("Aufgabe 7: Temperaturanalyse")
plt.legend()

# Gitternetz hinzufügen
plt.grid(axis='y', linewidth=0.5, alpha=0.25)

# Diagramm anzeigen
plt.show()