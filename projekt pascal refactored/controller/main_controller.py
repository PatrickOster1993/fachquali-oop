import logging
import os
from typing import Dict, Any, Tuple

from PyQt5.QtWidgets import QTabWidget, QMainWindow, QAction, QMessageBox

from model.product_model import Product
from model.customer_model import Customer
from model.product_manager import ProductManager
from model.customer_manager import CustomerManager
from model.database_config import DatabaseConfig
from model.database_connection_factory import DatabaseConnectionFactory
from view.product_form_view import ProductFormView
from view.customer_form_view import CustomerFormView
from view.database_settings_dialog import DatabaseSettingsDialog

logger = logging.getLogger('MainController')

class MainController:
    """
    The MainController class acts as the central controller of the application.
    
    It connects the views (ProductFormView, CustomerFormView) with the models
    (ProductManager, CustomerManager) and handles user interactions.
    
    Attributes:
        db_connection: The database connection.
        product_manager (ProductManager): Manager for products.
        customer_manager (CustomerManager): Manager for customers.
        main_window (QMainWindow): The main application window.
        tabs (QTabWidget): The tab widget for product and customer views.
        product_view (ProductFormView): The product form view.
        customer_view (CustomerFormView): The customer form view.
    """
    
    def __init__(self):
        """
        Initialize the MainController with models and views and set up the main window.
        """
        # Initialize database connection
        self._initialize_database()
        
        # Initialize models
        self.product_manager = ProductManager(self.db_connection)
        self.customer_manager = CustomerManager(self.db_connection)
        
        # Initialize main window
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("WaWi - Warehouse Management System")
        self.main_window.setMinimumSize(600, 500)
        self.main_window.closeEvent = self.closeEvent
        
        # Create menus
        self._create_menus()
        
        # Initialize views
        self._initialize_views()
    
    def _initialize_database(self):
        """
        Initialize the database connection.
        """
        # Check if a configuration file exists
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "db_config.json")
        config = DatabaseConfig(config_path) if os.path.exists(config_path) else None
        
        # Create database connection
        factory = DatabaseConnectionFactory(config)
        self.db_connection = factory.create_connection()
        
        # Verify database is working
        test_query = "SELECT 1 FROM products LIMIT 1"
        if self.db_connection.execute_query(test_query):
            logger.info("Database tables verified.")
        else:
            logger.warning("Database tables might not exist or are empty.")
    
    def _create_menus(self):
        """
        Create application menus.
        """
        menu_bar = self.main_window.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("File")
        
        # Database settings action
        settings_action = QAction("Database Settings", self.main_window)
        settings_action.triggered.connect(self._show_database_settings)
        file_menu.addAction(settings_action)
        
        # Import sample data action
        import_action = QAction("Import Sample Data", self.main_window)
        import_action.triggered.connect(self._import_sample_data)
        file_menu.addAction(import_action)
        
        # Exit action
        exit_action = QAction("Exit", self.main_window)
        exit_action.triggered.connect(self.main_window.close)
        file_menu.addAction(exit_action)
    
    def _initialize_views(self):
        """
        Initialize and connect the views.
        """
        self.tabs = QTabWidget()
        
        # Initialize product view
        self.product_view = ProductFormView()
        self.product_view.submitButton.clicked.connect(self._add_product)
        self.product_view.deleteButton.clicked.connect(self._remove_product)
        
        # Initialize customer view
        self.customer_view = CustomerFormView()
        self.customer_view.submitButton.clicked.connect(self._add_customer)
        self.customer_view.deleteButton.clicked.connect(self._remove_customer)
        
        # Add tabs
        self.tabs.addTab(self.product_view, "Products")
        self.tabs.addTab(self.customer_view, "Customers")
        
        # Set central widget
        self.main_window.setCentralWidget(self.tabs)
    
    def _show_database_settings(self):
        """
        Show the database settings dialog.
        """
        dialog = DatabaseSettingsDialog(self.main_window)
        
        if dialog.exec_():
            self._reconnect_database(dialog.get_config())
    
    def _reconnect_database(self, config=None):
        """
        Reconnect to the database with new settings.
        
        Args:
            config (DatabaseConfig, optional): New database configuration.
                If None, the existing configuration will be used.
        """
        # Close existing connection
        if hasattr(self, 'db_connection') and self.db_connection:
            self.db_connection.disconnect()
        
        # Create new connection
        factory = DatabaseConnectionFactory(config)
        self.db_connection = factory.create_connection()
        
        # Update managers
        self.product_manager.db = self.db_connection
        self.product_manager.load_all()
        
        self.customer_manager.db = self.db_connection
        self.customer_manager.load_all()
        
        # Update views
        self.product_view.updateProductList(self.product_manager.items)
        self.customer_view.updateCustomerList(self.customer_manager.items)
    
    def _import_sample_data(self):
        """
        Import sample data into the database if it's empty.
        """
        # Check if the database is empty
        product_count_query = "SELECT COUNT(*) as count FROM products"
        result = self.db_connection.fetch_one(product_count_query)
        
        if result and result.get('count', 0) == 0:
            logger.info("Database is empty. Importing sample data...")
            
            # Add sample products
            sample_products = [
                Product(name="Laptop", price=999.99, quantity=10),
                Product(name="Mouse", price=19.99, quantity=50),
                Product(name="Keyboard", price=49.99, quantity=30),
                Product(name="Monitor", price=299.99, quantity=15)
            ]
            
            for product in sample_products:
                self.product_manager.add(product)
            
            # Add sample customers
            sample_customers = [
                Customer(name="John Doe", address="123 Main St", email="john@example.com", phone="555-1234"),
                Customer(name="Jane Smith", address="456 Oak Ave", email="jane@example.com", phone="555-5678"),
                Customer(name="Bob Johnson", address="789 Pine Rd", email="bob@example.com", phone="555-9012")
            ]
            
            for customer in sample_customers:
                self.customer_manager.add(customer)
            
            # Update views
            self.product_view.updateProductList(self.product_manager.items)
            self.customer_view.updateCustomerList(self.customer_manager.items)
            
            logger.info("Sample data imported successfully.")
            QMessageBox.information(self.main_window, "Sample Data", "Sample data has been imported successfully.")
        else:
            logger.info("Database already contains data. Skipping sample import.")
            QMessageBox.information(self.main_window, "Sample Data", "Database already contains data. No new data was imported.")
    
    def closeEvent(self, event):
        """
        Handle the window close event to clean up resources.
        
        Args:
            event: The close event object.
        """
        if hasattr(self, 'db_connection') and self.db_connection:
            logger.info("Closing database connection...")
            self.db_connection.disconnect()
        event.accept()
    
    def _add_product(self):
        """
        Add a new product to the inventory.
        """
        name, price, quantity = self.product_view.getInput()
        
        # Validate inputs
        if not name:
            self._show_message(self.product_view, "Error", "Product name cannot be empty!")
            return
        
        if not price:
            self._show_message(self.product_view, "Error", "Price cannot be empty!")
            return
        
        if not quantity:
            self._show_message(self.product_view, "Error", "Quantity cannot be empty!")
            return
        
        # Create and add product
        try:
            product = Product(name=name, price=float(price), quantity=int(quantity))
            
            if self.product_manager.add(product):
                self.product_view.clearInputs()
                self.product_view.updateProductList(self.product_manager.items)
                self._show_message(self.product_view, "Success", f"Product '{name}' successfully added!")
            else:
                self._show_message(self.product_view, "Error", f"Failed to add product: {self.product_manager.db.error}")
                
        except ValueError as e:
            self._show_message(self.product_view, "Error", str(e))
    
    def _remove_product(self):
        """
        Remove a product from the inventory.
        """
        selected_items = self.product_view.listWidget.selectedItems()
        
        if not selected_items:
            self._show_message(self.product_view, "Note", "Please select a product to remove.")
            return
        
        for item in selected_items:
            self.product_view.listWidget.takeItem(self.product_view.listWidget.row(item))
            
            try:
                # Extract ID from item text
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                
                if self.product_manager.remove(selected_id):
                    logger.info(f"Product removed: {selected_id}")
                else:
                    self._show_message(self.product_view, "Error", f"Failed to remove product: {self.product_manager.db.error}")
                    return
                    
            except (ValueError, IndexError) as e:
                self._show_message(self.product_view, "Error", f"Error removing product: {str(e)}")
                return
        
        self._show_message(self.product_view, "Success", "Selected products have been removed.")
    
    def _add_customer(self):
        """
        Add a new customer to the database.
        """
        name, address, email, phone = self.customer_view.getInput()
        
        # Validate inputs
        if not name:
            self._show_message(self.customer_view, "Error", "Name cannot be empty!")
            return
        
        if not address:
            self._show_message(self.customer_view, "Error", "Address cannot be empty!")
            return
        
        if not email:
            self._show_message(self.customer_view, "Error", "Email cannot be empty!")
            return
        
        # Create and add customer
        try:
            customer = Customer(name=name, address=address, email=email, phone=phone)
            
            if self.customer_manager.add(customer):
                self.customer_view.clearInputs()
                self.customer_view.updateCustomerList(self.customer_manager.items)
                self._show_message(self.customer_view, "Success", f"Customer '{name}' successfully added!")
            else:
                self._show_message(self.customer_view, "Error", f"Failed to add customer: {self.customer_manager.db.error}")
                
        except ValueError as e:
            self._show_message(self.customer_view, "Error", str(e))
    
    def _remove_customer(self):
        """
        Remove a customer from the database.
        """
        selected_items = self.customer_view.listWidget.selectedItems()
        
        if not selected_items:
            self._show_message(self.customer_view, "Note", "Please select a customer to remove.")
            return
        
        for item in selected_items:
            self.customer_view.listWidget.takeItem(self.customer_view.listWidget.row(item))
            
            try:
                # Extract ID from item text
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                
                if self.customer_manager.remove(selected_id):
                    logger.info(f"Customer removed: {selected_id}")
                else:
                    self._show_message(self.customer_view, "Error", f"Failed to remove customer: {self.customer_manager.db.error}")
                    return
                    
            except (ValueError, IndexError) as e:
                self._show_message(self.customer_view, "Error", f"Error removing customer: {str(e)}")
                return
        
        self._show_message(self.customer_view, "Success", "Selected customers have been removed.")
    
    def _show_message(self, view, title, message):
        """
        Display a message box in the specified view.
        
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
        Update the views with loaded data and display the main window.
        """
        self.product_view.updateProductList(self.product_manager.items)
        self.customer_view.updateCustomerList(self.customer_manager.items)
        self.main_window.show()