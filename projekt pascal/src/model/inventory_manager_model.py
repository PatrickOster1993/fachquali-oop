from .product_model import Product
import os
import json

class InventoryManager:
    """
    InventoryManager is responsible for managing the inventory of products.
    It provides methods to add, remove, save, load, and retrieve products.
    
    Attributes:
        products (list): A list of Product objects representing the inventory.
        currentId (int): The ID of the currently selected product.
        path (str): Path to the product data file.
        
    Methods:
        addProduct(product): Adds a new product to the inventory.
        removeProduct(productId): Removes a product from the inventory based on its ID.
        saveProduct(): Saves the current product to a file.
        loadProducts(): Loads the inventory from a file.
        getProduct(productId): Retrieves a product from the inventory based on its ID.
    """
    def __init__(self):
        """
        Initializes the InventoryManager with an empty product list and sets the currentId to 0.
        """
        self.products = []
        self.currentId = 0
        self.path = os.getcwd() + "/projekt pascal/src/data/products.json"
        self.loadProducts()

    def addProduct(self, product: Product):
        """
        Adds a new product to the inventory.
        
        Args:
            product (Product): The product to be added to the inventory.
        """
        self.currentId += 1
        product.productId = self.currentId
        self.products.append(product)
        self.saveProduct()

    def removeProduct(self, productId: int):
        """
        Removes a product from the inventory based on its ID.
        
        Args:
            productId (int): The ID of the product to be removed.
        """
        self.products = [product for product in self.products if product.productId != productId]
        self.saveProduct()

    def saveProduct(self):
        """
        Saves the current products to a file.
        """
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            
            with open(self.path, 'w') as file:
                json.dump([product.toDict() for product in self.products], file)
        except Exception as e:
            print(f"Products could not be saved as .json in {self.path}! Error: {e}")
            
    def loadProducts(self):
        """
        Loads the inventory from a file.
        Sets currentId to the highest existing productId.
        """
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                self.products = []
                max_id = 0
                for elem in data:
                    elem_dict = dict(elem)
                    try:
                        loaded_product = Product(
                            elem_dict["name"],
                            elem_dict["price"],
                            elem_dict["quantity"],
                            elem_dict["productId"]
                        )
                        self.products.append(loaded_product)
                        if loaded_product.productId > max_id:
                            max_id = loaded_product.productId
                    except (KeyError, ValueError) as e:
                        print(f"Error loading product: {e}")
                self.currentId = max_id
        except (FileNotFoundError, json.JSONDecodeError):
            print("Could not access the file!")
            self.products = []
            self.currentId = 0


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