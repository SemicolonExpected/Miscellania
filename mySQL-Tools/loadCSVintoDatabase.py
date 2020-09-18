import csv
#Use if python 2
#import MySQLdb
#Use if python 3
import pymysql
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c',action='store_true', help='if create new table')
parser.add_argument('filename')
parser.add_argument('tablename')

args = parser.parse_args()

file = args.filename
tablename = args.tablename

#db = MySQLdb.connect(host='localhost', user='vz338', passwd='orange13', db='vz338')
db = pymysql.connect(host='localhost', user='user', passwd='password', db='database')
cursor = db.cursor()

with open(file, 'r') as csvfile:
	reader = csv.reader(csvfile)
	colnames = " varchar(255), ".join(next(reader)) #this defaults the datatypes to var, play with this if you want random datatypes
	colnames = colnames+" varchar(255)"
	if args.c:
		#create table
		#query = "CREATE TABLE %s(%s);"
		#cursor.execute(query,(tablename,colnames));
		cursor.execute("CREATE TABLE "+tablename+"("+colnames+");")
	for row in reader:
		#query = "INSERT INTO %s VALUES (%s)"
		#cursor.execute(query,(tablename, ",".join(row)))
		temp = []
		for item in row:
			try:
				item = int(item)
				temp.append(item);
			except ValueError:
				temp.append("'%s'" % item)
		tempstr = ",".join(temp)
		cursor.execute("INSERT INTO "+tablename+" VALUES("+tempstr+");")

db.commit()
