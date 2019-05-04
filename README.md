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