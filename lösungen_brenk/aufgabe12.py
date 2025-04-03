class Stock:
    def __init__(self, name, price, volume):
        self.name = name
        self.__price = price
        self.volume = volume

    def updatePrice(self, newPrice):
        self.__price = newPrice
    
    def getMarketValue(self):
        return self.__price * self.volume

    def __str__(self):
        return f"Name der Aktie: {self.name} | Kurs: {self.__price} | Handelsvolumen: {self.volume}"
    
    def __truediv__(self, splitFactor):
        if splitFactor <= 0:
            raise ValueError("Der Split-Faktor muss größer als 0 sein.")
        
        self.__price /= splitFactor
        self.volume *= splitFactor
        return self
    
class Exchange:
    def __init__(self, name, location, currency, establishedYear):
        self.name = name
        self.location = location
        self.currency = currency
        self.establishedYear = establishedYear
        self.stocks = []

    def addStock(self, stock):
        self.stocks.append(stock)
    
    def removeStock(self, stock):
        if stock in self.stocks:
            self.stocks.remove(stock)
        else:
            print("{stock} is not listed.")

    def getStockByName(self, name):
        for stock in self.stocks:
            if name == stock.name:
                return stock

    def getStockCount(self):
        return len(self.stocks)

    def listStocks(self):
        print("\n".join(str(stock) for stock in self.stocks))

vw = Stock("VW", 167.79, 10000)
daimler = Stock("Daimler", 120.56, 10000000)
frankfurt = Exchange("Frankfurt", "Frankfurt", "EUR", 1920)

print(daimler.getMarketValue())

frankfurt.addStock(vw)
frankfurt.addStock(daimler)
frankfurt.listStocks()

daimler /= 2
frankfurt.listStocks()

print(frankfurt.getStockCount())

# ### **5. Zeichnen Sie abschließend ein Sequenzdiagramm für Ihren in Unterpunkt „3.“ beschriebenen Programmablauf.**  