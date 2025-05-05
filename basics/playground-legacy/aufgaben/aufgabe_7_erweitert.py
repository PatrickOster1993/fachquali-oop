import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

former_temperature = np.random.uniform(low=9, high=17, size=(10, 7))

# Aktuelle Temperatur (bis einschl. Donnerstag)
current_temperature = np.random.uniform(low=10, high=18, size=7)

# Setze die letzten 3 Werte auf NaN, da Fr - So noch nicht eingetroffen!
current_temperature[-3:] = np.nan

# Berechnung der Durchschnittstemperatur für jeden Wochentag
average_temperatures = np.mean(former_temperature, axis=0)

# Bestimmung des Höchst- und Tiefstwerts der Temperaturen
max_temp = np.max(average_temperatures)
min_temp = np.min(average_temperatures)

# DataFrame erstellen
days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
df_dict = {
    "Tag": days,
    "Durchschnittstemperatur (°C)": average_temperatures
}
df = pd.DataFrame(df_dict)

# DataFrame in Konsole ausgeben
print("\nDataFrame:")
print(df)

# Plotten
plt.style.use('dark_background')
plt.figure()
plt.plot(df["Tag"], df["Durchschnittstemperatur (°C)"], label='Durchschnittstemperatur', color='#ABE4F9')
plt.plot(df["Tag"], current_temperature, label='Aktuelle Woche', color='#F9E7AB')

# Höchst- und Tiefstwerte als horizontale Linien einzeichnen
plt.axhline(y=max_temp, color='#ABF9E7', linestyle=':', label='Max. Temperatur')
plt.axhline(y=min_temp, color='#F9ABBD', linestyle=':', label='Min. Temperatur')

# Achsenbeschriftung und Titel
plt.xlabel("Wochentag", fontsize=12)
plt.ylabel("Temperatur (°C)", fontsize=12)
plt.title("Temperaturvorhersage basierend auf den letzten 10 Wochen", fontsize=16)

# Legende und Gitternetz
plt.legend()
plt.grid(axis='y', linewidth=0.5, alpha=0.25)

# Diagramm anzeigen
plt.show()