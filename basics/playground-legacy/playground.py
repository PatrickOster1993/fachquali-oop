print("##################")
print("### Playground ###")
print("##################")

test = 3
# ============================
# Anfänger
# ============================

# Einfacher Kommentar (1 Zeile)

"""
Kommentar
über
mehrere
Zeilen
"""

# Variablen und Konstanten
x = 42  # Kann später geändert werden
PI = 3.14  # Keine Konstanten in Python, aber Namenskonvention (= Großbuchstaben)
print("Variable:", x)
print("Konstante:", PI)

# Datentypen
zahl = 11  # Integer
kommazahl = 11.5  # Float
text = "Hallo, Python!"  # String
wahrheitswert = True  # Boolean
nichts = None  # NoneType
print("Zahl:", zahl, "Datentyp:", type(zahl))
print("Kommazahl:", kommazahl, "Datentyp:", type(kommazahl))
print("Text:", text, "Datentyp:", type(text))
print("Wahrheitswert:", wahrheitswert, "Datentyp:", type(wahrheitswert))
print("Nichts:", nichts, "Datentyp:", type(nichts))

# Tuple
koordinaten = (10, 20)
print("Koordinaten:", koordinaten, "Datentyp:", type(koordinaten))

# Groß- und Kleinschreibung ändern
upper_text = text.upper()
print("In Großbuchstaben:", upper_text)
lower_text = text.lower()
print("In Kleinbuchstaben:", lower_text)

# Bedingung
if zahl > 50:
    print("Die Zahl ist größer als 50")
elif zahl > 30:
    print("Die Zahl ist größer als 30, aber 50 oder kleiner")
else:
    print("Die Zahl ist 30 oder kleiner")

# Logische Operatoren
ist_richtig = True
ist_falsch = False

# UND-Operator (and)
if ist_richtig and ist_falsch:
    print("Beide sind wahr")
else:
    print("Mindestens einer ist falsch")

# ODER-Operator (or)
if ist_richtig or ist_falsch:
    print("Mindestens einer ist wahr")
else:
    print("Beide sind falsch")

# '==' vs. 'is'
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True, weil die Listen den gleichen Wert haben
print(a is c)  # False, weil es zwei verschiedene Listen im Speicher sind
print(a is b)  # True, weil a und b dasselbe Objekt im Speicher sind

# Schleifen
# For-Schleife
for i in range(5):
    print("For-Schleife, Durchlauf:", i)

# While-Schleife
count = 0
while count < 3:
    print("While-Schleife, Zähler:", count)
    count += 1

# Do-While-Schleife (nachgebaut)
# Hinweis: Python hat keine eingebaute do-while-Schleife
count = 0
while True:
    print("Do-While-Schleife, Zähler:", count)
    count += 1
    if count >= 3:
        break

# Eingabe vom Nutzer
benutzer_input = input("Gib eine Zahl ein: ")
print("Du hast eingegeben:", benutzer_input)

# ============================
# Fortgeschrittene
# ============================

# Listen
zahlen_liste = [1, 2, 3, 4, 5]
print("Liste:", zahlen_liste[1])

# Liste durchlaufen
for zahl in zahlen_liste:
    print("Zahl aus der Liste:", zahl)

# join (Liste in String umwandeln)
liste_als_string = ", ".join(map(str, zahlen_liste))
print("Liste als String:", liste_als_string)

# append (Neues Element ans Ende hinzufügen)
zahlen_liste.append(6)
print("Liste nach append:", zahlen_liste)

# pop (Letztes Element entfernen)
zahlen_liste.pop()
print("Liste nach pop:", zahlen_liste)

# insert (Element an bestimmter Position einfügen)
zahlen_liste.insert(0, 0)
print("Liste nach insert:", zahlen_liste)

# reverse (Liste umdrehen)
zahlen_liste.reverse()
print("Liste nach reverse:", zahlen_liste)

# sort (Liste sortieren)
sortierte_liste = [3, 1, 4, 5, 2]
sortierte_liste.sort()
print("Sortierte Liste:", sortierte_liste)

# Dictionary
person = {
    "name": {
        "vorname": "Max",
        "nachname": "Mustermann",
    },
    "alter": 25,
    "hobby": "Programmieren",
}

print("Person:", person)
print("Name der Person:", person["name"]["vorname"])

# Set (nur eindeutige Werte)
eindeutige_werte = {1, 2, 3, 2, 1}
print("Set (nur eindeutige Werte):", eindeutige_werte)

# String-Manipulation
beispiel_text = "Python ist mächtig!"

# in-Operator (Substring prüfen)
enthält_python = "Python" in beispiel_text
print("Enthält 'Python'?", enthält_python)

# replace (Text ersetzen)
neuer_text = beispiel_text.replace("mächtig", "cool")
print("Ersetzter Text:", neuer_text)

# Funktionen
def addieren(a, b):
    return a + b

summe = addieren(5, 10)
print("Ergebnis der Funktion addieren:", summe)

# Modulo-Operator
a = 17
b = 5
print("17 % 5 =", a % b)  # Gibt den Rest der Division zurück (17 geteilt durch 5)

# Fehlerbehandlung
try:
    fehler = nicht_definiert + 1  # Diese Variable ist nicht definiert
except NameError as error:
    print("Fehler gefunden:", error)
else:
    print("Kein Fehler aufgetreten.")
finally:
    print("Immer schön Fehler abfangen!")

# Dateien lesen und schreiben
# Schreiben
with open("example.txt", "w") as file:
    file.write("Hallo, Datei!\n")

# Lesen
with open("example.txt", "r") as file:
    content = file.read()
print("Inhalt der Datei:", content)

# =====================================
# Experten
# =====================================

# List Comprehension
verdoppelte_werte = [num * 2 for num in zahlen_liste]
print("Verdoppelte Werte:", verdoppelte_werte)

# Lambda-Funktion
quadrieren = lambda num: num * num
print("Quadrat von 4 (Lambda-Funktion):", quadrieren(4))

# filter (Liste mit Bedingung filtern)
gefilterte_zahlen = list(filter(lambda num: num > 3, zahlen_liste))
print("Gefilterte Zahlen > 3:", gefilterte_zahlen)

# Eigene Fehler mit raise
def check_positive(value):
    if value < 0:
        raise ValueError(f"Wert muss positiv sein, aber {value} wurde übergeben.")
    return value

try:
    check_positive(-1)
except ValueError as e:
    print("Fehler erkannt:", e)

# Switch-Case Alternative
# Hinweis: Python hat kein echtes switch-case; Dictionary wird verwendet
operation = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Division durch Null!",
}

op = "add"
result = operation[op](10, 5)
print(f"Operation {op}: Ergebnis =", result)

# Dekoratoren
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Aufruf von {func.__name__} mit {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Ergebnis: {result}")
        return result
    return wrapper

@debug
def multiplizieren(a, b):
    return a * b

multiplizieren(3, 4)

# Generatoren und yield
def zahlen_generator():
    for i in range(5):
        yield i

for zahl in zahlen_generator():
    print("Generator-Zahl:", zahl)