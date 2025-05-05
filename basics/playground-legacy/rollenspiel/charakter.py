from abc import ABC, abstractmethod

# Teil 1: Neue Klassen hinzufügen (Vererbung und Abstraktion)
class Charakter(ABC):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, waffe=None): # Tragen der Waffe kein Muss!
        self.name = name # Name öffentlich zugänglich!
        # Geschützte Attribute (= nur Klasse & Unterklassen zugänglich)
        self._lebenspunkte = max(0, lebenspunkte) # sorgt dafür, dass lebenspunkte niemals < 0
        self._angriffskraft = max(0, angriffskraft)
        self._ruestung = max(0, ruestung)
        # Waffe nach Außen hin sichtbar!
        self.waffe = waffe

    # Angriff sieht von Charakter zu Charakter unterschiedlich aus
    @abstractmethod
    def angreifen(self, ziel):
        pass

    # Bei allen Charakteren gleich!
    def checkStatus(self):
        print(f"{self.name} - LP: {self._lebenspunkte}, Angriff: {self._angriffskraft}, Rüstung: {self._ruestung}, Waffe: {self.waffe.name if self.waffe else 'Keine'}")

    # Teil 5: Überladung von Operatoren
    def __eq__(self, andere):
        return (
            self.name == andere.name and
            self._angriffskraft == andere._angriffskraft and
            self._ruestung == andere._ruestung
        )
    
    @property
    def lebenspunkte(self):
        return self._lebenspunkte

    @lebenspunkte.setter
    def lebenspunkte(self, wert):
        self._lebenspunkte = max(0, wert) # Interne Logik = Property