import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorView(QWidget):
    def __init__(self, controller):
        """
        Initialisiert die View mit einem Controller.
        """
        super().__init__()
        self.controller = controller
        
        # Fenster konfigurieren
        self.setWindowTitle('PyQt5 Taschenrechner (MVC)')
        self.setFixedSize(300, 400)
        
        # UI aufbauen
        self.init_ui()
    
    def init_ui(self):
        """
        Initialisiert die Benutzeroberfläche.
        """
        # Hauptlayout erstellen
        main_layout = QVBoxLayout()
        
        # Display erstellen
        self.display_field = QLineEdit()
        self.display_field.setReadOnly(True)          # Nur für Anzeige
        self.display_field.setAlignment(Qt.AlignRight)  # Text rechtsbündig
        self.display_field.setFixedHeight(50)         # Höhe festlegen
        main_layout.addWidget(self.display_field)     # Zum Layout hinzufügen
        
        # Grid-Layout für Tasten erstellen
        buttons_layout = QGridLayout()
        
        # Definition der Tasten und ihrer Positionen
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]
        
        # Tasten erstellen und hinzufügen
        self.buttons_dict = {}
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(50, 50)  # Einheitliche Größe
            
            # Lambda mit Standardparameter für den Button-Text
            button.clicked.connect(lambda checked, text=button_text: 
                                 self.controller.handle_button_click(text))
            
            buttons_layout.addWidget(button, row, col)
            self.buttons_dict[button_text] = button
        
        # Layouts zusammenfügen
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
    
    def update_display(self, text):
        """
        Aktualisiert das Anzeigefeld.
        """
        self.display_field.setText(text)
    
    def show_app(self):
        """
        Zeigt die Anwendung an.
        """
        self.show()