from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Tuple

class DatabaseInterface(ABC):
    """
    Abstract interface for database connections.
    
    This ensures that all database implementations follow the same interface,
    making them interchangeable.
    """
    
    @abstractmethod
    def connect(self) -> bool:
        """
        Establish a connection to the database.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        """
        Close the database connection.
        
        Returns:
            bool: True if disconnection successful, False otherwise
        """
        pass
    
    @abstractmethod
    def execute_query(self, query: str, params: Optional[Tuple] = None) -> bool:
        """
        Execute a SQL query with optional parameters.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, optional): Parameters for the query
            
        Returns:
            bool: True if query executed successfully, False otherwise
        """
        pass
    
    @abstractmethod
    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Execute a query and return all matching rows.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, optional): Parameters for the query
            
        Returns:
            Optional[List[Dict[str, Any]]]: List of dictionaries with the results, or None if error
        """
        pass
    
    @abstractmethod
    def fetch_one(self, query: str, params: Optional[Tuple] = None) -> Optional[Dict[str, Any]]:
        """
        Execute a query and return a single row.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, optional): Parameters for the query
            
        Returns:
            Optional[Dict[str, Any]]: Dictionary with the result, or None if no result or error
        """
        pass
    
    @abstractmethod
    def commit(self) -> bool:
        """
        Commit the current transaction.
        
        Returns:
            bool: True if commit successful, False otherwise
        """
        pass
    
    @abstractmethod
    def rollback(self) -> bool:
        """
        Roll back the current transaction.
        
        Returns:
            bool: True if rollback successful, False otherwise
        """
        pass
    
    @abstractmethod
    def get_last_insert_id(self) -> Optional[int]:
        """
        Get the ID of the last inserted row.
        
        Returns:
            Optional[int]: The last insert ID, or None if error
        """
        pass
    
    @abstractmethod
    def create_tables(self, queries: Optional[List[str]] = None) -> bool:
        """
        Create tables in the database.
        
        Args:
            queries (List[str], optional): SQL queries to create tables
            
        Returns:
            bool: True if tables created successfully, False otherwise
        """
        pass
    
    @property
    @abstractmethod
    def error(self) -> Optional[str]:
        """
        Get the last error message.
        
        Returns:
            Optional[str]: The last error message, or None if no error
        """
        pass