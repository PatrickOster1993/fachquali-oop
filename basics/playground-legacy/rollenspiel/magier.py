from charakter import Charakter

class Magier(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana, waffe=None):
        # Aufruf des Konstruktors der abstrakten Klasse (= gemeinsame Eigenschaften aller Charaktere)
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, waffe)
        # individuelle Eigenschaft der Klasse Magier!
        self._mana = max(0, mana)

    # individuelle Angriffsmethode der Klasse Magier!
    def angreifen(self, ziel):
        if self._mana >= 10:
            schaden = self._angriffskraft + (self.waffe.schaden if self.waffe else 0)
            ziel.lebenspunkte -= schaden
            self._mana -= 10
            print(f"{self.name} greift {ziel.name} mit Magie und {self.waffe.name if self.waffe else 'Händen'} an und verursacht {schaden} Schaden.")
        else:
            print(f"{self.name} hat nicht genug Mana zum Angreifen.")

    # zusätzliches Verhalten der Klasse Magier!
    def zaubern(self, ziel):
        if self._mana >= 20:
            schaden = (self._angriffskraft * 2) + (self.waffe.schaden if self.waffe else 0)
            ziel.lebenspunkte -= schaden
            self._mana -= 20
            print(f"{self.name} zaubert und verursacht {schaden} Schaden an {ziel.name}.")
        else:
            print(f"{self.name} hat nicht genug Mana zum Zaubern.")