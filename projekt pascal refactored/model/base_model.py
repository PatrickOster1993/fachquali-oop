from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
    Base class for all models in the application.
    
    This abstract class provides common functionality for model classes,
    reducing code duplication and ensuring consistent behavior.
    
    Attributes:
        id (int): The unique identifier for the model instance.
    """
    
    def __init__(self, id=None):
        """
        Initialize a new BaseModel instance.
        
        Args:
            id (int, optional): The unique identifier. Defaults to None.
        """
        self.id = int(id) if id is not None else None
    
    @abstractmethod
    def validate(self):
        """
        Validate the model's attributes.
        
        Raises:
            ValueError: If any attributes are invalid.
        """
        pass
    
    def to_dict(self):
        """
        Convert the model to a dictionary.
        
        Returns:
            dict: A dictionary representation of the model.
        """
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
    
    def __str__(self):
        """
        Return a string representation of the model.
        
        Returns:
            str: A string describing the model.
        """
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{key}={value}" for key, value in self.to_dict().items())
        return f"{class_name}({attributes})"