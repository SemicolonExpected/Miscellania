import sys

import argparse
import csv

from collections import Counter
from operator import itemgetter # apparently faster than the lambda function lambda x: x[1]
import heapq
import numpy as np 

from multiprocessing import Process

def binSearch(data, keyindex, start, end)

def knn(k, training, test, ifLabel=False):
	if k > len(training):
		print ("There are less than k data points, all points are nearest neighbors")
		sys.exit(1)

	euclideanDistance = np.linalg.norm
	subtract = np.subtract
	push = heapq.heappush
	pop = heapq.heappop
	getMax = heapq.nsmallest
	if ifLabel:
		for i in range(len(test)):
			minDist = []

			test[i] = list(map(float, test[i]))

			[push(minDist, (-euclideanDistance( abs(subtract(test[i], training[j][1:]  ))),training[j][0] ) ) for j in range(k)] 

			for j in range(k, len(training)):

				# check if need to calculate euclid
				diff = -abs(subtract(test[i], list(map(float,training[j][1:]))))
				# because for some reason heappq cant get max we have to turn everything into negatives and flip the sign
				if all( diff > getMax(1,minDist)[0][0] ) :
					#print(diff, getMax(1,minDist)[0][0], test[i], training[j])
					dist = -euclideanDistance(diff) 
					if dist > getMax(1,minDist)[0][0]:
						pop(minDist)
						push(minDist, (dist, training[j][0])) 

			labels = [item[1] for item in minDist]
			print (Counter(labels).most_common(1)[0][0], test[i])

	else:
		'''
		for i in range(len(test)):
			minDist = []
			test[i] = list(map(float, test[i]))

			# [push(minDist, (euclideanDistance(abs(subtract(test[i], list(map(float,training[j]))  ))), training[j]) ) for j in range(k)] # gets the first k values
			[push(minDist, (euclideanDistance(abs(subtract(test[i], training[j]  ))), training[j]) ) for j in range(k)] 
			for j in range(k, len(training)):

				# check if need to calculate euclid
				diff = -abs(subtract(test[i], list(map(float,training[j]))))
				# because for some reason heappq cant get max we have to turn everything into negatives and flip the sign
				if all( diff > getMax(1,minDist)[0][0] ) :
					#print(diff, getMax(1,minDist)[0][0], test[i], training[j])
					dist = -euclideanDistance(diff) 
					if dist > getMax(1,minDist)[0][0]:
						pop(minDist)
						push(minDist, (dist, training[j])) 

			labels = [item[1] for item in minDist]
			print (test[i],":",[item[1] for item in minDist])
		'''

def parallelknn(k, training, test, threadcount, ifLabel=False):
	# np.subtract(arr1,arr2)
	# np.abs(arr)
	# dist = np.linalg.norm(point1 - point2) 
	numtestrows = len(test)
	start = 0
	inc = int(np.ceil(numtestrows/threadcount))
	end = start + inc
	for i in range (threadcount):
		thread = Process(target = knn, args = (k, training, test[start:end], ifLabel))
		thread.start()

		if end == numtestrows:
			break;

		start = end
		end = (start + inc) if ((end + inc) < numtestrows) else numtestrows

def rowToFloat(row, ifLabel = False):
	data = []
	if ifLabel:
		data = list(map(float,row[1:]))
		data.insert(0,row[0])
	else:
		data = list(map(float,row))

	return data

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('k', type = int, help = "number of nearest neighbors to find")  # is there a better way to say this?
	parser.add_argument('trainingdata')
	parser.add_argument('testdata')
	parser.add_argument('--threadcount', default = 1, type = int, help = "THREADCOUNT: Will equally partition your data into that amount of threads")
	parser.add_argument('--label-included',action='store_true', dest = 'ifLabel', help='if the training data has labels')
	args = parser.parse_args()

	trainingfile = args.trainingdata
	testfile = args.testdata
	
	with open(trainingfile, "r") as datafile:
		reader = csv.reader(datafile)
		# trainingdata = list(reader)

		trainingdata = sorted([rowToFloat(row, args.ifLabel) for row in reader],key=itemgetter(1))
		trainingdata = [rowToFloat(row, args.ifLabel) for row in reader]

	with open(testfile, "r") as datafile:
		reader = csv.reader(datafile)
		testdata = list(reader)
	
	parallelknn(args.k, trainingdata, testdata, args.threadcount, args.ifLabel)

if __name__ == "__main__":
	main()
