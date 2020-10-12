## loadCSVintoDatabase.py

Loads CSV data into a mySQL database. It assumes the first row values are column names. Change the username, password, and db in file. 
Has option for python 2 and 3, just comment out `pymysql` and uncomment out `mysqldb` for python2 for both the import and connector lines.
Unfortunately the create table value creates a table where all the columns are just `varchar(255)` right now. Would be good if we could somehow easily write a script to create varied tables

    loadCSVintoDatabase.py -c <filename> <tablename>

This script is deprecated since `LOAD DATA INFILE` is a lot faster.

## ParallelLoader/ploadCSVintoDatabase.py

Parallel Loader to load CSV data into a mySQL database. 
Tablename here defaults to the csv name. 


    ploadCSVintoDatabase.py [-field][-partitions][--create-table] [--header-included] <filename> <threadcount>

    <filename> is the csv file you want to load into the database

    <threadcount> is the number of threads you will insert on. 

### Partitioning

    [-field] is the number of the column we will partition by. If left out the table created will not partition.

    [-partition] is the number of partitions for the table. The default # of partitions is the number of threads, which I find leads to the best execution time

Be careful what you choose to partition on as that can affect performance, making the program run faster than even `LOAD DATA INFILE`, or slower than running without partitions. 

### ParallelLoader/getOptimalThreadCount.py

Helper for Parallel Loader to see how many threads work best. 
Basically tests loading starting at the minimum # of threads thread and increments until we dont see any speed increase. 
Default minthreads == 1
Not very useful unless you are looking to generalize for all SIMD multithreading needs on that computer or doing a competition and a split second in performance matters.

    getOptimalThreadCount.py [--minthreads=int] <filename>