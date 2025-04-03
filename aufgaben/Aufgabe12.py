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