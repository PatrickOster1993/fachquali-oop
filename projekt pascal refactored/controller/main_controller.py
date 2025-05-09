import logging
import os
from typing import Dict, Any, Tuple

from PyQt5.QtWidgets import (QTabWidget, QMainWindow, QAction, QMessageBox)
from PyQt5.QtCore import Qt

from model.product_model import Product
from model.customer_model import Customer
from model.product_manager import ProductManager
from model.customer_manager import CustomerManager
from model.database_config import DatabaseConfig
from model.database_connection_factory import DatabaseConnectionFactory
from view.product_form_view import ProductFormView
from view.customer_form_view import CustomerFormView
from view.database_settings_dialog import DatabaseSettingsDialog
from model.logger_service import LoggerService
from model.app_info import ABOUT_TEXT, HOW_TO_USE_TEXT

logger = LoggerService.get_logger('MainController')

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
        
        # Help menu
        help_menu = menu_bar.addMenu("Help")
        
        # How to use action
        how_to_action = QAction("How to Use", self.main_window)
        how_to_action.triggered.connect(self._show_how_to_use)
        help_menu.addAction(how_to_action)
        
        # About action
        about_action = QAction("About", self.main_window)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
    
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
        Import sample data into the database, adding only missing data.
        Existing data will be preserved.
        """
        logger.info("Checking database for sample data import...")
        
        # Sample data
        sample_products = [
            {"name": "Laptop", "price": 999.99, "quantity": 10},
            {"name": "Mouse", "price": 19.99, "quantity": 50},
            {"name": "Keyboard", "price": 49.99, "quantity": 30},
            {"name": "Monitor", "price": 299.99, "quantity": 15}
        ]
        
        sample_customers = [
            {"name": "John Doe", "address": "123 Main St", "email": "john@example.com", "phone": "555-1234"},
            {"name": "Jane Smith", "address": "456 Oak Ave", "email": "jane@example.com", "phone": "555-5678"},
            {"name": "Bob Johnson", "address": "789 Pine Rd", "email": "bob@example.com", "phone": "555-9012"}
        ]
        
        # Check existing data
        existing_products = self._get_existing_products()
        existing_customers = self._get_existing_customers()
        
        imported_products = 0
        imported_customers = 0
        
        # Import missing products
        for product_data in sample_products:
            # Check if product with this name already exists
            if not any(p.name.lower() == product_data["name"].lower() for p in existing_products):
                try:
                    product = Product(
                        name=product_data["name"],
                        price=product_data["price"],
                        quantity=product_data["quantity"]
                    )
                    
                    if self.product_manager.add(product):
                        imported_products += 1
                        logger.info(f"Imported sample product: {product_data['name']}")
                    else:
                        logger.warning(f"Failed to import sample product: {product_data['name']}")
                except Exception as e:
                    logger.error(f"Error importing sample product: {e}")
        
        # Import missing customers
        for customer_data in sample_customers:
            # Check if customer with this email already exists
            if not any(c.email.lower() == customer_data["email"].lower() for c in existing_customers):
                try:
                    customer = Customer(
                        name=customer_data["name"],
                        address=customer_data["address"],
                        email=customer_data["email"],
                        phone=customer_data["phone"]
                    )
                    
                    if self.customer_manager.add(customer):
                        imported_customers += 1
                        logger.info(f"Imported sample customer: {customer_data['name']}")
                    else:
                        logger.warning(f"Failed to import sample customer: {customer_data['name']}")
                except Exception as e:
                    logger.error(f"Error importing sample customer: {e}")
        
        # Update views
        self.product_view.updateProductList(self.product_manager.items)
        self.customer_view.updateCustomerList(self.customer_manager.items)
        
        # Show message
        if imported_products > 0 or imported_customers > 0:
            message = f"Imported {imported_products} new products and {imported_customers} new customers."
            logger.info(message)
            QMessageBox.information(self.main_window, "Sample Data", message)
        else:
            message = "No new sample data was imported. All sample data already exists."
            logger.info(message)
            QMessageBox.information(self.main_window, "Sample Data", message)
    
    def _get_existing_products(self):
        """
        Get a list of all existing products.
        
        Returns:
            list: List of existing Product objects.
        """
        # Ensure products are loaded
        self.product_manager.load_all()
        return self.product_manager.items
        
    def _get_existing_customers(self):
        """
        Get a list of all existing customers.
        
        Returns:
            list: List of existing Customer objects.
        """
        # Ensure customers are loaded
        self.customer_manager.load_all()
        return self.customer_manager.items
    
    def _show_how_to_use(self):
        """
        Show the 'How to Use' dialog.
        """
        # Create message box with content from app_info.py
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle("How to Use WaWi")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(HOW_TO_USE_TEXT)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()

    def _show_about(self):
        """
        Show the 'About' dialog.
        """
        # Create message box with content from app_info.py
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle("About WaWi")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(ABOUT_TEXT)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
    
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
            # Price is directly passed to the Product constructor
            # The Product class will handle decimal point/comma conversion
            product = Product(name=name, price=price, quantity=int(quantity))
            
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
        Remove selected products from the inventory.
        """
        selected_items = self.product_view.listWidget.selectedItems()
        
        if not selected_items:
            self._show_message(self.product_view, "Note", "Please select a product to remove.")
            return
        
        # Track statistics
        removed_count = 0
        failed_count = 0
        
        for item in selected_items:
            self.product_view.listWidget.takeItem(self.product_view.listWidget.row(item))
            
            try:
                # Extract ID from item text
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                
                if self.product_manager.remove(selected_id):
                    logger.info(f"Product removed: {selected_id}")
                    removed_count += 1
                else:
                    logger.error(f"Failed to remove product: {self.product_manager.db.error}")
                    failed_count += 1
                    
            except (ValueError, IndexError) as e:
                logger.error(f"Error removing product: {str(e)}")
                failed_count += 1
        
        # Show result message if not in silent mode or if there were failures
        if failed_count > 0:
            self._show_message(
                self.product_view, 
                "Error", 
                f"Failed to remove {failed_count} product(s)."
            )
        elif removed_count > 0:
            self._show_message(
                self.product_view, 
                "Success", 
                f"Successfully removed {removed_count} product(s)."
            )
    
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
        Remove selected customers from the database.
        """
        selected_items = self.customer_view.listWidget.selectedItems()
        
        if not selected_items:
            self._show_message(self.customer_view, "Note", "Please select a customer to remove.")
            return
        
        # Track statistics
        removed_count = 0
        failed_count = 0
        
        for item in selected_items:
            self.customer_view.listWidget.takeItem(self.customer_view.listWidget.row(item))
            
            try:
                # Extract ID from item text
                selected_id = int(item.text().split(' | ')[0].split(' ')[1])
                
                if self.customer_manager.remove(selected_id):
                    logger.info(f"Customer removed: {selected_id}")
                    removed_count += 1
                else:
                    logger.error(f"Failed to remove customer: {self.customer_manager.db.error}")
                    failed_count += 1
                    
            except (ValueError, IndexError) as e:
                logger.error(f"Error removing customer: {str(e)}")
                failed_count += 1
        
        # Show result message if not in silent mode or if there were failures
        if failed_count > 0:
            self._show_message(
                self.customer_view, 
                "Error", 
                f"Failed to remove {failed_count} customer(s)."
            )
        elif removed_count > 0:
            self._show_message(
                self.customer_view, 
                "Success", 
                f"Successfully removed {removed_count} customer(s)."
            )
    
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
            # For views that don't have a custom showMessage method
            # Check if we're in silent mode and this is a success message for removal
            if hasattr(view, 'silentDeleteCheckbox') and view.silentDeleteCheckbox.isChecked() and title == "Success" and "removed" in message:
                # Skip showing message for successful deletions in silent mode
                return
                
            QMessageBox.information(view, title, message)
    
    def start(self):
        """
        Update the views with loaded data and display the main window.
        """
        self.product_view.updateProductList(self.product_manager.items)
        self.customer_view.updateCustomerList(self.customer_manager.items)
        self.main_window.show()