from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt

# Import custom widgets
from widgets.todo_lineedit import TodoLineEdit # Changed from relative to absolute
from widgets.todo_button import TodoButton   # Changed from relative to absolute

class TodoView(QWidget):
    # Signals emitted when user interacts with the view
    addTaskClicked = pyqtSignal(str) # Emits the text from the input field
    deleteTaskClicked = pyqtSignal(int) # Emits the index of the selected task
    windowClosed = pyqtSignal() # Emitted when the window is about to close

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        """Initializes the user interface elements."""
        self.setWindowTitle("DAA-ToDo-Liste (MVC)")
        self.setFixedSize(400, 400)

        self.layout = QVBoxLayout(self) # Main layout for the widget

        # Task input field
        self.task_input = TodoLineEdit(placeholder_text="Neue Aufgabe eingeben...")
        self.layout.addWidget(self.task_input)
        # Connect return key press in input field to adding a task
        self.task_input.returnPressed.connect(self._on_add_button_clicked)

        # Add Task button
        self.add_button = TodoButton("Task hinzufügen")
        self.add_button.clicked.connect(self._on_add_button_clicked)
        self.layout.addWidget(self.add_button)

        # Task list widget
        self.task_list = QListWidget()
        self.task_list.setSelectionMode(QListWidget.SingleSelection) # Allow only single selection
        # Connect double click on item to deleting it (optional usability feature)
        self.task_list.itemDoubleClicked.connect(self._on_delete_button_clicked)
        self.layout.addWidget(self.task_list)

        # Delete Task button
        self.delete_button = TodoButton("Task löschen")
        self.delete_button.clicked.connect(self._on_delete_button_clicked)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def _on_add_button_clicked(self):
        """Handles the add button click or return key press."""
        task_text = self.task_input.text().strip()
        if task_text:
            self.addTaskClicked.emit(task_text) # Emit signal with task text

    def _on_delete_button_clicked(self):
        """Handles the delete button click or list item double-click."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.deleteTaskClicked.emit(selected_index) # Emit signal with index

    def update_task_list(self, tasks):
        """Clears and repopulates the list widget with the given tasks."""
        print(f"View: Updating task list with: {tasks}") # Debugging
        self.task_list.clear()
        for task in tasks:
            item = QListWidgetItem(task)
            self.task_list.addItem(item)

    def get_selected_task_index(self):
        """Returns the index of the currently selected item, or None if no item is selected."""
        selected_items = self.task_list.selectedItems()
        if selected_items:
            return self.task_list.row(selected_items[0])
        return None

    def clear_input(self):
        """Clears the task input field."""
        self.task_input.clear()

    def closeEvent(self, event):
        """Overrides the default close event handler."""
        print("View: Close event triggered.") # Debugging
        self.windowClosed.emit() # Emit signal before closing
        super().closeEvent(event) # Call the parent class's handler
