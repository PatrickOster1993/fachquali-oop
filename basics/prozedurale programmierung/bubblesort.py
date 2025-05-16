# https://de.wikipedia.org/wiki/Bubblesort#/media/Datei:Bubble-sort-example-300px.gif

import random

def bubblesort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            print(i, j)
            if liste[j + 1] < liste [j]:
                liste[j], liste [j + 1] = liste[j + 1], liste [j]
    return liste

# Liste erstellen:
meine_liste = []

# Liste initialisieren (Zufallswerte) = unsortierte Liste
for _ in range(10):
    meine_liste.append(random.randint(0, 50))
print("Unsortierte Liste:")
print(meine_liste)

print("Sortierte Liste:")
print(bubblesort(meine_liste))

