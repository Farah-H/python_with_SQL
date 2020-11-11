import pyodbc

class DB_connection:
    
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = ""
        self.password = ""
        
    def establish_connection(self):
        connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}")
        cursor = connection.cursor()
        return cursor 
    
    def new_table(self, tablename, column_name , data_type): 
        # I want args to be a list of column names and character type, maybe a dict 
        cursor = establish_connection()
        cursor.execute(f'CREATE TABLE {tablename} ({column_name} {data_type})')
        view_new_table = cursor.execute(f'SELECT * FROM {tablename}').fetchall()
        # printing the column to check the table exists
        for record in view_new_table:
            print(record)
    
    def 