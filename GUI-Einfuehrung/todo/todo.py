import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt

# Importiere die benutzerdefinierte LineEdit-Klasse
from widgets.todo_lineedit import TodoLineEdit
# Importiere die benutzerdefinierte Button-Klasse
from widgets.todo_button import TodoButton


class TodoApp(QWidget):
    def __init__(self, dataName):
        self.dataPath = os.getcwd() + '/GUI-Einfuehrung/todo/data/' + dataName
        print(self.dataPath)
        super().__init__()
        self.initUI()
        self.loadTasks()
    
    # Lädt Tasks aus der Datei beim Start
    def loadTasks(self):
        if os.path.exists(self.dataPath): # gleichbedeutend mit "./tasks.txt"
            with open(self.dataPath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.task_list.addItem(line)
    
    def createTaskList(self):
        # Erstellt das Listen-Widget
        return QListWidget()
    
    def addWidgetToLayout(self, widget):
        # Hilfsmethode zum Hinzufügen von Widgets zum Layout
        self.layout.addWidget(widget)

    def setStyling(self):
        self.setWindowTitle("DAA-ToDo-Liste")
        self.setFixedSize(400, 400)

    def initUI(self):
        
        self.setStyling()
        self.layout = QVBoxLayout()

        # Eingabefeld für neue Tasks
        self.task_input = TodoLineEdit( # Korrigierter Klassenname (großes E)
            placeholder_text= "Neue Aufgabe eingeben..." # Korrigierter Parametername
        )
        self.addWidgetToLayout(self.task_input)

        # Button zum Hinzufügen neuer Tasks
        add_button = TodoButton("Task hinzufügen", click=self.addTask)
        self.addWidgetToLayout(add_button)

        # Liste für mehrere Tasks
        self.task_list = self.createTaskList()
        self.addWidgetToLayout(self.task_list)

        # Button zum Löschen von Tasks
        delete_button = TodoButton("Task löschen", click=self.deleteTask)
        self.addWidgetToLayout(delete_button)

        self.setLayout(self.layout)
    
    def addTask(self):
        task_text = self.task_input.text()

        # Füge den Task hinzu, wenn Text vorhanden ist
        if task_text:
            self.task_list.addItem(task_text)

        self.task_input.clear()

    # wird automatisch aufgerufen beim Beenden
    def closeEvent(self, event): # PyQt Event-Handler
        self.saveTasks()
        event.accept()

    # gegen Ende der Anwendung sollen alle Tasks in eine .txt gespeichert werden (persistentes Speichern!)
    def saveTasks(self):
        with open(self.dataPath, "w", encoding="utf-8") as file:
            for i in range(self.task_list.count()):
                file.write(self.task_list.item(i).text() + '\n')

    def deleteTask(self):
        # Löscht die aktuell ausgewählten Elemente
        selected_items = self.task_list.selectedItems()
        # print(selected_items) # Debugging-Zwecke

        for item in selected_items:

            # print(self.task_list.row(item)) # Debugging-Zweck
            self.task_list.takeItem(self.task_list.row(item))
