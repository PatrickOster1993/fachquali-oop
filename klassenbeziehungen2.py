import random

def kampfsimulation(krieger1, krieger2):
    while True :
        krieger = [krieger1, krieger2]
        am_zug = random.randint(0, 1)
        angreifender_krieger = krieger[am_zug]
        krieger.remove(angreifender_krieger)
        verteidigender_krieger = krieger[0]
        angreifender_krieger.angreifen(verteidigender_krieger)
        verteidigender_krieger.verteidigen(angreifender_krieger)
        print(angreifender_krieger)
        print(verteidigender_krieger)
        if verteidigender_krieger.gefallen():
            break

class Krieger:
    
    def __init__(self, name, lebenspunkte, angriffskraft, verteidigung, ruestung = None):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.verteidigung = verteidigung
        self.ruestung = ruestung
        self.setRuestung(ruestung)
    
    def setRuestung(self, ruestung):
        self.ruestung = ruestung
        if self.ruestung != None:
            self.verteidigung += self.ruestung.bonus

    def __str__(self):
        return f"Name: {self.name} | Lebenspunkte: {self.lebenspunkte} | Angriffskraft: {self.angriffskraft} | Verteidigung: {self.verteidigung}"

    def angreifen(self, gegner):
        print(f"{self.name} attackiert {gegner.name} mit einer Angfrifsstärke von {self.angriffskraft}!")

    def verteidigen(self, gegner):
        schaden = gegner.angriffskraft - 0.5 * self.verteidigung
        self.lebenspunkte -= schaden
        print(f"{self.name} verteidigt sich gegen {gegner.name} und nimmt {schaden} Schaden!")
        if self.gefallen():
            print(f"{self.name} ist leider im Krieg gefallen! Er war ein stolzer Kämpfer!")
            self.lebenspunkte = 0

    def gefallen(self):
        return self.lebenspunkte <= 0
    
    def __eq__(self, value):
        return (
            self.name == value.name and
            self.lebenspunkte == value.lebenspunkte and
            self.angriffskraft == value.angriffskraft and
            self.verteidigung == value.verteidigung
        )
    
    # def critical(self, factor: int) -> int:
    #     return self.angriffskraft * factor

class Ruestung:
    
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
    
    def __str__(self):
        return f"{self.name} liefert einen Verteidigungsbonus von {self.bonus}!"

herbert = Krieger("Sir Herbert", 100, 80, 35)

meine_ruestung = Ruestung("Eisenschild", 25)
arthur = Krieger("King Arthur", 90, 60, 75, meine_ruestung)
herbert.setRuestung(meine_ruestung)

print(herbert)
print(arthur)


# kampfsimulation(herbert, arthur)

