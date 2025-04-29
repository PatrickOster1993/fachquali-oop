import sys
from PyQt5.QtWidgets import QApplication

# Importiere unsere MVC-Komponenten
from models.todo_model import TodoList
from views.main_view import TodoView
from controllers.todo_controller import TodoController

def main():
    """
    Hauptfunktion der Anwendung.
    Erstellt die MVC-Komponenten und startet die Anwendung.
    """
    # PyQt-Anwendung erstellen
    app = QApplication(sys.argv)
    
    # MVC-Komponenten initialisieren
    model = TodoList()
    view = TodoView()
    controller = TodoController(model, view)
    
    # Ein paar Beispiel-Todos zum Testen hinzufügen
    controller.add_todo("PyQt5 und MVC-Pattern lernen")
    controller.add_todo("Clean Code-Prinzipien anwenden")
    controller.add_todo("Eine tolle Todo-App entwickeln")
    
    # View anzeigen
    view.show()
    
    # Anwendungsschleife starten
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()