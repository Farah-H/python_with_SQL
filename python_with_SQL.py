# this file will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to ourr Northwind DB which we have already used in the SQL week
import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
connection = pyodbc.connect(
    f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

# server namme - server name - username - and password is required to connect to pyodbc 

cursor = connection.cursor()
# lets us know where the cursor is 

# cursor.execute('SELECT @@VERSION')
# # select the version of the current DB
# row = cursor.fetchone()
# print(row)


# In our DB we have table called Customers that has customers data available
cust_row = cursor.execute('SELECT * FROM Customers;').fetchall()
for records in cust_row:
    print(records)



# iterate through the table data and fine the unit prices
product_rows = cursor.execute('SELECT * FROM Products').fetchall()
for products_records in product_rows:
    print(products_records.UnitPrice)


product_rows = cursor.execute('SELECT * FROM Products')
# getting through table 
# iterating the data until the last line of the data (until condition is false)
while True:
    records = product_rows.fetchone()
    if records is None:
        break 
    print(records.UnitPrice)