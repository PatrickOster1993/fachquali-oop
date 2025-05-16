import logging
import os
from typing import Optional

class LoggerService:
    """
    Centralized logging service for the application.
    
    This class provides a consistent way to log messages across the application.
    It ensures that all loggers use the same format and level.
    
    Attributes:
        DEFAULT_FORMAT (str): The default log format.
        DEFAULT_LEVEL (int): The default log level.
    """
    
    DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DEFAULT_LEVEL = logging.INFO
    
    @classmethod
    def configure(cls, level: Optional[int] = None, log_file: Optional[str] = None):
        """
        Configure the root logger for the application.
        
        Args:
            level (int, optional): The log level. Defaults to DEFAULT_LEVEL.
            log_file (str, optional): Path to log file. If provided, logs will be written to this file.
        """
        level = level or cls.DEFAULT_LEVEL
        
        # Configure root logger
        logging.basicConfig(
            level=level,
            format=cls.DEFAULT_FORMAT
        )
        
        # Add file handler if log_file is provided
        if log_file:
            # Ensure directory exists
            log_dir = os.path.dirname(os.path.abspath(log_file))
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            
            # Create file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(logging.Formatter(cls.DEFAULT_FORMAT))
            file_handler.setLevel(level)
            
            # Add file handler to root logger
            root_logger = logging.getLogger()
            root_logger.addHandler(file_handler)
    
    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Get a logger with the specified name.
        
        Args:
            name (str): The logger name.
            
        Returns:
            logging.Logger: The logger instance.
        """
        return logging.getLogger(name)