class Stock :
    def __init__(self, name, price, volume) -> None:
        self.name = name
        self.price = price 
        self.volume = volume

    def __str__(self) -> str:
        return f"Aktueller Preis der Aktie {self.name} beträgt {self.price} und das Handelsvolumen {self.volume} "

    def __truediv__ (self,name, price, volume, splitfactor):
        pass

    def updatePrice(self, price, newprice):
        pass

    def getMarkedValue(self, name, price, volume):
        pass



# #Operatorüberladung soll der Simulation eines sog.
# „Aktiensplits“ dienen. Dabei soll der Preis der Aktie durch den übergebenen Split-Faktor
# geteilt, und das Volumen der Aktie mit dem gleichen Faktor multipliziert werden. Nach
# der Berechnung soll die Methode das Stock-Objekt selbst zurückgeben, sodass der Split
# direkt auf das Objekt angewendet wird.