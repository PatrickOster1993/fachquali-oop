from .product_model import Product

class InventoryManager:
    """
    InventoryManager is responsible for managing the inventory of products.
    It provides methods to add, remove, save, load, and retrieve products.
    Args:
        InventoryManager (object): The base class for all classes in Python.
    Attributes:
        products (list): A list of Product objects representing the inventory.
        currentId (int): The ID of the currently selected product.
    Methods:
        addProduct(product): Adds a new product to the inventory.
        removeProduct(productId): Removes a product from the inventory based on its ID.
        saveProduct(): Saves the current product to a file.
        loadProducts(): Loads the inventory from a file.
        getProduct(productId): Retrieves a product from the inventory based on its ID.
    Example:
        inventory = InventoryManager()
        product = Product(1, "Laptop", 999.99, 10)
        inventory.addProduct(product)
        print(inventory.getProduct(1))
        inventory.saveProducts()
        inventory.loadProducts()
    """
    def __init__(self):
        """
        Initializes the InventoryManager with an empty product list and sets the currentId to None.
        Args:
            InventoryManager (object): The base class for all classes in Python.
        Attributes:
            products (list): A list of Product objects representing the inventory.
            currentId (int): The ID of the currently selected product.
        Example:
            inventory = InventoryManager()
            print(inventory.products)
            print(inventory.currentId)
        """
        self.products = []
        self.currentId = None

    def addProduct(self, product: Product):
        """
        Adds a new product to the inventory.
        Args:
            product (Product): The product to be added to the inventory.
        Returns:
            None
        """
        if product.productId in [products.productId for products in self.products]:
            raise ValueError("Product with this ID already exists.")
        else:
            self.currentId = product.productId
            self.products.append(product)
        
        self.saveProduct()

    def removeProduct(self, productId: int):
        """
        Removes a product from the inventory based on its ID.
        Args:
            productId (int): The ID of the product to be removed.
        Returns:
            None
        """
        pass
    def saveProduct(self):
        """
        Saves the current Product to a file.
        Args:
            None
        Returns:
            None
        """
        pass
    def loadProducts(self):
        """
        Loads the inventory from a file.
        Args:
            None
        Returns:
            None
        """
        pass
    def getProduct(self, productId: int) -> Product:
        """
        Retrieves a product from the inventory based on its ID.
        Args:
            productId (int): The ID of the product to be retrieved.
        Returns:
            Product: The product object if found, otherwise None.
        """
        for product in self.products:
            if product.productId == productId:
                return product
        return None
        