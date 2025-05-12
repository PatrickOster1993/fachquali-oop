import logging
import os
from .MariaDBConnection import MariaDBConnection
from .SQLiteConnection import SQLiteConnection
from .database_config import DatabaseConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DatabaseConnectionFactory')

class DatabaseConnectionFactory:
    """
    Factory class that creates database connections based on configuration.
    """
    
    def __init__(self, config=None):
        """
        Initializes the database connection factory.
        
        Args:
            config (DatabaseConfig, optional): Database configuration.
                If None, a new DatabaseConfig will be created.
        """
        self.config = config or DatabaseConfig()
    
    def create_connection(self):
        """
        Creates and returns a database connection based on the configuration.
        Also ensures that the necessary tables exist.
        
        Returns:
            object: MariaDBConnection or SQLiteConnection
        """
        db_type = self.config.get_active_db_type()
        
        if db_type == "mariadb":
            connection = self._create_mariadb_connection()
        else:
            connection = self._create_sqlite_connection()
        
        # create tables if they do not exist
        from .database_queries import DatabaseQueries
        connection.create_tables(DatabaseQueries.create_tables_query())
        
        return connection
    
    def _create_mariadb_connection(self):
        """
        Creates a MariaDB connection.
        If the connection fails, falls back to SQLite.
        
        Returns:
            object: MariaDBConnection or SQLiteConnection
        """
        try:
            mariadb_config = self.config.get_mariadb_config()
            
            connection = MariaDBConnection(
                host=mariadb_config.get("host", "localhost"),
                user=mariadb_config.get("user", "root"),
                password=mariadb_config.get("password", ""),
                database=mariadb_config.get("database", "wawi")
            )

            if connection.connection is not None:
                logger.info("Successfully connected to MariaDB.")
                return connection
            else:
                logger.warning("Could not connect to MariaDB. Falling back to SQLite.")
                return self._create_sqlite_connection()
        except Exception as e:
            logger.warning(f"Error connecting to MariaDB: {e}. Falling back to SQLite.")
            return self._create_sqlite_connection()
    
    def _create_sqlite_connection(self):
        """
        Creates a SQLite connection.
        
        Returns:
            object: SQLiteConnection
        """
        sqlite_config = self.config.get_sqlite_config()
        
        database_path = sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH)

        connection = SQLiteConnection(database_path)
        
        logger.info(f"Using SQLite database at {database_path}")
        return connection