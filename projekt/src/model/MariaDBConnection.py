import mariadb

class MariaDBConnection:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.error = None
    
    def connect(self):
        try:
            self.connection = mariadb.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                port = self.port,
            )
            return self.connection
        except mariadb.Error as e:
            self.error = str(e)
            return None
    
    def getError(self):
        return self.error
    
