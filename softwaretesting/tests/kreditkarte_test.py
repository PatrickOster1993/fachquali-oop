# __init__(self, inhaber, konto, limit)
# bezahlen(self, betrag)

# Your turn!

import unittest
from bankkonto import Bankkonto
from kreditkarte import Kreditkarte

class TestKreditkarte(unittest.TestCase):
    
    def setUp(self):
        self.konto = Bankkonto("Testuser", 1000)
        self.karte = Kreditkarte(self.konto.getInhaber(), self.konto, 10000)

    def testLimitNegativBeiInit(self):
        with self.assertRaises(ValueError):
            Kreditkarte(self.konto.getInhaber(), self.konto, -100)
    
    def testBetragNegativ(self):
        with self.assertRaises(ValueError):
            self.karte.bezahlen(-50)
    
    def testBetragUeberLimit(self):
        erfolgreich = self.karte.bezahlen(2000)
        self.assertFalse(erfolgreich)
    
    def testBezahlenErfolgreich(self):
        erfolgreich = self.karte.bezahlen(500)
        self.assertTrue(erfolgreich)

    def testInhaberIdentisch(self):
        self.assertEqual(self.karte.getInhaber(), self.konto.getInhaber())