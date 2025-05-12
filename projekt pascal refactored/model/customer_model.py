import re
from model.base_model import BaseModel

class Customer(BaseModel):
    """
    Represents a customer in the system.
 
    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        id (int): Unique identifier for the customer.
    """
    
    def __init__(self, name: str, address: str, email: str, phone: str, id=None):
        """
        Initialize a new Customer instance.
 
        Args:
            name (str): The name of the customer.
            address (str): The address of the customer.
            email (str): The email address of the customer.
            phone (str): The phone number of the customer.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.name = str(name) if name else ""
        self.address = str(address) if address else ""
        self.email = str(email) if email else ""
        self.phone = str(phone) if phone else ""
        
        # Validate all fields
        self.validate()
    
    def validate(self):
        """
        Validate the customer attributes.
        
        Raises:
            ValueError: If any attributes are invalid.
        """
        if not self.name:
            raise ValueError("Customer name cannot be empty.")
            
        if not self.address:
            raise ValueError("Customer address cannot be empty.")
            
        if not self.email:
            raise ValueError("Customer email cannot be empty.")
            
        # Validate email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, self.email):
            raise ValueError("Invalid email format. Please use format: name@example.com")