from .MariaDBConnection import MariaDBConnection

class QueryExecuter(MariaDBConnection):
    def __init__(self, query):
        self.query = query
        super().__init__()

    def execute(self, params=None, fetch_all=True):
        connection = self.connect()
        if connection is None:
            return None, self.getError()
       #Jede DB Type Connection hat seinen eigenen cursor , curser ist in realität  carrier für die DB Connection
       # z.B MongoDB connection hat sein eigenen cursor und MariaDB hat sein eigenen cursor
        cursor = connection.cursor()
        try:
            if params is not None:
                cursor.execute(self.query, params)
            else:
                cursor.execute(self.query)

            # Check if the query is a SELECT statement    
            is_select = self.query.strip().upper().startswith("SELECT")
            
            result = None
            if is_select:
                if fetch_all:
                    result = cursor.fetchall()
                else:
                    result = cursor.fetchone()
            else:
                # For non-SELECT queries, return affected row count
                result = cursor.rowcount
                
            connection.commit()    
            return result, None
        except Exception as e:
            connection.rollback()
            return None, str(e)
        finally:
            cursor.close()
            self.close()



        
