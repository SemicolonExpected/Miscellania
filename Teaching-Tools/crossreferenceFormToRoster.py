import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('rosterfile')
parser.add_argument('formresponses')
parser.add_argument('columnNumber', type = int, help = "Which column are the student ids in? Column Numbers start at 0")
parser.add_argument('-maxteamsize', type = int, default = 1, action="store", dest = "max", required = False)

args = parser.parse_args()

roster = args.rosterfile
response = args.formresponses
col = args.columnNumber
maxsize = args.max

with open(response,"r") as responsefile:
    reader = csv.reader(responsefile)
    data = list(reader)
    row_count = len(data)-1

counter = [0]*row_count

with open(roster,"r") as rosterfile:
    reader = csv.reader(rosterfile)
    rosterdata = list(reader)

outfile = roster.split('.')
outfile[0] = outfile[0]+"_out"
outfile = ".".join(outfile)
with open(outfile,"w") as outputfile:
	writer = csv.writer(outputfile)
	ifFirstRow = 1
	for person in rosterdata:
		
		if ifFirstRow == 1:
			ifFirstRow = 0
			person.append(response)
		else:
			if len(person) != 0:
				ifFound = 0
				for row in range(1,row_count):
					if counter[row-1] < maxsize: #if we havent accounted for all the potential people in the team. ie if a max team size is 6 if 6 people havent been ticked off
						rowdata = "|".join(data[row])
						if person[col] in rowdata:
							person.append(1)
							counter[row-1] = counter[row-1]+1
							ifFound = 1
							break
				if ifFound == 0:
					person.append(0)
		writer.writerow(person)