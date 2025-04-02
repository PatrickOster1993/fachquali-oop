class Auto:
    def __init__(self, marke, modell, baujahr, tankinhalt_l, kraftstoffverbrauch_pro_100_km, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.tankinhalt_l = tankinhalt_l
        self.kraftstoffverbrauch_pro_100_km = kraftstoffverbrauch_pro_100_km
        self.kilometerstand = kilometerstand
    
    def starten(self):
        print("Das Auto startet.")
    
    def fahren(self, km):
        verbrauch = self.kraftstoffverbrauch_pro_100_km / 100 * km
        if self.tankinhalt_l > verbrauch:
            self.tankinhalt_l -= self.kraftstoffverbrauch_pro_100_km / 100 * km
            self.kilometerstand += km
            print(f"Das Auto fährt {km} Kilometer.")
            print(f"Der Tank enthält noch {self.tankinhalt_l} Liter.")
            print(f"Kilometerstand: {self.kilometerstand}.")
        else:
            print(f"Nicht genug Kraftstoff für {km} km.")

    def tanken(self, liter):
        self.tankinhalt_l += liter

    def stoppen(self):
        print("Das Auto stoppt.")

    def __str__(self):
        return f"{self.marke} {self.modell} {self.baujahr}"
    
    def __eq__(self, other):
        return (
            self.marke == other.marke and
            self.modell == other.modell and
            self.baujahr == other.baujahr
        )

bmw = Auto("bmw", "i3", "2015", 50, 4, 20000)
up = Auto("VW ", "Up!", "201()", 50, 5, 100000)
print(bmw)
bmw.fahren(500)
eq = bmw == up
print(eq)
