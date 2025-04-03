# Aufgabe 11   Kapselung (Encapsulation)
# Schauen  Sie  sich  nochmals  „Aufgabe  6“  (=  Online-Shop)  an  und  ergänzen  Sie  den  Code  um  eine 
# sinnvolle  Kapselung.  Überlegen  Sie  sich  hierbei  vor  allem,  welche  Attribute  und  Methoden  in 
# welchem Maße geschützt werden sollten.



class Produkt:
    def __init__(self, name, preis, lagerbestand):
        self.__name = name  # Privates Attribut
        self.__preis = preis  # Privates Attribut
        self.__lagerbestand = lagerbestand  # Privates Attribut

    # Getter-Methode für den Namen
    def get_name(self):
        return self.__name

    # Getter-Methode für den Preis
    def get_preis(self):
        return self.__preis

    # Setter-Methode für den Preis
    def set_preis(self, neuer_preis):
        if neuer_preis > 0:
            self.__preis = neuer_preis
        else:
            print("Der Preis muss positiv sein!")

    # Getter-Methode für den Lagerbestand
    def get_lagerbestand(self):
        return self.__lagerbestand

    # Setter-Methode für den Lagerbestand
    def set_lagerbestand(self, neuer_lagerbestand):
        if neuer_lagerbestand >= 0:
            self.__lagerbestand = neuer_lagerbestand
        else:
            print("Der Lagerbestand darf nicht negativ sein!")

    # Methode zur Darstellung des Produkts
    def __str__(self):
        return f"{self.__name}: Preis: {self.__preis}€, Lagerbestand: {self.__lagerbestand}"


# Beispiel: Online-Shop
class OnlineShop:
    def __init__(self):
        self.produkte = []

    def produkt_hinzufuegen(self, produkt):
        self.produkte.append(produkt)

    def produkt_entfernen(self, produkt):
        if produkt in self.produkte:
            self.produkte.remove(produkt)
        else:
            print("Produkt nicht im Shop vorhanden.")

    def __str__(self):
        produkt_liste = "\n".join(str(produkt) for produkt in self.produkte)
        return f"Online-Shop:\n{produkt_liste}"


# Testen des Codes
produkt1 = Produkt("Laptop", 999.99, 10)
produkt2 = Produkt("Smartphone", 499.99, 20)

# Zugriff auf Attribute über Getter-Methoden
print(produkt1.get_name())  # Ausgabe: Laptop
print(produkt1.get_preis())  # Ausgabe: 999.99
print(produkt1.get_lagerbestand())  # Ausgabe: 10

# Ändern des Preises und Lagerbestands über Setter-Methoden
produkt1.set_preis(899.99)
produkt1.set_lagerbestand(15)

# Überprüfen der Änderungen
print(produkt1.get_preis())  # Ausgabe: 899.99
print(produkt1.get_lagerbestand())  # Ausgabe: 15

# Online-Shop erstellen
shop = OnlineShop()
shop.produkt_hinzufuegen(produkt1)
shop.produkt_hinzufuegen(produkt2)

# Ausgabe des Shops
print(shop)
