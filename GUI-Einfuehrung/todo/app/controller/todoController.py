#from PyQt5.QtWidgets import QWidget
from app.view.todoView import TodoView
from app.model.todoModel import TodoModel

class TodoController:

    def __init__(self, filePath: str):
        super().__init__()
        self.view = TodoView()
        self.model = TodoModel(filePath)
        self.signalConnector()
        self.loadTasks()
        self.view.closeEvent = self.closeEvent

    def loadTasks(self):
        self.model.loadTasks()
        for task in self.model.getTasks():
            self.view.task_list.addItem(task)

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
    
    def closeEvent(self, event):
        text_list = []
        for i in range(self.view.task_list.count()):
            text_list.append(self.view.task_list.item(i).text() + '\n')
        self.model.saveTasks(text_list)
        event.accept()