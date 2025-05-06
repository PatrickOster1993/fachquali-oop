# 2. Vererbung:

# Erstelle zwei Unterklassen Sachbuch und Roman, die von der Klasse Buch erben.



# Roman:

# Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut genre haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
# Auch soll die Klasse eine Property fsk beinhalten, welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12, 16 oder 18 setzt.

# lesen()
# Roman: Gibt "Ich lese, um in eine fesselnde Welt einzutauchen." aus.

# 4. Kapselung:
# Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als privat (__), protected (_) oder public gelten.

from buch import Buch

class Roman(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, genre_ein):
        super().__init__(titel_ein, autor_ein, isbn_ein)
        self.genre = genre_ein
    
    @property
    def fsk(self):
        FSK_MAPPING = {
            "kinderbuch": 0,
            "comedy": 6,
            "fantasy": 12,
            "thriller": 16,
            "erotik": 18
        }
        return FSK_MAPPING[self.genre.lower()]
    
    def lesen(self):
        print("Ich lese, um in eine fesselnde Welt einzutauchen.")

# mein_roman = Roman(
#     titel_ein="Der große Gatsby", 
#     autor_ein="F. Scott Fitzgerald",
#     isbn_ein="123456789",
#     genre_ein="erotik"
#     )

# mein_roman.lesen()