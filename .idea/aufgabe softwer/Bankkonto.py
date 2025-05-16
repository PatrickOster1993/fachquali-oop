# +----------------------------------------+
# |               Bankkonto                |
# +----------------------------------------+
# | - inhaber: str                         |
# | - kontostand: float                    |
# +----------------------------------------+
# | + __init__(inhaber, kontostand)        |
# | + einzahlen(betrag: int) : void        |
# | + abheben(betrag: int) : bool          |
# +----------------------------------------+

class Bankkonto:
    def __init__(self, inhaber: str, kontostand: float):
        self.__inhaber = inhaber
        self.__kontostand = kontostand

    def einzahlen(self, betrag: int) -> None:
        if betrag > 0:
            self.__kontostand += betrag
        else:
            print("Invalid amount. Deposit amount must be positive.")

    def abheben(self, betrag: int) -> bool:
        if betrag > 0 and self.__kontostand >= betrag:
            self.__kontostand -= betrag
            return True
        return False

    
    def get_kontostand(self) -> float:
        return self.__kontostand

    def get_inhaber(self) -> str:
        return self.__inhaber