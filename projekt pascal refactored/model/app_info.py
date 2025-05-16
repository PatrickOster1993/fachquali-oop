"""
This file contains information about the application,
such as version info and user guides.
"""

# Application information
APP_NAME = "WaWi - Warehouse Management System"
APP_VERSION = "1.0.0"
APP_CREATION_DATE = "May 2025"
APP_COPYRIGHT = "© 2025 Pascal. All rights reserved."

# About information as HTML-formatted text
ABOUT_TEXT = f"""
<h2>{APP_NAME}</h2>
<p>Version: {APP_VERSION}</p>
<p>Created: {APP_CREATION_DATE}</p>
<p>{APP_COPYRIGHT}</p>
<p>
    WaWi is a simple warehouse management system designed to manage
    products and customers in a small business environment.
</p>
<p>
    Developed as a project to learn the Object-Oriented Programming.
</p>
"""

# User guide as HTML-formatted text
HOW_TO_USE_TEXT = """
<h2>WaWi - Warehouse Management System</h2>
<h3>User Guide</h3>

<h4>Overview</h4>
<p>
    WaWi is a simple warehouse management system that allows you to manage products and customers.
    The application consists of two main tabs: Products and Customers.
</p>

<h4>Managing Products</h4>
<p>
    <b>Adding a Product:</b>
    <ol>
        <li>Navigate to the 'Products' tab</li>
        <li>Fill in the product details (name, price, quantity)</li>
        <li>Click the 'Add' button</li>
    </ol>
    
    <b>Removing a Product:</b>
    <ol>
        <li>Navigate to the 'Products' tab</li>
        <li>Select one or more products from the list</li>
        <li>Click the 'Remove Selected Products' button</li>
    </ol>
</p>

<h4>Managing Customers</h4>
<p>
    <b>Adding a Customer:</b>
    <ol>
        <li>Navigate to the 'Customers' tab</li>
        <li>Fill in the customer details (name, address, email, phone)</li>
        <li>Click the 'Add' button</li>
    </ol>
    
    <b>Removing a Customer:</b>
    <ol>
        <li>Navigate to the 'Customers' tab</li>
        <li>Select one or more customers from the list</li>
        <li>Click the 'Remove Selected Customers' button</li>
    </ol>
</p>

<h4>Database Settings</h4>
<p>
    You can configure the database connection by:
    <ol>
        <li>Click on 'File' > 'Database Settings'</li>
        <li>Choose between MariaDB and SQLite</li>
        <li>Configure the connection details</li>
        <li>Test the connection</li>
        <li>Save the settings</li>
    </ol>
</p>

<h4>Sample Data</h4>
<p>
    If you are starting with an empty database, you can import sample data:
    <ol>
        <li>Click on 'File' > 'Import Sample Data'</li>
        <li>Confirm the import</li>
    </ol>
</p>
"""