# Importiert notwendige Klassen aus PyQt5 für GUI-Elemente
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QLineEdit

# Definiert die Klasse TodoList, die von QWidget erbt (ein Basis-GUI-Element)
class TodoList(QWidget):
    def __init__(self):
        super().__init__() # Ruft den Konstruktor der Elternklasse (QWidget) auf

        self.layout = QVBoxLayout() # Erstellt ein vertikales Hauptlayout

        self.list_widget = QListWidget() # Erstellt die Listenansicht für die To-Do-Einträge
        self.layout.addWidget(self.list_widget) # Fügt die Listenansicht zum Hauptlayout hinzu

        self.input_layout = QHBoxLayout() # Erstellt ein horizontales Layout für Eingabefeld und Button
        self.input_field = QLineEdit() # Erstellt das Texteingabefeld
        self.input_layout.addWidget(self.input_field) # Fügt das Eingabefeld zum horizontalen Layout hinzu

        self.add_button = QPushButton("Add") # Erstellt den "Add"-Button
        self.add_button.clicked.connect(self.add_item) # Verbindet das Klick-Signal des Buttons mit der add_item Methode
        self.input_layout.addWidget(self.add_button) # Fügt den "Add"-Button zum horizontalen Layout hinzu

        self.layout.addLayout(self.input_layout) # Fügt das horizontale Eingabe-Layout zum vertikalen Hauptlayout hinzu

        self.remove_button = QPushButton("Remove") # Erstellt den "Remove"-Button
        self.remove_button.clicked.connect(self.remove_item) # Verbindet das Klick-Signal des Buttons mit der remove_item Methode
        self.layout.addWidget(self.remove_button) # Fügt den "Remove"-Button zum Hauptlayout hinzu

        self.setLayout(self.layout) # Setzt das Hauptlayout für das gesamte TodoList Widget

    def add_item(self):
        text = self.input_field.text()
        if text:
            item = QListWidgetItem(text)
            self.list_widget.addItem(item)
            self.input_field.clear()
    # Methode zum Entfernen des aktuell ausgewählten Eintrags
    def remove_item(self):
        current_item = self.list_widget.currentItem() # Holt das aktuell ausgewählte Element aus der Liste
        if current_item: # Prüft, ob überhaupt ein Element ausgewählt ist
            # Entfernt das ausgewählte Element aus der Liste. row() gibt den Index des Elements zurück.
            self.list_widget.takeItem(self.list_widget.row(current_item))
