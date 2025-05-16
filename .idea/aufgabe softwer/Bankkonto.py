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
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.kontostand = kontostand
        
        def einzahlen(self, betrag):
            self.kontostand += betrag
            
        def abheben(self, betrag):
            if betrag
            if self._kontostand < betrag:
                raise ValueError("Betrag größer als Kontostand")
            if betrag > self._kontostand:
                
            else:
                self._kontostand -= betrag
                return True
            def testKontostand(self):
                self.assertEqual(self.konto.kontostand, 100)
                
                
                
                
                
                