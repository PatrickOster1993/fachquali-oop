import unittest
from Bankkonto import Bankkonto  # Ensure this line is correct

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

    def setUp(self):
        self.konto = Bankkonto("John Doe", 1000.0)

    def test_einzahlen(self):
        self.konto.einzahlen(500)
        self.assertEqual(self.konto.get_kontostand(), 1500.0)

        self.konto.einzahlen(-200)
        self.assertEqual(self.konto.get_kontostand(), 1500.0)

    def test_abheben(self):
        erfolg = self.konto.abheben(200)
        self.assertTrue(erfolg)
        self.assertEqual(self.konto.get_kontostand(), 800.0)

        erfolg = self.konto.abheben(2000)
        self.assertFalse(erfolg)
        self.assertEqual(self.konto.get_kontostand(), 800.0)

        erfolg = self.konto.abheben(-100)
        self.assertFalse(erfolg)
        self.assertEqual(self.konto.get_kontostand(), 800.0)

    def test_kontostand(self):
        self.assertEqual(self.konto.get_kontostand(), 1000.0)

    def test_inhaber(self):
        self.assertEqual(self.konto.get_inhaber(), "John Doe")

if __name__ == '__main__':
    unittest.main()