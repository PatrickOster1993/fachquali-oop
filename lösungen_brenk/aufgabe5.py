class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
    
    def starten(self):
        print("Das Auto startet.")
    
    def fahren(self, km):
        print(f"Das Auto fährt {km} Kilometer.")

    def stoppen(self):
        print("Das Auto stoppt.")

    def __str__(self):
        return f"{self.marke} {self.modell} {self.baujahr}"
    

bwm = Auto("BWM", "i3", "2015")
print(bwm)