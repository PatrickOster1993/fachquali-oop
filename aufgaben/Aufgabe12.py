###########################################################
############# Aufgabe 1 Code ##############################


class Stock:

    def __init__(self, name:str, price:int, volume:int):
        self._name = name
        self._price = price
        self._volume = volume

    def __str__(self):
        return f"Name: {self._name}\nPreis: {self._price}\nVolumen: {self._volume}"
    
    def __truediv__(self, splitFactor):
        priceAfterSplit = self._price / splitFactor
        volumeAfterSplit = self._volume * splitFactor
        self._price = priceAfterSplit
        self._volume = volumeAfterSplit
        return self._price / splitFactor and self._volume * splitFactor
    
    def _updatePrice(self, newPrice):
        self._price = newPrice
        return self._price

    def getMarketValue(self):
        marketValue = self._price * self._volume
        return marketValue



###########################################################
############# Aufgabe 2 Code ##############################

class Exchange:

    def __init__(self, name:str, location:str, currency:str, establishedYear:int):
        self._name = name
        self._location = location
        self._currency = currency
        self._establishedYear = establishedYear
        self._stocks = []

    def _addStock(self, stock:str):
        self._stocks.append(stock)

    def _removeStock(self, stock:str):
        self._stocks.remove(stock)

    def getStockByName(self, name:str):
        if name in self._stocks:
            return f"Aktie: {name} ist vorhanden."
        else:
            return f"Aktie {name} ist nicht vorhanden."
        
    def getAmountOfStock(self):
        return len(self._stocks)

    def listStocks(self):
        for stock in self._stocks:
            print(stock)
    
    def __str__(self):
        return f"Name: {self._name}\nStandort: {self._location}\nWährung: {self._currency}"

###########################################################
############# Aufgabe 1 Abfragen ##########################

mystock = Stock("ING Group", 17.44, 1_000_000)

print(mystock)
print("####################################################")
mystock/2

print(mystock)
print("####################################################")

mystock._updatePrice(9.00)

print(mystock)
print("####################################################")

print(f"Marktvolumen: {mystock.getMarketValue()}€")

print("####################################################")


###########################################################
############# Aufgabe 2 Abfragen ##########################

myExchange = Exchange("NYSE", "New York", "USD", 1971)

print(myExchange)

print("####################################################")

myExchange._addStock("Caterpillar")
myExchange._addStock("Coca-Cola")
myExchange._addStock("UnitedHealth")

myExchange.listStocks()
print("####################################################")

myExchange._removeStock("Coca-Cola")

myExchange.listStocks()
print("####################################################")

print(myExchange.getStockByName("Caterpillar"))

print("####################################################")

print(f"Aktienanzahl: {myExchange.getAmountOfStock()}")