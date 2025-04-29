from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QListWidget, QLineEdit, QPushButton, QLabel)
from PyQt5.QtCore import Qt, pyqtSignal

class TodoView(QMainWindow):
    """
    Die Hauptansicht unserer Todo-Anwendung.
    
    Die View ist zuständig für die Darstellung der Benutzeroberfläche und
    das Weiterleiten von Benutzeraktionen. Sie kommuniziert nicht direkt
    mit dem Model, sondern sendet Signale an den Controller.
    """
    
    # Definiere Signale, die vom Controller abgefangen werden können
    add_todo_signal = pyqtSignal(str)
    remove_todo_signal = pyqtSignal(int)
    toggle_todo_signal = pyqtSignal(int)
    
    def __init__(self):
        """Initialisiert die Hauptansicht mit allen UI-Elementen."""
        super().__init__()
        
        # Fenstertitel und Grundabmessungen festlegen
        self.setWindowTitle("MVC Todo-Liste")
        self.setGeometry(100, 100, 500, 600)
        
        # Zentrales Widget und Layout erstellen
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # UI-Komponenten initialisieren
        self._setup_ui()
    
    def _setup_ui(self):
        """Richtet alle UI-Komponenten ein und verbindet Signale."""
        # Header
        header_label = QLabel("Meine Todo-Liste")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(header_label)
        
        # Eingabebereich für neue Todos
        input_layout = QHBoxLayout()
        
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Neues Todo eingeben...")
        self.todo_input.returnPressed.connect(self._on_add_clicked)
        input_layout.addWidget(self.todo_input, 7)
        
        self.add_button = QPushButton("Hinzufügen")
        self.add_button.clicked.connect(self._on_add_clicked)
        input_layout.addWidget(self.add_button, 3)
        
        self.main_layout.addLayout(input_layout)
        
        # Liste der Todos
        self.todo_list = QListWidget()
        self.todo_list.setStyleSheet("QListWidget::item { padding: 6px; }")
        self.todo_list.itemDoubleClicked.connect(self._on_item_double_clicked)
        self.main_layout.addWidget(self.todo_list)
        
        # Entfernen-Button
        self.remove_button = QPushButton("Ausgewähltes Todo entfernen")
        self.remove_button.clicked.connect(self._on_remove_clicked)
        self.main_layout.addWidget(self.remove_button)
    
    def _on_add_clicked(self):
        """Handler für das Hinzufügen eines neuen Todos."""
        todo_text = self.todo_input.text().strip()
        if todo_text:
            # Signal an den Controller senden
            self.add_todo_signal.emit(todo_text)
            # Eingabefeld leeren
            self.todo_input.clear()
    
    def _on_remove_clicked(self):
        """Handler für das Entfernen des ausgewählten Todos."""
        current_item = self.todo_list.currentRow()
        if current_item >= 0:
            # Signal an den Controller senden
            self.remove_todo_signal.emit(current_item)
    
    def _on_item_double_clicked(self, item):
        """
        Handler für Doppelklick auf ein Todo-Item.
        Wird verwendet, um den Erledigungsstatus zu ändern.
        """
        index = self.todo_list.row(item)
        self.toggle_todo_signal.emit(index)
    
    def update_todo_list(self, todo_items):
        """
        Aktualisiert die Todo-Liste in der Benutzeroberfläche.
        
        Args:
            todo_items (list): Liste von TodoItem-Objekten
        """
        self.todo_list.clear()
        for item in todo_items:
            status = "✓" if item.completed else "☐"
            self.todo_list.addItem(f"{status} {item.title}")
            
    def show_info(self, message):
        """
        Zeigt eine Informationsnachricht in der Statusleiste an.
        
        Args:
            message (str): Die anzuzeigende Nachricht
        """
        self.statusBar().showMessage(message, 3000)  # Zeigt die Nachricht für 3 Sekunden