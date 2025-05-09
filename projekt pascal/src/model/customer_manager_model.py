from .customer_model import Customer
from .MariaDBConnection import MariaDBConnection
from .database_queries import DatabaseQueries
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('CustomerManager')

class CustomerManager:
    """
    CustomerManager is responsible for managing customer data in a MariaDB database.
    It provides methods to add, remove, and retrieve customers.
    
    Attributes:
        customers (list): A list of Customer objects.
        db: MariaDBConnection instance for database operations.
        
    Methods:
        addCustomer(customer): Adds a new customer to the database.
        removeCustomer(customerId): Removes a customer based on their ID.
        loadCustomers(): Loads the customers from the database.
        getCustomer(customerId): Retrieves a customer based on their ID.
    """
    def __init__(self, db_connection):
        """
        Initializes the CustomerManager with a database connection and loads customers.
        
        Args:
            db_connection: Database connection to use
        """
        self.customers = []
        self.db = db_connection
        self.loadCustomers()

    def addCustomer(self, customer: Customer):
        """
        Adds a new customer to the database.
        
        Args:
            customer (Customer): The customer to be added.
        """
        query = DatabaseQueries.insert_customer_query()
        
        if self.db.execute_query(query, (customer.name, customer.address, customer.email, customer.phone)):
            self.db.commit()
            customer.customerId = self.db.get_last_insert_id()
            self.customers.append(customer)
            logger.info(f"Customer added: {customer}")
            return True
        else:
            logger.error(f"Failed to add customer: {self.db.error}")
            return False

    def removeCustomer(self, customerId: int):
        """
        Removes a customer from the database based on their ID.
        
        Args:
            customerId (int): The ID of the customer to be removed.
        """
        query = DatabaseQueries.delete_customer_query()
        
        if self.db.execute_query(query, (customerId,)):
            self.db.commit()
            # Update local cache
            self.customers = [customer for customer in self.customers if customer.customerId != customerId]
            logger.info(f"Customer removed: ID {customerId}")
            return True
        else:
            logger.error(f"Failed to remove customer: {self.db.error}")
            return False
            
    def loadCustomers(self):
        """
        Loads the customers from the database.
        """
        query = DatabaseQueries.select_all_customers_query()
        result = self.db.fetch_all(query)
        
        self.customers = []
        if result:
            for row in result:
                try:
                    customer = Customer(
                        name=row['name'],
                        address=row['address'],
                        email=row['email'],
                        phone=row['phone'],
                        customerId=row['customer_id']
                    )
                    self.customers.append(customer)
                except ValueError as e:
                    logger.error(f"Error loading customer: {e}")
            
            logger.info(f"Loaded {len(self.customers)} customers from database")
        else:
            if self.db.error:
                logger.error(f"Error loading customers: {self.db.error}")

    def getCustomer(self, customerId: int) -> Customer:
        """
        Retrieves a customer from the database based on their ID.
        
        Args:
            customerId (int): The ID of the customer to be retrieved.
            
        Returns:
            Customer: The customer object if found, otherwise None.
        """
        query = DatabaseQueries.select_customer_by_id_query()
        result = self.db.fetch_one(query, (customerId,))
        
        if result:
            try:
                return Customer(
                    name=result['name'],
                    address=result['address'],
                    email=result['email'],
                    phone=result['phone'],
                    customerId=result['customer_id']
                )
            except ValueError as e:
                logger.error(f"Error creating customer object: {e}")
                return None
        else:
            return None