import mariadb
import logging

import MariaDBConnection

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MariaDBConnection')

class MariaDBConnection:
    """
    Handles the connection to a MariaDB database.
    
    This class manages the connection to a MariaDB database and provides
    methods for executing queries and managing transactions.
    
    Attributes:
        host (str): Database host
        user (str): Database user
        password (str): Database password
        database (str): Database name
        port (int): Database port
        connection: Active database connection
        cursor: Cursor for executing queries
        error (str): Last error message, if any
    """
    
    def __init__(self, host, user, password, database, port=3306):
        """
        Initializes the MariaDB connection with the provided credentials.
        
        Args:
            host (str): Database host
            user (str): Database user
            password (str): Database password
            database (str): Database name
            port (int, optional): Database port. Defaults to 3306.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None
        self.error = None
        
        self.connect()
        
    def connect(self):
        """
        Establishes a connection to the MariaDB database.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            
            self.cursor = self.connection.cursor(dictionary=True) # without it, it would be a tuple like: (1, "Laptop") and as a dict: {"product_id": 1, "name": "Laptop"}
            
            # enable autocommit for simple operations
            self.connection.autocommit = False
            
            logger.info(f"Connected to MariaDB database: {self.database}")
            return True
            
        except mariadb.Error as e:
            self.error = f"Error connecting to MariaDB: {e}"
            logger.error(self.error)
            return False
    
    def disconnect(self):
        """
        Closes the database connection.
        
        Returns:
            bool: True if disconnection successful, False otherwise
        """
        try:
            if self.cursor:
                self.cursor.close()
                
            if self.connection:
                self.connection.close()
                
            logger.info("Disconnected from MariaDB")
            return True
            
        except mariadb.Error as e:
            self.error = f"Error disconnecting from MariaDB: {e}"
            logger.error(self.error)
            return False
    
    def execute_query(self, query, params=None):
        """
        Executes a SQL query with optional parameters.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, list, dict, optional): Parameters for the query
            
        Returns:
            bool: True if query executed successfully, False otherwise
        """
        try:
            if not self.connection or not self.cursor:
                if not self.connect():
                    return False
                    
            self.cursor.execute(query, params or ())
            return True
            
        except mariadb.Error as e:
            self.error = f"Error executing query: {e}"
            logger.error(f"{self.error}\nQuery: {query}\nParams: {params}")
            return False
    
    def fetch_all(self, query, params=None):
        """
        Executes a query and returns all matching rows.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, list, dict, optional): Parameters for the query
            
        Returns:
            list: List of dictionaries containing the query results, 
                 or None if an error occurred
        """
        try:
            if not self.execute_query(query, params):
                return None
                
            return self.cursor.fetchall()
            
        except mariadb.Error as e:
            self.error = f"Error fetching data: {e}"
            logger.error(self.error)
            return None
    
    def fetch_one(self, query, params=None):
        """
        Executes a query and returns a single row.
        
        Args:
            query (str): The SQL query to execute
            params (tuple, list, dict, optional): Parameters for the query
            
        Returns:
            dict: Dictionary containing the query result, 
                 or None if no results or an error occurred
        """
        try:
            if not self.execute_query(query, params):
                return None
                
            return self.cursor.fetchone()
            
        except mariadb.Error as e:
            self.error = f"Error fetching data: {e}"
            logger.error(self.error)
            return None
    
    def commit(self):
        """
        Commits the current transaction.
        
        Returns:
            bool: True if commit was successful, False otherwise
        """
        try:
            if self.connection:
                self.connection.commit()
                return True
            return False
            
        except mariadb.Error as e:
            self.error = f"Error committing transaction: {e}"
            logger.error(self.error)
            return False
    
    def rollback(self):
        """
        Rolls back the current transaction.
        
        Returns:
            bool: True if rollback was successful, False otherwise
        """
        try:
            if self.connection:
                self.connection.rollback()
                return True
            return False
            
        except mariadb.Error as e:
            self.error = f"Error rolling back transaction: {e}"
            logger.error(self.error)
            return False
    
    def get_last_insert_id(self):
        """
        Retrieves the ID of the last inserted row.
        
        Returns:
            int: The last insert ID, or None if an error occurred
        """
        result = self.fetch_one("SELECT LAST_INSERT_ID() as id")
        if result and 'id' in result:
            return result['id']
        return None
    
    def create_tables(self):
        """
        Creates the necessary database tables if they don't exist.
        
        Returns:
            bool: True if tables were created successfully, False otherwise
        """
        try:
            self.execute_query('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL,
                    quantity INT NOT NULL
                )
            ''')
            
            self.execute_query('''
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    address TEXT NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    phone VARCHAR(50)
                )
            ''')
            
            self.commit()
            logger.info("Database tables created successfully")
            return True
            
        except mariadb.Error as e:
            self.error = f"Error creating tables: {e}"
            logger.error(self.error)
            self.rollback()
            return False
    
    def __enter__(self):
        """
        Support for using the connection as a context manager.
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ensures the connection is closed when exiting a context.
        """
        self.disconnect()