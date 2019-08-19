# Start the MySQL service
mysql-ctl start

# Log into the MySQL shell
mysql -u $C9_USER -p mysql -u root -p

# Download the chinook database
wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql

# Import the Chinook SQL script file into MySQL
mysql -u $C9_USER -p < Chinook_MySql_AutoIncrementPKs.sql

# Install pymsql
after exiting the mysql server, sudo pip3 install pymysql

#    Create table command
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
        
#  Insert many rows into table
with connection.cursor() as cursor:
        rows = [("bob", 21, "1990-02-06 23:04:56"),
            ("jim", 56, "1955-05-09 13:12:45"),
            ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
        
# Update table method I
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()
        
# Update table method II
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        connection.commit()
        
# Update many in the table
    with connection.cursor() as cursor:
        rows = [(29, 'bob'),
                (64, 'jim'),
                (99, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
# Delete I
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()

# Delete II
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        connection.commit()
# Delete many rows
try:
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim'])
        connection.commit()
# Delete Where in (List)
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()