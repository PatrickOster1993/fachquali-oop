import logging
from typing import List, Dict, Optional, Any, Tuple

import mariadb

from model.database_interface import DatabaseInterface
from model.logger_service import LoggerService

logger = LoggerService.get_logger('MariaDBConnection')

class MariaDBConnection(DatabaseInterface):
    """
    Adapter for MariaDB database connection.
    
    This class implements the DatabaseInterface for MariaDB connections.
    
    Attributes:
        host (str): Database host.
        user (str): Database user.
        password (str): Database password.
        database (str): Database name.
        port (int): Database port.
        connection: Active database connection.
        cursor: Cursor for executing queries.
        _error (str): Last error message.
    """
    
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        """
        Initialize a new MariaDBConnection instance.
        
        Args:
            host (str): Database host.
            user (str): Database user.
            password (str): Database password.
            database (str): Database name.
            port (int, optional): Database port. Defaults to 3306.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
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
            # Verbindungsdetails protokollieren
            logger.info(f"Connecting to MariaDB: host={self.host}, user={self.user}, database={self.database}, port={self.port}")
            
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            
            self.cursor = self.connection.cursor(dictionary=True)
            self.connection.autocommit = False
            
            logger.info(f"Connected to MariaDB database: {self.database}")
            return True
            
        except mariadb.Error as e:
            self._error = f"Error connecting to MariaDB: {e}"
            logger.error(self._error)
            
            # Detailliertere Fehlermeldung für Authentifizierungsprobleme
            if "Access denied" in str(e):
                logger.error(f"Authentication failed for user '{self.user}'. Please check username and password.")
            elif "Can't connect" in str(e):
                logger.error(f"Cannot connect to host '{self.host}' on port {self.port}. Please check host and port settings.")
            elif "Unknown database" in str(e):
                logger.error(f"Database '{self.database}' does not exist. Please check database name.")
                
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
                
            logger.info("Disconnected from MariaDB")
            return True
            
        except mariadb.Error as e:
            self._error = f"Error disconnecting from MariaDB: {e}"
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
                    
            self.cursor.execute(query, params or ())
            return True
            
        except mariadb.Error as e:
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
                
            return self.cursor.fetchall()
            
        except mariadb.Error as e:
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
                
            return self.cursor.fetchone()
            
        except mariadb.Error as e:
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
            
        except mariadb.Error as e:
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
            
        except mariadb.Error as e:
            self._error = f"Error rolling back transaction: {e}"
            logger.error(self._error)
            return False
    
    def get_last_insert_id(self) -> Optional[int]:
        """
        Get the ID of the last inserted row.
        
        Returns:
            Optional[int]: The last insert ID, or None if error.
        """
        result = self.fetch_one("SELECT LAST_INSERT_ID() as id")
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
                if not self.execute_query(query):
                    raise mariadb.Error(self._error or "Query execution failed")
            
            self.commit()
            logger.info("Database tables created successfully")
            return True
            
        except mariadb.Error as e:
            self._error = f"Error creating tables: {e}"
            logger.error(self._error)
            self.rollback()
            return False