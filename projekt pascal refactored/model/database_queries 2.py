from typing import List

class DatabaseQueries:
    """
    Contains all SQL queries used in the application.
    
    This class centralizes all SQL queries to make them easier to maintain,
    test, and modify. It follows the Repository pattern to separate
    data access logic from business logic.
    
    All methods are static and return SQL query strings or lists of query strings.
    """
    
    @staticmethod
    def create_tables_query() -> List[str]:
        """
        Get SQL queries to create all necessary tables if they don't exist.
        
        Returns:
            List[str]: A list of SQL queries to create tables.
        """
        return [
            '''
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address TEXT NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(50)
            )
            '''
        ]