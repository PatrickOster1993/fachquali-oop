class TodoController:
    """
    Der Controller für unsere Todo-Anwendung.
    
    Der Controller verbindet das Model mit der View und enthält die Anwendungslogik.
    Er reagiert auf Benutzereingaben aus der View und aktualisiert sowohl
    das Model als auch die Anzeige in der View.
    """
    
    def __init__(self, model, view):
        """
        Initialisiert den Controller mit Referenzen auf Model und View.
        
        Args:
            model (TodoList): Das Datenmodell unserer Anwendung
            view (TodoView): Die Benutzeroberfläche
        """
        self.model = model
        self.view = view
        
        # View-Signale mit Controller-Methoden verbinden
        self.view.add_todo_signal.connect(self.add_todo)
        self.view.remove_todo_signal.connect(self.remove_todo)
        self.view.toggle_todo_signal.connect(self.toggle_todo)
        
        # Initial die View mit Daten aus dem Model aktualisieren
        self.update_view()
        
    def add_todo(self, title):
        """
        Fügt ein neues Todo hinzu und aktualisiert die View.
        
        Args:
            title (str): Der Titel des neuen Todos
        """
        self.model.add_item(title)
        self.update_view()
        self.view.show_info(f"Todo '{title}' wurde hinzugefügt")
        
    def remove_todo(self, index):
        """
        Entfernt ein Todo anhand seines Index und aktualisiert die View.
        
        Args:
            index (int): Index des zu entfernenden Todos
        """
        removed_item = self.model.remove_item(index)
        if removed_item:
            self.update_view()
            self.view.show_info(f"Todo '{removed_item.title}' wurde entfernt")
        
    def toggle_todo(self, index):
        """
        Ändert den Erledigungsstatus eines Todos und aktualisiert die View.
        
        Args:
            index (int): Index des zu ändernden Todos
        """
        if 0 <= index < len(self.model.items):
            todo_item = self.model.items[index]
            todo_item.toggle_completed()
            self.update_view()
            
            status = "erledigt" if todo_item.completed else "nicht erledigt"
            self.view.show_info(f"Todo '{todo_item.title}' als {status} markiert")
    
    def update_view(self):
        """
        Aktualisiert die View mit den aktuellen Daten aus dem Model.
        Diese Methode synchronisiert die Anzeige mit dem Datenmodell.
        """
        self.view.update_todo_list(self.model.get_all_items())