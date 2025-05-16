from charakter import Charakter

class Schurke(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, geschicklichkeit, waffe=None):
        # Aufruf des Konstruktors der abstrakten Klasse (= gemeinsame Eigenschaften aller Charaktere)        
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, waffe)
        # individuelle Eigenschaft der Klasse Schurke!       
        self._geschicklichkeit = max(0, geschicklichkeit)

    # individuelle Angriffsmethode der Klasse Schurke!
    def angreifen(self, ziel):
        from random import random
        kritischer_treffer = random() < self._geschicklichkeit * 0.1
        schaden = (self._angriffskraft + (self.waffe.schaden if self.waffe else 0)) * (2 if kritischer_treffer else 1)
        ziel.lebenspunkte -= schaden
        print(f"{self.name} greift {ziel.name} an und verursacht {schaden} Schaden.")
        if kritischer_treffer:
            print("Kritischer Treffer!")

    # zusätzliches Verhalten der Klasse Schurke!
    def verstecken(self):
        self._geschicklichkeit += 1
        print(f"{self.name} versteckt sich und erhöht seine Geschicklichkeit.")