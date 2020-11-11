import pyodbc

class DB_connection:
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"

    def establish_connection(self):
        connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        cursor = connection.cursor()
        return cursor

    def new_table(self, tablename, column_name, data_type):
        # I want args to be a list of column names and character type, maybe a dict
        cursor = self.establish_connection()
        cursor.execute(f"CREATE TABLE {tablename} ({column_name} {data_type});")
        view_new_table = cursor.execute(f"SELECT * FROM {tablename};").fetchall()
        # printing the column to check the table exists
        for record in view_new_table:
            print(record)

    def add_info(self):
        cursor = self.establish_connection()
        cursor.execute(f"INSERT INTO {table_name} ({column_name})")



table_name = input("What would you like your table to be called?")
column_name = input("Please enter the name of your first column, remembering to use SQL conventions.")
# it would be cool to increment this to convert whatever they put into an appropriate format
# e.g by replacing spaces with _ 
char_type = 
class_instance = DB_connection()
class_instance.new_table("farahs_table", "customer_name", "VARCHAR(20)")

