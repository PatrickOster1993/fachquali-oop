class DatabaseQueries:
    """
    Contains all SQL queries used in the application.
    
    This class centralizes all SQL queries to make them easier to maintain,
    test, and modify. It follows the Repository pattern to separate
    data access logic from business logic.
    
    Attributes:
        None - This is a static utility class
        
    Methods:
        All methods are static and return SQL query strings or execute
        queries through a provided database connection.
    """
    
    @staticmethod
    def create_tables_query():
        """Returns SQL to create all necessary tables if they don't exist."""
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
    
    @staticmethod
    def insert_product_query():
        """Returns SQL to insert a new product."""
        return """
            INSERT INTO products (name, price, quantity) 
            VALUES (?, ?, ?)
        """
    
    @staticmethod
    def delete_product_query():
        """Returns SQL to delete a product by ID."""
        return "DELETE FROM products WHERE product_id = ?"
    
    @staticmethod
    def select_all_products_query():
        """Returns SQL to select all products."""
        return "SELECT product_id, name, price, quantity FROM products"
    
    @staticmethod
    def select_product_by_id_query():
        """Returns SQL to select a specific product by ID."""
        return "SELECT product_id, name, price, quantity FROM products WHERE product_id = ?"
    
    @staticmethod
    def update_product_query():
        """Returns SQL to update a product."""
        return """
            UPDATE products 
            SET name = ?, price = ?, quantity = ?
            WHERE product_id = ?
        """
    
    @staticmethod
    def insert_customer_query():
        """Returns SQL to insert a new customer."""
        return """
            INSERT INTO customers (name, address, email, phone) 
            VALUES (?, ?, ?, ?)
        """
    
    @staticmethod
    def delete_customer_query():
        """Returns SQL to delete a customer by ID."""
        return "DELETE FROM customers WHERE customer_id = ?"
    
    @staticmethod
    def select_all_customers_query():
        """Returns SQL to select all customers."""
        return "SELECT customer_id, name, address, email, phone FROM customers"
    
    @staticmethod
    def select_customer_by_id_query():
        """Returns SQL to select a specific customer by ID."""
        return "SELECT customer_id, name, address, email, phone FROM customers WHERE customer_id = ?"
    
    @staticmethod
    def update_customer_query():
        """Returns SQL to update a customer."""
        return """
            UPDATE customers 
            SET name = ?, address = ?, email = ?, phone = ?
            WHERE customer_id = ?
        """