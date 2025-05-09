import logging
import os
from typing import Optional

from model.database_interface import DatabaseInterface
from model.database_config import DatabaseConfig
from model.mariadb_connection import MariaDBConnection
from model.sqlite_connection import SQLiteConnection
from model.logger_service import LoggerService

logger = LoggerService.get_logger('DatabaseConnectionFactory')

class DatabaseConnectionFactory:
    """
    Factory class that creates database connections based on configuration.
    
    This class follows the Factory pattern to create and return the appropriate
    database connection based on configuration.
    
    Attributes:
        config (DatabaseConfig): The database configuration.
    """
    
    def __init__(self, config: Optional[DatabaseConfig] = None):
        """
        Initialize a new DatabaseConnectionFactory instance.
        
        Args:
            config (DatabaseConfig, optional): The database configuration.
                If None, a new configuration will be created from default settings.
        """
        self.config = config or DatabaseConfig()
    
    def create_connection(self) -> DatabaseInterface:
        """
        Create and return a database connection based on configuration.
        
        This method creates a connection based on the active database type in the
        configuration. If the preferred connection fails, it falls back to SQLite.
        
        Returns:
            DatabaseInterface: A database connection that implements DatabaseInterface.
        """
        db_type = self.config.get_active_db_type()
        
        if db_type == "mariadb":
            connection = self._create_mariadb_connection()
            # If MariaDB connection fails, fall back to SQLite
            if connection is None:
                logger.warning("Failed to connect to MariaDB, falling back to SQLite")
                connection = self._create_sqlite_connection()
        else:
            connection = self._create_sqlite_connection()
        
        # Initialize database tables
        if connection is not None:
            self._initialize_tables(connection)
        
        return connection
    
    def _create_mariadb_connection(self) -> Optional[MariaDBConnection]:
        """
        Create a MariaDB connection.
        
        Returns:
            Optional[MariaDBConnection]: A MariaDB connection, or None if connection fails.
        """
        try:
            mariadb_config = self.config.get_mariadb_config()
            
            # Port aus der Konfiguration extrahieren
            port = mariadb_config.get("port", 3306)
            
            connection = MariaDBConnection(
                host=mariadb_config.get("host", "localhost"),
                user=mariadb_config.get("user", "root"),
                password=mariadb_config.get("password", ""),
                database=mariadb_config.get("database", "wawi"),
                port=port
            )
            
            if connection.connect():
                logger.info(f"Successfully connected to MariaDB on {connection.host}:{connection.port}")
                return connection
            else:
                logger.warning(f"Failed to connect to MariaDB: {connection.error}")
                return None
                
        except Exception as e:
            logger.warning(f"Error creating MariaDB connection: {e}")
            return None
    
    def _create_sqlite_connection(self) -> SQLiteConnection:
        """
        Create a SQLite connection.
        
        Returns:
            SQLiteConnection: A SQLite connection.
        """
        sqlite_config = self.config.get_sqlite_config()
        database_path = sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(database_path), exist_ok=True)
        
        connection = SQLiteConnection(database_path)
        
        if connection.connect():
            logger.info(f"Successfully connected to SQLite at {database_path}")
        else:
            logger.warning(f"Failed to connect to SQLite: {connection.error}")
        
        return connection
    
    def _initialize_tables(self, connection: DatabaseInterface) -> bool:
        """
        Initialize database tables.
        
        Args:
            connection (DatabaseInterface): The database connection.
            
        Returns:
            bool: True if tables were created successfully, False otherwise.
        """
        from model.database_queries import DatabaseQueries
        
        if connection.create_tables(DatabaseQueries.create_tables_query()):
            logger.info("Database tables initialized successfully.")
            return True
        else:
            logger.warning(f"Failed to initialize database tables: {connection.error}")
            return False