'''
Author: Victoria Zhong
''' 

import sys
from time import time

import csv
import math

import pymysql
import argparse

import multiprocessing
from threading import Thread
from queue import Queue



'''
Parameters needed
CSV file
if there is a header in the csv file 
if a table needs to be created
how many partitions to make
'''

def checkIfIndexExists(data, index):  # we're really just checking whether an index exists
	try:
		temp = data[index]
	except IndexError:
		print ("\n ERROR: INDEX "+index+" does not exist")
		sys.exit(1)

def getDataType(data):  # can we expand this to check if timestamp?
	datatype = "VARCHAR(255)"
	if data.replace('.','',1).isdigit():
		#if is some number
		if float(data).is_integer():
			datatype = "INT(255)"
		else:
			datatype = "DOUBLE"
	return datatype


def insertionThread(startrow, endrow, tablename, rows):

	#db = pymysql.connect(host='localhost', user='user', passwd='password', db='test')
	db = pymysql.connect(host='localhost', user='vz338', passwd='orange13', db='vz338')
	cursor = db.cursor()

	#rows is a list of rows to insert (rows in rows are in list form as well)
	tempquery = "INSERT INTO `"+tablename+"` VALUES "

	values = []
	temp = []
	extend = values.extend
	append = temp.append
	for i in range(startrow, endrow):
		extend(rows[i])  # extends values
		if i == startrow:
			tempstr = tempquery + "("+ "%s,"*(len(rows[i])-1) +"%s)"
		else:
			tempstr = "("+ "%s,"*(len(rows[i])-1) +"%s)"
		append(tempstr)  # appends to temp
	
	query = ",".join(temp)	
	query = query + ";"

	try:
		cursor.execute(query, values)
	except:
		'''
		Usually a broken pipe error can be expanded to catch other things Imay not have encountered
		'''
		print("Error")
		sys.exit("Threads results in too big of a payload. Insert Aborted")

	db.commit()


def main():
	#ts = time() #initial time

	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	parser.add_argument('threadcount', type = int, help = "THREADCOUNT: Will equally partition your data into that amount of threads")  # is there a better way to say this?
	parser.add_argument('-field', type = int, default = -1, action="store", dest = "field", required = False, help = "Which field/column to partition by if any. Column count starts at 0")
	parser.add_argument('-partitions', type = int, default = -1, action="store", dest = "partitions", required = False, help = "How many partitions do you want? Default is thread number")
	parser.add_argument('--create-table',action='store_true', dest = 'ifCreate', help='if create new table')
	parser.add_argument('--header-included',action='store_true', dest = 'ifHeader', help='if create new table')

	args = parser.parse_args()

	file = args.filename
	tablename = file.split(".")[0]
	x = args.threadcount

	#db = pymysql.connect(host='localhost', user='user', passwd='password', db='test')
	db = pymysql.connect(host='localhost', user='vz338', passwd='orange13', db='vz338')
	cursor = db.cursor()


	with open(file, "r") as datafile:
		reader = csv.reader(datafile)
		data = list(reader)

	'''
	CREATE TABLE
	'''
	if args.ifCreate:
		colnames = ""
		datatypes = []

		'''
		If there is a header use the header labels from the first row of data, 
		else call it C0x and use the first row to see how many columns exist

		'''

		try:
			if args.ifHeader:
				temp = data[0] 
				temp2 = data[1] # used to test datatypes depending on number of columns we might call this a lot 
			else:
				temp = data[0]
		except IndexError:
			print ("\n ERROR: CSV must have at least one row of data not including headers")
			sys.exit(1)


		colnameList = []
		if args.ifHeader:
			colnameList = [colnames + temp[i] + " " + getDataType(temp2[i]) for i in range (0,len(temp))]
		
		else:
			numCol = len(temp)
			colnameList = [colnames + "C"+str(i+1).zfill(2) + " " + getDataType(temp[i]) for i in range (0, numCol)]

		colnames = ", ".join(colnameList)
		partitionstr = ""
		if args.field != -1:
			try:
				if args.partitions != -1:
					partitionstr = " PARTITION BY KEY(%s) PARTITIONS %d" % (colnameList[args.field].split()[0], args.partitions)
				else:
					partitionstr = " PARTITION BY KEY(%s) PARTITIONS %d" % (colnameList[args.field].split()[0], x)
			except IndexError:
				"Invalid field, partitions not created"
		query = "CREATE TABLE `%s`(%s)%s;" % (tablename, colnames,partitionstr)
		cursor.execute(query)
		


	'''
	INSERT ROWS
	'''
	
	# Make sure we don't have more threads than rows of data
	# Also wanted to show off this disgusting monster of a nested ternary operation I made
	# Wonder if we should divide by 2 or 3 after just because having each thread do 1 line of code is real inefficient	
	x = ((len(data)-1) if (len(data)-1) < x else x) if args.ifHeader else (len(data) if len(data) < x else x)

	startrow = 1 if args.ifHeader else 0
	inc = math.ceil(len(data)/x)
	endrow = startrow + inc

	for i in range(x):

		thread = multiprocessing.Process(target = insertionThread, args = (startrow, endrow, tablename, data))

		thread.start()
		startrow = endrow
		endrow = (endrow + inc) if ((endrow + inc) < len(data)) else len(data)

	#print("Took %s seconds", time()-ts)

if __name__ == "__main__":
	main()