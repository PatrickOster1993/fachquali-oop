#Schreiben Sie ein Python-Programm, das eine Liste von Temperaturen (in Grad Celsius) speichert
#und verschiedene Berechnungen und Manipulationen durchführt.
#1. Erstellen Sie eine Liste, welche die folgenden Temperaturen für 7 Tage in °C enthält: [15, 18, 20, 22, 17, 19, 21].
#2. Berechnen Sie die Durchschnittstemperatur und geben Sie diese in der Konsole aus.
#3. Bestimmen Sie die höchste und die niedrigste Temperatur (max(), min()) und geben Sie die
#Werte entsprechend in der Konsole aus.
#4. Ersetzen Sie alle Temperaturen unter 18°C durch den Wert 18.
#5. Tauschen Sie nun die Temperatur des letzten mit der des ersten Tages.

# 1. Liste erstellen
temperaturen = [15, 18, 20, 22, 17, 19, 21]
print(temperaturen)

# 2. Durchschnittstemperatur erstellen + Ausgabe
# print(sum(temperaturen) / len(temperaturen)) # -> für Praxis

## für Prüfung:
temp_sum = 0
temp_len = 0

for temp in temperaturen:
    temp_len += 1
    temp_sum += temp

durchschnitt = temp_sum / temp_len

print("Länge d. Liste:", temp_len)
print("Summe d. Temperaturen:", temp_sum)
print("Durchschnittstemperatur:", durchschnitt)

# 3. Min. und Max. Temperatur bestimmen:
print("Min:", min(temperaturen), "Max:", max(temperaturen)) # -> für Praxis

# Für Prüfung:
min_temp = temperaturen[0]
max_temp = temperaturen[0]

for temp in temperaturen:
    if temp < min_temp:
        min_temp = temp
    elif temp > max_temp:
        max_temp = temp

print("Min:", min_temp, "Max:", max_temp)

#4. Ersetzen Sie alle Temperaturen unter 18°C durch den Wert 18.
## zur Abwechslung mal mit while-Schleife:

print("Temperaturen vorher:", temperaturen)

i = 0

while i < temp_len:
    # temp = temperaturen[i]
    temp = temperaturen[i]
    if temp < 18:
        temperaturen[i] = 18
    i += 1

print("Temperaturen nachher:", temperaturen)

#5. Tauschen Sie nun die Temperatur des letzten mit der des ersten Tages.

## Praxis
# first_temp = temperaturen[0]
# last_temp = temperaturen[-1]

# temperaturen[0] = last_temp
# temperaturen[-1] = first_temp

## Prüfung
first_temp = temperaturen[0]
last_temp = temperaturen[temp_len - 1]

temperaturen[0] = last_temp
temperaturen[temp_len - 1] = first_temp

print("Temperaturen vertauscht:", temperaturen)

## zur Erklärung, warum "temp_len - 1" statt "temp_len":
# Index:   0   1   2   3   4   5   6
# Werte: [15, 18, 20, 22, 17, 19, 21]