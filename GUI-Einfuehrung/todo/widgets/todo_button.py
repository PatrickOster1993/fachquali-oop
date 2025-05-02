    # def createButton(self, title):
    #     button = QPushButton(title)
    #     return button

#  # Button zum Hinzufügen neuer Tasks
#         add_button = self.createButton("Task hinzufügen")
#         add_button.clicked.connect(self.addTask)

from PyQt5.QtWidgets import QPushButton

class TodoButton(QPushButton):
    def __init__(self, title: str, click = None):
        super().__init__(title)
        if click:
            self.clicked.connect(click)
