import os
import pymysql



# Get username from cloud9 workspace
# modify this variable if running on another environment
username = os.getenv("USER")

# connect the to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()