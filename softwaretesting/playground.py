# Erwartungshaltung Taschenrechner:
# - Ergebnis sollte richtig sein!
# - bei gleicher Eingabe sollte gleiche Ausgabe erfolgen!

def addiere(a, b):
    return str(a) + str(b) # anstatt return str(a + b)!

print(addiere(2, 2))

# Fazit: Softwaretesting erforderlich!

# Unterschied: SW-Test & Exception Handling:
# SW-Test: "Macht mein Code das, was er soll (zuverlässig)"
# Exception-Handling: "Maßnahme, sollte (dennoch) ein Fehler auftreten!"

# Warum testen:
# - Fehlervermeidung (konstengünstiger)
# - Warbarkeit!
# - Verlässlichkeit / Zuverlässigkeit
# - Doku: Tests zeigen an, welches Verhalten vom Code erwartet wird.

# Testarten (Bottom-up-Reihenfolge):
# - Unit-Test (Modultest): Einzelne Module mit Funktionen / Methoden testen
# - Integrationstest: Zusammenspiel mehrerer Module
# - Systemtest: Komplette Anwendung
# - (Regressionstest): Frühere Fehler auch dauerhaft gelöst bleiben

# -> in der Praxis: oftmals einen "Test-Branch"!

# Wesentliche Unterscheidung: manuelles Testen (Mensch) vs automatisiertes Testen (SW)

def verdopple(x):
    return 2 * x

# manuell:
print((verdopple(3))) # Auge prüft Ergebnis!

# halbwegs automatisiert (simpel, aber wenig nützlich):
## "assertion" = Bedingung, die wahr sein muss, sonst schlägt Test fehl!
assert verdopple(3) == 6

# Integrationstest (simpel):
def beschreibe(x):
    return f"Das Ergebnis ist {verdopple(x)}"

assert beschreibe(4) == "Das Ergebnis ist 8"

# Testmethoden nach Kenntnisstand (= wieviel weiß Tester über Code)
## Blackbox: nur Verhalten zählt / keine Kenntnis über Code / nur Eingabe bzw. Ausgabe prüfen!
### assert login("max", "12345") == True

## Whitebox: Innere Logik & Strukturen
# def login(user, pw):
#     if user == "admin" and pw == "1234":
#         return True
#     return False

# assert login("admin", "1234") == True
# assert login("admin", "password") == False

## Greybox: Mischung beider Prespektiven
### Bsp: API testen -> wir kennen Logik der API-Implementierung NICHT
### ABER wir wissen z. B. was die API zurückgibt ("status-codes")
### response = apiCall()
### assert response["status"] == "ok"

# Testkonzepte & Begriffe:
# - Testfall: Konkrete Eingabe + erwartete Ausgabe

# Eingabe: 2 und 3 - Erwartung: 5

assert addiere(2, 3) == 5

# - Testabdeckung (coverage): Anteil des Codes, der durch Testing geprüft wird

def istGerade(x):
    if x % 2 == 0:
        return True
    return False

assert istGerade(4) == True # nur gerade Zahl getestet -> ungerade fehlt!

# - Test-Driven Development (TDD): Erst Test schreiben! Danach erst Code!

# - Assertion: Bedingung, die wahr sein muss (sonst schlägt Test fehl)

# - Failure vs Error:
## Failure: Erwartete Ergebnis (Assertion) nicht erreicht!
## Error: Test selbst schlägt wegen Ausnahme fehl (z. B. Division durch 0)

# Testframeworks in Python:

## pytest: modern, simpel
## unittest: native Standard-Modul -> verwenden WIR!
## assert: für einfaches manuelles Testen / Alternative zu print()

# Best Practices im Testen:

## Unittests unabhängig von anderen Modulen!
## Ein Test prüft EINE Sache
## Fehlerfälle in Test mit einfließen lassen (z. B. Division durch 0)
## projekt/src/tests --> separater Ordner für Tests!