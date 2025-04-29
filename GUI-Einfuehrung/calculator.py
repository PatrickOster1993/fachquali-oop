# sys Wird benötigt, um Programm ordentlich zu beenden
import sys

# Widgets, die wir benötigen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.running = True
        self.display = ""
        self.initUI()
    
    def initUI(self):
        # Hauptlayout für das Fenster
        main_layout = QVBoxLayout()
        
        # Anzeigefeld für die Eingabe und Ergebnisse
        self.display_field = QLineEdit()
        self.display_field.setReadOnly(True)  # Nur für Anzeige, keine direkte Eingabe
        self.display_field.setAlignment(Qt.AlignRight)  # Text rechtsbündig
        self.display_field.setFixedHeight(50)  # Legt die Höhe fest
        main_layout.addWidget(self.display_field)
        
        # Grid-Layout für die Tasten
        buttons_layout = QGridLayout()
        
        # Definition der Tasten und ihrer Positionen
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]
        
        # Erstellen und Hinzufügen der Tasten zum Layout
        self.buttons_dict = {}
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(50, 50)  # Feste Größe für alle Tasten
            button.clicked.connect(self.on_button_click)  # Verbinde mit Event-Handler
            buttons_layout.addWidget(button, row, col)
            self.buttons_dict[button_text] = button
        
        # Füge das Tasten-Layout zum Hauptlayout hinzu
        main_layout.addLayout(buttons_layout)
        
        # Setze das Hauptlayout für das Fenster
        self.setLayout(main_layout)
        
        # Fenstereigenschaften
        self.setWindowTitle('PyQt5 Taschenrechner')
        self.setFixedSize(300, 400)  # Feste Fenstergröße
        
        print("Mein Taschenrechner")
        print("###################")

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()
        
        if button_text == 'C':
            self.display_field.clear()
        elif button_text == '=':
            try:
                result = eval(self.display_field.text())
                self.display_field.setText(str(result))
            except Exception as e:
                self.display_field.setText("Error")
        else:
            current_text = self.display_field.text()
            self.display_field.setText(current_text + button_text)
    
    # Alte Methode kann entfernt oder umbenannt werden, falls du sie noch benötigst
    def onButtonClicked(self):
        text = self.display.lower()
        if text == 'exit':
            print("Taschenrechner wird beendet!")
            self.running = False
        elif text == 'c':
            print("Bildschirm bereinigt!")
            self.display = ""
        elif text == '=':
            print("Nichts zu berechnen. Bitte Berechnung eingeben!")
        else:
            result = round(float(eval(text)), 8)
            print(f"Ergebnis: {result}")

app = QApplication(sys.argv) # sys.argv -> ordentliches Beenden (Integration von GUI in "Systemlandschaft") (*)
my_calculator = Calculator()

my_calculator.show()

sys.exit(app.exec_()) # (*) + initiales Starten der Ereignisschleife für Benutzerinteraktion.