from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel, 
                           QMessageBox, QListWidget, QHBoxLayout, 
                           QSplitter, QFrame, QGridLayout, QCheckBox)
from PyQt5.QtCore import Qt

class BaseFormView(QWidget):
    """
    Base class for form views in the application.
    
    This class provides common functionality for form views, reducing code
    duplication and ensuring consistent behavior and appearance.
    
    Attributes:
        listWidget (QListWidget): List widget to display items.
        submitButton (QPushButton): Button to submit the form.
        clearButton (QPushButton): Button to clear form fields.
        deleteButton (QPushButton): Button to delete selected items.
        silentDeleteCheckbox (QCheckBox): Checkbox to enable silent deletion without confirmation messages.
    """
    
    def __init__(self, title="Form"):
        """
        Initialize a new BaseFormView instance.
        
        Args:
            title (str, optional): The window title. Defaults to "Form".
        """
        super().__init__()
        self.setWindowTitle(f"WaWi - {title}")
        self._setupUI(title)
    
    def _setupUI(self, title):
        """
        Set up the common UI elements.
        
        This method initializes and arranges common UI components such as
        layouts, frames, and buttons.
        
        Args:
            title (str): The form title.
        """
        # Main layout
        mainLayout = QVBoxLayout()
        
        # Create a splitter for form and list
        splitter = QSplitter(Qt.Vertical)
        
        # Form frame
        formFrame = QFrame()
        formFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout = QGridLayout(formFrame)
        
        # Form title
        self.formLayout.addWidget(QLabel(f"<b>Add New {title}</b>"), 0, 0, 1, 2)
        
        # Derived classes will add form fields here
        
        # Button layout
        buttonLayout = QHBoxLayout()
        self.submitButton = QPushButton("Add")
        self.clearButton = QPushButton("Clear Fields")
        self.clearButton.clicked.connect(self.clearInputs)
        buttonLayout.addWidget(self.submitButton)
        buttonLayout.addWidget(self.clearButton)
        
        # Add button layout to form
        self.formLayout.addLayout(buttonLayout, 100, 0, 1, 2)  # Place at the end of the form
        
        # List frame
        listFrame = QFrame()
        listFrame.setFrameShape(QFrame.StyledPanel)
        listLayout = QVBoxLayout(listFrame)
        
        # List title
        listLayout.addWidget(QLabel(f"<b>{title} List</b>"))
        
        # List widget - Enable multiple selection
        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QListWidget.ExtendedSelection)  # Allow multiple selection
        listLayout.addWidget(self.listWidget)
        
        # Delete options layout
        deleteLayout = QHBoxLayout()
        
        # Delete button
        self.deleteButton = QPushButton(f"Remove Selected {title}s")
        deleteLayout.addWidget(self.deleteButton)
        
        # Silent delete checkbox
        self.silentDeleteCheckbox = QCheckBox("Silent delete (no confirmation)")
        self.silentDeleteCheckbox.setToolTip("When checked, items will be deleted without showing confirmation messages")
        deleteLayout.addWidget(self.silentDeleteCheckbox)
        
        # Add delete layout to list layout
        listLayout.addLayout(deleteLayout)
        
        # Add frames to splitter
        splitter.addWidget(formFrame)
        splitter.addWidget(listFrame)
        
        # Add splitter to main layout
        mainLayout.addWidget(splitter)
        
        # Set layout
        self.setLayout(mainLayout)
    
    def showMessage(self, title, message):
        """
        Display a message box.
        
        Args:
            title (str): The message box title.
            message (str): The message to display.
        """
        # Check if we're in silent mode and this is a success message
        if self.silentDeleteCheckbox.isChecked() and title == "Success" and "removed" in message:
            # Skip showing message for successful deletions in silent mode
            return
            
        QMessageBox.information(self, title, message)
    
    def clearInputs(self):
        """
        Clear all form inputs.
        
        This method should be overridden by derived classes to clear their
        specific input fields.
        """
        # Default implementation does nothing
        pass
    
    def getInput(self):
        """
        Get the input values from the form.
        
        This method should be overridden by derived classes to return their
        specific input values.
        
        Returns:
            tuple: The input values from the form.
        """
        # Default implementation returns an empty tuple
        return ()
    
    def updateList(self, items):
        """
        Update the list widget with items.
        
        This method should be overridden by derived classes to format their
        specific items for display.
        
        Args:
            items (list): The items to display.
        """
        # Default implementation clears the list
        self.listWidget.clear()