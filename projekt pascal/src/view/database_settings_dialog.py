from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFileDialog, QGroupBox, QFormLayout, QMessageBox)
from PyQt5.QtCore import Qt

from model.database_config import DatabaseConfig

class DatabaseSettingsDialog(QDialog):
    """
    Dialog for managing database connection settings.
    """
    
    def __init__(self, parent=None):
        """
        Initializes the database settings dialog.
        
        Args:
            parent (QWidget, optional): Parent widget
        """
        super().__init__(parent)
        
        self.config = DatabaseConfig()
        
        self.initUI()
        self.loadSettings()
    
    def initUI(self):
        """
        Sets up the dialog UI.
        """
        self.setWindowTitle("Database Settings")
        self.setMinimumWidth(400)
        
        mainLayout = QVBoxLayout()

        dbTypeLayout = QHBoxLayout()
        dbTypeLayout.addWidget(QLabel("Database Type:"))
        self.dbTypeCombo = QComboBox()
        self.dbTypeCombo.addItem("MariaDB")
        self.dbTypeCombo.addItem("SQLite")
        self.dbTypeCombo.currentIndexChanged.connect(self.onDbTypeChanged)
        dbTypeLayout.addWidget(self.dbTypeCombo)
        
        mainLayout.addLayout(dbTypeLayout)

        self.mariadbGroup = QGroupBox("MariaDB Settings")
        mariadbLayout = QFormLayout()
        
        self.hostInput = QLineEdit()
        mariadbLayout.addRow("Host:", self.hostInput)
        
        self.userInput = QLineEdit()
        mariadbLayout.addRow("User:", self.userInput)
        
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        mariadbLayout.addRow("Password:", self.passwordInput)
        
        self.databaseInput = QLineEdit()
        mariadbLayout.addRow("Database:", self.databaseInput)
        
        self.mariadbGroup.setLayout(mariadbLayout)
        mainLayout.addWidget(self.mariadbGroup)
        
        self.sqliteGroup = QGroupBox("SQLite Settings")
        sqliteLayout = QFormLayout()
        
        self.sqlitePathLayout = QHBoxLayout()
        self.sqlitePathInput = QLineEdit()
        self.sqlitePathInput.setReadOnly(True)
        self.sqlitePathLayout.addWidget(self.sqlitePathInput)
        
        browseButton = QPushButton("Browse...")
        browseButton.clicked.connect(self.browseSqlitePath)
        self.sqlitePathLayout.addWidget(browseButton)
        
        sqliteLayout.addRow("Database File:", self.sqlitePathLayout)
        
        self.sqliteGroup.setLayout(sqliteLayout)
        mainLayout.addWidget(self.sqliteGroup)
        
        testButton = QPushButton("Test Connection")
        testButton.clicked.connect(self.testConnection)
        mainLayout.addWidget(testButton)
        
        buttonLayout = QHBoxLayout()
        
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.saveSettings)
        buttonLayout.addWidget(saveButton)
        
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.reject)
        buttonLayout.addWidget(cancelButton)
        
        mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)
    
    def loadSettings(self):
        """
        Loads current settings into the UI.
        """
        db_type = self.config.get_active_db_type()
        self.dbTypeCombo.setCurrentIndex(0 if db_type == "mariadb" else 1)
        
        mariadb_config = self.config.get_mariadb_config()
        self.hostInput.setText(mariadb_config.get("host", "localhost"))
        self.userInput.setText(mariadb_config.get("user", "root"))
        self.passwordInput.setText(mariadb_config.get("password", ""))
        self.databaseInput.setText(mariadb_config.get("database", "wawi"))
        
        sqlite_config = self.config.get_sqlite_config()
        self.sqlitePathInput.setText(sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH))
        
        self.onDbTypeChanged()
    
    def onDbTypeChanged(self):
        """
        Handles database type selection changes.
        """
        is_mariadb = self.dbTypeCombo.currentIndex() == 0
        
        self.mariadbGroup.setVisible(is_mariadb)
        self.sqliteGroup.setVisible(not is_mariadb)
    
    def browseSqlitePath(self):
        """
        Opens a file dialog to select the SQLite database file.
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Select SQLite Database File",
            self.sqlitePathInput.text(),
            "SQLite Database (*.db);;All Files (*)"
        )
        
        if file_path:
            self.sqlitePathInput.setText(file_path)
    
    def testConnection(self):
        """
        Tests the database connection with the current settings.
        """
        self.saveSettingsToConfig()
        
        if self.dbTypeCombo.currentIndex() == 0:
            from model.MariaDBConnection import MariaDBConnection
            mariadb_config = self.config.get_mariadb_config()
            
            try:
                connection = MariaDBConnection(
                    host=mariadb_config.get("host", "localhost"),
                    user=mariadb_config.get("user", "root"),
                    password=mariadb_config.get("password", ""),
                    database=mariadb_config.get("database", "wawi")
                )
                
                if connection.connection is not None:
                    QMessageBox.information(
                        self,
                        "Connection Test",
                        "MariaDB connection successful!"
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Connection Test",
                        f"MariaDB connection failed: {connection.error}"
                    )
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Connection Test",
                    f"MariaDB connection failed: {e}"
                )
        else:
            from model.SQLiteConnection import SQLiteConnection
            sqlite_config = self.config.get_sqlite_config()
            
            try:
                connection = SQLiteConnection(
                    sqlite_config.get("database_path", DatabaseConfig.DEFAULT_SQLITE_PATH)
                )
                
                if connection.connection is not None:
                    QMessageBox.information(
                        self,
                        "Connection Test",
                        "SQLite connection successful!"
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Connection Test",
                        f"SQLite connection failed: {connection.error}"
                    )
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Connection Test",
                    f"SQLite connection failed: {e}"
                )
    
    def saveSettingsToConfig(self):
        """
        Saves the settings to the configuration without closing the dialog.
        """
        db_type = "mariadb" if self.dbTypeCombo.currentIndex() == 0 else "sqlite"
        self.config.set_db_type(db_type)

        self.config.set_mariadb_config(
            self.hostInput.text(),
            self.userInput.text(),
            self.passwordInput.text(),
            self.databaseInput.text()
        )

        self.config.set_sqlite_path(self.sqlitePathInput.text())
    
    def saveSettings(self):
        """
        Saves the settings and closes the dialog.
        """
        self.saveSettingsToConfig()
        self.accept()
    
    def get_config(self):
        """
        Returns the current database configuration.
        
        Returns:
            DatabaseConfig: The current configuration.
        """
        return self.config