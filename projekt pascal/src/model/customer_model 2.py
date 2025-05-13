import re

class Customer:
    """
    Represents a customer in the inventory system.
 
    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        customerId (int): Unique identifier for the customer.

    Methods:
        __init__(name, address, email, phone, customerId): Initializes a new instance of the Customer class.
        __str__(): Returns a string representation of the Customer instance.
        toDict(): Converts the Customer instance to a dictionary.
    """
    
    def __init__(self, name: str, address: str, email: str, phone: str, customerId = None):
        """
        Initializes a new instance of the Customer class.
 
        Args:
            name (str): The name of the customer.
            address (str): The address of the customer.
            email (str): The email address of the customer.
            phone (str): The phone number of the customer.
            customerId (int, optional): The unique identifier for the customer. Defaults to None.
        """
        self.customerId = int(customerId) if customerId is not None else None
        
        if not name:
            raise ValueError("Customer name cannot be empty.")
        self.name = str(name)
        
        if not address:
            raise ValueError("Customer address cannot be empty.")
        self.address = str(address)
        
        if not email:
            raise ValueError("Customer email cannot be empty.")
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format. Please use format: name@example.com")
        self.email = str(email)
        
        self.phone = str(phone) if phone else ""

    def toDict(self):
        """
        Converts the Customer instance to a dictionary.

        Returns:
            dict: A dictionary representation of the customer.
        """
        return {
            "customerId": self.customerId,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone": self.phone
        }

    def __str__(self):
        """
        Returns a string representation of the Customer instance.
 
        Returns:
            str: A string describing the customer.
        """
        return f"Customer(customerId: {self.customerId}, name={self.name}, address={self.address}, email={self.email}, phone={self.phone})"