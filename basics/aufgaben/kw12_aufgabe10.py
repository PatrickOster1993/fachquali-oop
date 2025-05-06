#Schreiben Sie ein Python-Programm, das eine Liste von simulierten Aktienkursen erstellt und grundlegende Analysen durchführt.
#Erstellen Sie eine Liste mit 20 (= ca. 1 Handelsmonat) zufälligen Aktienkursen zwischen 75€ und 150€ für ein Unternehmen.
#Berechnen Sie und geben Sie aus:
#A. Den durchschnittlichen Aktienkurs des Monats.
#B. Den höchsten und niedrigsten Kurs.
#C. Die Anzahl der Tage, an denen der Kurs gestiegen ist.
#D. Die Anzahl der Tage, an denen der Kurs gefallen ist
#Finden Sie den Tag, an dem der Kurs am stärksten gestiegen ist.
#Berechnen Sie den gesamten Kursanstieg oder -rückgang über den Monat hinweg.

import random

# Kursdaten erstellen
# kurse = [random.uniform(75, 150) for _ in range(20)] # -> für Praxis (über Comprehension)

## für die Prüfung:

KURS_LEN = 20
kurse = []

i = 0

while i < KURS_LEN:
    kurse.append(random.randint(75, 150))
    i += 1

print(kurse)

# A: Durchnittsberechnung:

kurs_sum = 0

for kurs in kurse:
    kurs_sum += kurs # äquivalent zu "kurs_sum = kurs_sum + kurs"

durchschnitt = kurs_sum / KURS_LEN

print("Durchschnittl. Aktienkurs:", durchschnitt)

# B: Höchster u. niedrigster Kurs im Monat:
kurs_max = kurse[0]
kurs_min = kurse[0]

for kurs in kurse:
    if kurs > kurs_max:
        kurs_max = kurs
    elif kurs < kurs_min:
        kurs_min = kurs

print("Min. Kurs:", kurs_min, "Max. Kurs:", kurs_max)

# C: Anzahl der Tage, an denen Kurs gestiegen ist:
print("Aktuelle Kursdaten:", kurse)

anstieg_tage = 0
abfall_tage = 0

i = 0

while i < (KURS_LEN - 1):
    aktueller_kurs = kurse[i]
    naechster_kurs = kurse[i + 1]
    if aktueller_kurs < naechster_kurs:
        anstieg_tage += 1
    # elif aktueller_kurs > naechster_kurs: -> in der Praxis: nur 1 Schleife vonnöten.. (Aufgabe D)
        # abfall_tage += 1
    i += 1

print("Anzahl Tage, an denen Kurs gestiegen:", anstieg_tage)

#D. Die Anzahl der Tage, an denen der Kurs gefallen ist

for i in range (1, KURS_LEN):
    if kurse[i] < kurse[i-1]:
        abfall_tage += 1

print (f"Anzahl Tage, an denen Kurs gefallen: {abfall_tage}")

#Finden Sie den Tag, an dem der Kurs am stärksten gestiegen ist.
i = 0

max_anstiegs_tag = 0
max_anstieg = 0

while i < (KURS_LEN - 1):
    aktueller_kurs = kurse[i]
    naechster_kurs = kurse[i + 1]
    aktueller_anstieg = naechster_kurs - aktueller_kurs
    if aktueller_anstieg > max_anstieg:
        max_anstieg = aktueller_anstieg
        max_anstiegs_tag = i + 1  # Tag des maximalen Anstiegs (i+1, da der Anstieg zwischen i und i+1 erfolgt)
    i += 1

print("Max. Anstiegstag:", max_anstiegs_tag)

#Berechnen Sie den gesamten Kursanstieg oder -rückgang über den Monat hinweg.
monats_anstieg = kurse[KURS_LEN - 1] - kurse[0]
print("Kursanstieg über Monat hinweg:", monats_anstieg)