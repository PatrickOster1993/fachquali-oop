class Stock:
    def __init__(self, name, price, __volume):
        self.name = name
        self.__price = price
        self.__volume = __volume

    def updatePrice(self, newPrice):
        self.__price = newPrice
    
    def getMarketValue(self):
        return self.__price * self.__volume

    def __str__(self):
        return f"Name der Aktie: {self.name} | Kurs: {self.__price} | Handels__volumen: {self.__volume}"
    
    def __truediv__(self, splitFactor):
        if splitFactor <= 0:
            raise ValueError("Der Split-Faktor muss größer als 0 sein.")
        
        self.__price /= splitFactor
        self.__volume *= splitFactor
        return self
    
class Exchange:
    def __init__(self, name, location, currency, establishedYear):
        self.name = name
        self.location = location
        self.currency = currency
        self.establishedYear = establishedYear
        self.__stocks = []

    def addStock(self, stock):
        self.__stocks.append(stock)
    
    def removeStock(self, stock):
        if stock in self.__stocks:
            self.__stocks.remove(stock)
        else:
            print("{stock} is not listed.")

    def getStockByName(self, name):
        for stock in self.__stocks:
            if name == stock.name:
                return stock

    def getStockCount(self):
        return len(self.__stocks)

    def list__stocks(self):
        print("\n".join(str(stock) for stock in self.__stocks))

vw = Stock("VW", 167.79, 10000)
daimler = Stock("Daimler", 120.56, 10000000)
frankfurt = Exchange("Frankfurt", "Frankfurt", "EUR", 1920)

print(daimler.getMarketValue())

frankfurt.addStock(vw)
frankfurt.addStock(daimler)
frankfurt.list__stocks()

daimler /= 2
frankfurt.list__stocks()
print(daimler)
print(frankfurt.getStockCount())

# ### **5. Zeichnen Sie abschließend ein Sequenzdiagramm für Ihren in Unterpunkt „3.“ beschriebenen Programmablauf.**  