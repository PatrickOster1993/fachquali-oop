# Aufgabe 12   Klassen- und Sequenzdiagramm
# Werfen  Sie  einen  Blick  auf  das  Ihnen  vorliegende  Klassendiagramm,  welches  das  Zusammenspiel 
# zwischen einer Börse und, an der jeweiligen Börse gelisteten, Unternehmen veranschaulichen soll. 
# Führen Sie nun die nachfolgenden Arbeitsschritte aus:
# 1. Erstellen  Sie  zunächst  die  Klasse  Stock,  indem  Sie  folgende  Attribute  und  Methoden 
# hinzufügen (denken Sie dabei auch an die Erstellung eines geeigneten Konstruktors):
# - name: Name des der Aktie zugrundeliegenden Unternehmens
# - price: aktueller Preis der Aktie
# - volume: aktuelles Handelsvolumen der Aktie
# - __str__():  Soll  eine  geeignete,  lesbare  Darstellung  der  wichtigsten  Informationen  der 
# Aktie liefern.
# - __truediv__(splitFactor): Operatorüberladung soll der Simulation eines sog. 
# „Aktiensplits“ dienen. Dabei soll der Preis der Aktie durch den übergebenen Split-Faktor 
# geteilt, und das Volumen der Aktie mit dem gleichen Faktor multipliziert werden. Nach 
# der  Berechnung  soll  die  Methode  das  Stock-Objekt  selbst  zurückgeben,  sodass  der  Split 
# direkt auf das Objekt angewendet wird.
# - updatePrice(newPrice):  Soll  das  Attribut  „price“  mit  dem  übergebenen  Argument 
# „newPrice“ überschreiben.
# - getMarketValue():  Soll  den  Marktwert  einer  Aktie  berechnen,  indem  das  Produkt  aus 
# dem Preis und dem Volumen zurückgegeben wird.
# 2. Erstellen  Sie  daraufhin  die  Klasse  Exchange,  indem  Sie  folgende  Attribute  und  Methoden 
# hinzufügen (denken Sie auch hier an die Erstellung eines geeigneten Konstruktors):
# - name: Name der Börse (z. B. „NASDAQ“)
# - location: Geographische Lage der Börse (z. B. „USA“)
# - currency: Währung, in der gehandelt wird (z. B. „USD“)
# - establishedYear: Gründungsjahr der Börse
# - stocks: Liste aller aller an der entsprechenden Börse gelisteter Aktien
# - addStock(stock): Soll die als Argument übergebene Aktie der als Attribut hinterlegten 
# Liste „stocks“ hinzufügen.
# - removeStock(stock):  Soll  die  als  Argument  übergebene  Aktie  aus  der  als  Attribut 
# hinterlegten  Liste  „stocks“  entfernen,  sofern  sich  diese  innerhalb  der  Liste  befindet. 
# Andernfalls soll eine entsprechende Meldung in der Konsole ausgegeben werden.
# - getStockByName(name): Soll die jeweilige, sich in der Liste befindenden, Aktie 
# zurückgeben, deren Name sich mit dem als Argument übergebenen Namen deckt.
# - getStockByName(): Soll die Anzahl der sich in der Liste befindenden Aktien 
# zurückgeben.
# - listStocks():  Soll  alle  sich  in  der  Liste  befindenden  Aktien  sowie  deren  wichtigsten 
# Informationen in einer gut lesbaren, strukturierten Form in der Konsole ausgeben.
# 3. Testen  Sie im Nachfolgenden Ihre Implementierungen, indem Sie mehrere Objekte / 
# Instanzen der Klassen erzeugen und alle implementierten Methoden anwenden.
# 4. Entspricht  die  Beziehung  zwischen  „Exchange“  und  „Stock“  einer  Aggregations-  oder 
# Kompositionsbeziehung?
# 5. Zeichnen Sie abschließend ein Sequenzdiagramm für Ihren in Unterpunkt „3.“ 
# Programmablauf.





# Klasse Stock
class Stock:
    def __init__(self, name, price, volume):
        self.name = name  # Name des Unternehmens
        self.price = price  # Aktueller Preis der Aktie
        self.volume = volume  # Aktuelles Handelsvolumen

    def __str__(self):
        return f"Aktie: {self.name}, Preis: {self.price}, Volumen: {self.volume}"

    def __truediv__(self, splitFactor):
        """Operatorüberladung für Aktiensplit"""
        if splitFactor <= 0:
            raise ValueError("Split-Faktor muss größer als 0 sein.")
        self.price /= splitFactor
        self.volume *= splitFactor
        return self

    def updatePrice(self, newPrice):
        """Aktualisiert den Preis der Aktie"""
        if newPrice > 0:
            self.price = newPrice
        else:
            print("Der Preis muss positiv sein.")

    def getMarketValue(self):
        """Berechnet den Marktwert der Aktie"""
        return self.price * self.volume


# Klasse Exchange
class Exchange:
    def __init__(self, name, location, currency, establishedYear):
        self.name = name  # Name der Börse
        self.location = location  # Geographische Lage
        self.currency = currency  # Währung
        self.establishedYear = establishedYear  # Gründungsjahr
        self.stocks = []  # Liste der gelisteten Aktien

    def addStock(self, stock):
        """Fügt eine Aktie zur Liste hinzu"""
        self.stocks.append(stock)

    def removeStock(self, stock):
        """Entfernt eine Aktie aus der Liste"""
        if stock in self.stocks:
            self.stocks.remove(stock)
        else:
            print(f"Die Aktie {stock.name} ist nicht an der Börse gelistet.")

    def getStockByName(self, name):
        """Gibt eine Aktie basierend auf dem Namen zurück"""
        for stock in self.stocks:
            if stock.name == name:
                return stock
        return None

    def getStockCount(self):
        """Gibt die Anzahl der gelisteten Aktien zurück"""
        return len(self.stocks)

    def listStocks(self):
        """Gibt alle gelisteten Aktien in lesbarer Form aus"""
        if not self.stocks:
            print("Keine Aktien an der Börse gelistet.")
        else:
            print(f"Aktien an der {self.name} ({self.location}, {self.currency}):")
            for stock in self.stocks:
                print(stock)


# Testen der Implementierung
if __name__ == "__main__":
    # Erstellen von Aktien
    stock1 = Stock("Apple", 150.0, 1000000)
    stock2 = Stock("Microsoft", 300.0, 500000)
    stock3 = Stock("Tesla", 750.0, 200000)

    # Erstellen einer Börse
    nasdaq = Exchange("NASDAQ", "USA", "USD", 1971)

    # Aktien zur Börse hinzufügen
    nasdaq.addStock(stock1)
    nasdaq.addStock(stock2)
    nasdaq.addStock(stock3)

    # Liste der Aktien anzeigen
    nasdaq.listStocks()

    # Aktiensplit simulieren
    print("\nSimuliere Aktiensplit für Apple (Faktor 2):")
    stock1 = stock1 / 2
    print(stock1)

    # Aktualisieren des Preises einer Aktie
    print("\nAktualisiere Preis von Tesla auf 800.0:")
    stock3.updatePrice(800.0)
    print(stock3)

    # Marktwert berechnen
    print("\nMarktwert von Microsoft:")
    print(stock2.getMarketValue())

    # Aktie entfernen
    print("\nEntferne Aktie Microsoft:")
    nasdaq.removeStock(stock2)
    nasdaq.listStocks()

    # Suche nach einer Aktie
    print("\nSuche nach Aktie Apple:")
    found_stock = nasdaq.getStockByName("Apple")
    if found_stock:
        print(found_stock)
    else:
        print("Aktie nicht gefunden.")

    # Anzahl der Aktien anzeigen
    print("\nAnzahl der Aktien an der Börse:")
    print(nasdaq.getStockCount())
