from model.inventory_manager_model import InventoryManager
from model.product_model import Product
from view.product_form_view import ProductFormView
from model.customer_manager_model import CustomerManager
from model.customer_model import Customer
from view.customer_form_view import CustomerFormView
from model.database_config import DatabaseConfig
from view.database_settings_dialog import DatabaseSettingsDialog
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QAction, QMenu
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MainController')

class MainController:
    """
    The MainController class acts as the central controller of the application.

    It connects the views (ProductFormView, CustomerFormView) with the models 
    (InventoryManager, CustomerManager) and handles user interactions.
    """
    
    def __init__(self):
        """
        Initializes the MainController with models and views and
        sets up the main window with tabs.
        """
        from model.SQLiteConnection import SQLiteConnection

        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "wawi.db")

        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        self.db_connection = SQLiteConnection(db_path)

        from model.database_queries import DatabaseQueries
        self.db_connection.create_tables(DatabaseQueries.create_tables_query())

        test_query = "SELECT 1 FROM products LIMIT 1"
        if self.db_connection.execute_query(test_query):
            logger.info("Database tables verified.")
        else:
            logger.warning("Database tables might not exist or are empty.")

        self.inventory_manager = InventoryManager(self.db_connection)
        self.customer_manager = CustomerManager(self.db_connection)

        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("WaWi - Warehouse Management System")
        self.main_window.setMinimumSize(600, 500)

        self.main_window.closeEvent = self.closeEvent

        self.createMenus()
        
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
    
    def createMenus(self):
        """
        Creates application menus.
        """
        menu_bar = self.main_window.menuBar()

        file_menu = menu_bar.addMenu("File")

        settings_action = QAction("Database Settings", self.main_window)
        settings_action.triggered.connect(self.showDatabaseSettings)
        file_menu.addAction(settings_action)

        import_action = QAction("Import Sample Data", self.main_window)
        import_action.triggered.connect(self.importSampleData)
        file_menu.addAction(import_action)

        exit_action = QAction("Exit", self.main_window)
        exit_action.triggered.connect(self.main_window.close)
        file_menu.addAction(exit_action)
    
    def showDatabaseSettings(self):
        """
        Shows the database settings dialog.
        """
        dialog = DatabaseSettingsDialog(self.main_window)
        
        if dialog.exec_():
            self.reconnectDatabase(dialog.get_config())
    
    def reconnectDatabase(self, config=None):
        """
        Reconnects to the database with the current settings.
        
        Args:
            config (DatabaseConfig, optional): New database configuration.
                If None, the existing configuration will be used.
        """
        if hasattr(self, 'db_connection') and self.db_connection:
            self.db_connection.disconnect()

        if config:
            db_type = config.get_active_db_type()
            
            if db_type == "mariadb":
                from model.MariaDBConnection import MariaDBConnection
                mariadb_config = config.get_mariadb_config()
                
                try:
                    self.db_connection = MariaDBConnection(
                        host=mariadb_config.get("host", "localhost"),
                        user=mariadb_config.get("user", "root"),
                        password=mariadb_config.get("password", ""),
                        database=mariadb_config.get("database", "wawi")
                    )
                    logger.info("Reconnected to MariaDB.")
                except Exception as e:
                    logger.warning(f"Error connecting to MariaDB: {e}. Falling back to SQLite.")
                    self._create_sqlite_connection(config)
            else:
                self._create_sqlite_connection(config)
        else:
            self._create_sqlite_connection()

        from model.database_queries import DatabaseQueries
        self.db_connection.create_tables(DatabaseQueries.create_tables_query())

        self.inventory_manager.db = self.db_connection
        self.inventory_manager.loadProducts()
        
        self.customer_manager.db = self.db_connection
        self.customer_manager.loadCustomers()

        self.product_view.updateProductList(self.inventory_manager.products)
        self.customer_view.updateCustomerList(self.customer_manager.customers)

    def _create_sqlite_connection(self, config=None):
        """
        Creates a SQLite connection.
        
        Args:
            config (DatabaseConfig, optional): Database configuration.
                If None, the default path will be used.
        """
        from model.SQLiteConnection import SQLiteConnection
        import os
        
        if config:
            sqlite_config = config.get_sqlite_config()
            database_path = sqlite_config.get("database_path")
        else:
            database_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "wawi.db")
        
        os.makedirs(os.path.dirname(database_path), exist_ok=True)

        self.db_connection = SQLiteConnection(database_path)
        logger.info(f"Connected to SQLite database at {database_path}")
    
    def importSampleData(self):
        """
        Imports sample data into the database if it's empty.
        """
        # check if the database is empty
        product_count_query = "SELECT COUNT(*) as count FROM products"
        result = self.db_connection.fetch_one(product_count_query)
        
        if result and result.get('count', 0) == 0:
            logger.info("Database is empty. Importing sample data...")
            
            # add sample products for testing
            sample_products = [
                Product(name="Laptop", price=999.99, quantity=10),
                Product(name="Mouse", price=19.99, quantity=50),
                Product(name="Keyboard", price=49.99, quantity=30),
                Product(name="Monitor", price=299.99, quantity=15)
            ]
            
            for product in sample_products:
                self.inventory_manager.addProduct(product)
            
            # add sample customers to the database for testing
            sample_customers = [
                Customer(name="John Doe", address="123 Main St", email="john@example.com", phone="555-1234"),
                Customer(name="Jane Smith", address="456 Oak Ave", email="jane@example.com", phone="555-5678"),
                Customer(name="Bob Johnson", address="789 Pine Rd", email="bob@example.com", phone="555-9012")
            ]
            
            for customer in sample_customers:
                self.customer_manager.addCustomer(customer)
            
            self.product_view.updateProductList(self.inventory_manager.products)
            self.customer_view.updateCustomerList(self.customer_manager.customers)
            
            logger.info("Sample data imported successfully.")
            QMessageBox.information(self.main_window, "Sample Data", "Sample data has been imported successfully.")
        else:
            logger.info("Database already contains data. Skipping sample import.")
            QMessageBox.information(self.main_window, "Sample Data", "Database already contains data. No new data was imported.")
            
    def closeEvent(self, event):
        """
        Handles the window close event to clean up resources.
        
        Args:
            event: The close event object.
        """
        if hasattr(self, 'db_connection') and self.db_connection:
            logger.info("Closing database connection...")
            self.db_connection.disconnect()
        event.accept()

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
                price=float(price),
                quantity=int(quantity)
            )
            if self.inventory_manager.addProduct(product):
                self.product_view.clearInputs()
                self.product_view.updateProductList(self.inventory_manager.products)
                self.showMessage(self.product_view, "Success", f"Product '{name}' successfully added!")
            else:
                self.showMessage(self.product_view, "Error", f"Failed to add product: {self.inventory_manager.db.error}")
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
                if self.inventory_manager.removeProduct(selected_id):
                    logger.info(f"Product removed: {selected_id}")
                else:
                    self.showMessage(self.product_view, "Error", f"Failed to remove product: {self.inventory_manager.db.error}")
                    return
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
            if self.customer_manager.addCustomer(customer):
                self.customer_view.clearInputs()
                self.customer_view.updateCustomerList(self.customer_manager.customers)
                self.showMessage(self.customer_view, "Success", f"Customer '{name}' successfully added!")
            else:
                self.showMessage(self.customer_view, "Error", f"Failed to add customer: {self.customer_manager.db.error}")
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
                if self.customer_manager.removeCustomer(selected_id):
                    logger.info(f"Customer removed: {selected_id}")
                else:
                    self.showMessage(self.customer_view, "Error", f"Failed to remove customer: {self.customer_manager.db.error}")
                    return
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