import os
import argparse
import subprocess
import multiprocessing

from time import time

maxThreads = multiprocessing.cpu_count()

parser = argparse.ArgumentParser()
parser.add_argument('training')
parser.add_argument('test')
parser.add_argument('--minthreads', default = 1, dest = 'min', type = int, action ='store')
args = parser.parse_args()


for i in range(args.min,maxThreads+1):
	
	tcstr= "--threadcount="+str(i)

	ts = time()

	file = open("output.txt", "w")
	run = subprocess.call(['python3','knn.py','7',args.training,args.test,tcstr,'--label-included'], stdout = file)
	runtime = time()-ts

	print("%d Threads ran fastest at %s time"% (i,runtime))