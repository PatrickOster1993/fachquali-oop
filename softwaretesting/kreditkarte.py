# class TestKreditkarte(unittest.TestCase):
    
#     def setUp(self):
#         self.konto = Bankkonto("Testuser", 1000)
#         self.karte = Kreditkarte(self.konto.getInhaber(), self.konto, 10000)

#     def testLimitNegativBeiInit(self):
#         with self.assertRaises(ValueError):
#             Kreditkarte(self.konto.getInhaber(), self.konto, -100)
    
#     def testBetragNegativ(self):
#         with self.assertRaises(ValueError):
#             self.karte.bezahlen(-50)
    
#     def testBetragUeberLimit(self):
#         erfolgreich = self.karte.bezahlen(2000)
#         self.asserFalse(erfolgreich)
    
#     def testBezahlenErfolgreich(self):
#         erfolgreich = self.karte.bezahlen(500)
#         self.assertTrue(erfolgreich)

#     def testInhaberIdentisch(self):
#         self.assertEqual(self.karte.getInhaber(), self.konto.getInhaber())

from bankkonto import Bankkonto

class Kreditkarte:
    def __init__(self, inhaber, konto, limit):
        self.__inhaber = inhaber
        self.konto = konto
        if limit < 0:
            raise ValueError("Limit darf nicht negativ sein!")
        self.limit = limit

    def bezahlen(self, betrag):
        return self.konto.abheben(betrag)

    def getInhaber(self):
        return self.__inhaber