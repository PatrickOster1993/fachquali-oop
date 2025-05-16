import unittest
from tests.bankkonto_test import TestBankkonto

def bankkonto():
    # alle Testmethoden aus Testklasse laden
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBankkonto)

    # Alternativ: wenn nur bestimmte Testmethoden erwünscht:
    ## suite.addTests(TestBankkonto("testKontostandStart"))
    ## suite.addTests(...)

    # verbosity: Deitail-Grad des Testberichts: 1 = rudimentär // ... // 3 = sehr detailliert
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    bankkonto()