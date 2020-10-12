import pymysql

import os
import argparse
import subprocess
import multiprocessing

from time import time

maxThreads = multiprocessing.cpu_count()

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('--minthreads', default = 1, dest = 'min', type = int, action ='store')
args = parser.parse_args()

file = args.filename
tablename = file.split(".")[0]

db = pymysql.connect(host='localhost', user='user', passwd='password', db='test')
cursor = db.cursor()


shortestTime = 10000
shortest = args.min

for i in range(args.min,maxThreads+1):

	try:
		q = "DROP TABLE "+ tablename + ";"
		cursor.execute(q)
		db.commit()
	except:
		print("Can't drop table")


	ts = time()
	
	try:
		run = subprocess.run(['python3','pLoadCSVintoDatabase.py',file,str(i),'--create-table','-field=2'])
		runtime = time()-ts
		if (runtime < shortestTime):
			shortestTime = runtime
			shortest = i
		else:
			print("%d Threads ran fastest at %s time", (shortest, shortestTime))
			#break
	except:
		print("%d Threads results in too big of a payload")
		continue
	

