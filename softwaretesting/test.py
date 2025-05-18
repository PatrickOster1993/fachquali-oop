import unittest
from tests.bankkonto_test import TestBankkonto
from tests.kreditkarte_test import TestKreditkarte

def bankkonto():
    # alle Testmethoden aus Testklasse laden
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBankkonto)

    # verbosity: Deitail-Grad des Testberichts: 1 = rudimentär // ... // 3 = sehr detailliert
    unittest.TextTestRunner(verbosity=2).run(suite)

def kreditkarte():
    # alle Testmethoden aus Testklasse laden
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKreditkarte)

    # verbosity: Deitail-Grad des Testberichts: 1 = rudimentär // ... // 3 = sehr detailliert
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    bankkonto() # Modultest
    kreditkarte() # Integrationstest (zwischen Bankkonto- und Kreditkarte-Modul)