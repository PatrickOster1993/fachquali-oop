# 1. Erstellung einer Basisklasse:

# Erstelle eine Basisklasse Buch, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# Gemeinsame Attribute:

# titel: Der Titel des Buches.
# autor: Der Autor des Buches.
# isbn: Die ISBN des Buches.

# Gemeinsame Methoden:
# details: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

# 3. Abstraktion:

# Erstelle eine abstrakte Methode in der Klasse Buch, die in den Unterklassen implementiert werden muss. Die Methode lesen() soll in jeder Unterklasse unterschiedlich implementiert werden:

# 4. Kapselung:
# Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als privat (__), protected (_) oder public gelten.

from abc import ABC, abstractmethod

class Buch(ABC):
    def __init__(self, titel_ein, autor_ein, isbn_ein):
        self.titel = titel_ein
        self.autor = autor_ein
        self.isbn = isbn_ein

    def details(self):
        print(f"Das Buch {self.titel} wurde vom Autor {self.autor} verfasst und ist über die ISBN {self.isbn} verfügbar!")

    @abstractmethod
    def lesen(self):
        pass