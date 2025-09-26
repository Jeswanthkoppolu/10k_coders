import mysql.connector
from info import info

try:
    con=mysql.connector.connect(**info)
    print("Connection successful")
except:
    print("not able to connect")
cursor=con.cursor()



#creating database
query='create database if not exists 10kcoders'
cursor.execute(query)

#use database
cursor.execute('use 10kcoders')

#creating a table with id,name,email,course,join_date ---
try:
    create_table = """ 
    CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    course VARCHAR(50),
    join_date DATE
    );"""
    cursor.execute(create_table)
    print('table created successfuly')
except mysql.connector.errors.ProgrammingError as e:
    print(e)

#inserting single row data into table ----
try:
    data=('bob','bob@gmail.com','pfs','2025-07-15')
    insert_data=""" insert into students (name,email,course,join_date) values(%s,%s,%s,%s)"""
    cursor.execute(insert_data,data)
    print('data inserted')
except:
    print('something went wrong')


#geting the data ---
def getrecords():
    try: 
        query="select * from students"
        cursor.execute(query)
        results=cursor.fetchall()
        for row in results:
            print(row)
    except:
        print('something went wrong')
getrecords()