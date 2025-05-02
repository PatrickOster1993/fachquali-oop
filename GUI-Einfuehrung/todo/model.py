import os
from PyQt5.QtCore import QObject, pyqtSignal

class TodoModel(QObject):
    tasksChanged = pyqtSignal(list) # Signal emitted when tasks change

    def __init__(self, data_filename="tasks.txt"):
        super().__init__()
        self._tasks = []
        self.data_path = os.path.join(os.getcwd(), 'GUI-Einfuehrung', 'todo', 'data', data_filename)
        print(f"Model using data path: {self.data_path}") # Debugging output
        self.load_tasks()

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self._tasks.copy() # Return a copy to prevent external modification

    def add_task(self, text):
        """Adds a new task to the list."""
        if text:
            self._tasks.append(text)
            print(f"Model: Added task '{text}'. Current tasks: {self._tasks}") # Debugging
            self.tasksChanged.emit(self._tasks.copy()) # Emit signal with a copy

    def delete_task(self, index):
        """Deletes a task at the given index."""
        if 0 <= index < len(self._tasks):
            deleted_task = self._tasks.pop(index)
            print(f"Model: Deleted task '{deleted_task}' at index {index}. Current tasks: {self._tasks}") # Debugging
            self.tasksChanged.emit(self._tasks.copy()) # Emit signal with a copy
        else:
            print(f"Model: Invalid index {index} for deletion.") # Debugging

    def load_tasks(self):
        """Loads tasks from the data file."""
        self._tasks = []
        try:
            if os.path.exists(self.data_path):
                with open(self.data_path, "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()
                        if line:
                            self._tasks.append(line)
                print(f"Model: Loaded tasks: {self._tasks}") # Debugging
            else:
                print(f"Model: Data file not found at {self.data_path}. Starting with empty list.") # Debugging
        except Exception as e:
            print(f"Model: Error loading tasks from {self.data_path}: {e}") # Debugging
        # Emit signal even if loading failed or file didn't exist, to ensure view is initialized
        self.tasksChanged.emit(self._tasks.copy())


    def save_tasks(self):
        """Saves the current tasks to the data file."""
        print(f"Model: Saving tasks: {self._tasks} to {self.data_path}") # Debugging
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            with open(self.data_path, "w", encoding="utf-8") as file:
                for task in self._tasks:
                    file.write(task + '\n')
            print("Model: Tasks saved successfully.") # Debugging
        except Exception as e:
            print(f"Model: Error saving tasks to {self.data_path}: {e}") # Debugging
