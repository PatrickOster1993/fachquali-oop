from .QueryExecuter import QueryExecuter

class SimpleCRUD:

    def __init__(self, table_name):

        self.table_name = table_name
    
    def create(self, data):

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        
        executer = QueryExecuter(query)
        return executer.execute(params=list(data.values()))
    
    def read_by_id(self, id_column, id_value):

        query = f"SELECT * FROM {self.table_name} WHERE {id_column} = ?"
        executer = QueryExecuter(query)
        return executer.execute(params=[id_value], fetch_all=False)
    
    def read_all(self, where_clause=None, where_params=None, order_by=None, limit=None):

        query = f"SELECT * FROM {self.table_name}"
        
        if where_clause:
            query += f" WHERE {where_clause}"
        
        if order_by:
            query += f" ORDER BY {order_by}"
            
        if limit:
            query += f" LIMIT {limit}"
        
        executer = QueryExecuter(query)
        return executer.execute(params=where_params)
    
    def update(self, data, where_clause, where_params):

        # Prepare the SET part of the query
        set_clause = ', '.join([f"{column} = ?" for column in data.keys()])
        
        # Build the query
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {where_clause}"
        
        # Combine data values and where_params
        params = list(data.values()) + where_params
        
        # Execute the query
        executer = QueryExecuter(query)
        return executer.execute(params=params)
    
    def delete(self, where_clause, where_params):

        query = f"DELETE FROM {self.table_name} WHERE {where_clause}"
        executer = QueryExecuter(query)
        return executer.execute(params=where_params)
    
    def count(self, where_clause=None, where_params=None):

        query = f"SELECT COUNT(*) FROM {self.table_name}"
        
        if where_clause:
            query += f" WHERE {where_clause}"
        
        executer = QueryExecuter(query)
        result, error = executer.execute(params=where_params, fetch_all=False)
        
        if error:
            return None, error
        
        # Return just the count value (first column of the first row)
        return result[0], None 