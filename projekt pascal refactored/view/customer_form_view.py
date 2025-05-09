from PyQt5.QtWidgets import QLineEdit, QLabel
from view.base_form_view import BaseFormView

class CustomerFormView(BaseFormView):
    """
    Form view for managing customers.
    
    Attributes:
        nameInput (QLineEdit): Input field for customer name.
        addressInput (QLineEdit): Input field for customer address.
        emailInput (QLineEdit): Input field for customer email.
        phoneInput (QLineEdit): Input field for customer phone.
    """
    
    def __init__(self):
        """
        Initialize a new CustomerFormView instance.
        """
        super().__init__("Customer")
        self._setupFormFields()
    
    def _setupFormFields(self):
        """
        Set up the customer-specific form fields.
        """
        # Name field
        self.formLayout.addWidget(QLabel("Name:"), 1, 0)
        self.nameInput = QLineEdit()
        self.formLayout.addWidget(self.nameInput, 1, 1)
        
        # Address field
        self.formLayout.addWidget(QLabel("Address:"), 2, 0)
        self.addressInput = QLineEdit()
        self.formLayout.addWidget(self.addressInput, 2, 1)
        
        # Email field
        self.formLayout.addWidget(QLabel("Email:"), 3, 0)
        self.emailInput = QLineEdit()
        self.formLayout.addWidget(self.emailInput, 3, 1)
        
        # Phone field
        self.formLayout.addWidget(QLabel("Phone:"), 4, 0)
        self.phoneInput = QLineEdit()
        self.formLayout.addWidget(self.phoneInput, 4, 1)
    
    def getInput(self):
        """
        Get the input values from the form.
        
        Returns:
            tuple: (name, address, email, phone)
        """
        return (
            self.nameInput.text(),
            self.addressInput.text(),
            self.emailInput.text(),
            self.phoneInput.text()
        )
    
    def clearInputs(self):
        """
        Clear all form inputs.
        """
        self.nameInput.clear()
        self.addressInput.clear()
        self.emailInput.clear()
        self.phoneInput.clear()
        self.nameInput.setFocus()
    
    def updateCustomerList(self, customers):
        """
        Update the customer list widget.
        
        Args:
            customers (list): The customers to display.
        """
        self.listWidget.clear()
        for customer in customers:
            self.listWidget.addItem(f"ID: {customer.id} | Name: {customer.name} | Email: {customer.email} | Phone: {customer.phone}")