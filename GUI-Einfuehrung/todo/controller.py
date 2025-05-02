from PyQt5.QtCore import QObject

from model import TodoModel # Changed from relative to absolute
from view import TodoView   # Changed from relative to absolute

class TodoController(QObject):
    def __init__(self, data_filename="tasks.txt"):
        super().__init__()
        self._model = TodoModel(data_filename)
        self._view = TodoView()

        self._connect_signals()

    def _connect_signals(self):
        """Connects signals and slots between Model, View, and Controller."""
        # View signals to Controller/Model slots
        self._view.addTaskClicked.connect(self._handle_add_task)
        self._view.deleteTaskClicked.connect(self._model.delete_task) # Directly connect to model's slot
        self._view.windowClosed.connect(self._handle_window_close) # Connect to controller's handler

        # Model signals to View slots
        self._model.tasksChanged.connect(self._view.update_task_list)

    def _handle_add_task(self, task_text):
        """Handles adding a task: calls model and clears view input."""
        self._model.add_task(task_text)
        self._view.clear_input() # Clear input field after adding

    def _handle_window_close(self):
        """Handles the window close event: saves tasks."""
        print("Controller: Handling window close. Saving tasks...") # Debugging
        self._model.save_tasks()

    def run(self):
        """Shows the main application window."""
        # Initial population of the view
        initial_tasks = self._model.get_tasks()
        self._view.update_task_list(initial_tasks)
        self._view.show()
