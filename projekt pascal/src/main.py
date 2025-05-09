import sys
from PyQt5.QtWidgets import QApplication
from controller.main_controller import MainController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    controller.start()
    sys.exit(app.exec_())