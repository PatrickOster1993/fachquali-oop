import os
import json
import logging
from typing import Dict, Any, Optional

from model.logger_service import LoggerService

logger = LoggerService.get_logger('DatabaseConfig')

class DatabaseConfig:
    """
    Class to manage and store database configuration.
    
    This class handles loading and saving database configuration from a JSON file,
    and provides methods to access and modify the configuration.
    
    Attributes:
        config_path (str): Path to the configuration file.
        config (dict): The database configuration.
        project_root (str): The absolute path to the project root directory.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the database configuration.
        
        Args:
            config_path (str, optional): Path to the configuration file.
                If None, a default path inside the data directory will be used.
        """
        # Determine project root directory (parent of directory containing this file)
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__))))
        
        # Set default paths relative to project root
        self.data_dir = os.path.join(self.project_root, "data")
        self.default_config_path = os.path.join(self.data_dir, "db_config.json")
        self.default_sqlite_path = os.path.join(self.data_dir, "wawi.db")
        
        # Use provided config path or default
        self.config_path = config_path or self.default_config_path
        
        # Default configuration
        self.config = {
            "db_type": "sqlite",  # options: "mariadb", "sqlite"
            "mariadb": {
                "host": "localhost",
                "user": "root",
                "password": "",
                "database": "wawi",
                "port": 3306  # Standard MariaDB/MySQL Port
            },
            "sqlite": {
                "database_path": "data/wawi.db"  # Store as relative path by default
            }
        }
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load configuration from file if it exists
        self.load_config()
    
    def _get_absolute_sqlite_path(self):
        """
        Get the absolute SQLite database path.
        
        Returns:
            str: The absolute path to the SQLite database.
        """
        relative_path = self.config.get("sqlite", {}).get("database_path", "data/wawi.db")
        
        # If it's already an absolute path, return as is
        if os.path.isabs(relative_path):
            return relative_path
        
        # Otherwise, make it absolute relative to project root
        return os.path.normpath(os.path.join(self.project_root, relative_path))
    
    def _get_relative_sqlite_path(self, absolute_path):
        """
        Convert an absolute path to a path relative to the project root.
        
        Args:
            absolute_path (str): The absolute path to convert.
            
        Returns:
            str: A path relative to the project root, or the original path if not possible.
        """
        try:
            # Make absolute path for consistency
            absolute_path = os.path.abspath(absolute_path)
            
            # Try to make the path relative to the project root
            rel_path = os.path.relpath(absolute_path, self.project_root)
            
            # Use forward slashes for cross-platform compatibility
            rel_path = rel_path.replace(os.path.sep, '/')
            
            # If the relative path goes outside the project root, use the default path
            if rel_path.startswith('../'):
                logger.warning(f"Path {absolute_path} is outside the project directory. Using default path.")
                return "data/wawi.db"
            
            return rel_path
        except Exception as e:
            logger.error(f"Error converting path to relative: {e}")
            return "data/wawi.db"
    
    def load_config(self) -> bool:
        """
        Load configuration from file.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as file:
                    loaded_config = json.load(file)
                    
                    # Update config without losing default values for missing keys
                    if "db_type" in loaded_config:
                        self.config["db_type"] = loaded_config["db_type"]
                    
                    if "mariadb" in loaded_config:
                        for key, value in loaded_config["mariadb"].items():
                            self.config["mariadb"][key] = value
                        
                        # Ensure port is present
                        if "port" not in self.config["mariadb"]:
                            self.config["mariadb"]["port"] = 3306
                    
                    if "sqlite" in loaded_config and "database_path" in loaded_config["sqlite"]:
                        # Store the SQLite path as a relative path
                        sqlite_path = loaded_config["sqlite"]["database_path"]
                        self.config["sqlite"]["database_path"] = self._get_relative_sqlite_path(sqlite_path)
                    
                logger.info(f"Loaded database configuration from {self.config_path}")
                return True
            else:
                logger.info("No configuration file found. Using defaults.")
                self.save_config()
                return False
                
        except Exception as e:
            logger.error(f"Error loading database configuration: {e}", exc_info=True)
            return False
    
    def save_config(self) -> bool:
        """
        Save configuration to file.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            
            # Save the config to file
            with open(self.config_path, 'w') as file:
                json.dump(self.config, file, indent=2)
                
            logger.info(f"Saved database configuration to {self.config_path}")
            logger.info(f"SQLite path stored as: {self.config['sqlite']['database_path']}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving database configuration: {e}", exc_info=True)
            return False
    
    def get_active_db_type(self) -> str:
        """
        Get the currently active database type.
        
        Returns:
            str: "mariadb" or "sqlite".
        """
        return self.config.get("db_type", "sqlite")
    
    def set_db_type(self, db_type: str) -> bool:
        """
        Set the database type.
        
        Args:
            db_type (str): "mariadb" or "sqlite".
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if db_type not in ["mariadb", "sqlite"]:
            logger.error(f"Invalid database type: {db_type}")
            return False
        
        self.config["db_type"] = db_type
        return self.save_config()
    
    def get_mariadb_config(self) -> Dict[str, Any]:
        """
        Get the MariaDB configuration.
        
        Returns:
            Dict[str, Any]: MariaDB configuration.
        """
        config = self.config.get("mariadb", {}).copy()
        
        # Ensure the port is present
        if "port" not in config:
            config["port"] = 3306
            
        return config
    
    def set_mariadb_config(self, host: str, user: str, password: str, database: str) -> bool:
        """
        Set the MariaDB configuration (without port).
        
        Args:
            host (str): Database host.
            user (str): Database user.
            password (str): Database password.
            database (str): Database name.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        # Keep existing port if available
        existing_port = self.config.get("mariadb", {}).get("port", 3306)
        
        self.config["mariadb"] = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": existing_port
        }
        return self.save_config()
    
    def set_mariadb_config_with_port(self, host: str, user: str, password: str, database: str, port: int = 3306) -> bool:
        """
        Set the MariaDB configuration including port.
        
        Args:
            host (str): Database host.
            user (str): Database user.
            password (str): Database password.
            database (str): Database name.
            port (int): Database port.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        self.config["mariadb"] = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": port
        }
        return self.save_config()
    
    def get_sqlite_config(self) -> Dict[str, Any]:
        """
        Get the SQLite configuration with absolute path.
        
        Returns:
            Dict[str, Any]: SQLite configuration.
        """
        return {
            "database_path": self._get_absolute_sqlite_path()
        }
    
    def set_sqlite_path(self, database_path: str) -> bool:
        """
        Set the SQLite database path.
        
        Args:
            database_path (str): Path to the SQLite database file.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        # Store as relative path
        self.config["sqlite"] = {
            "database_path": self._get_relative_sqlite_path(database_path)
        }
        return self.save_config()