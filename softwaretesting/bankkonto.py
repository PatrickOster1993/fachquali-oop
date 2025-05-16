# +----------------------------------------+
# |               Bankkonto                |
# +----------------------------------------+
# | - inhaber: str                         |
# | - kontostand: float                     |
# +----------------------------------------+
# | + __init__(inhaber, kontostand)        |
# | + einzahlen(betrag: int) : void        |
# | + abheben(betrag: int) : bool          |
# +----------------------------------------+

class Bankkonto:

    def __init__(self, inhaber, kontostand):
        self.__inhaber = inhaber
        if kontostand < 0:
            raise ValueError("Kontostand darf nicht negativ sein!")
        self.__kontostand = kontostand
    
    def einzahlen(self, betrag):
        if betrag < 0:
            raise ValueError("Betrag muss positiv sein!")
        self.__kontostand += betrag
    
    def abheben(self, betrag):
        if betrag < 0:
            raise ValueError("Betrag muss positiv sein!")
        if betrag > self.__kontostand:
            return False
        self.__kontostand -= betrag
        return True
    
    def getKontostand(self):
        return self.__kontostand