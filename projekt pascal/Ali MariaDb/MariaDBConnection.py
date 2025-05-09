import mariadb
import os
import dotenv
from dotenv import load_dotenv

class MariaDBConnection:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        self.__host = os.environ.get('DB_HOST')
        self.__user = os.environ.get('DB_USER')
        self.__password = os.environ.get('DB_PASSWORD')
        self.__database = os.environ.get('DB_NAME')
        self.__port = int(os.environ.get('DB_PORT'))
        self.connection = None
        self.error = None
        

    def connect(self):
        try:
            self.connection = mariadb.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                port=self.__port
            )
            return self.connection
        except mariadb.Error as e:
                self.error = str(e)
                return None



    def getError(self):
        return self.error
    
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            
        
       