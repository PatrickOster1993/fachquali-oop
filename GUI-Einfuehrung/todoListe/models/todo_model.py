class TodoItem:
    """
    Repräsentiert einen einzelnen Todo-Eintrag.
    
    Das Model ist verantwortlich für die Datenhaltung und Geschäftslogik.
    Es weiß nichts über die Benutzeroberfläche oder wie die Daten angezeigt werden.
    """
    def __init__(self, title, completed=False):
        """
        Initialisiert ein neues Todo-Item.
        
        Args:
            title (str): Der Titel oder die Beschreibung des Todo-Eintrags
            completed (bool): Status, ob das Todo erledigt ist (Standard: False)
        """
        self.title = title
        self.completed = completed
        
    def toggle_completed(self):
        """Wechselt den Erledigungsstatus des Todo-Eintrags."""
        self.completed = not self.completed
        
    def __str__(self):
        """String-Repräsentation des Todo-Eintrags."""
        status = "✓" if self.completed else "☐"
        return f"{status} {self.title}"


class TodoList:
    """
    Verwaltet eine Sammlung von Todo-Einträgen.
    
    Diese Klasse dient als Container-Model für alle Todo-Items
    und implementiert Methoden zur Verwaltung der Liste.
    """
    def __init__(self, storage):
        """Initialisiert eine leere Todo-Liste."""
        self.storage = storage
        self.items = []
        self._load_from_storage()
        
    def add_item(self, title):
        """
        Fügt ein neues Todo-Item zur Liste hinzu.
        
        Args:
            title (str): Titel des neuen Todo-Items
            
        Returns:
            TodoItem: Das neu erstellte TodoItem
        """
        item = TodoItem(title)
        self.items.append(item)
        return item
        
    def remove_item(self, index):
        """
        Entfernt ein Todo-Item anhand seines Index.
        
        Args:
            index (int): Index des zu entfernenden Items
            
        Returns:
            TodoItem: Das entfernte Item oder None bei ungültigem Index
        """
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None
    
    def get_all_items(self):
        """
        Gibt alle Todo-Items zurück.
        
        Returns:
            list: Liste aller TodoItems
        """
        return self.items
    
    def _save_to_storage(self):
        """
        Private Methode zum Speichern in den persistenten Speicher.
        Wird nach jeder Änderung an der Liste aufgerufen.
        """
        if self.storage:
            self.storage.save_todos(self.items)

    def _load_from_storage(self):
        """
        Private Methode zum Laden aus dem persistenten Speicher.
        Wird bei der Initialisierung aufgerufen.
        """
        if self.storage:
            # Lade gespeicherte Daten
            loaded_items = self.storage.load_todos()
            
            # Konvertiere die geladenen Daten in TodoItem-Objekte
            self.items = []
            for item_data in loaded_items:
                self.items.append(TodoItem(
                    title=item_data['title'],
                    completed=item_data['completed']
                ))