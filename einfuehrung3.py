class Rechteck:

    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite
    
    def getFlaeche(self):
        return self.laenge * self.breite
    
    def getUmfang(self):
        return 2 * (self.laenge + self.breite)
    
    def visualizeRechteck(self):
        print("Fläche visualisiert:")
        for i in range(self.breite + 1):
            for j in range(self.laenge + 1):
                zeichen = "#"
                if i == 0:
                    zeichen = j
                elif j == 0:
                    zeichen = i
                if zeichen == 0:
                    zeichen = " "
                print(zeichen, end=" ")
            print()

# mein_rechteck = Rechteck(3, 5)
# meine_flaeche = mein_rechteck.getFlaeche()
# mein_umfang = mein_rechteck.getUmfang()
# print("Fläche:", meine_flaeche, "Umfang:", mein_umfang)
# mein_rechteck.visualizeRechteck()

# dein_rechteck = Rechteck(6, 5)
# deine_flaeche = dein_rechteck.getFlaeche()
# dein_umfang = dein_rechteck.getUmfang()
# print("Fläche:", deine_flaeche, "Umfang:", dein_umfang)
# dein_rechteck.visualizeRechteck()

class Kreis:

    # Konstante (unabh. von Instanz!)
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def getFlaeche(self):
        return self.radius * self.radius * self.PI

    def getUmfang(self):
        return 2 * self.radius * self.PI
    

mein_kreis = Kreis(5)
print("Fläche:", mein_kreis.getFlaeche())
print("PI:", Kreis.PI)
