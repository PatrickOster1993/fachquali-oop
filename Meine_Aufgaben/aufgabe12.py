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

    def addStock (self, stock):
        self.stocks.append(stock)
        return f"Aktie {stock.name} Hinzugefügt"
        

    def removeStock (self, stock):
        self.stocks.remove(stock)
        return f"Aktie {stock.name} wurde gelöscht"

    def getStockByName(self, name):
        if self.search(name):
            print (self.stocks[name])
            return None
        else: 
            print ("Nichts gefunden du opfer")
            return None
        
        

    def search(self, search):
        for i in self.stocks:
            print(i)
            if search == i.name:
                return search

    def getStockAmount (self):
        pass

    def listStocks (self):
        a= "Stocks:\n"
        for stock in self.stocks:
            a += stock.name +"\n"
        return a

    def __str__(self) -> str:
        return (f"Börse {self.boerse} location {self.location} currency {self.currency} established year {self.establishedyear}. {self.listStocks()}")
    
        


boerse1 = Exchange("bitvavo", "germany", "euro", 2010)

stock1 = Stock("XRP", 2.10, 1000000 )
stock2 = Stock("XRP2", 2.10, 1000000 ) 
stock3 = Stock("XRP3", 2.10, 1000000 )
stock4 = Stock("XRP4", 2.10, 1000000 )

print (stock1)

boerse1.addStock(stock1)
boerse1.addStock(stock2)
boerse1.addStock(stock3)
boerse1.addStock(stock4)


print (boerse1)

remove =(boerse1.removeStock(stock1))
print (remove)

print (boerse1.listStocks())

nameeee= boerse1.search("XRP3")

print (nameeee)
sname = boerse1.getStockByName("XRP3")
print (sname)