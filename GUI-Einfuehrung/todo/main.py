import sys
import os

from PyQt5.QtWidgets import QApplication
from app.controller.todoController import TodoController

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    path = os.getcwd() + '/GUI-Einfuehrung/todo/data/tasks.txt'
    controller = TodoController(path)
    controller.view.show()
    sys.exit(app.exec_())

main()