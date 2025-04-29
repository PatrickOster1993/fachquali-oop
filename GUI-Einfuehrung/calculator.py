# sys Wird benötigt, um Programm ordentlich zu beenden
import sys

# Widgets, die wir benötigen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# QApplication: Erstellen einer Instanz ihrer Applikation
# QWidget: Basisklasse (= Elternklasse), die etwaige, für das Fenster erforderliche Attribute, Methoden, ... besitzt.
# QVBoxLayout: Erstellt ein vertikales Layout, um grafische Elemente (= Widgets) untereinander anzuordnen / stacken

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.running = True
        self.display = ""
        self.initUI()
    
    def initUI(self):
        print("Mein Taschenrechner")
        print("###################")
        

    def onButtonClicked(self):
        text = self.display.lower()
        if text == 'exit':
            print("Taschenrechner wird beendet!")
            self.running = False
        elif text == 'c':
            print("Bildschirm bereinigt!")
            self.display = ""
        elif text == '=':
            print("Nichts zu berechnen. Bitte Berechnung eingeben!")
        else:
            result = round(float(eval(text)), 8)
            print(f"Ergebnis: {result}")

app = QApplication(sys.argv) # sys.argv -> ordentliches Beenden (Integration von GUI in "Systemlandschaft") (*)
my_calculator = Calculator()

my_calculator.show()

sys.exit(app.exec_()) # (*) + initiales Starten der Ereignisschleife für Benutzerinteraktion.

