import sys

from PyQt5.QtWidgets import QApplication
from app.controller.todoController import TodoController

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    controller = TodoController("tasks.txt")
    controller.view.show()
    sys.exit(app.exec_())

main()