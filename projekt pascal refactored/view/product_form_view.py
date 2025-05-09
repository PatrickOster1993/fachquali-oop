from PyQt5.QtWidgets import QLineEdit, QLabel
from view.base_form_view import BaseFormView

class ProductFormView(BaseFormView):
    """
    Form view for managing products.
    
    Attributes:
        nameInput (QLineEdit): Input field for product name.
        priceInput (QLineEdit): Input field for product price.
        quantityInput (QLineEdit): Input field for product quantity.
    """
    
    def __init__(self):
        """
        Initialize a new ProductFormView instance.
        """
        super().__init__("Product")
        self._setupFormFields()
    
    def _setupFormFields(self):
        """
        Set up the product-specific form fields.
        """
        # Product name field
        self.formLayout.addWidget(QLabel("Product Name:"), 1, 0)
        self.nameInput = QLineEdit()
        self.formLayout.addWidget(self.nameInput, 1, 1)
        
        # Price field
        self.formLayout.addWidget(QLabel("Price:"), 2, 0)
        self.priceInput = QLineEdit()
        self.formLayout.addWidget(self.priceInput, 2, 1)
        
        # Quantity field
        self.formLayout.addWidget(QLabel("Quantity:"), 3, 0)
        self.quantityInput = QLineEdit()
        self.formLayout.addWidget(self.quantityInput, 3, 1)
    
    def getInput(self):
        """
        Get the input values from the form.
        
        Returns:
            tuple: (name, price, quantity)
        """
        return (
            self.nameInput.text(),
            self.priceInput.text(),
            self.quantityInput.text()
        )
    
    def clearInputs(self):
        """
        Clear all form inputs.
        """
        self.nameInput.clear()
        self.priceInput.clear()
        self.quantityInput.clear()
        self.nameInput.setFocus()
    
    def updateProductList(self, products):
        """
        Update the product list widget.
        
        Args:
            products (list): The products to display.
        """
        self.listWidget.clear()
        for product in products:
            self.listWidget.addItem(f"ID: {product.id} | Name: {product.name} | Price: {product.price} | Quantity: {product.quantity}")