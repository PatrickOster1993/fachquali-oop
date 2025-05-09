import sqlite3
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('SQLiteConnection')

class SQLiteConnection:
    """
    Handles the connection to a SQLite database.
    """
    
    def __init__(self, database_path):
        """
        Initializes the SQLite connection with the provided database path.
        
        Args:
            database_path (str): Path to the SQLite database file
        """
        self.database_path = database_path
        self.connection = None
        self.cursor = None
        self.error = None
        
        self.connect()
        
    def connect(self):
        """
        Establishes a connection to the SQLite database.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            db_dir = os.path.dirname(os.path.abspath(self.database_path))
            if not os.path.exists(db_dir):
                os.makedirs(db_dir)
            
            self.connection = sqlite3.connect(self.database_path)
            
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            
            logger.info(f"Connected to SQLite database: {self.database_path}")
            return True
            
        except sqlite3.Error as e:
            self.error = f"Error connecting to SQLite: {e}"
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
                
            logger.info("Disconnected from SQLite")
            return True
            
        except sqlite3.Error as e:
            self.error = f"Error disconnecting from SQLite: {e}"
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
            
            # convert MySQL-style '?' to SQLite's '?'
            query = query.replace('?', '?')
                    
            self.cursor.execute(query, params or ())
            return True
            
        except sqlite3.Error as e:
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
                
            results = self.cursor.fetchall()
            
            return [{k: item[k] for k in item.keys()} for item in results]
            
        except sqlite3.Error as e:
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
                
            result = self.cursor.fetchone()
            
            if result:
                return {k: result[k] for k in result.keys()}
            return None
            
        except sqlite3.Error as e:
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
            
        except sqlite3.Error as e:
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
            
        except sqlite3.Error as e:
            self.error = f"Error rolling back transaction: {e}"
            logger.error(self.error)
            return False
    
    def get_last_insert_id(self):
        """
        Retrieves the ID of the last inserted row.
        
        Returns:
            int: The last insert ID, or None if an error occurred
        """
        result = self.fetch_one("SELECT last_insert_rowid() as id")
        if result and 'id' in result:
            return result['id']
        return None
    
    def create_tables(self, queries=None):
        """
        Creates the necessary database tables if they don't exist.
        
        Args:
            queries (list, optional): List of SQL queries to execute for table creation.
                If None, no tables will be created.
        
        Returns:
            bool: True if tables were created successfully, False otherwise
        """
        if not queries:
            return True
            
        try:
            for query in queries:
                # In SQLite, AUTO_INCREMENT ist falsch - muss PRIMARY KEY AUTOINCREMENT heißen
                # und INT ist INTEGER
                query = query.replace("INT AUTO_INCREMENT PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
                query = query.replace("INT ", "INTEGER ")
                
                if not self.execute_query(query):
                    raise sqlite3.Error(self.error or "Query execution failed")
            
            self.commit()
            logger.info("Database tables created successfully")
            return True
            
        except sqlite3.Error as e:
            self.error = f"Error creating tables: {e}"
            logger.error(self.error)
            self.rollback()
            return False