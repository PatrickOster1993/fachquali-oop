from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QListWidget, QGridLayout, QHBoxLayout, QSplitter, QFrame)
from PyQt5.QtCore import Qt

class ProductFormView(QWidget):
    """
    Represents the product form view in the application.
 
    This class provides a graphical interface for managing product-related
    operations, such as displaying messages, updating the product list,
    retrieving input values, and clearing form fields.

    Attributes:
        nameInput (QLineEdit): Input field for the product name.
        priceInput (QLineEdit): Input field for the product price.
        quantityInput (QLineEdit): Input field for the product quantity.
        submitButton (QPushButton): Button to submit the form data.
        deleteButton (QPushButton): Deletes the selected products.
        productList (QListWidget): List widget to display products.

    Methods:
        __init__(): Initializes the ProductFormView instance.
        initUI(): Sets up the graphical user interface for the product form.
        showMessage(title: str, message: str): Displays a message box with the given message.
        updateProductList(products: list): Updates the product list in the view.
        getInput() -> tuple: Retrieves the input values from the form fields.
        clearInputs(): Clears the input fields in the form.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the ProductFormView class.
 
        Sets up the base QWidget and prepares the UI components.
        """
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """
        Sets up the graphical user interface for the product form.
 
        This method initializes and arranges all UI components, such as labels,
        input fields, and buttons, within the form.
        """
        self.setWindowTitle("WaWi - Product Management")

        mainLayout = QVBoxLayout()
        
        splitter = QSplitter(Qt.Vertical)
        
        formFrame = QFrame()
        formFrame.setFrameShape(QFrame.StyledPanel)
        formLayout = QGridLayout(formFrame)

        formLayout.addWidget(QLabel("<b>Add New Product</b>"), 0, 0, 1, 2)
        
        formLayout.addWidget(QLabel("Product Name:"), 1, 0)
        self.nameInput = QLineEdit()
        formLayout.addWidget(self.nameInput, 1, 1)
        
        formLayout.addWidget(QLabel("Price:"), 2, 0)
        self.priceInput = QLineEdit()
        formLayout.addWidget(self.priceInput, 2, 1)
        
        formLayout.addWidget(QLabel("Quantity:"), 3, 0)
        self.quantityInput = QLineEdit()
        formLayout.addWidget(self.quantityInput, 3, 1)

        buttonLayout = QHBoxLayout()
        self.submitButton = QPushButton("Add")
        self.clearButton = QPushButton("Clear Fields")
        self.clearButton.clicked.connect(self.clearInputs)
        buttonLayout.addWidget(self.submitButton)
        buttonLayout.addWidget(self.clearButton)

        formLayout.addLayout(buttonLayout, 4, 0, 1, 2)

        listFrame = QFrame()
        listFrame.setFrameShape(QFrame.StyledPanel)
        listLayout = QVBoxLayout(listFrame)
        
        listLayout.addWidget(QLabel("<b>Product List</b>"))

        self.productList = QListWidget()
        listLayout.addWidget(self.productList)

        self.deleteButton = QPushButton("Remove Selected Products")
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

    def updateProductList(self, products: list):
        """
        Updates the product list in the view.
 
        Args:
            products (list): The list of products to display.
        """
        self.productList.clear() 
        for product in products:
            self.productList.addItem(f"ID: {product.productId} | Name: {product.name} | Price: {product.price} | Quantity: {product.quantity}")

    def getInput(self) -> tuple:
        """
        Retrieves the input values from the form fields.
 
        Returns:
            tuple: A tuple containing the input values (name, price, quantity).
        """
        return (
            self.nameInput.text(),
            self.priceInput.text(),
            self.quantityInput.text()
        )

    def clearInputs(self):
        """
        Clears the input fields in the form.
        """
        self.nameInput.clear()
        self.priceInput.clear()
        self.quantityInput.clear()
        self.nameInput.setFocus()