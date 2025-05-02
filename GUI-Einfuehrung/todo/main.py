import sys
from PyQt5.QtWidgets import QApplication

# Import the controller
from controller import TodoController

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Instantiate and run the controller
    # Pass the desired data filename to the controller
    controller = TodoController(data_filename="tasks.txt")
    controller.run() # The controller will show the view

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
