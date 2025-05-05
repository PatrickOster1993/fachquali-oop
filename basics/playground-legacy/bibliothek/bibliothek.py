# 4. Kapselung:
# Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als privat (__), protected (_) oder public gelten.

# 5. Aggregation:

# Erstelle eine Klasse Bibliothek, die mehrere Bücher speichern kann. Die Bibliothek enthält eine Liste von Buch-Objekten. Sie soll Methoden zum Hinzufügen und Entfernen von Büchern haben.

# Attribute:
# - List [Buch]

# Methoden:
# - Bücher hinzufügen
# - Bücher entfernen


## wichtig: Klasse Bibliothek um Kundenliste erweitern (*)

### Verleih um begrenzte Anzahl an Exemplaren limitieren!

from buch import Buch
from kunde import Kunde

class Bibliothek:

    def __init__(self):
        self.__buecher = {}
        self.__kunden = []
    
    def kundeHinzufuegen(self, kunde_ein):
        if isinstance(kunde_ein, Kunde):
            self.__kunden.append(kunde_ein)
            print(f"Der Kunde {kunde_ein.name} hat sich erfolgreich registriert!")
        else:
            print(f"Es handelt sich dabei um keinen potenziellen Kunden - vielleicht ein Alien?")

    def buchHinzufuegen(self, buch_ein):
        if isinstance(buch_ein, Buch):
            if buch_ein in self.__buecher:
                self.__buecher[buch_ein] += 1
                print(f"Der Bestand bzgl. des Buchs mit dem Titel {buch_ein.titel} wurde um 1 Exemplar erhöht!")
            else:
                self.__buecher[buch_ein] = 1
                print(f"Das Buch mit dem Titel {buch_ein.titel} wurde erfolgreich zur Bibliothek hinzugefügt!")
        else:
            print("Es handelt sich dabei um kein Buch!")
    
    def buchEntfernen(self, buch_ein):
        if buch_ein in self.__buecher:
            if self.__buecher[buch_ein] > 1:
                self.__buecher[buch_ein] -= 1
                print(f"Der Bestand bzgl. des Buchs mit dem Titel {buch_ein.titel} wurde um 1 Exemplar verringert!")
            else:
                del self.__buecher[buch_ein]
                print(f"Das Buch mit dem Titel {buch_ein.titel} wurde erfolgreich entfernt!")
        else:
            print(f"Das Buch {buch_ein.titel} ist noch nicht im Sortiment der Bibliothek!")

    def buchVerleihen(self, buch_ein, kunde_ein):
        if kunde_ein in self.__kunden and buch_ein in self.__buecher:
            kunde_ein.buchAusleihen(buch_ein)
            print(f"Kunde {kunde_ein.name} hat sich das Buch {buch_ein.titel} geliehen!")
            self.buchEntfernen(buch_ein)
        else:
            print(f"Entweder es gibt den Kunden {kunde_ein.name} nicht oder das Buch {buch_ein.titel} ist nicht in unserem Bestand!")

    def buchZuruecknehmen(self, buch_ein, kunde_ein):
        if kunde_ein in self.__kunden:
            kunde_ein.buchZurueckgeben(buch_ein)
            print(f"Kunde {kunde_ein.name} hat das Buch zurück gebracht!")
            self.buchHinzufuegen(buch_ein)
    
    def zeigeBuchbestand(self):
        print(self.__buecher)