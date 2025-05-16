from PyQt5.QtWidgets import QPushButton

class TodoButton(QPushButton):
    def __init__(self, title: str):
        super().__init__(title)
