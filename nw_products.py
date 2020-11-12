from SQL_task import DB_connection

#instantiating DB_connection class to establish connection (DRY)
connection_instance = DB_connection()
cursor = connection_instance.establish_connection()

# doing the command in SQL is much more efficient than trying to loop through and avg in python
average_units_in_stock = cursor.execute('SELECT AVG(UnitsInStock) FROM Products;')
for row in average_units_in_stock:
    # ugly output, fix later
    print(f'We have, on average,{row} units of each item in stock.')

