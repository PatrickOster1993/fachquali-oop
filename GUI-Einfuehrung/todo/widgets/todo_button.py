from PyQt5.QtWidgets import QPushButton

class TodoButton(QPushButton):
    def __init__(self, title: str, click = None):
        super().__init__(title)
        if click:
            self.clicked.connect(click)
