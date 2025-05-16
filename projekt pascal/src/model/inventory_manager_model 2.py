from .product_model import Product
from .MariaDBConnection import MariaDBConnection
from .database_queries import DatabaseQueries
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('InventoryManager')

class InventoryManager:
    """
    InventoryManager is responsible for managing the inventory of products.
    It provides methods to add, remove, and retrieve products using a MariaDB database.
    
    Attributes:
        products (list): A list of Product objects representing the inventory.
        db: MariaDBConnection instance for database operations.
        
    Methods:
        addProduct(product): Adds a new product to the inventory.
        removeProduct(productId): Removes a product from the inventory based on its ID.
        loadProducts(): Loads the inventory from the database.
        getProduct(productId): Retrieves a product from the inventory based on its ID.
    """
    def __init__(self, db_connection=None):
        """
        Initializes the InventoryManager with a database connection and loads products.
        
        Args:
            db_connection (MariaDBConnection, optional): Database connection to use.
                If None, a new connection will be created.
        """
        self.products = []
        
        if db_connection:
            self.db = db_connection
        else:
            self.db = MariaDBConnection(
                host="localhost",
                user="root",
                password="",
                database="wawi"
            )
            
        self.loadProducts()

    def addProduct(self, product: Product):
        """
        Adds a new product to the inventory database.
        
        Args:
            product (Product): The product to be added to the inventory.
        """
        query = DatabaseQueries.insert_product_query()
        
        if self.db.execute_query(query, (product.name, product.price, product.quantity)):
            self.db.commit()
            product.productId = self.db.get_last_insert_id()
            self.products.append(product)
            logger.info(f"Product added: {product}")
            return True
        else:
            logger.error(f"Failed to add product: {self.db.error}")
            return False

    def removeProduct(self, productId: int):
        """
        Removes a product from the inventory based on its ID.
        
        Args:
            productId (int): The ID of the product to be removed.
        """
        query = DatabaseQueries.delete_product_query()
        
        if self.db.execute_query(query, (productId,)):
            self.db.commit()
            # Update local cache
            self.products = [product for product in self.products if product.productId != productId]
            logger.info(f"Product removed: ID {productId}")
            return True
        else:
            logger.error(f"Failed to remove product: {self.db.error}")
            return False
            
    def loadProducts(self):
        """
        Loads the inventory from the database.
        """
        query = DatabaseQueries.select_all_products_query()
        result = self.db.fetch_all(query)
        
        self.products = []
        if result:
            for row in result:
                try:
                    product = Product(
                        name=row['name'],
                        price=row['price'],
                        quantity=row['quantity'],
                        productId=row['product_id']
                    )
                    self.products.append(product)
                except ValueError as e:
                    logger.error(f"Error loading product: {e}")
            
            logger.info(f"Loaded {len(self.products)} products from database")
        else:
            if self.db.error:
                logger.error(f"Error loading products: {self.db.error}")

    def getProduct(self, productId: int) -> Product:
        """
        Retrieves a product from the inventory based on its ID.
        
        Args:
            productId (int): The ID of the product to be retrieved.
            
        Returns:
            Product: The product object if found, otherwise None.
        """
        query = DatabaseQueries.select_product_by_id_query()
        result = self.db.fetch_one(query, (productId,))
        
        if result:
            try:
                return Product(
                    name=result['name'],
                    price=result['price'],
                    quantity=result['quantity'],
                    productId=result['product_id']
                )
            except ValueError as e:
                logger.error(f"Error creating product object: {e}")
                return None
        else:
            return None