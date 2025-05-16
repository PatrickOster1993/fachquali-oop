import logging
import os
import sqlite3
from typing import List, Dict, Optional, Any, Tuple

from model.database_interface import DatabaseInterface

logger = logging.getLogger('SQLiteConnection')

class SQLiteConnection(DatabaseInterface):
    """
    Adapter for SQLite database connection.
    
    This class implements the DatabaseInterface for SQLite connections.
    
    Attributes:
        database_path (str): Path to the SQLite database file.
        connection: Active database connection.
        cursor: Cursor for executing queries.
        _error (str): Last error message.
    """
    
    def __init__(self, database_path: str):
        """
        Initialize a new SQLiteConnection instance.
        
        Args:
            database_path (str): Path to the SQLite database file.
        """
        self.database_path = database_path
        self.connection = None
        self.cursor = None
        self._error = None
    
    @property
    def error(self) -> Optional[str]:
        """
        Get the last error message.
        
        Returns:
            Optional[str]: The last error message, or None if no error.
        """
        return self._error
    
    def connect(self) -> bool:
        """
        Establish a connection to the database.
        
        Returns:
            bool: True if connection successful, False otherwise.
        """
        try:
            # Ensure directory exists
            db_dir = os.path.dirname(os.path.abspath(self.database_path))
            if not os.path.exists(db_dir):
                os.makedirs(db_dir)
            
            self.connection = sqlite3.connect(self.database_path)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            
            logger.info(f"Connected to SQLite database: {self.database_path}")
            return True
            
        except sqlite3.Error as e:
            self._error = f"Error connecting to SQLite: {e}"
            logger.error(self._error)
            return False
    
    def disconnect(self) -> bool:
        """
        Close the database connection.
        
        Returns:
            bool: True if disconnection successful, False otherwise.
        """
        try:
            if self.cursor:
                self.cursor.close()
                
            if self.connection:
                self.connection.close()
                
            logger.info("Disconnected from SQLite")
            return True
            
        except sqlite3.Error as e:
            self._error = f"Error disconnecting from SQLite: {e}"
            logger.error(self._error)
            return False
    
    def execute_query(self, query: str, params: Optional[Tuple] = None) -> bool:
        """
        Execute a SQL query with optional parameters.
        
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.
            
        Returns:
            bool: True if query executed successfully, False otherwise.
        """
        try:
            if not self.connection or not self.cursor:
                if not self.connect():
                    return False
            
            # Handle AUTO_INCREMENT vs AUTOINCREMENT and INT vs INTEGER differences
            if "CREATE TABLE" in query.upper():
                query = query.replace("INT AUTO_INCREMENT PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
                query = query.replace("INT ", "INTEGER ")
                    
            self.cursor.execute(query, params or ())
            return True
            
        except sqlite3.Error as e:
            self._error = f"Error executing query: {e}"
            logger.error(f"{self._error}\nQuery: {query}\nParams: {params}")
            return False
    
    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Execute a query and return all matching rows.
        
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.
            
        Returns:
            Optional[List[Dict[str, Any]]]: List of dictionaries with the results, or None if error.
        """
        try:
            if not self.execute_query(query, params):
                return None
                
            results = self.cursor.fetchall()
            
            # Convert Row objects to dictionaries
            return [{k: item[k] for k in item.keys()} for item in results]
            
        except sqlite3.Error as e:
            self._error = f"Error fetching data: {e}"
            logger.error(self._error)
            return None
    
    def fetch_one(self, query: str, params: Optional[Tuple] = None) -> Optional[Dict[str, Any]]:
        """
        Execute a query and return a single row.
        
        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.
            
        Returns:
            Optional[Dict[str, Any]]: Dictionary with the result, or None if no result or error.
        """
        try:
            if not self.execute_query(query, params):
                return None
                
            result = self.cursor.fetchone()
            
            # Convert Row object to dictionary
            if result:
                return {k: result[k] for k in result.keys()}
            return None
            
        except sqlite3.Error as e:
            self._error = f"Error fetching data: {e}"
            logger.error(self._error)
            return None
    
    def commit(self) -> bool:
        """
        Commit the current transaction.
        
        Returns:
            bool: True if commit successful, False otherwise.
        """
        try:
            if self.connection:
                self.connection.commit()
                return True
            return False
            
        except sqlite3.Error as e:
            self._error = f"Error committing transaction: {e}"
            logger.error(self._error)
            return False
    
    def rollback(self) -> bool:
        """
        Roll back the current transaction.
        
        Returns:
            bool: True if rollback successful, False otherwise.
        """
        try:
            if self.connection:
                self.connection.rollback()
                return True
            return False
            
        except sqlite3.Error as e:
            self._error = f"Error rolling back transaction: {e}"
            logger.error(self._error)
            return False
    
    def get_last_insert_id(self) -> Optional[int]:
        """
        Get the ID of the last inserted row.
        
        Returns:
            Optional[int]: The last insert ID, or None if error.
        """
        result = self.fetch_one("SELECT last_insert_rowid() as id")
        if result and 'id' in result:
            return result['id']
        return None
    
    def create_tables(self, queries: Optional[List[str]] = None) -> bool:
        """
        Create tables in the database.
        
        Args:
            queries (List[str], optional): SQL queries to create tables.
            
        Returns:
            bool: True if tables created successfully, False otherwise.
        """
        if not queries:
            return True
            
        try:
            for query in queries:
                # Handle AUTO_INCREMENT vs AUTOINCREMENT and INT vs INTEGER differences
                query = query.replace("INT AUTO_INCREMENT PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
                query = query.replace("INT ", "INTEGER ")
                
                if not self.execute_query(query):
                    raise sqlite3.Error(self._error or "Query execution failed")
            
            self.commit()
            logger.info("Database tables created successfully")
            return True
            
        except sqlite3.Error as e:
            self._error = f"Error creating tables: {e}"
            logger.error(self._error)
            self.rollback()
            return False