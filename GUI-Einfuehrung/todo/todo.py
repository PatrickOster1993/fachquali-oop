import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class TodoApp(QWidget):
    def __init__(self, dataName):
        self.dataPath = os.getcwd() + '/GUI-Einfuehrung/todo/data/' + dataName
        print(self.dataPath)
        super().__init__()
        self.initUI()
        self.loadTasks()
    
    # zu Beginn der Anwendung sollen alle bereits früher angelegten Tasks in der Task-Liste angezeigt werden!
    def loadTasks(self):
        if os.path.exists(self.dataPath): # gleichbedeutend mit "./tasks.txt"
            with open(self.dataPath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.task_list.addItem(line)

    def createLineedit(current_text: str, placeholder_text="") -> QLineEdit:
        lineedit = QLineEdit(current_text)
        lineedit.setPlaceholderText(placeholder_text)
        return lineedit
    
    def createButton(self, title):
        button = QPushButton(title)
        return button
    
    def createTaskList(self):
        return QListWidget()
    
    def addWidgetToLayout(self, widget):
        self.layout.addWidget(widget)

    def setStyling(self):
        self.setWindowTitle("DAA-ToDo-Liste")
        self.setFixedSize(400, 400)

    def initUI(self):
        
        self.setStyling()
        self.layout = QVBoxLayout()

        # Eingabefeld für neue Tasks
        self.task_input = self.createLineedit("Neue Aufgabe eingeben...")
        self.addWidgetToLayout(self.task_input)

        # Button zum Hinzufügen neuer Tasks
        add_button = self.createButton("Task hinzufügen")
        add_button.clicked.connect(self.addTask)
        self.addWidgetToLayout(add_button)

        # Liste für mehrere Tasks
        self.task_list = self.createTaskList()
        self.addWidgetToLayout(self.task_list)

        # Button zum Löschen von Tasks
        delete_button = self.createButton("Task löschen")
        delete_button.clicked.connect(self.deleteTask)
        self.addWidgetToLayout(delete_button)

        self.setLayout(self.layout)
    
    def addTask(self):
        task_text = self.task_input.text()

        if task_text == "" or None:
            task_text = self.task_input.text()
 
        if task_text:
            self.task_list.addItem(task_text)

        self.task_input.clear()

    # wird automatisch aufgerufen beim Beenden
    def closeEvent(self, event):
        self.saveTasks()
        event.accept()

    # gegen Ende der Anwendung sollen alle Tasks in eine .txt gespeichert werden (persistentes Speichern!)
    def saveTasks(self):
        with open(self.dataPath, "w", encoding="utf-8") as file:
            for i in range(self.task_list.count()):
                file.write(self.task_list.item(i).text() + '\n')

    def deleteTask(self):
        selected_items = self.task_list.selectedItems()
        # print(selected_items) # Debugging-Zwecke

        for item in selected_items:

            # print(self.task_list.row(item)) # Debugging-Zweck
            self.task_list.takeItem(self.task_list.row(item))