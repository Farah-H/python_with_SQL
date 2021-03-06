import pyodbc

class DB_connection:

    # initialising the class
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"


    # function to establish connection with the server
    def establish_connection(self):
        connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        cursor = connection.cursor()
        return cursor



    # function to add new table to the DBB 
    def new_table(self, tablename, column_name, data_type):
        # I want kwargs to be able to put in.
        cursor = self.establish_connection()
        cursor.execute(f"CREATE TABLE {tablename} ({column_name} {data_type});")
        view_new_table = cursor.execute(f"SELECT * FROM {tablename};").fetchall()
        # printing the column to check the table exists
        for record in view_new_table:
            print(record)

    # function which inserts data into the table
    # to do: change this so it can take kwargs
    def add_info(self,table_name,column_name, data):
        cursor = self.establish_connection()
        cursor.execute(f"INSERT INTO {table_name} ({column_name}) VALUES ({data});")



# # Create a function which prompts the user for input

# table_name = input("What table are you editing? If you are creating a new table, what would youlike to call it?")
# column_name = input("Please enter the name of the column you are adding / changing.")
# # it would be cool to increment this to convert whatever they put into an appropriate format
# # e.g by replacing spaces with _ 
# data_type = input("What is the variable type for your column? If you're not sure type 'VARCHAR(155)'.")
# data = 'Please enter the information you want to add to your column.'

# class_instance = DB_connection()
# class_instance.new_table(table_name, column_name, data_type)
# class_instance.add_info(table_name,column_name,data)