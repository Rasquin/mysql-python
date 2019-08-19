import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
                             
try:
    # Run a query
    """
    we open a connection to the database and then we use that connection to create the cursor.
    The cursor is the object that we actually use to execute queries.
    
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        
        Executing a query with a cursor will cause the query to run in the server, but it won't return the data to your application.
        To do that, you need to fetch the data.
        result = cursor.fetchall()
        print(result)
        
        for row in cursor:
            print(row)
    """
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()       
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()