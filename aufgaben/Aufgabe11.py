
class OnlineShop:

    def __init__(self):
        self._produkte = []
        self._zuletztAufsteigend = True
    
    def __str__(self):
        tabellarische_auflistung = ""
        for product in self._produkte:
            bezeichnung = product[0]
            preis = product[1]
            tabellarische_auflistung += "- "
            tabellarische_auflistung += bezeichnung # Produktname links
            tabellarische_auflistung += ":" # Tab-Space zwischen Name und Preis
            tabellarische_auflistung += str(preis)
            tabellarische_auflistung += "\n"
        return f"{tabellarische_auflistung}"
    
    def __produkteUnsortiert(self, ascending):
         # gibt True zurück, wenn produkte unsortiert, und False, falls nicht!
        counter = 0

        for i in range(len(self._produkte) - 1):
            aktueller_preis = self._produkte[i][1]
            naechster_preis = self._produkte[i + 1][1]
            diff = naechster_preis - aktueller_preis
            if ascending and diff > 0:
                counter += 1
            elif not ascending and diff < 0:
                counter += 1
    
        if counter == (len(self._produkte) - 1):
            if ascending:
                print("Produkte bereits aufsteigend sortiert!")
            elif not ascending:
                print("Produkte bereits absteigend sortiert!")
            return False
        return True

    def sortProducts(self, ascending = True):
        self._zuletztAufsteigend = ascending
        if self.__produkteUnsortiert(ascending):
            for i in range(len(self._produkte)):
                for j in range(len(self._produkte) - i - 1):
                    if (self._produkte[j + 1][1] < self._produkte[j][1]) and ascending:
                        self._produkte[j], self._produkte[j + 1] = self._produkte[j + 1], self._produkte[j]
                    elif (self._produkte[j + 1][1] > self._produkte[j][1]) and not ascending:
                        self._produkte[j], self._produkte[j + 1] = self._produkte[j + 1], self._produkte[j]
    
    def produktInListe(self, produktname):
        produkt_nicht_enthalten = True
        for produkt in self._produkte:
            bezeichnung = produkt[0]
            if bezeichnung == produktname:
                produkt_nicht_enthalten = False
                preis = produkt[1]
                print(f"Produkt {produktname} kostet {preis} €!")
                return True
        if produkt_nicht_enthalten:
            print(produktname + " (noch) nicht in Liste enthalten!")
            return False
    
    def _addProduct(self, name, preis):
        if not self.produktInListe(name):
            self._produkte.append([name, preis])
        else:
            for i in range(len(self._produkte)):
                produkt_bezeichnung = self._produkte[i][0]
                if produkt_bezeichnung == name:
                    self._produkte[i][1] = preis
        self.sortProducts(self._zuletztAufsteigend)
    
    def _removeProduct(self, product):
        if self.produktInListe(product):
            gesuchte_teilliste = [product]
            for i in range(len(self._produkte)):
                sortiment_produkt = self._produkte[i]
                sortiment_produkt_bezeichnung = sortiment_produkt[0]
                sortiment_produkt_preis = sortiment_produkt[1]
                if product == sortiment_produkt_bezeichnung:
                    gesuchte_teilliste.append(sortiment_produkt_preis)
            self._produkte.remove(gesuchte_teilliste)
        else:
            print(f"Das Produkt mit der Bezeichnung {product} befindet sich noch nicht im Sortiment!")

# TESTEN:
produkte = [['Laptop', 1200], ['Smartphone', 800], ['Tablet', 500], ['Monitor', 300], ['Maus', 50]]

# Instanz erzeugen
mein_shop = OnlineShop()


# Anpassung an protected produkte
for i in range(len(produkte)):
    mein_shop._addProduct(produkte[i][0],produkte[i][1])


# Objekt / Instanz als String ausgeben (Konsole)
print(mein_shop)

# überprüfen, ob Produkte unsortiert sind, nicht mehr möglich weil private!
# print(mein_shop.__produkteUnsortiert(True))

# produkte sortieren
mein_shop.sortProducts(True)
print(mein_shop)
#print(mein_shop.produkteUnsortiert(True))

# produkt in Liste vorhanden (Überprüfung)
produkt = ['iPhone', 650]
mein_shop.produktInListe(produkt[0])

# iPhone hinzufügen
mein_shop._addProduct(produkt[0], produkt[1])
print(mein_shop)

# Versuch, bereits vorhandenes Produkt hinzuzufügen:
neues_produkt = ['iPhone', 1000]
mein_shop._addProduct(neues_produkt[0], neues_produkt[1])
print(mein_shop)

# Produkt entfernen:
mein_shop._removeProduct(neues_produkt[0])
mein_shop._removeProduct("Nintendo Switch")
print(mein_shop)

mein_shop._addProduct("Drucker", 1000)
mein_shop.sortProducts(False)
print(mein_shop)