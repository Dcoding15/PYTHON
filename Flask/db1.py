import sqlite3

# Setting up connection

#conn = sqlite3.connect(':memory:')  # short time database connection like cache memory

# Connecting to database
conn = sqlite3.connect('mydatabase.db')     # file name take as argument

# Creating a cursor
# cursor --> It is a database object that used to store in temporary memory
# We can create many no. of cursor at a time.
csr = conn.cursor()

# Creating a table
create_table = """ 
    create table student ( sid int, name char[50], state char[50] )
"""
#csr.execute(create_table)

# Insert single data into table
insert_one = """
    insert into student values (195, 'Debrishi Biswas', 'Kolkata')
"""
#csr.execute(insert_one)


# Insert many data into table
many_data = [
                (89, 'White Clover', 'USA'),
                (90, 'Wilman Kala', 'Finland'),
                (91, 'Wolski', 'Poland'),
                (92, 'Cardinal', 'Norway')
            ]
insert_many = """
    insert into student values (?,?,?)
"""
#csr.executemany(insert_many, many_data)

display_cmd = """ select * from student """
describe_table = """ pragma student """
#csr.execute(display_cmd)
#query = csr.fetchall()

for i in query:
    print(i)

'''
fetchone() --> fetch data from first row.
fetchmany([no. of row]) --> fetch specified no. of rows.
fetchall() --> fetch all rows from the table.
Note: -
    1. We can access these data from using indexing.
'''

# Always commit
conn.commit()

# Closing connection
conn.close()


'''

Datatypes: -
NULL        - It represents nothing
INTEGER     - It represents numbers without fractional part
DECIMAL     - It represents numbers with fractional part
TEXT        - It reprsents simple text or string
BLOB        - It represents binary data


Command in SQLite3: -
------------------

To open sqlite3              : .open [ file name ].db
To display exited table      : .tables
To execute command in SQLite3: .shell arg...
To exit from sqlite3 shell   : .exit or .quit
To export into csv           : .mode column
                               .mode csv
                               .output [ file name ].csv
                               SELECT * FROM [ table name ] or SQLite query
                               .quit

'''
