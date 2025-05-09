from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFileDialog, QGroupBox, QFormLayout, QMessageBox)
from PyQt5.QtGui import QIntValidator

from model.database_config import DatabaseConfig
from model.mariadb_connection import MariaDBConnection
from model.sqlite_connection import SQLiteConnection
from model.logger_service import LoggerService

logger = LoggerService.get_logger('DatabaseSettingsDialog')

class DatabaseSettingsDialog(QDialog):
    """
    Dialog for managing database connection settings.
    
    This dialog allows the user to configure database settings for both
    MariaDB and SQLite connections.
    
    Attributes:
        config (DatabaseConfig): The database configuration.
        dbTypeCombo (QComboBox): Database type selection combo box.
        mariadbGroup (QGroupBox): Group box for MariaDB settings.
        sqliteGroup (QGroupBox): Group box for SQLite settings.
        hostInput (QLineEdit): Input field for MariaDB host.
        portInput (QLineEdit): Input field for MariaDB port.
        userInput (QLineEdit): Input field for MariaDB user.
        passwordInput (QLineEdit): Input field for MariaDB password.
        databaseInput (QLineEdit): Input field for MariaDB database name.
        sqlitePathInput (QLineEdit): Input field for SQLite database path.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the database settings dialog.
        
        Args:
            parent (QWidget, optional): Parent widget.
        """
        super().__init__(parent)
        
        # Load database configuration
        self.config = DatabaseConfig()
        
        # Initialize UI
        self._init_ui()
        
        # Load settings into UI
        self._load_settings()
    
    def _init_ui(self):
        """
        Initialize the dialog UI.
        """
        # Set dialog properties
        self.setWindowTitle("Database Settings")
        self.setMinimumWidth(400)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Database type selection
        db_type_layout = QHBoxLayout()
        db_type_layout.addWidget(QLabel("Database Type:"))
        self.dbTypeCombo = QComboBox()
        self.dbTypeCombo.addItem("MariaDB")
        self.dbTypeCombo.addItem("SQLite")
        self.dbTypeCombo.currentIndexChanged.connect(self._on_db_type_changed)
        db_type_layout.addWidget(self.dbTypeCombo)
        
        main_layout.addLayout(db_type_layout)
        
        # MariaDB settings group
        self.mariadbGroup = QGroupBox("MariaDB Settings")
        mariadb_layout = QFormLayout()
        
        # Host input
        self.hostInput = QLineEdit()
        mariadb_layout.addRow("Host:", self.hostInput)
        
        # Port input
        self.portInput = QLineEdit()
        self.portInput.setValidator(QIntValidator(1, 65535))  # Gültiger Port-Bereich
        mariadb_layout.addRow("Port:", self.portInput)
        
        # User input
        self.userInput = QLineEdit()
        mariadb_layout.addRow("User:", self.userInput)
        
        # Password input
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        mariadb_layout.addRow("Password:", self.passwordInput)
        
        # Database input
        self.databaseInput = QLineEdit()
        mariadb_layout.addRow("Database:", self.databaseInput)
        
        self.mariadbGroup.setLayout(mariadb_layout)
        main_layout.addWidget(self.mariadbGroup)
        
        # SQLite settings group
        self.sqliteGroup = QGroupBox("SQLite Settings")
        sqlite_layout = QFormLayout()
        
        # SQLite path input
        sqlite_path_layout = QHBoxLayout()
        self.sqlitePathInput = QLineEdit()
        self.sqlitePathInput.setReadOnly(True)
        sqlite_path_layout.addWidget(self.sqlitePathInput)
        
        # Browse button
        browse_button = QPushButton("Browse...")
        browse_button.clicked.connect(self._browse_sqlite_path)
        sqlite_path_layout.addWidget(browse_button)
        
        sqlite_layout.addRow("Database File:", sqlite_path_layout)
        
        self.sqliteGroup.setLayout(sqlite_layout)
        main_layout.addWidget(self.sqliteGroup)
        
        # Test connection button
        test_button = QPushButton("Test Connection")
        test_button.clicked.connect(self._test_connection)
        main_layout.addWidget(test_button)
        
        # Dialog buttons
        button_layout = QHBoxLayout()
        
        # Save button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self._save_settings)
        button_layout.addWidget(save_button)
        
        # Cancel button
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        main_layout.addLayout(button_layout)
        
        # Set dialog layout
        self.setLayout(main_layout)
    
    def _load_settings(self):
        """
        Load current settings into the UI.
        """
        # Set database type
        db_type = self.config.get_active_db_type()
        self.dbTypeCombo.setCurrentIndex(0 if db_type == "mariadb" else 1)
        
        # Load MariaDB settings
        mariadb_config = self.config.get_mariadb_config()
        self.hostInput.setText(mariadb_config.get("host", "localhost"))
        self.portInput.setText(str(mariadb_config.get("port", 3306)))  # Default zu 3306
        self.userInput.setText(mariadb_config.get("user", "root"))
        self.passwordInput.setText(mariadb_config.get("password", ""))
        self.databaseInput.setText(mariadb_config.get("database", "wawi"))
        
        # Load SQLite settings
        sqlite_config = self.config.get_sqlite_config()
        self.sqlitePathInput.setText(sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH))
        
        # Show/hide groups based on selected database type
        self._on_db_type_changed()
    
    def _on_db_type_changed(self):
        """
        Handle database type selection changes.
        """
        is_mariadb = self.dbTypeCombo.currentIndex() == 0
        
        # Show/hide settings groups based on selected database type
        self.mariadbGroup.setVisible(is_mariadb)
        self.sqliteGroup.setVisible(not is_mariadb)
    
    def _browse_sqlite_path(self):
        """
        Open a file dialog to select the SQLite database file.
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Select SQLite Database File",
            self.sqlitePathInput.text(),
            "SQLite Database (*.db);;All Files (*)"
        )
        
        if file_path:
            self.sqlitePathInput.setText(file_path)
    
    def _save_settings_to_config(self):
        """
        Save the settings to the configuration without closing the dialog.
        """
        # Save database type
        db_type = "mariadb" if self.dbTypeCombo.currentIndex() == 0 else "sqlite"
        self.config.set_db_type(db_type)
        
        # Save MariaDB settings
        try:
            port = int(self.portInput.text()) if self.portInput.text().strip() else 3306
        except ValueError:
            port = 3306
            
        # Speichern der MariaDB-Konfiguration mit Port
        self.config.set_mariadb_config_with_port(
            host=self.hostInput.text(),
            user=self.userInput.text(),
            password=self.passwordInput.text(),
            database=self.databaseInput.text(),
            port=port
        )
        
        # Save SQLite settings
        self.config.set_sqlite_path(self.sqlitePathInput.text())
    
    def _test_connection(self):
        """
        Test the database connection with the current settings.
        """
        # Save settings to config
        self._save_settings_to_config()
        
        try:
            # Test connection based on selected database type
            if self.dbTypeCombo.currentIndex() == 0:
                # Test MariaDB connection
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
                    QMessageBox.information(
                        self,
                        "Connection Test",
                        f"MariaDB connection successful! Connected to {connection.database} on {connection.host}:{connection.port}"
                    )
                    connection.disconnect()
                else:
                    QMessageBox.warning(
                        self,
                        "Connection Test",
                        f"MariaDB connection failed: {connection.error}"
                    )
            else:
                # Test SQLite connection
                sqlite_config = self.config.get_sqlite_config()
                
                connection = SQLiteConnection(
                    sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH)
                )
                
                if connection.connect():
                    QMessageBox.information(
                        self,
                        "Connection Test",
                        f"SQLite connection successful! Connected to {connection.database_path}"
                    )
                    connection.disconnect()
                else:
                    QMessageBox.warning(
                        self,
                        "Connection Test",
                        f"SQLite connection failed: {connection.error}"
                    )
                    
        except Exception as e:
            QMessageBox.critical(
                self,
                "Connection Test",
                f"Error testing connection: {str(e)}"
            )
            logger.error(f"Error testing database connection: {e}", exc_info=True)
    
    def _save_settings(self):
        """
        Save the settings and close the dialog.
        """
        # Save settings to config
        self._save_settings_to_config()
        
        # Accept dialog (close with OK result)
        self.accept()
    
    def get_config(self):
        """
        Get the current database configuration.
        
        Returns:
            DatabaseConfig: The current configuration.
        """
        return self.config