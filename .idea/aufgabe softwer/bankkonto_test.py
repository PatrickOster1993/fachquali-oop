import unittest
from bankkonto import Bankkonto

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

class TestBankkonto(unittest.TestCase):
    
    # wird vor jedem einzelnen Test aufgerufen, damit die Tests unabhaengig voneinander ausgefuehrt werden
    def setUp(self):
        self.konto = Bankkonto("Patrick", 100)
        
        
        
       #wird  der Kontostand denn überhaupt korrekt gesetzt!
        def testKonstostandStart(self):           
            self.assertEqual(self.konto1. getkontostand(), 100)
            
            #Testet ob ein Fehler abgefangen wird, wenn kontostand bei Beginn negativ ist
        def testKontoStartNegativ(self):
            with self.assertRaises(self.konto1.getkontostand() < 0):
                self.konto1 = Bankkonto("Patrick", -100)
                
                def testEinzahlen(self):
                    self.konto1.einzahlen(50)
                    self.assertEqual(self.konto1.getkontostand(), 150)
                    
                    #Testet ob ein Fehler abgefangen wird, wenn Betrag negativ ist
            
            
        