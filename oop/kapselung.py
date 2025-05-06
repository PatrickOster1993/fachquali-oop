class Konto:

    def __init__(self, blz, iban, pin):
        self.blz = blz
        self._iban = iban # Art "protected" --> aber nur Namenskonvention (kein echtes "protected")
        self.__pin = pin

    def __pinCorrect(self, pin):
        return self.__pin == pin
    
    def pinEingeben(self, pin):
        if self.__pinCorrect(pin):
            print("Anmeldung erfolgreich!")
        else:
            print("Falsche PIN!")


mein_konto = Konto("0239480244", "DExxxxxxxxxxx", "1345")
# print(mein_konto._Konto__pin) # technisch gesehen speichert Python __pin in andere Variable _Konto__pin (= "Names mangling")
# print(mein_konto.__pin) # direkter Zugriff nicht möglich --> Art "private" (= Python-Konvention)

mein_konto.pinEingeben("1434")
print(mein_konto.__pinCorrect("2344"))