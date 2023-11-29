import sqlite3

conn = sqlite3.connect('cache.db')
curs = conn.cursor()
create_table = 'create table emp (e_id int primary key, e_name text, e_salary number, e_age int, e_gender text, e_dept text)'
conn.execute(create_table)

insert_values = [(1, 'sam', 95000, 45, 'Male', 'Operations'),
                (2, 'bob', 8000, 21, 'Male', 'Support'),
                (4, 'julia', 73000, 30, 'Female', 'Analytics'),
                (3, 'anne', 125000, 25, 'Female', 'Analytics'),
                (5, 'matt', 159000, 33, 'Male', 'Sales'),
                (6, 'jeff', 112000, 27, 'Male', 'Operations')]

insert_values1 = """insert into emp values (1, 'sam', 95000, 45, 'Male', 'Operations'),
                (2, 'bob', 8000, 21, 'Male', 'Support'),
                (4, 'julia', 73000, 30, 'Female', 'Analytics'),
                (3, 'anne', 125000, 25, 'Female', 'Analytics'),
                (5, 'matt', 159000, 33, 'Male', 'Sales'),
                (6, 'jeff', 112000, 27, 'Male', 'Operations')"""

try:
        # conn.executemany("insert into emp values (?,?,?,?,?,?)",insert_values)
        # conn.execute(insert_values1)
        conn.commit()   #Always commit at the time of transaction
        print("Completed")
except Exception as msg:
    conn.execute("drop table emp")
    conn.commit()
    print('ERROR: ',msg)

conn.close()
