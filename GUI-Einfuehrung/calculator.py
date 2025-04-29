# Wird benötigt um Program ordentlich zu beenden
import sys

# Widgets die wir benötigen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print("Mein Taschenrecher")
        print("##################")

        vbox = QVBoxLayout()

        self.display = QLineEdit()
        vbox.addWidget(self.display) # einzelnes graphisches Element ( Texteingabefeld )

        grid = QGridLayout()

        

        self.setLayout(vbox) # Hauptlayout auf Fenster anwenden
        self.setWindowTitle("Taschenrechner")

    
    def onButtonClicked(self):
        pass

app = QApplication(sys.argv)
my_calculator = Calculator()

my_calculator.show()

sys.exit(app.exec_())

