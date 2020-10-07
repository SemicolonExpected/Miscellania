## loadCSVintoDatabase.py

Loads CSV data from file into a database. It assumes the first row values are column names. Change the username, password, and db in file. 
Has option for python 2 and 3, just comment out `pymysql` and uncomment out `mysqldb` for python2 for both the import and connector lines. Set to python3 by default.
Unfortunately the create table value currently creates a table where all the columns are just `varchar(255)` right now. Would be good if we could write a script to create varied tables.

    loadCSVintoDatabase.py -c <filename> <tablename>
