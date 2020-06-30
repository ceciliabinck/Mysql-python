import os
import pymysql




# Get username from  workspace
# modify this variable if running on 
username = os.getenv("USER")

# connect the to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                        (23, 'Bob'))
        connection.commit()
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()