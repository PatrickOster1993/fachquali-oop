from .base_model import BaseModel

class Product(BaseModel):
    """
    Represents a product in the inventory system.
 
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        id (int): Unique identifier for the product.
    """
    
    def __init__(self, name: str, price: float, quantity: int, id=None):
        """
        Initialize a new Product instance.
 
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.name = str(name) if name else ""
        self.price = None
        self.quantity = None
        
        # Set price and quantity through properties to ensure validation
        self.set_price(price)
        self.set_quantity(quantity)
        
        # Final validation
        self.validate()
    
    def set_price(self, price):
        """
        Set the product price with validation.
        
        Args:
            price (float or str): The price to set. Can be a float or a string with decimal point or comma.
            
        Raises:
            ValueError: If price is not a valid number or is negative.
        """
        try:
            # Handle string input
            if isinstance(price, str):
                # Replace comma with dot for decimal values
                price = price.replace(',', '.')
            
            parsed_price = float(price)
            if parsed_price < 0:
                raise ValueError("Price cannot be negative.")
            self.price = parsed_price
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number.")
    
    def set_quantity(self, quantity):
        """
        Set the product quantity with validation.
        
        Args:
            quantity (int): The quantity to set.
            
        Raises:
            ValueError: If quantity is not a valid integer or is negative.
        """
        try:
            parsed_quantity = int(quantity)
            if parsed_quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            self.quantity = parsed_quantity
        except (ValueError, TypeError):
            raise ValueError("Quantity must be an integer.")
    
    def validate(self):
        """
        Validate the product attributes.
        
        Raises:
            ValueError: If any attributes are invalid.
        """
        if not self.name:
            raise ValueError("Product name cannot be empty.")
        if self.price is None:
            raise ValueError("Product must have a valid price.")
        if self.quantity is None:
            raise ValueError("Product must have a valid quantity.")