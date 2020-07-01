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
        cursor.execute("DELETE FROM Friends WHERE name in ('Jim', 'BOb')")
        connection.commit()
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()