import os
import pymysql



# Get username from another environment
username = os.getenv("USER")

# connect the to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute(""" CREATE TABLE IF NOT EXIST
                        Friends(name char(20), age int, DOB datetime);""")

        # note that the above will still display a warning (not errror)if the 
        # tabel already exists
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()