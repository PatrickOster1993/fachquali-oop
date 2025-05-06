import sys

from PyQt5.QtWidgets import QApplication
from calculator import Calculator

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

main()