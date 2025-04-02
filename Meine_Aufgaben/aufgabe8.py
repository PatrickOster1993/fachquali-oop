class Auto:
    def __init__(self, marke, modell, baujahr, tankinhalt, kraftstoffverbrauch, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.tankinhalt = tankinhalt
        self.kraftstoffverbrauch = kraftstoffverbrauch
        self.kilometerstand = kilometerstand

    def __eq__(self, value: object) -> bool:
        if self.marke == value.marke and self.modell == value.modell and self.baujahr == value.baujahr:
            return True
        else:
            return False
        
        

    
    def starten(self):
        return f"Das Auto startet"

    def fahren(self,km):
        if self.tankinhalt <= (km*self.kraftstoffverbrauch)/100:
            return f"Tank reicht nicht aus"
        if self.tankinhalt >= (km*self.kraftstoffverbrauch)/100:
            self.tankinhalt-=(km*self.kraftstoffverbrauch)/100
            self.kilometerstand+=km
            return f"Auto fährt {km} Kilometer."
    
    def tanken(self, tankenmenge):
        self.tankinhalt+= tankenmenge
        return f"du tankst {tankenmenge}. du hast {self.tankinhalt} liter tank" 

    def stoppen(self):
        return f"Das Auto stoppt"
    
    def __str__(self):
        return f"Auto: {self.marke} {self.modell}, Baujahr: {self.baujahr} Tankinhalt: {self.tankinhalt} Verbrauch: {self.kraftstoffverbrauch} Kilometerstand: {self.kilometerstand}"

auto1 = Auto("VW", "Golf", 2020, 20, 8, 100000)
auto2 = Auto("VW", "Golf", 2020, 20, 8, 100000)



auto_starten = auto1.starten()
auto_fahren = auto1.fahren(100)
auto_stoppen = auto1.stoppen()
auto_tanken = auto1.tanken (20)

print(auto1.tanken(1))
print (auto_tanken)
print(auto_starten)
print(auto_fahren)
print(auto_stoppen)
print (auto1)

print (auto1.__eq__(auto2))
