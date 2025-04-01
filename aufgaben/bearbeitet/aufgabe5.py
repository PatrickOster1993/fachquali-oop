# Aufgabe 5: Klassen und Objekte
# Erstellen Sie eine Klasse Auto mit den Attributen marke, modell und baujahr.#klasse Auto
class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def starten(self):
        print(" Auto start.")

    def fahren(self, km):
        print(f" Auto fährt {km} Kilometer.")

    def stoppen(self):
        print(" Auto stoppt.")

    def __str__(self):
        return f"Auto: {self.marke} {self.modell}, Baujahr {self.baujahr}"


auto1 = Auto("VW", "Golf", 2020)
auto2 = Auto("BMW", "3er", 2018)
auto3 = Auto("Toyota", "Corolla", 2022)

# Ausgabe
print(f"\n{auto1}")
auto1.starten()
auto1.fahren(50)
auto1.stoppen()

print(f"\n{auto2}")
auto2.starten()
auto2.fahren(100)
auto2.stoppen()

print(f"\n{auto3}")
auto3.starten()
auto3.fahren(75)
auto3.stoppen()
