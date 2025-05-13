import logging
from abc import ABC, abstractmethod
from typing import List, Optional, Type

from model.base_model import BaseModel

logger = logging.getLogger('BaseManager')

class BaseManager(ABC):
    """
    Base class for all managers that handle database operations for models.
    
    This abstract class provides common functionality for manager classes,
    reducing code duplication and ensuring consistent behavior.
    
    Attributes:
        _items (list): A list of model instances.
        db: Database connection instance.
        model_class (Type[BaseModel]): The model class this manager handles.
    """
    
    def __init__(self, db_connection, model_class: Type[BaseModel]):
        """
        Initialize a new BaseManager instance.
        
        Args:
            db_connection: Database connection to use.
            model_class: The model class this manager handles.
        """
        self._items = []
        self.db = db_connection
        self.model_class = model_class
        
    @property
    def items(self) -> List[BaseModel]:
        """
        Get all items managed by this manager.
        
        Returns:
            List[BaseModel]: A list of model instances.
        """
        return self._items
    
    @abstractmethod
    def get_table_name(self) -> str:
        """
        Get the database table name for this manager.
        
        Returns:
            str: The table name.
        """
        pass
    
    @abstractmethod
    def model_to_db_mapping(self) -> dict:
        """
        Get the mapping between model attributes and database columns.
        
        Returns:
            dict: A mapping from model attributes to database columns.
        """
        pass
    
    @abstractmethod
    def db_to_model_factory(self, db_row: dict) -> BaseModel:
        """
        Create a model instance from a database row.
        
        Args:
            db_row (dict): The database row.
            
        Returns:
            BaseModel: A new model instance.
        """
        pass
    
    def add(self, item: BaseModel) -> bool:
        """
        Add a new item to the database.
        
        Args:
            item (BaseModel): The item to add.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if not isinstance(item, self.model_class):
            logger.error(f"Cannot add item of type {type(item).__name__}, expected {self.model_class.__name__}")
            return False
        
        try:
            # Validate the item before adding
            item.validate()
            
            # Get field mapping
            mapping = self.model_to_db_mapping()
            
            # Prepare columns and values for insert
            columns = ", ".join(mapping.values())
            placeholders = ", ".join(["?"] * len(mapping))
            
            # Build query
            query = f"INSERT INTO {self.get_table_name()} ({columns}) VALUES ({placeholders})"
            
            # Get values from item
            values = [getattr(item, attr) for attr in mapping.keys()]
            
            # Execute query
            if self.db.execute_query(query, tuple(values)):
                self.db.commit()
                
                # Set ID from database
                setattr(item, "id", self.db.get_last_insert_id())
                
                # Add to local cache
                self._items.append(item)
                
                logger.info(f"Added {type(item).__name__}: {item}")
                return True
            else:
                logger.error(f"Failed to add {type(item).__name__}: {self.db.error}")
                return False
                
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return False
        except Exception as e:
            logger.error(f"Error adding {type(item).__name__}: {e}")
            return False
    
    def remove(self, item_id: int) -> bool:
        """
        Remove an item from the database.
        
        Args:
            item_id (int): The ID of the item to remove.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            id_field = self.get_id_field_name()
            query = f"DELETE FROM {self.get_table_name()} WHERE {id_field} = ?"
            
            if self.db.execute_query(query, (item_id,)):
                self.db.commit()
                
                # Update local cache
                self._items = [item for item in self._items if getattr(item, "id") != item_id]
                
                logger.info(f"Removed {self.model_class.__name__} with ID {item_id}")
                return True
            else:
                logger.error(f"Failed to remove {self.model_class.__name__}: {self.db.error}")
                return False
                
        except Exception as e:
            logger.error(f"Error removing {self.model_class.__name__}: {e}")
            return False
    
    def load_all(self) -> bool:
        """
        Load all items from the database.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            query = f"SELECT * FROM {self.get_table_name()}"
            result = self.db.fetch_all(query)
            
            self._items = []
            
            if result:
                for row in result:
                    try:
                        item = self.db_to_model_factory(row)
                        self._items.append(item)
                    except ValueError as e:
                        logger.error(f"Error creating {self.model_class.__name__} from row: {e}")
                
                logger.info(f"Loaded {len(self._items)} {self.model_class.__name__} instances from database")
                return True
            else:
                if self.db.error:
                    logger.error(f"Error loading {self.model_class.__name__} instances: {self.db.error}")
                    return False
                logger.info(f"No {self.model_class.__name__} instances found in database")
                return True
                
        except Exception as e:
            logger.error(f"Error loading {self.model_class.__name__} instances: {e}")
            return False
    
    def get_by_id(self, item_id: int) -> Optional[BaseModel]:
        """
        Get an item by its ID.
        
        Args:
            item_id (int): The ID of the item to get.
            
        Returns:
            Optional[BaseModel]: The item if found, None otherwise.
        """
        try:
            id_field = self.get_id_field_name()
            query = f"SELECT * FROM {self.get_table_name()} WHERE {id_field} = ?"
            result = self.db.fetch_one(query, (item_id,))
            
            if result:
                try:
                    return self.db_to_model_factory(result)
                except ValueError as e:
                    logger.error(f"Error creating {self.model_class.__name__} object: {e}")
                    return None
            else:
                return None
                
        except Exception as e:
            logger.error(f"Error getting {self.model_class.__name__} by ID: {e}")
            return None
    
    def get_id_field_name(self) -> str:
        """
        Get the name of the ID field in the database.
        
        Returns:
            str: The name of the ID field.
        """
        # Default implementation based on table name convention
        singular = self.get_table_name().rstrip('s')
        return f"{singular}_id"