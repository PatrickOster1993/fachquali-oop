class Auto:
    
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def __str__(self):
        return f"Auto: {self.marke} {self.modell}, Baujahr: {self.baujahr}"
    
    def starten(self):
        print("Das Auto startet.")

    def fahren(self, km):
        print(f"Das Auto fährt {km} Kilometer.")

    def stoppen(self):
        print("Das Auto stoppt.")


Mein_Lambo = Auto(marke="Lamborghini", modell="Aventador", baujahr=2024)
Mein_Audi = Auto(marke="Audi", modell="RSQ8", baujahr=2023)
Mein_Volvo = Auto(marke="Volvo", modell="XC90", baujahr=2024)

print(Mein_Lambo)
Mein_Audi.fahren(1400)
Mein_Volvo.starten()