# Erstellen Sie eine 4×4-Liste (= 4 Zeilen u. 4 Spalten) mit zufälligen Zahlen zwischen 1 und 9.
# Implementieren Sie danach folgende Funktionen:
# 1. Geben Sie die Liste in einer schönen Tabellenform auf der Konsole aus.
# 2. Berechnen Sie die Summe aller Zahlen.
# 3. Finden Sie die größte Zahl in der Liste sowie deren Indizes.

import random

# 4x4 Liste erstellen:

numbers = []

for _ in range(4):
    inner_numbers = []
    for _ in range(4):
        inner_numbers.append(random.randint(1, 9))
    numbers.append(inner_numbers)

print(numbers)

# 1. Funktion: Geben Sie die Liste in einer schönen Tabellenform auf der Konsole aus.

print("################")

def display_list(list):
    for inner_list in list:
        for elem in inner_list:
            print(elem, end=' ')
        print()   

## Aufruf der Funktion:
display_list(numbers)

# 2. Funktion: Berechnen Sie die Summe aller Zahlen.

print("################")

def summe_berechnen(list):
    summe = 0
    for zeile in list:
        for spalte in zeile:
            summe += spalte
    return summe

print("Summe der Zahlen:", summe_berechnen(numbers))

# 3. Funktion: Finden Sie die größte Zahl in der Liste sowie deren Indizes.

print("################")

def max_zahl_index(list):
    max_zahl = 0
    zeilen_index = 0
    spalten_index = 0

    for i in range(4):
        for j in range(4):
            wert = list[i][j]
            if wert > max_zahl:
                max_zahl = wert
                zeilen_index = i
                spalten_index = j
    
    return {
        "max": max_zahl,
        "zeile": zeilen_index,
        "spalte": spalten_index
    }

print(max_zahl_index(numbers))