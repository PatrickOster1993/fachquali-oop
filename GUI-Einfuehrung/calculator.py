# sys Wird benötigt, um Programm ordentlich zu beenden
import sys

# Widgets, die wir benötigen
from PyQt5.QtGui import QPalette, QColor # eigene Farbgebung festlegen:)
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
# QLineEdit: erstellt uns ein Display, auf dem alle Eingaben und Ausgaben dargestellt werden
# QGridLayout: Ähnlich wie "Grid" in Webentwicklung, wodurch wir den "tabellarischen" Aufbau (Zeilen u. Spalten) festlegen können
# QPushButton: Button für die einzelnen Elemente auf Taschenrechner (z. B. '+' oder '5')

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        my_palette = QPalette()
        my_palette.setColor(QPalette.Background, QColor(57, 13, 120)) # nur Hintergrund
        # my_palette.setColor(QPalette.Window, QColor(77, 9, 0)) # Fenster selbst
        self.setPalette(my_palette)

        self.setFixedSize(400, 300)
        vbox = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setStyleSheet("font-size: 24px; height: 40px;")
        vbox.addWidget(self.display) # einzelnes graphisches Element (hier Texteingabefeld) dem Layout hinzufügen

        grid = QGridLayout()

        # Liste mit allen für grid erforderlichen Infos zu Button anlegen (wird später durch Schleife einfacher und cleaner!)
        
        # 7 8 9 /
        # 4 5 6 *
        # 1 2 3 -
        # 0 C = +
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('.', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4) # (... 1, 4) bedeutet: soll sich über 1 Zeile und 4 Spalten erstrecken
        ]
        # (Text auf Button, Zeile, Spalte) -> z. B. ('7', 0, 0)
        for item in buttons:
            btnText = item[0]
            row = item[1]
            col = item[2]
            rowSpan = 1
            colSpan = 1

            if len(item) > 3:
                rowSpan = item[3]
                colSpan = item[4]

            button = QPushButton(btnText)
            button.setStyleSheet("font-size: 24px; height: 40px;")
            button.clicked.connect(self.onButtonClicked) # Verbinden des jeweiligen Buttons mit der gewünschten "Klick-Funktionalität"
            grid.addWidget(button, row, col, rowSpan, colSpan) # 1, 1 = jeder Button soll in diesem Fall über 1 Zeile und Spalte gehen

        vbox.addLayout(grid) # einzelnes graphisches Element (hier Grid mit allen Buttons) dem Layout hinzufügen

        self.setLayout(vbox) # Hauptlayout auf Fenster anwenden!
        self.setWindowTitle("DAA-Taschenrechner") # Setzen des Fenstertitels

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
        sender = self.sender()
        text = sender.text() # Text auf jeweiligem Sender-Button
        # print(text) -> nur für Debugging-Zwecke

        if text.lower() == 'c':
            self.display.clear() # Inhalt auf Display leeren
        elif text.lower() == '=':
            result = round(eval(self.display.text()), 8) # Rechenoperation vornehmen (das was in Display gerade steht)
            self.display.setText(str(result)) # Ergebnis soll Display wieder updaten
        else:
            # bei allen anderen Eingaben sollen die Strings (z. B. eine Zahl) einfach hinter das Display platziert werden!
            self.display.setText(self.display.text() + text)

app = QApplication(sys.argv) # sys.argv -> ordentliches Beenden (Integration von GUI in "Systemlandschaft") (*)
app.setStyle('Fusion') # von PyQT zur Verfügung gestelltes "Theme" verwendet!
my_calculator = Calculator()

my_calculator.show() # Fenster anzeigen!

sys.exit(app.exec_()) # (*) + initiales Starten der Ereignisschleife für Benutzerinteraktion.