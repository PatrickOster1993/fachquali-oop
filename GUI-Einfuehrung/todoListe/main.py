import sys
from PyQt5.QtWidgets import QApplication

# Importiere unsere MVC-Komponenten
from models.todo_model import TodoList
from models.storage import TodoStorage
from views.main_view import TodoView
from controllers.todo_controller import TodoController

def main():
    """
    Hauptfunktion der Anwendung.
    Erstellt die MVC-Komponenten und startet die Anwendung.
    """
    # PyQt-Anwendung erstellen
    app = QApplication(sys.argv)
    
    # Speichermechanismus initialisieren
    storage = TodoStorage("my_todos.json")
    
    # MVC-Komponenten initialisieren
    model = TodoList(storage)  # Speicher an das Modell übergeben
    view = TodoView()
    controller = TodoController(model, view)
    
    # Wenn keine Todos vorhanden sind (z.B. beim ersten Start),
    # füge einige Beispiele hinzu
    if len(model.get_all_items()) == 0:
        controller.add_todo("PyQt5 und MVC-Pattern lernen")
        controller.add_todo("Clean Code-Prinzipien anwenden")
        controller.add_todo("Eine tolle Todo-App entwickeln")
    
    # View anzeigen
    view.show()
    
    # Anwendungsschleife starten
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()