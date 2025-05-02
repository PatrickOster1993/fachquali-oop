from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.todo_lineedit import TodoLineedit
from widgets.todo_button import TodoButton
from widgets.todo_list import TodoList

class TodoView(QWidget):

    def __init__(self):
        super().__init__()

    def initUI(self):
        
        self.setStyling()
        self.layout = QVBoxLayout()

        # Eingabefeld für neue Tasks
        self.task_input = TodoLineedit(
            placeholderText= "Neue Aufgabe eingeben..."
        )
        self.addWidgetToLayout(self.task_input)

        # Button zum Hinzufügen neuer Tasks
        self.add_button = TodoButton("Task hinzufügen")
        self.addWidgetToLayout(self.add_button)

        # Liste für mehrere Tasks
        self.task_list = TodoList()
        self.addWidgetToLayout(self.task_list)

        # Button zum Löschen von Tasks
        self.delete_button = TodoButton("Task löschen")
        self.addWidgetToLayout(self.delete_button)

        self.setLayout(self.layout)

    def addWidgetToLayout(self, widget):
        self.layout.addWidget(widget)

    def setStyling(self):
        self.setWindowTitle("DAA-ToDo-Liste")
        self.setFixedSize(400, 400)
    
