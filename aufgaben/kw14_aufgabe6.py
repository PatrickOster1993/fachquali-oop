# Werfen Sie nochmals einen Blick auf die bereits behandelte „Aufgabe 17“ aus dem Dokument „aufgaben_kw12.pdf“ (= Bubblesort & Lineare Suche) und versuchen Sie nun die Aufgabe objektorientiert zu lösen:
    # 1. Zeichnen Sie sich hierfür zunächst ein geeignetes Klassendiagramm.
    # 2. Beginnen Sie daraufhin die Implementierung der Klasse.
    # 3. Ergänzen Sie die Methode addProduct(...) um eine zusätzliche Bedingung, die
    # sicherstellen soll, dass sich ein bereits vorhandenes Produkt niemals zweimal im Sortiment befindet. In diesem Falle, soll lediglich der als Argument übergebene Preis aktualisiert werden.
    # 4. Erweitern Sie die Klasse zuletzt um eine Methode removeProduct(product), welche das übergebene Produkt aus dem Sortiment entfernen soll, sofern dieses existiert - andernfalls soll eine entsprechende Meldung in der Konsole ausgegeben werden.
    # 5. Erstellen Sie abschließend noch eine geeignete Methode, welche alle sich im Sortiment befindlichen Produkte (inkl. Preis) in tabellarischer Form auflistet (= Konsolenausgabe).
# 6. Klassendiagramm ergänzen!

class OnlineShop:

    def __init__(self, produkte):
        self.produkte = produkte
        self.zuletztAufsteigend = True
    
    def __str__(self):
        tabellarische_auflistung = ""
        for product in self.produkte:
            bezeichnung = product[0]
            preis = product[1]
            tabellarische_auflistung += "- "
            tabellarische_auflistung += bezeichnung # Produktname links
            tabellarische_auflistung += ":" # Tab-Space zwischen Name und Preis
            tabellarische_auflistung += str(preis)
            tabellarische_auflistung += "\n"
        return f"{tabellarische_auflistung}"
    
    def produkteUnsortiert(self, ascending):
         # gibt True zurück, wenn produkte unsortiert, und False, falls nicht!
        counter = 0

        for i in range(len(self.produkte) - 1):
            aktueller_preis = self.produkte[i][1]
            naechster_preis = self.produkte[i + 1][1]
            diff = naechster_preis - aktueller_preis
            if ascending and diff > 0:
                counter += 1
            elif not ascending and diff < 0:
                counter += 1
    
        if counter == (len(self.produkte) - 1):
            if ascending:
                print("Produkte bereits aufsteigend sortiert!")
            elif not ascending:
                print("Produkte bereits absteigend sortiert!")
            return False
        return True

    def sortProducts(self, ascending = True):
        self.zuletztAufsteigend = ascending
        if self.produkteUnsortiert(ascending):
            for i in range(len(self.produkte)):
                for j in range(len(self.produkte) - i - 1):
                    if (self.produkte[j + 1][1] < self.produkte[j][1]) and ascending:
                        self.produkte[j], self.produkte[j + 1] = self.produkte[j + 1], self.produkte[j]
                    elif (self.produkte[j + 1][1] > self.produkte[j][1]) and not ascending:
                        self.produkte[j], self.produkte[j + 1] = self.produkte[j + 1], self.produkte[j]
    
    def produktInListe(self, produktname):
        produkt_nicht_enthalten = True
        for produkt in self.produkte:
            bezeichnung = produkt[0]
            if bezeichnung == produktname:
                produkt_nicht_enthalten = False
                preis = produkt[1]
                print(f"Produkt {produktname} kostet {preis} €!")
                return True
        if produkt_nicht_enthalten:
            print(produktname + " (noch) nicht in Liste enthalten!")
            return False
    
    def addProduct(self, name, preis):
        if not self.produktInListe(name):
            self.produkte.append([name, preis])
        else:
            for i in range(len(self.produkte)):
                produkt_bezeichnung = self.produkte[i][0]
                if produkt_bezeichnung == name:
                    self.produkte[i][1] = preis
        self.sortProducts(self.zuletztAufsteigend)
    
    def removeProduct(self, product):
        if self.produktInListe(product):
            gesuchte_teilliste = [product]
            for i in range(len(self.produkte)):
                sortiment_produkt = self.produkte[i]
                sortiment_produkt_bezeichnung = sortiment_produkt[0]
                sortiment_produkt_preis = sortiment_produkt[1]
                if product == sortiment_produkt_bezeichnung:
                    gesuchte_teilliste.append(sortiment_produkt_preis)
            self.produkte.remove(gesuchte_teilliste)
        else:
            print(f"Das Produkt mit der Bezeichnung {product} befindet sich noch nicht im Sortiment!")

# TESTEN:
produkte = [['Laptop', 1200], ['Smartphone', 800], ['Tablet', 500], ['Monitor', 300], ['Maus', 50]]

# Instanz erzeugen
mein_shop = OnlineShop(produkte)

# Objekt / Instanz als String ausgeben (Konsole)
print(mein_shop)

# überprüfen, ob Produkte unsortiert sind
print(mein_shop.produkteUnsortiert(True))

# produkte sortieren
mein_shop.sortProducts(True)
print(mein_shop)
#print(mein_shop.produkteUnsortiert(True))

# produkt in Liste vorhanden (Überprüfung)
produkt = ['iPhone', 650]
mein_shop.produktInListe(produkt[0])

# iPhone hinzufügen
mein_shop.addProduct(produkt[0], produkt[1])
print(mein_shop)

# Versuch, bereits vorhandenes Produkt hinzuzufügen:
neues_produkt = ['iPhone', 1000]
mein_shop.addProduct(neues_produkt[0], neues_produkt[1])
print(mein_shop)

# Produkt entfernen:
mein_shop.removeProduct(neues_produkt[0])
mein_shop.removeProduct("Nintendo Switch")
print(mein_shop)

mein_shop.addProduct("Drucker", 1000)
mein_shop.sortProducts(False)
print(mein_shop)