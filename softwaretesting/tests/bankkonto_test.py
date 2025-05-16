import unittest
import random
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
        self.primaryTestKonto = Bankkonto("PrimärUser", 100)
        self.anzahlKonten = 100
        self.minKontostand = 10000
        self.maxKontostand = 100000
        self.konten = []
        for i in range(self.anzahlKonten):
            inhaber = f"Testuser{i}"
            kontostand = random.randint(self.minKontostand, self.maxKontostand)
            self.konten.append(Bankkonto(inhaber, kontostand))
        # self.konten.append(Bankkonto("Extreme1", 0))
        # self.konten.append(Bankkonto("Extreme1", 249.99))

    # Wird der Kontostand denn überhaupt korrekt gesetzt!
    def testKontostandStart(self):
        self.assertEqual(self.primaryTestKonto.getKontostand(), 100)
    
    # Testet, ob ein Fehler abgefangen wird, wenn Kontostand bei Beginn negativ!
    def testKontostandNegativBeiInit(self):
        with self.assertRaises(ValueError):
            Bankkonto("Roy", -100)
    
    # Testet, ob Fehler abgefangen, sollte negativer Betrag eingezahlt werden
    def testEinzahlenNegativ(self):
        with self.assertRaises(ValueError):
            self.primaryTestKonto.einzahlen(-50)
    
    # Testet, ob Fehler abgefangen, wenn negativer Betrag abgehoben
    def testAbhebenNegativ(self):
        with self.assertRaises(ValueError):
            self.primaryTestKonto.abheben(-20)

    # Testet, ob auch wirklich True zurückgeliefert wird
    def testAbhebenErfolgreich(self):
        for i, konto in enumerate(self.konten):
            betrag = random.randint(0, self.minKontostand)
            with self.subTest(i=i):
                erfolgreich = konto.abheben(betrag)
                self.assertTrue(erfolgreich) # Abhebung erfolgreich

    # - Für Fließkommazahlen: assertAlmostEqual()
    # - Zur Überprüfung, ob etwas in einer Collection ist: assertIn() / assertNotIn()