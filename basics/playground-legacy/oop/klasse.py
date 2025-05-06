class Krieger:
    ### Attribute ###
    # Getter und Setter für Attribut Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text

    # Getter und Setter für Attribut Lebenspunkte
    @property
    def lebenspunkte(self):
        return self._lebenspunkte

    @lebenspunkte.setter
    def lebenspunkte(self, wert):
        if wert < 0:
            print("Lebenspunkte können nicht negativ sein!")
            print("#######################################")
        else:
            self._lebenspunkte = wert

    # Getter und Setter für Attribut Angriffskraft
    @property
    def angriffskraft(self):
        return self._angriffskraft

    @angriffskraft.setter
    def angriffskraft(self, wert):
        if wert < 0:
            print("Angriffskraft kann nicht negativ sein!")
            print("######################################")
        else:
            self._angriffskraft = wert

    # Getter und Setter für Attribut Rüstung
    @property
    def ruestung(self):
        return self._ruestung
    
    @ruestung.setter
    def ruestung(self, wert):
        if wert < 0:
            print("Rüstung kann nicht negativ sein!")
            print("################################")
        else:
            self._ruestung = wert

    ### Konstruktor ###
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung):
        """Initialisiert einen Krieger mit den angegebenen Attributen."""
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.ruestung = ruestung

    def angreifen(self, gegner):
        """Führt einen Angriff auf einen anderen Krieger aus und zieht dessen Lebenspunkte ab."""
        schaden = self.angriffskraft - gegner.ruestung
        if schaden > 0:
            gegner.lebenspunkte -= schaden
            print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu!")
            print("#########################################################")
        else:
            print(f"{self.name} greift {gegner.name} an, aber der Angriff hat keinen Schaden verursacht!")
            print("###########################################################################")

    def verteidigen(self):
        """Erhöht die Rüstung des Kriegers."""
        self.ruestung += 5
        print(f"{self.name} verteidigt sich und erhöht seine Rüstung auf {self.ruestung}.")
        print("#####################################################################")
    
    def checkStatus(self):
        print(f"############## {self.name} ###############")
        print("Lebenspunkte: ", self.lebenspunkte)
        print("Angriffskraft: ", self.angriffskraft)
        print("Rüstung: ", self.ruestung)
        print(f"##########################################")