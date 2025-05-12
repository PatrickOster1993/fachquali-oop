from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QListWidget, QGridLayout, QHBoxLayout, QSplitter, QFrame)
from PyQt5.QtCore import Qt

class CustomerFormView(QWidget):
    """
    Represents the customer form view in the application.
 
    This class provides a graphical interface for managing customer-related
    operations, such as displaying messages, updating the customer list,
    retrieving input values, and clearing form fields.

    Attributes:
        nameInput (QLineEdit): Input field for the customer name.
        addressInput (QLineEdit): Input field for the customer address.
        emailInput (QLineEdit): Input field for the customer email.
        phoneInput (QLineEdit): Input field for the customer phone number.
        submitButton (QPushButton): Button to submit the form data.
        deleteButton (QPushButton): Deletes the selected customers.
        customerList (QListWidget): List widget to display customers.

    Methods:
        __init__(): Initializes the CustomerFormView instance.
        initUI(): Sets up the graphical user interface for the customer form.
        showMessage(title: str, message: str): Displays a message box with the given message.
        updateCustomerList(customers: list): Updates the customer list in the view.
        getInput() -> tuple: Retrieves the input values from the form fields.
        clearInputs(): Clears the input fields in the form.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the CustomerFormView class.
 
        Sets up the base QWidget and prepares the UI components.
        """
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """
        Sets up the graphical user interface for the customer form.
 
        This method initializes and arranges all UI components, such as labels,
        input fields, and buttons, within the form.
        """
        self.setWindowTitle("WaWi - Customer Management")

        mainLayout = QVBoxLayout()

        splitter = QSplitter(Qt.Vertical)

        formFrame = QFrame()
        formFrame.setFrameShape(QFrame.StyledPanel)
        formLayout = QGridLayout(formFrame)

        formLayout.addWidget(QLabel("<b>Add New Customer</b>"), 0, 0, 1, 2)
        
        formLayout.addWidget(QLabel("Name:"), 1, 0)
        self.nameInput = QLineEdit()
        formLayout.addWidget(self.nameInput, 1, 1)
        
        formLayout.addWidget(QLabel("Address:"), 2, 0)
        self.addressInput = QLineEdit()
        formLayout.addWidget(self.addressInput, 2, 1)
        
        formLayout.addWidget(QLabel("Email:"), 3, 0)
        self.emailInput = QLineEdit()
        formLayout.addWidget(self.emailInput, 3, 1)
        
        formLayout.addWidget(QLabel("Phone:"), 4, 0)
        self.phoneInput = QLineEdit()
        formLayout.addWidget(self.phoneInput, 4, 1)

        buttonLayout = QHBoxLayout()
        self.submitButton = QPushButton("Add")
        self.clearButton = QPushButton("Clear Fields")
        self.clearButton.clicked.connect(self.clearInputs)
        buttonLayout.addWidget(self.submitButton)
        buttonLayout.addWidget(self.clearButton)

        formLayout.addLayout(buttonLayout, 5, 0, 1, 2)

        listFrame = QFrame()
        listFrame.setFrameShape(QFrame.StyledPanel)
        listLayout = QVBoxLayout(listFrame)
        
        listLayout.addWidget(QLabel("<b>Customer List</b>"))

        self.customerList = QListWidget()
        listLayout.addWidget(self.customerList)

        self.deleteButton = QPushButton("Remove Selected Customers")
        listLayout.addWidget(self.deleteButton)

        splitter.addWidget(formFrame)
        splitter.addWidget(listFrame)

        mainLayout.addWidget(splitter)
        
        self.setLayout(mainLayout)

    def showMessage(self, title: str, message: str):
        """
        Displays a message box with the given message.
 
        Args:
            title (str): The title of the message box.
            message (str): The message to display.
        """
        QMessageBox.information(self, title, message)

    def updateCustomerList(self, customers: list):
        """
        Updates the customer list in the view.
 
        Args:
            customers (list): The list of customers to display.
        """
        self.customerList.clear() 
        for customer in customers:
            self.customerList.addItem(f"ID: {customer.customerId} | Name: {customer.name} | Email: {customer.email} | Phone: {customer.phone}")

    def getInput(self) -> tuple:
        """
        Retrieves the input values from the form fields.
 
        Returns:
            tuple: A tuple containing the input values (name, address, email, phone).
        """
        return (
            self.nameInput.text(),
            self.addressInput.text(),
            self.emailInput.text(),
            self.phoneInput.text()
        )

    def clearInputs(self):
        """
        Clears the input fields in the form.
        """
        self.nameInput.clear()
        self.addressInput.clear()
        self.emailInput.clear()
        self.phoneInput.clear()
        self.nameInput.setFocus()