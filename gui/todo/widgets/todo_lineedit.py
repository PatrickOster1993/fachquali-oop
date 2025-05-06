from PyQt5.QtWidgets import QLineEdit

class TodoLineedit(QLineEdit):
    def __init__(self, currentText: str = "", placeholderText = ""):
        super().__init__(currentText)
        self.setPlaceholderText(placeholderText)
