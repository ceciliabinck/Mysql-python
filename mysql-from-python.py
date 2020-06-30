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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()