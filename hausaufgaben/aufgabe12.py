class Stock:

    def __init__(self, name, price, volume):
        self.name = name
        self.__price = price
        self.__volume = volume


    def __str__(self):
        return f"Name: {self.name}, Preis: {self.__price}, Volume: {self.__volume}."

    def __truediv__(self, splitFactor):
        self.__price = self.__price / splitFactor
        self.__volume = self.__volume * splitFactor
        return self
    
    def updatePrice(self, newPrice):
        self.__price = newPrice

    def getMarktetValue(self):
        return self.__price * self.__volume
    

class Exchange:

    def __init__(self, name, location, currency):
        self.name = name
        self.location = location
        self.currency = currency
        self.__stocks = []
    
    def addStock(self, stock):
        self.__stocks.append(stock)

    def removeStock(self, name):
        for stock in self.__stocks:
            if name == stock.name:
                self.__stocks.remove(stock)
            else:
                print(f"{name} nicht gefunden, konnte nicht entfernt werden!!")

    def getStockByName(self, name):
        for stock in self.__stocks:
            if name == stock.name:
                return stock

    def getStockCount(self):
        return len(self.__stocks)

    def listStocks(self): 
        print(f"bei {self.name} gelistete Unternehmen sind:/n")
        for stock in self.__stocks:
            print(str(stock))
            