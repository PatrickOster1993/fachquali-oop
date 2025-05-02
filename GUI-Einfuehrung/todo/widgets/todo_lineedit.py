# def createLineedit(current_text: str, placeholder_text="") -> QLineEdit:
#         lineedit = QLineEdit(current_text)
#         lineedit.setPlaceholderText(placeholder_text)
#         return lineedit

# self.task_input = self.createLineedit("Neue Aufgabe eingeben...")


from PyQt5.QtWidgets import QLineEdit


class TodoLineEdit(QLineEdit):

    def __init__(self, current_text: str = "", placeholder_text: str = ""):
        super().__init__(current_text)
        self.setPlaceholderText(placeholder_text)

    def setPlaceholderText(self, placeholder_text: str):
        super().setPlaceholderText(placeholder_text)