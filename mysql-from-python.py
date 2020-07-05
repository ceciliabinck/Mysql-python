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
        list_of_names = ['Fred', 'Fred'] 
        # prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # close the connection, regardless of whether the above was successful
    connection.close()