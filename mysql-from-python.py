import os
import pymysql
import datetime 



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
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES(%s,%s,%s);", row)
        connection.commit()
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()