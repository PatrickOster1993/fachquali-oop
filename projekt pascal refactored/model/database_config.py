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
        DEFAULT_CONFIG_PATH (str): Default path to the configuration file.
        DEFAULT_SQLITE_PATH (str): Default path to the SQLite database file.
    """
    
    # Default paths
    DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "db_config.json")
    DEFAULT_SQLITE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "wawi.db")
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the database configuration.
        
        Args:
            config_path (str, optional): Path to the configuration file.
                If None, the default path will be used.
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        
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
                "database_path": self.DEFAULT_SQLITE_PATH
            }
        }
        
        # Load configuration from file if it exists
        self.load_config()
    
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
                    self.config.update(loaded_config)
                    
                    # Stellen Sie sicher, dass der Port in der MariaDB-Konfiguration existiert
                    if "mariadb" in self.config and "port" not in self.config["mariadb"]:
                        self.config["mariadb"]["port"] = 3306
                    
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
            
            with open(self.config_path, 'w') as file:
                json.dump(self.config, file, indent=2)
                
            logger.info(f"Saved database configuration to {self.config_path}")
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
        
        # Stellen Sie sicher, dass der Port vorhanden ist
        if "port" not in config:
            config["port"] = 3306
            
        return config
    
    def set_mariadb_config(self, host: str, user: str, password: str, database: str) -> bool:
        """
        Set the MariaDB configuration (ohne Port).
        
        Args:
            host (str): Database host.
            user (str): Database user.
            password (str): Database password.
            database (str): Database name.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        # Bestehende Port-Einstellung beibehalten, falls vorhanden
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
        Get the SQLite configuration.
        
        Returns:
            Dict[str, Any]: SQLite configuration.
        """
        return self.config.get("sqlite", {}).copy()
    
    def set_sqlite_path(self, database_path: str) -> bool:
        """
        Set the SQLite database path.
        
        Args:
            database_path (str): Path to the SQLite database file.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        self.config["sqlite"] = {
            "database_path": database_path
        }
        return self.save_config()