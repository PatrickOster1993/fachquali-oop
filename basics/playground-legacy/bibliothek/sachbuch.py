# 2. Vererbung:

# Erstelle zwei Unterklassen Sachbuch und Roman, die von der Klasse Buch erben.

# Sachbuch:

# Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut thema haben, das das Thema des Sachbuches angibt.
# Eine Methode wissenVermitteln, die in der Konsole ausgibt, zu welchem Thema das Buch Wissen vermittelt (als Satz).

# lesen()
# Sachbuch: Gibt "Ich lese, um zu lernen!" aus.

# 4. Kapselung:
# Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als privat (__), protected (_) oder public gelten.

from buch import Buch

class Sachbuch(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, thema_ein):
        # super().__init__(...) = ruft Konstruktor der Elternklasse auf (= Zuweisung gemeinsamer Attribute)
        super().__init__(titel_ein, autor_ein, isbn_ein)
        # Zuweisung der spezifischen Attribute
        # privat, da einziger aktuell interessanter Use-Case über "wissenVermitteln()" ohnehin nach Außen zugänglich
        self.__thema = thema_ein
    
    def wissenVermitteln(self):
        print(f"Das Buch {self.titel} vermittelt Wissen zum Thema {self.__thema}.")

    def lesen(self):
        print("Ich lese, um zu lernen!")

# mein_sachbuch = Sachbuch(
#     titel_ein="Physik ist toll",
#     autor_ein="Albert Zweistein",
#     isbn_ein="123456789",
#     thema_ein="Physik",
# )

# mein_sachbuch.wissenVermitteln()
# mein_sachbuch.details()