import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def createLineEdit(current_text: str, placeholder_text="") -> QLineEdit:
        lineedit = QLineEdit(current_text)

        lineedit.setPlaceholderText(placeholder_text)

        return lineedit

    def createButton(self, title):
        button = QPushButton(title)
        return button
    
    def addTask(self):
        task_text = self.task_input.text()
        self.task_input.clear()

    
    def addWidgetToLayout(self, widget):
        self.layout(widget)
    
    def initUI(self):
        self.setWindowTitle("Mattijn's To Do List")
        self.setFixedSize(400,400)

        layout = QVBoxLayout()

        self.task_input = self.createLineEdit("Geef hier de nieuwe activiteit in...")
        self.addWidgetToLayout(self.task_input)

        add_button = self.createButton("toevoegen")
        add_button.clicked.connect(self.addTask)
        self.addWidgetToLayout(add_button)

        delete_button = self.createButton("activiteit verwijderen")
        self.addWidgetToLayout(delete_button)

        self.setLayout(layout)


app = QApplication(sys.argv)
todo = ToDoApp()
todo.show()
sys.exit(app.exec_())