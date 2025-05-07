from model.inventory_manager_model import InventoryManager
from model.product_model import Product
from view.product_form_view import ProductFormView
from model.customer_manager_model import CustomerManager
from model.customer_model import Customer
from view.customer_form_view import CustomerFormView
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QWidget, QVBoxLayout, QMessageBox

class MainController:
    """
    The MainController class acts as the central controller of the application.

    It connects the views (ProductFormView, CustomerFormView) with the models 
    (InventoryManager, CustomerManager) and handles user interactions.

    Attributes:
        inventory_manager (InventoryManager): Manages the inventory of products.
        customer_manager (CustomerManager): Manages the customer database.
        product_view (ProductFormView): The GUI for product management.
        customer_view (CustomerFormView): The GUI for customer management.
        main_window (QMainWindow): The main application window.
        tabs (QTabWidget): Tab widget to hold different views.

    Methods:
        __init__(): Initializes the MainController instance.
        addProduct(): Adds a new product to the inventory.
        removeProduct(): Removes a product from the inventory by its ID.
        addCustomer(): Adds a new customer to the database.
        removeCustomer(): Removes a customer from the database by ID.
        start(): Starts the application.
    """
    
    def __init__(self):
        """
        Initializes the MainController with models and views and
        sets up the main window with tabs.
        """
        self.inventory_manager = InventoryManager()
        self.customer_manager = CustomerManager()

        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("WaWi - Warehouse Management System")
        self.main_window.setMinimumSize(600, 500)
        
        self.tabs = QTabWidget()

        self.product_view = ProductFormView()
        self.product_view.submitButton.clicked.connect(self.addProduct)
        self.product_view.deleteButton.clicked.connect(self.removeProduct)
        
        self.customer_view = CustomerFormView()
        self.customer_view.submitButton.clicked.connect(self.addCustomer)
        self.customer_view.deleteButton.clicked.connect(self.removeCustomer)
        
        self.tabs.addTab(self.product_view, "Products")
        self.tabs.addTab(self.customer_view, "Customers")
        
        self.main_window.setCentralWidget(self.tabs)

    def addProduct(self):
        """
        Adds a new product to the inventory.
        """
        name, price, quantity = self.product_view.getInput()
        
        if not name:
            self.showMessage(self.product_view, "Error", "Product name cannot be empty!")
            return
            
        if not price:
            self.showMessage(self.product_view, "Error", "Price cannot be empty!")
            return
            
        if not quantity:
            self.showMessage(self.product_view, "Error", "Quantity cannot be empty!")
            return
            
        try:
            product = Product(
                name=name,
                price=price,
                quantity=quantity
            )
            self.inventory_manager.addProduct(product)
            products = self.inventory_manager.products
            self.product_view.updateProductList(products)
            self.product_view.clearInputs()
            self.showMessage(self.product_view, "Success", f"Product '{name}' successfully added!")
        except ValueError as e:
            self.showMessage(self.product_view, "Error", str(e))

    def removeProduct(self):
        """
        Removes a product from the inventory by its ID.
        """
        selected_items = self.product_view.productList.selectedItems()
        if not selected_items:
            self.showMessage(self.product_view, "Note", "Please select a product to remove.")
            return
            
        for item in selected_items:
            self.product_view.productList.takeItem(self.product_view.productList.row(item))
            try:
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                self.inventory_manager.removeProduct(selected_id)
            except (ValueError, IndexError) as e:
                self.showMessage(self.product_view, "Error", f"Error removing product: {str(e)}")
                return
        
        self.showMessage(self.product_view, "Success", "Selected products have been removed.")

    def addCustomer(self):
        """
        Adds a new customer to the database.
        """
        name, address, email, phone = self.customer_view.getInput()
        
        if not name:
            self.showMessage(self.customer_view, "Error", "Name cannot be empty!")
            return
            
        if not address:
            self.showMessage(self.customer_view, "Error", "Address cannot be empty!")
            return
            
        if not email:
            self.showMessage(self.customer_view, "Error", "Email cannot be empty!")
            return
            
        try:
            customer = Customer(
                name=name,
                address=address,
                email=email,
                phone=phone
            )
            self.customer_manager.addCustomer(customer)
            customers = self.customer_manager.customers
            self.customer_view.updateCustomerList(customers)
            self.customer_view.clearInputs()
            self.showMessage(self.customer_view, "Success", f"Customer '{name}' successfully added!")
        except ValueError as e:
            self.showMessage(self.customer_view, "Error", str(e))

    def removeCustomer(self):
        """
        Removes a customer from the database by ID.
        """
        selected_items = self.customer_view.customerList.selectedItems()
        if not selected_items:
            self.showMessage(self.customer_view, "Note", "Please select a customer to remove.")
            return
            
        for item in selected_items:
            self.customer_view.customerList.takeItem(self.customer_view.customerList.row(item))
            try:
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                self.customer_manager.removeCustomer(selected_id)
            except (ValueError, IndexError) as e:
                self.showMessage(self.customer_view, "Error", f"Error removing customer: {str(e)}")
                return
        
        self.showMessage(self.customer_view, "Success", "Selected customers have been removed.")
        
    def showMessage(self, view, title, message):
        """
        Displays a message box in the specified view.
        
        Args:
            view: The view where the message should be displayed.
            title (str): The title of the message box.
            message (str): The message to display.
        """
        if hasattr(view, 'showMessage') and callable(view.showMessage):
            view.showMessage(title, message)
        else:
            QMessageBox.information(view, title, message)

    def start(self):
        """
        Updates the views for loaded data and displays the main window.
        """
        self.product_view.updateProductList(self.inventory_manager.products)

        self.customer_view.updateCustomerList(self.customer_manager.customers)

        self.main_window.show()