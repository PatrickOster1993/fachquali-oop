import unittest
from bankkonto import Bankkonto

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

class TestBankkonto(unittest.TestCase):

    # Wird vor jedem einzelnen Test ausgeführt, damit immer brav Instanz von Bankkonto erzeugt wird
    def setUp(self):
        self.konto1 = Bankkonto("Patrick", 100)
    
    # Wird der Kontostand denn überhaupt korrekt gesetzt!
    def testKontostandStart(self):
        self.assertEqual(self.konto1.getKontostand(), 100)
    
    # Testet, ob ein Fehler abgefangen wird, wenn Kontostand bei Beginn negativ!
    def testKontostandNegativBeiInit(self):
        with self.assertRaises(ValueError):
            Bankkonto("Roy", -100)
    
    # Testet, ob Fehler abgefangen, sollte negativer Betrag eingezahlt werden
    def testEinzahlenNegativ(self):
        with self.assertRaises(ValueError):
            self.konto1.einzahlen(-50)
    
    # Testet, ob Fehler abgefangen, wenn negativer Betrag abgehoben
    def testAbhebenNegativ(self):
        with self.assertRaises(ValueError):
            self.konto1.abheben(-10)

    # Testet, ob auch wirklich True zurückgeliefert wird
    def testAbhebenErfolgreich(self):
        erfolgreich = self.konto1.abheben(50)
        self.assertTrue(erfolgreich) # Abhebung erfolgreich
        self.assertEqual(self.konto1.getKontostand(), 50)