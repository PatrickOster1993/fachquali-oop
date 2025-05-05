from .product_model import Product

class InventoryManager:
    
    def __init__(self):
        self.products = []
        self.currentId = None
    
    def addProduct(self, product: Product):
        pass

    def removeProduct(self, productId: int):
        pass

    def saveProducts(self):
        pass

    def loadProducts(self):
        pass

    def getProduct(self, productId: int) -> Product:
        pass
    
