import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor

class Todo(QWidget):

    def __init__(self):
        super().__init__()
        self.buttons = [
            ('Haushalt machen', 0, 0),
            ('Teppich reinigen', 1, 0),
            ('Javascript lernen', 2, 0)
        ]
        self.grid = QGridLayout()
        self.initUI()

    def initUI(self):
        my_palette = QPalette()
        my_palette.setColor(QPalette.Background, QColor(20, 110, 60))
        self.setPalette(my_palette)

        vbox = QVBoxLayout()

        for item in self.buttons:
            btnText = item[0]
            row = item[1]
            col = item[2]
            rowSpan = 1
            colSpan = 1

            if len(item) > 3:
                rowSpan = item[3]
                colSpan = item[4]

            button = QPushButton(btnText)
            button.setStyleSheet("font-size: 24px; height: 40px;")
            button.clicked.connect(self.onButtonClicked)
            self.grid.addWidget(button, row, col, rowSpan, colSpan)

        vbox.addLayout(self.grid)

        self.setLayout(vbox)
        self.setWindowTitle("To-Do-App")

    def onButtonClicked(self):
        sender = self.sender()
        text = sender.text()
        self.buttons = [b for b in self.buttons if b[0] != text]
        self.grid.removeWidget(sender)
        sender.deleteLater()

app = QApplication(sys.argv)
app.setStyle('Fusion')
my_calculator = Todo()

my_calculator.show()

sys.exit(app.exec_())