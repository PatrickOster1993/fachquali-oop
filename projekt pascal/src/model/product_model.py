class Product:
    """
    Represents a product in the inventory system.
 
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        productId (int): ID of the product.

    Methods:
        __init__(productId, name, price, quantity): Initializes a new instance of the Product class.
        __str__(): Returns a string representation of the Product instance.
        toDict(): Converts the Product instance to a dictionary.
    """
    
    def __init__(self, name: str, price: float, quantity: int, productId = None):
        """
        Initializes a new instance of the Product class.

        Args:
            productId (int): The unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        self.productId = int(productId) if productId is not None else None
        self.name = str(name)
        
        try:
            self.price = float(price)
            if self.price < 0:
                raise ValueError("Price must not be negative.")
        except ValueError:
            raise ValueError("Price must be a number.")

        try:
            self.quantity = int(quantity)
            if self.quantity < 0:
                raise ValueError("Quantity must not be negative.")
        except ValueError:
            raise ValueError("Quantity must be an integer")
        

    def toDict(self):
        """
        Converts the Product instance to a dictionary.

        Returns:
            dict: A dictionary representation of the product.
        """
        return {
            "productId": self.productId,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self):
        """
        Returns a string representation of the Product instance.
 
        Returns:
            str: A string describing the product.
        """
        return f"Product(productId: {self.productId}, name={self.name}, price={self.price}, quantity={self.quantity})"
    

# help(Product) # Zeigt entsprechende Doku für jeweilige Klasse in Konsole!
