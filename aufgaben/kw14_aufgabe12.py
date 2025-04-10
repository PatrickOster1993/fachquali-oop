class Stock:

    def __init__(self, name, price, volume):
        self.name = name
        self.__price = price
        self.__volume = volume

    def __str__(self):
        return f"Aktie: {self.name} | Preis: {self.__price} | Volumen: {self.__volume}"

    def __truediv__(self, splitFactor):
        self.__price /= splitFactor
        self.__volume *= splitFactor

        return self

    def updatePrice(self, newPrice):
        self.__price = newPrice

    def getMarketValue(self):
        return self.__price * self.__volume
    
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
            print(f"Die Atie {stock.name} ist nicht in der Börse {self.name} gelistet!")

    def getStockByName(self, name):
        for stock in self.__stocks:
            if name == stock.name:
                return stock
        return None # Ich will in einem Getter immer etwas zurückgeben... falls Aktie nicht vorhanden, dann einfach None!

    def getStockCount(self):
        return len(self.__stocks)

    def listStocks(self):
        if not self.__stocks:
            print(f"Keine Aktien in der Börse {self.name} gelistet!")
        else:
            print(f"Aktien in der Börse {self.name}:")
            for stock in self.__stocks:
                print(stock)

############ Programmablauf "Börse" ##############
stock1 = Stock("Apfel", 150, 1000)
stock2 = Stock("Mikroweich", 100, 850)

print("Marktwert von Apfel:", stock1.getMarketValue())

stock2 /= 2
print("Marktwert von Mikroweich:", stock2.getMarketValue())

nasdaq = Exchange("NASDAQ", "USA", "USD", 1971)
nasdaq.addStock(stock1)
nasdaq.addStock(stock2)
nasdaq.listStocks()
######### Programmablauf "Börse" (Ende) ###########





# my_stock = Stock("Mikroweich", 1, 1000)
# print(my_stock)
# my_stock /= 2 # my_stock = my_stock / 2
# print(my_stock)

# zahl = 6

# print(zahl)

# print(zahl / 2)

# print(zahl)

# zahl /= 2 # zahl = zahl / 2

# print(zahl)
# print(zahl)

# stock / 2
# stock /= 2 --> stock = stock / 2

# __truediv__() <=> /