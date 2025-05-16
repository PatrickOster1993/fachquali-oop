import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DatabaseConfig')

class DatabaseConfig:
    """
    Class to manage and store database configuration.
    """

    DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "db_config.json")

    DEFAULT_SQLITE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "wawi.db")
    
    def __init__(self, config_path=None):
        """
        Initializes the database configuration.
        
        Args:
            config_path (str, optional): Path to the configuration file.
                If None, the default path will be used.
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH

        self.config = {
            "db_type": "mariadb", # options: "mariadb", "sqlite"
            "mariadb": {
                "host": "localhost",
                "user": "root",
                "password": "",
                "database": "wawi"
            },
            "sqlite": {
                "database_path": self.DEFAULT_SQLITE_PATH
            }
        }
        
        self.load_config()
    
    def load_config(self):
        """
        Loads configuration from file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as file:
                    loaded_config = json.load(file)
                    
                    self.config.update(loaded_config)
                    
                logger.info(f"Loaded database configuration from {self.config_path}")
                return True
            else:
                logger.info("No configuration file found. Using defaults.")
                self.save_config()
                return False
        except Exception as e:
            logger.error(f"Error loading database configuration: {e}")
            return False
    
    def save_config(self):
        """
        Saves configuration to file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            
            with open(self.config_path, 'w') as file:
                json.dump(self.config, file, indent=2)
                
            logger.info(f"Saved database configuration to {self.config_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving database configuration: {e}")
            return False
    
    def get_active_db_type(self):
        """
        Gets the currently active database type.
        
        Returns:
            str: "mariadb" or "sqlite"
        """
        return self.config.get("db_type", "mariadb")
    
    def set_db_type(self, db_type):
        """
        Sets the database type.
        
        Args:
            db_type (str): "mariadb" or "sqlite"
            
        Returns:
            bool: True if successful, False otherwise
        """
        if db_type not in ["mariadb", "sqlite"]:
            logger.error(f"Invalid database type: {db_type}")
            return False
        
        self.config["db_type"] = db_type
        return self.save_config()
    
    def get_mariadb_config(self):
        """
        Gets the MariaDB configuration.
        
        Returns:
            dict: MariaDB configuration
        """
        return self.config.get("mariadb", {})
    
    def set_mariadb_config(self, host, user, password, database):
        """
        Sets the MariaDB configuration.
        
        Args:
            host (str): Database host
            user (str): Database user
            password (str): Database password
            database (str): Database name
            
        Returns:
            bool: True if successful, False otherwise
        """
        self.config["mariadb"] = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        return self.save_config()
    
    def get_sqlite_config(self):
        """
        Gets the SQLite configuration.
        
        Returns:
            dict: SQLite configuration
        """
        return self.config.get("sqlite", {})
    
    def set_sqlite_path(self, database_path):
        """
        Sets the SQLite database path.
        
        Args:
            database_path (str): Path to the SQLite database file
            
        Returns:
            bool: True if successful, False otherwise
        """
        self.config["sqlite"] = {
            "database_path": database_path
        }
        return self.save_config()