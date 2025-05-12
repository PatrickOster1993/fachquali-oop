import logging
from model.base_manager import BaseManager
from model.product_model import Product

logger = logging.getLogger('ProductManager')

class ProductManager(BaseManager):
    """
    Manager for handling Product model database operations.
    
    Attributes:
        db: Database connection instance.
    """
    
    def __init__(self, db_connection):
        """
        Initialize a new ProductManager instance.
        
        Args:
            db_connection: Database connection to use.
        """
        super().__init__(db_connection, Product)
        self.load_all()
    
    def get_table_name(self) -> str:
        """
        Get the database table name for this manager.
        
        Returns:
            str: The table name.
        """
        return "products"
    
    def model_to_db_mapping(self) -> dict:
        """
        Get the mapping between model attributes and database columns.
        
        Returns:
            dict: A mapping from model attributes to database columns.
        """
        return {
            "name": "name", 
            "price": "price", 
            "quantity": "quantity"
        }
    
    def db_to_model_factory(self, db_row: dict) -> Product:
        """
        Create a Product instance from a database row.
        
        Args:
            db_row (dict): The database row.
            
        Returns:
            Product: A new Product instance.
        """
        return Product(
            name=db_row['name'],
            price=db_row['price'],
            quantity=db_row['quantity'],
            id=db_row['product_id']
        )