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
        for i in range(len(self._stocks)):
                stockName = self._stocks[i]
                if stockName._name == name:
                    return f"Aktie: {name} ist vorhanden."
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

stock_ing = Stock("ING Group", 17.44, 1_000_000)

print(stock_ing)
print("####################################################")
stock_ing/2

print(stock_ing)
print("####################################################")

stock_ing._updatePrice(9.00)

print(stock_ing)
print("####################################################")

print(f"Marktvolumen: {stock_ing.getMarketValue()}€")

print("####################################################")


###########################################################
############# Aufgabe 2 und 3 Abfragen ####################

exchange_nyse = Exchange("NYSE", "New York", "USD", 1971)

print(exchange_nyse)

print("####################################################")

stock_caterpillar = Stock("Caterpillar", 250, 1_500_000)

exchange_nyse._addStock(stock_caterpillar)

exchange_nyse.listStocks()
print("####################################################")

# exchange_nyse._removeStock("Coca-Cola")

exchange_nyse.listStocks()
print("####################################################")

print(exchange_nyse.getStockByName("Caterpillar"))

print("####################################################")

print(f"Aktienanzahl: {exchange_nyse.getAmountOfStock()}")

print("####################################################")

###########################################################
############# Aufgabe 4 ###################################
