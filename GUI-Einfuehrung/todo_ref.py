# Notwendige Importe für die GUI-Anwendung
import sys
from PyQt5.QtGui import QPalette, QColor  # Für Farbgestaltung der Benutzeroberfläche
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton  # UI-Komponenten
from PyQt5.QtCore import Qt  # Qt-Konstanten für Ausrichtung und andere Eigenschaften

class CalculatorModel:
    """
    Die Model-Komponente im MVC-Muster.
    
    Verantwortlich für die Geschäftslogik des Taschenrechners und die Datenverwaltung.
    Führt Berechnungen durch und speichert den aktuellen Zustand ohne Abhängigkeiten zur UI.
    """
    def __init__(self):
        """
        Initialisiert das Model mit Standardwerten.
        
        current_input: Speichert die aktuelle Benutzereingabe als String
        last_result: Speichert das letzte Berechnungsergebnis
        error: Gibt an, ob der letzte Berechnungsversuch einen Fehler verursacht hat
        """
        self.current_input = ""  # Aktuelle Benutzereingabe
        self.last_result = ""    # Letztes Berechnungsergebnis
        self.error = False       # Fehlerindikator
    
    def append_input(self, value):
        """
        Fügt einen Wert zur aktuellen Eingabe hinzu.
        
        Args:
            value (str): Der Wert, der zur aktuellen Eingabe hinzugefügt werden soll.
            
        Returns:
            str: Die aktualisierte Eingabe
        """
        # Wenn ein Fehler vorliegt, zurücksetzen bevor neue Eingabe akzeptiert wird
        if self.error:
            self.clear()
            self.error = False
        
        # Wert zur aktuellen Eingabe hinzufügen
        self.current_input += value
        return self.current_input
    
    def calculate(self):
        """
        Führt die Berechnung basierend auf der aktuellen Eingabe durch.
        
        Verwendet eval() für die Berechnung, was in einer Produktionsumgebung
        durch eine sicherere Alternative ersetzt werden sollte.
        
        Returns:
            str: Das Berechnungsergebnis oder eine Fehlermeldung
        """
        # Leere Eingabe prüfen
        if not self.current_input:
            return ""
        
        try:
            # Berechnung durchführen und auf 8 Stellen runden
            # HINWEIS: eval() ist in Produktionsumgebungen unsicher und sollte
            # durch eine eigene Parsing- und Berechnungslogik ersetzt werden
            result = round(eval(self.current_input), 8)
            
            # Ergebnis speichern und zurückgeben
            self.last_result = str(result)
            self.current_input = self.last_result
            return self.last_result
        except Exception as e:
            # Fehlerbehandlung
            self.error = True
            return "Error"
    
    def clear(self):
        """
        Setzt die aktuelle Eingabe zurück.
        
        Returns:
            str: Die zurückgesetzte (leere) Eingabe
        """
        self.current_input = ""
        return self.current_input


class CalculatorView(QWidget):
    """
    Die View-Komponente im MVC-Muster.
    
    Verantwortlich für die gesamte Benutzeroberfläche des Taschenrechners.
    Erstellt und organisiert alle UI-Elemente ohne Geschäftslogik.
    """
    def __init__(self):
        """
        Initialisiert die View-Komponente und richtet die UI ein.
        """
        super().__init__()  # Initialisierung der Elternklasse QWidget
        
        # UI-Elemente, die später referenziert werden müssen
        self.display = None       # Anzeigefeld für Ein- und Ausgabe
        self.buttons = {}         # Dictionary zum Speichern aller Buttons für einfachen Zugriff
        
        # UI-Setup aufrufen
        self._setup_theme()       # Visuelles Erscheinungsbild konfigurieren
        self._setup_ui()          # UI-Elemente erstellen und anordnen
    
    def _setup_theme(self):
        """
        Konfiguriert das visuelle Erscheinungsbild des Taschenrechners.
        
        Private Methode, die nur innerhalb der Klasse verwendet werden sollte.
        """
        # Farbpalette für den Hintergrund erstellen
        my_palette = QPalette()
        my_palette.setColor(QPalette.Background, QColor(57, 13, 120))  # Dunkler Lila-Hintergrund
        self.setPalette(my_palette)
        
        # Fenstergröße festlegen und Titel setzen
        self.setFixedSize(300, 400)  # Feste Größe für konsistentes Erscheinungsbild
        self.setWindowTitle("PyQt5 Taschenrechner")  # Fenstertitel
    
    def _setup_ui(self):
        """
        Erstellt und positioniert alle UI-Elemente des Taschenrechners.
        
        Private Methode, die nur innerhalb der Klasse verwendet werden sollte.
        """
        # Hauptlayout erstellen (vertikal)
        main_layout = QVBoxLayout()
        
        # Anzeigefeld für Ein- und Ausgabe
        self.display = QLineEdit()
        self.display.setReadOnly(True)                      # Nur für Anzeige, keine direkte Texteingabe
        self.display.setAlignment(Qt.AlignRight)            # Text rechtsbündig ausrichten
        self.display.setStyleSheet("font-size: 24px; height: 50px;")  # Schriftgröße und Höhe anpassen
        main_layout.addWidget(self.display)                 # Zum Hauptlayout hinzufügen
        
        # Grid-Layout für die Tasten erstellen
        buttons_layout = QGridLayout()
        
        # Tastendefinitionen: (Text, Zeile, Spalte, [Zeilenspanne], [Spaltenspanne])
        # Format: Text auf der Taste, Position im Grid, optional: wie viele Zeilen/Spalten der Button einnimmt
        button_definitions = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),  # Erste Zeile
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),  # Zweite Zeile
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),  # Dritte Zeile
            ('0', 3, 0), ('C', 3, 1), ('.', 3, 2), ('+', 3, 3),  # Vierte Zeile
            ('=', 4, 0, 1, 4)  # Fünfte Zeile: '=' nimmt alle 4 Spalten ein
        ]
        
        # Tasten erstellen und zum Layout hinzufügen
        for button_def in button_definitions:
            # Button-Eigenschaften aus der Definition extrahieren
            text = button_def[0]     # Text auf dem Button
            row = button_def[1]      # Zeile im Grid
            col = button_def[2]      # Spalte im Grid
            rowSpan = 1              # Standardwert: Button nimmt 1 Zeile ein
            colSpan = 1              # Standardwert: Button nimmt 1 Spalte ein
            
            # Falls der Button über mehrere Zeilen/Spalten geht
            if len(button_def) > 3:
                rowSpan = button_def[3]  # Anzahl der Zeilen, die der Button einnimmt
                colSpan = button_def[4]  # Anzahl der Spalten, die der Button einnimmt
            
            # Button erstellen und konfigurieren
            button = QPushButton(text)
            button.setStyleSheet("font-size: 24px; height: 40px;")  # Styling
            
            # Button zum Layout hinzufügen
            buttons_layout.addWidget(button, row, col, rowSpan, colSpan)
            
            # Button im Dictionary speichern für späteren Zugriff
            self.buttons[text] = button
        
        # Button-Layout zum Hauptlayout hinzufügen
        main_layout.addLayout(buttons_layout)
        
        # Hauptlayout auf das Fenster anwenden
        self.setLayout(main_layout)
    
    def set_display_text(self, text):
        """
        Aktualisiert den Text im Anzeigefeld.
        
        Args:
            text (str): Der neue Text, der im Anzeigefeld angezeigt werden soll.
        """
        self.display.setText(text)
    
    def get_display_text(self):
        """
        Gibt den aktuellen Text des Anzeigefelds zurück.
        
        Returns:
            str: Der aktuelle Text im Anzeigefeld
        """
        return self.display.text()
    
    def connect_button_signals(self, callback):
        """
        Verbindet die Klick-Ereignisse aller Buttons mit dem übergebenen Callback.
        
        Diese Methode ermöglicht es dem Controller, auf Button-Klicks zu reagieren.
        
        Args:
            callback (function): Die Funktion, die bei Button-Klicks aufgerufen werden soll.
        """
        # Für jeden Button im Dictionary
        for button in self.buttons.values():
            # Button-Klick-Signal mit dem Callback verbinden
            button.clicked.connect(callback)


class CalculatorController:
    """
    Die Controller-Komponente im MVC-Muster.
    
    Verbindet Model und View und handhabt die Benutzerinteraktionen.
    Reagiert auf UI-Ereignisse, aktualisiert das Model und die View entsprechend.
    """
    def __init__(self, model, view):
        """
        Initialisiert den Controller mit Referenzen auf Model und View.
        
        Implementiert Dependency Injection für bessere Testbarkeit.
        
        Args:
            model (CalculatorModel): Das Model für die Geschäftslogik
            view (CalculatorView): Die View für die Benutzeroberfläche
        """
        # Referenzen auf Model und View speichern
        self.model = model
        self.view = view
        
        # View mit Event-Handler verbinden
        # Dies ist ein Beispiel für das Observer-Pattern
        self.view.connect_button_signals(self.handle_button_click)
    
    def handle_button_click(self):
        """
        Verarbeitet Button-Klicks und aktualisiert Model und View entsprechend.
        
        Diese Methode wird aufgerufen, wenn ein Button in der View geklickt wird.
        Sie identifiziert den geklickten Button und führt die entsprechende Aktion aus.
        """
        # Sender des Signals (den geklickten Button) ermitteln
        sender = self.view.sender()
        button_text = sender.text()
        
        # Aktion basierend auf dem Button-Text ausführen
        if button_text == 'C':
            # Clear-Button: Eingabe löschen
            result = self.model.clear()
        elif button_text == '=':
            # Equals-Button: Berechnung durchführen
            result = self.model.calculate()
        else:
            # Alle anderen Buttons: Wert zur Eingabe hinzufügen
            result = self.model.append_input(button_text)
        
        # Anzeige in der View aktualisieren
        self.view.set_display_text(result)


class CalculatorApp:
    """
    Hauptklasse der Taschenrechner-Anwendung.
    
    Fungiert als Einstiegspunkt und koordiniert die Erstellung der MVC-Komponenten.
    """
    def __init__(self):
        """
        Initialisiert die Anwendung und erstellt die MVC-Komponenten.
        """
        # Qt-Anwendung erstellen
        self.app = QApplication(sys.argv)  # sys.argv wird für die CLI-Argument-Verarbeitung verwendet
        self.app.setStyle('Fusion')        # Einheitliches Erscheinungsbild auf allen Plattformen
        
        # MVC-Komponenten erstellen
        self.model = CalculatorModel()                        # Model erstellen
        self.view = CalculatorView()                          # View erstellen
        self.controller = CalculatorController(self.model, self.view)  # Controller erstellen und mit Model und View verbinden
    
    def run(self):
        """
        Startet die Anwendung und den Event-Loop.
        
        Returns:
            int: Exit-Code der Anwendung
        """
        # Start-Nachricht ausgeben
        print("Mein Taschenrechner")
        print("###################")
        
        # View anzeigen
        self.view.show()
        
        # Ereignisschleife starten und Exit-Code zurückgeben
        # Diese Schleife läuft, bis das Fenster geschlossen wird
        return self.app.exec_()


# Haupteinstiegspunkt der Anwendung
if __name__ == "__main__":
    # Anwendungsobjekt erstellen
    calculator = CalculatorApp()
    
    # Anwendung starten und Exit-Code an das Betriebssystem übergeben
    # Dies ermöglicht eine ordnungsgemäße Beendigung der Anwendung
    sys.exit(calculator.run())