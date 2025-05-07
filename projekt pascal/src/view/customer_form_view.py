from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, 
                           QLabel, QMessageBox, QListWidget, QGridLayout, 
                           QHBoxLayout, QSplitter, QFrame)
from PyQt5.QtCore import Qt

class CustomerFormView(QWidget):
    """
    Represents the customer form view in the application.
 
    This class provides a graphical interface for managing customer-related
    operations, such as displaying messages, updating the customer list,
    retrieving input values, and clearing form fields.

    Attributes:
        layout (QVBoxLayout): The main layout of the form.
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
        self.setWindowTitle("WaWi - Kundenverwaltung")

        # Hauptlayout für das Widget erstellen
        mainLayout = QVBoxLayout()
        
        # Splitter erstellen (teilt das Fenster in Form- und Listenbereich)
        splitter = QSplitter(Qt.Vertical)
        
        # ===== Formularframe =====
        formFrame = QFrame()
        formFrame.setFrameShape(QFrame.StyledPanel)
        formLayout = QGridLayout(formFrame)
        
        # Eingabefelder und Labels im Grid-Layout anordnen
        formLayout.addWidget(QLabel("<b>Neuen Kunden hinzufügen</b>"), 0, 0, 1, 2)
        
        formLayout.addWidget(QLabel("Name:"), 1, 0)
        self.nameInput = QLineEdit()
        formLayout.addWidget(self.nameInput, 1, 1)
        
        formLayout.addWidget(QLabel("Adresse:"), 2, 0)
        self.addressInput = QLineEdit()
        formLayout.addWidget(self.addressInput, 2, 1)
        
        formLayout.addWidget(QLabel("E-Mail:"), 3, 0)
        self.emailInput = QLineEdit()
        formLayout.addWidget(self.emailInput, 3, 1)
        
        formLayout.addWidget(QLabel("Telefon:"), 4, 0)
        self.phoneInput = QLineEdit()
        formLayout.addWidget(self.phoneInput, 4, 1)
        
        # Buttons in einem horizontalen Layout anordnen
        buttonLayout = QHBoxLayout()
        self.submitButton = QPushButton("Hinzufügen")
        self.clearButton = QPushButton("Felder leeren")
        self.clearButton.clicked.connect(self.clearInputs)
        buttonLayout.addWidget(self.submitButton)
        buttonLayout.addWidget(self.clearButton)
        
        # Buttons zum Formular hinzufügen
        formLayout.addLayout(buttonLayout, 5, 0, 1, 2)
        
        # ===== Listenframe =====
        listFrame = QFrame()
        listFrame.setFrameShape(QFrame.StyledPanel)
        listLayout = QVBoxLayout(listFrame)
        
        listLayout.addWidget(QLabel("<b>Kundenliste</b>"))
        
        # Kundenliste erstellen
        self.customerList = QListWidget()
        listLayout.addWidget(self.customerList)
        
        # Button zum Löschen von Kunden
        self.deleteButton = QPushButton("Ausgewählte Kunden entfernen")
        listLayout.addWidget(self.deleteButton)
        
        # Frames zum Splitter hinzufügen
        splitter.addWidget(formFrame)
        splitter.addWidget(listFrame)
        
        # Splitter zum Hauptlayout hinzufügen
        mainLayout.addWidget(splitter)
        
        # Layout auf das Widget anwenden
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
            self.customerList.addItem(f"ID: {customer.customerId} | Name: {customer.name} | E-Mail: {customer.email} | Telefon: {customer.phone}")

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