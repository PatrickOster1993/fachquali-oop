from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QListWidget

class ProductFormView(QWidget):
    """
    Represents the product form view in the application.
 
    This class provides a graphical interface for managing product-related
    operations, such as displaying messages, updating the product list,
    retrieving input values, and clearing form fields.

    Attributes:
        layout (QVBoxLayout): The main layout of the form.
        nameInput (QLineEdit): Input field for the product name.
        priceInput (QLineEdit): Input field for the product price.
        quantityInput (QLineEdit): Input field for the product quantity.
        submitButton (QPushButton): Button to submit the form data.
        deleteButton (QPushButton): Deletes the selected products.

    Methods:
        __init__(): Initializes the ProductFormView instance.
        initUI(): Sets up the graphical user interface for the product form.
        showMessage(title: str, message: str): Displays a message box with the given message.
        updateProductList(products: list): Updates the product list in the view.
        getInput() -> tuple: Retrieves the input values from the form fields.
        clearInput(): Clears the input fields in the form.
        addWidget(widget: QWidget, info: str): Add specified widget to layout.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the ProductFormView class.
 
        Sets up the base QWidget and prepares the UI components.
        """
        super().__init__()
        self.initUI()
    
    def addWidget(self, widget: QWidget, context: str):
        """
        Adds widget to layout and sets placeholder text as given within arguments.

        Args:
            widget (QWidget): Widget Object to add to layout
            placeholder (str): Further information regarding widget.
        """

        if isinstance(widget, QLineEdit):
            self.layout.addWidget(QLabel(context))
        elif isinstance(widget, QPushButton):
            widget.setText(context)

        self.layout.addWidget(widget)
        
    def initUI(self):
        """
        Sets up the graphical user interface for the product form.
 
        This method initializes and arranges all UI components, such as labels,
        input fields, and buttons, within the form.
        """
        self.setWindowTitle("WaWi")

        self.layout = QVBoxLayout()

        self.nameInput = QLineEdit(self)
        self.addWidget(self.nameInput, "Produktbezeichnung")

        self.priceInput = QLineEdit(self)
        self.addWidget(self.priceInput, "Preis")

        self.quantityInput = QLineEdit(self)
        self.addWidget(self.quantityInput, "Menge")

        self.productList = QListWidget(self)
        self.addWidget(self.productList, "Produkte")

        self.submitButton = QPushButton(self)
        self.addWidget(self.submitButton, "Hinzufügen")

        self.deleteButton = QPushButton(self)
        self.addWidget(self.deleteButton, "Entfernen")

        self.setLayout(self.layout)

    def showMessage(self, title: str, message: str):
        """
        Displays a message box with the given message.
 
        Args:
            title (str): The title of the message box.
            message (str): The message to display.
        """
        pass

    def updateProductList(self, products: list):
        """
        Updates the product list in the view.
 
        Args:
            products (list): The list of products to display.
        """
        self.productList.clear() 
        for product in products:
            self.productList.addItem(f"ID: {product.productId} | Name: {product.name} | Preis: {product.price} | Menge: {product.quantity}")

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