import sys

from PyQt5.QtWidgets import QApplication
from app.todo import TodoApp

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    todo = TodoApp("tasks.txt")
    todo.show()
    sys.exit(app.exec_())

main()