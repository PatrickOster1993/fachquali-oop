class Stock :
    def __init__(self, name, price, volume) -> None:
        self.name = name
        self.price = price 
        self.volume = volume

    def __str__(self) -> str:
        return f"Aktueller Preis der Aktie {self.name} beträgt {self.price} und das Handelsvolumen {self.volume} "

    def __truediv__ (self,name, price, volume, splitfactor):
        pass

    def updatePrice(self, name,  price, newprice):
        pass

    def getMarkedValue(self, name, price, volume):
        pass



# #Operatorüberladung soll der Simulation eines sog.
# „Aktiensplits“ dienen. Dabei soll der Preis der Aktie durch den übergebenen Split-Faktor
# geteilt, und das Volumen der Aktie mit dem gleichen Faktor multipliziert werden. Nach
# der Berechnung soll die Methode das Stock-Objekt selbst zurückgeben, sodass der Split
# direkt auf das Objekt angewendet wird.

class Exchange:
    def __init__(self, boerse, location, currency, establishedyear) -> None:
        self.boerse = boerse
        self.location = location
        self.currency = currency
        self.establishedyear = establishedyear
        self.stocks = []

    def addStock (self, stocks):
        self.stocks.append(stocks)
        return f"Aktie Hinzugefügt"
        

    def removeStock (self, stocks):
        pass

    def getStockByName(self, name):
        pass

    def getStockAmount (self):
        pass

    def listStocks (self):
        pass

    # def __str__(self) -> str:
    #     return f"Börse {self.boerse} location {self.location} currency {self.currency} established year {self.establishedyear} stocks {self.stocks}"


boerse1 = Exchange("bitvavo", "germany", "euro", 2010)

stock1 = Stock("XRP", 2.10, 1000000 )

print (stock1)

boerse1.addStock(stock1)
print (boerse1)