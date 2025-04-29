import sys
from PyQt5.QtWidgets import QApplication
from calculator_model import CalculatorModel
from calculator_controller import CalculatorController
from calculator_view import CalculatorView

def main():
    """
    Haupteinstiegspunkt der Anwendung.
    Erstellt die MVC-Komponenten und startet die Anwendung.
    """
    # QApplication erstellen
    app = QApplication(sys.argv)
    
    # MVC-Komponenten erstellen und verbinden
    model = CalculatorModel()
    controller = CalculatorController(model)
    view = CalculatorView(controller)
    
    # View dem Controller zuweisen
    controller.set_view(view)
    
    # Anwendung anzeigen und starten
    view.show_app()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()