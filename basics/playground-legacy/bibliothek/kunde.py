# 7. Bonus:

# Klasse Kunde
## wichtig: Klasse Bibliothek um Kundenliste erweitern (*)
### Verleih um begrenzte Anzahl an Exemplaren limitieren!

## Attribute:
### Bücher: enthält die aktuell geliehenen Bücher (check)

## Methode:
### Logik für Verleih der Bücher (*) (check)

## Kapselung überlegen! (check)

# from roman import Roman
from buch import Buch

class Kunde:
    def __init__(self, name_ein, kundenNr_ein):
        self.name = name_ein
        self.kundenNr = kundenNr_ein
        self.__buecher = []

    def buchAusleihen(self, buch):
        self.__buecher.append(buch)

    def buchZurueckgeben(self, buch):
        if buch in self.__buecher:
            self.__buecher.remove(buch)
            print(f"{self.name} hat das Buch mit dem Titel {buch.titel} zurückgegeben!")
        else:
            print(f"{self.name} besitzt das Buch mit dem Titel {buch.titel} aktuell gar nicht!")

    def gelieheneBuecher(self):
        print(f"Von {self.name} geliehene Bücher:")
        for buch in self.__buecher:
            buch.details()

# ich = Kunde(
#     name_ein="Patrick", 
#     kundenNr_ein=0
#     )

# mein_buch = Roman("blabla", "Test-Mensch", "123456789", "Erotik")
# mein_anderes_buch = Roman("blub", "Test-Mensch", "123456680", "Fantasy")

# ich.buchAusleihen(mein_buch)
# ich.buchAusleihen(mein_anderes_buch)
# ich.gelieheneBuecher()

# ich.buchZurueckgeben(mein_buch)
# ich.gelieheneBuecher()