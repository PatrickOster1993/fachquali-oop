import logging
from model.base_manager import BaseManager
from model.customer_model import Customer

logger = logging.getLogger('CustomerManager')

class CustomerManager(BaseManager):
    """
    Manager for handling Customer model database operations.
    
    Attributes:
        db: Database connection instance.
    """
    
    def __init__(self, db_connection):
        """
        Initialize a new CustomerManager instance.
        
        Args:
            db_connection: Database connection to use.
        """
        super().__init__(db_connection, Customer)
        self.load_all()
    
    def get_table_name(self) -> str:
        """
        Get the database table name for this manager.
        
        Returns:
            str: The table name.
        """
        return "customers"
    
    def model_to_db_mapping(self) -> dict:
        """
        Get the mapping between model attributes and database columns.
        
        Returns:
            dict: A mapping from model attributes to database columns.
        """
        return {
            "name": "name", 
            "address": "address", 
            "email": "email", 
            "phone": "phone"
        }
    
    def db_to_model_factory(self, db_row: dict) -> Customer:
        """
        Create a Customer instance from a database row.
        
        Args:
            db_row (dict): The database row.
            
        Returns:
            Customer: A new Customer instance.
        """
        return Customer(
            name=db_row['name'],
            address=db_row['address'],
            email=db_row['email'],
            phone=db_row['phone'],
            id=db_row['customer_id']
        )