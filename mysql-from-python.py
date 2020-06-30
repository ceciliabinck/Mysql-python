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
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()