import os
import json
from .ProductModel import ProductModel

class InventoryManager:

    def __init__(self):
        """
        Initializes the InventoryManager with an empty product list and sets the currentId to 0.
        """
        self.products = []
        self.currentId = 0
        self.path = os.getcwd() + "/projekt pascal/src/data/products.json"
        self.loadProducts()

    def addProduct(self, product: ProductModel):
        self.products.append(product)
        product.create(product.toDict())

    def removeProduct(self, productId: int):
        pass

    def saveProduct(self):
        pass
            
    def loadProducts(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                self.products = []
                max_id = 0
                for elem in data:
                    elem_dict = dict(elem)
                    try:
                        loaded_product = ProductModel(
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


    def getProduct(self, productId: int) -> ProductModel:
        pass