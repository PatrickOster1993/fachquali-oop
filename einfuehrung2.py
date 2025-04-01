class Krieger:
    
    def __init__(self, name, lebenspunkte, angriffskraft, verteidigung):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.verteitigung = verteidigung

    def __str__(self):
        return f"Name: {self.name} | Lebenspunkte: {self.lebenspunkte} | Angriffskraft: {self.angriffskraft} | Verteidigung: {self.verteitigung}"

    def angreifen(self, gegner):
        print(f"{self.name} attackiert {gegner.name} mit einer Angfrifsstärke von {self.angriffskraft}!")

    def verteitigen(self, gegner):
        schaden = gegner.angriffskraft - 0.5 * self.verteitigung
        self.lebenspunkte -= schaden
        print(f"{self.name} verteidigt sich gegen {gegner.name} und nimmt {schaden} Schaden!")
        if self.gefallen():
            print(f"{self.name} ist leider im Krieg gefallen! Er war ein stolzer Kämpfer!")
            self.lebenspunkte = 0

    def gefallen(self):
        return self.lebenspunkte <= 0

herbert = Krieger("Sir Herbert", 100, 80, 35)
arthur = Krieger("King Arthur", 90, 65, 95)

print(herbert)
print(arthur)

print("#####################")
herbert.angreifen(arthur)
arthur.verteitigen(herbert)
herbert.angreifen(arthur)
arthur.verteitigen(herbert)
herbert.angreifen(arthur)
arthur.verteitigen(herbert)
print("#####################")

print(herbert)
print(arthur)

# print(herbert)
# print(arthur)