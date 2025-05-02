# sys Wird benötigt, um Programm ordentlich zu beenden
import sys

# Widgets, die wir benötigen
from PyQt5.QtGui import QPalette, QColor # eigene Farbgebung festlegen:)
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
# QApplication: Erstellen einer Instanz ihrer Applikation
# QWidget: Basisklasse (= Elternklasse), die etwaige, für das Fenster erforderliche Attribute, Methoden, ... besitzt.
# QVBoxLayout: Erstellt ein vertikales Layout, um grafische Elemente (= Widgets) untereinander anzuordnen / stacken
# QLineEdit: erstellt uns ein Display, auf dem alle Eingaben und Ausgaben dargestellt werden
# QGridLayout: Ähnlich wie "Grid" in Webentwicklung, wodurch wir den "tabellarischen" Aufbau (Zeilen u. Spalten) festlegen können
# QPushButton: Button für die einzelnen Elemente auf Taschenrechner (z. B. '+' oder '5')

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        print("Mein Taschenrechner")
        print("###################")
        

    def onButtonClicked(self):
        sender = self.sender()
        text = sender.text() # Text auf jeweiligem Sender-Button
        # print(text) -> nur für Debugging-Zwecke

        if text.lower() == 'c':
            self.display.clear() # Inhalt auf Display leeren
        elif text.lower() == '=':
            result = round(eval(self.display.text()), 8) # Rechenoperation vornehmen (das was in Display gerade steht)
            self.display.setText(str(result)) # Ergebnis soll Display wieder updaten
        else:
            # bei allen anderen Eingaben sollen die Strings (z. B. eine Zahl) einfach hinter das Display platziert werden!
            self.display.setText(self.display.text() + text)

app = QApplication(sys.argv) # sys.argv -> ordentliches Beenden (Integration von GUI in "Systemlandschaft") (*)
app.setStyle('Fusion') # von PyQT zur Verfügung gestelltes "Theme" verwendet!
my_calculator = Calculator()

my_calculator.show() # Fenster anzeigen!

sys.exit(app.exec_()) # (*) + initiales Starten der Ereignisschleife für Benutzerinteraktion.