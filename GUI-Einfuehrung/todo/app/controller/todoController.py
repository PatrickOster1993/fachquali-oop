





#     # wird automatisch aufgerufen beim Beenden
#     def closeEvent(self, event):
#         self.saveTasks()
#         event.accept()

from PyQt5.QtCore import QObject
from app.view.todoView import TodoView
from app.model.todoModel import TodoModel

class TodoController(QObject):

    def __init__(self, filePath: str):
        super().__init__()
        self.view = TodoView()
        self.model = TodoModel(filePath)

    
    def addTask(self):
        task_text = self.view.task_input.text()

        if task_text == "" or None:
            task_text = self.view.task_input.text()
 
        if task_text:
            self.view.task_list.addItem(task_text)

        self.view.task_input.clear()

    def deleteTask(self):
        selected_items = self.view.task_list.selectedItems()

        for item in selected_items:
            self.view.task_list.takeItem(self.view.task_list.row(item))
    
    def signalConnector(self):
        self.view.add_button.clicked.connect(self.addTask)
        self.view.delete_button.clicked.connect(self.deleteTask)