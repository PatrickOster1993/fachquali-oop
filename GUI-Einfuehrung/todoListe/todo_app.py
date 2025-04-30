import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class TodoApp(QMainWindow):
    """
    Hauptfenster unserer Todo-Anwendung.
    Diese Klasse erbt von QMainWindow und bildet das Grundgerüst der App.
    """
    def __init__(self):
        """
        Initialisiert das Hauptfenster mit allen grundlegenden Eigenschaften.
        """
        super().__init__()
        
        # Fenstertitel und Grundabmessungen festlegen
        self.setWindowTitle("Meine Todo-Liste")
        self.setGeometry(100, 100, 500, 600)  # x, y, Breite, Höhe
        
        # Zentrales Widget erstellen (wird für das Layout benötigt)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Hauptlayout für die Anwendung erstellen
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Initialisiere die UI-Komponenten
        self.init_ui()
        
    def init_ui(self):
        """
        Initialisiert die Benutzeroberfläche mit allen UI-Elementen.
        Diese Methode wird später erweitert, um alle Komponenten hinzuzufügen.
        """
        # Hier werden wir später unsere UI-Elemente hinzufügen
        pass

# Wenn das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # PyQt5-Anwendung erstellen
    app = QApplication(sys.argv)
    
    # Unser Hauptfenster instanziieren
    window = TodoApp()
    
    # Fenster anzeigen
    window.show()
    
    # Anwendungsschleife starten
    sys.exit(app.exec_())