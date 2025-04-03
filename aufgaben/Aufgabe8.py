class Auto:

    def __init__(self, marke, modell, baujahr, tankinhalt:int, tankkapazitaet:int, kraftstoffverbrauch:int, kilometerstand:int):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.tankinhalt = tankinhalt
        self.tankkapazitaet = tankkapazitaet
        self.kraftstoffverbrauch = kraftstoffverbrauch
        self.kilometerstand = kilometerstand

    def starten(self):
        return f"Das Auto startet"

    def fahren(self,km):
        if self.tankinhalt >= (km*self.kraftstoffverbrauch)/100:
            self.tankinhalt -= (km*self.kraftstoffverbrauch)/100
            self.kilometerstand += km
        else:
            return f"Das Auto hat nicht genug Tankinhalt um {km}km zu fahren!"
        return f"Das Auto fährt {km} Kilometer. Der Neue Kilometerstand beträgt jetzt {self.kilometerstand}km."

    def tanken(self, tankmenge):
        tankdiff = self.tankkapazitaet - self.tankinhalt
        if tankmenge > tankdiff:
            return f"Die Tankmenge ist zu hoch. Du kannst nur noch {tankdiff}L tanken, dann ist dein Tank voll."
        else:
            self.tankinhalt += tankmenge
            return f"Du hast {tankmenge}L getankt."
    def stoppen(self):
        return f"Das Auto stoppt"
    
    def __eq__(self, other):
        if self.marke == other.marke:
            return True
        return False


    def __str__(self):
        return f"Auto: {self.marke} {self.modell}, Baujahr: {self.baujahr}, Tankinhalt: {self.tankinhalt}, Kraftstoffverbrauch: {self.kraftstoffverbrauch}, Kilometerstand: {self.kilometerstand}"

auto1 = Auto("VW", "Golf", 2020, 50, 50, 5, 10000) 

auto2 = Auto("VW", "Golf", 2000, 45, 20, 7, 50000) 


fahren = auto1.fahren(100)

tanken = auto1.tanken(5)


print(fahren)
print(tanken)

print(auto1)

print(auto1.__eq__(auto2))