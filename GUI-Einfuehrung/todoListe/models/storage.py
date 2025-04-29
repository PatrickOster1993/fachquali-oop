import json
import os

class TodoStorage:
    """
    Eine Klasse zur persistenten Speicherung von Todo-Items.
    
    Diese Klasse ist für die Datenspeicherung zuständig und erfüllt damit
    das Single Responsibility Principle (SRP) des SOLID-Designs.
    """
    
    def __init__(self, filename="todos.json"):
        """
        Initialisiert den Speichermechanismus.
        
        Args:
            filename (str): Der Dateiname für die Speicherung der Todos
        """
        self.filename = filename
    
    def save_todos(self, todo_items):
        """
        Speichert die Todo-Items in einer JSON-Datei.
        
        Args:
            todo_items (list): Eine Liste von TodoItem-Objekten
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        try:
            # Konvertiere TodoItems in ein serialisierbares Format
            serialized_items = []
            for item in todo_items:
                serialized_items.append({
                    'title': item.title,
                    'completed': item.completed
                })
            
            # In JSON-Datei speichern
            with open(self.filename, 'w') as file:
                json.dump(serialized_items, file, indent=2)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Todos: {e}")
            return False
    
    def load_todos(self):
        """
        Lädt Todo-Items aus einer JSON-Datei.
        
        Returns:
            list: Eine Liste von Dictionaries mit Todo-Daten oder eine leere Liste bei Fehler
        """
        if not os.path.exists(self.filename):
            return []
            
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Fehler beim Laden der Todos: {e}")
            return []