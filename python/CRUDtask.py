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


#creating a table with id,username,email,gender,created_at 
try:
    create_table = """
CREATE TABLE IF NOT EXISTS Instagram (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    created_at DATETIME
);"""
    cursor.execute(create_table)  
    print('Table created successfully')
except mysql.connector.errors.ProgrammingError as e:
    print(e)



#inserting
try:
    data=[('surya','sur@gmail.com','male'),
            ('murari','mur@gmail.com','male'),
            ('sai','sai@gmail.com','male',)]
    insert_data=""" insert into instagram (username,email,gender,created_at) values(%s,%s,%s,NOW())"""
    cursor.executemany(insert_data,data)
    print('data inserted')
except:
    print('something went wrong')


#read
try:
    select_query = "SELECT * FROM instagram"
    cursor.execute(select_query)
    data = cursor.fetchall()
    for i in data:
        print(i)
except:
    print("Error reading data")


#update
try:
    update_query = """UPDATE instagram SET username = %s WHERE id = %s"""
    cursor.execute(update_query, ('bhargav', 4)) 
    con.commit()
    print("Record updated successfully")
except:
    print("Error updating data")



# #delete
def deletebyid(username, id):
    try:
        query = "DELETE FROM instagram WHERE username = %s AND id = %s"
        cursor.execute(query, (username, id))
        if cursor.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("No matching record found.")
    except Exception as e:
        print("Something went wrong:", e)
deletebyid('murari', 5)


con.commit()
cursor.close()
con.close()