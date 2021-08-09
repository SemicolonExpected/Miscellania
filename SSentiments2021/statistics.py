# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:25:28 2021

@author: SemicolonExpected
"""

import argparse
import numpy as np
import pandas as pd
import re
import sys
#import matplotlib.pyplot as plot

def aggStats(df):
    return pd.concat([df.count(), df.mean(axis = 0), df.median(axis = 0), df.std(axis = 0),  df.sem()], axis = 1).rename(columns={0:"n",1:"mean", 2:"median", 3:"std", 4:"stderr"})

parser = argparse.ArgumentParser(description='Clean up data from survey')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input datafile in csv format')

args = parser.parse_args()

infile = args.ifile.name

try:
    data = pd.read_csv(args.ifile.name, index_col = 0)

except:
    print('Input file not supported')
    sys.exit(1)

#print(data)

#data = data.select_dtypes(include=['number'])  # this is statistics, we only want numbers here
data.drop(['Progress', 'Duration (in seconds)'], inplace = True, axis = 1)  # we wont be analysing whether progress nor duration correlates to any info. might be good for stuff on bots??
data.replace(-100, np.NaN, inplace=True)  # fix this in clean data so we dont need -100. Probably dictionary replace tbh vs if and else so that nans and nulls can remain that way

nyu = data[data.University.str.contains('NYU', flags=re.I)]
notnyu = data[~data.University.str.contains('NYU', flags=re.I)]

nyu = nyu.select_dtypes(include=['number'])
notnyu = notnyu.select_dtypes(include=['number'])

#get the means and medians of all the numerical fields (ie likerts)
nyustats = aggStats(nyu)
notNYUStats = aggStats(notnyu)

#grab only the beliefs columns
cols = ['beliefsDataSentVidConId','beliefsDataSentLMSId', 'beliefsDataSentProctorId']
nyustats.drop(cols, inplace = True)
notNYUStats.drop(cols, inplace = True)
beliefsNYU = nyu.filter(cols, axis = 1)#.replace(-1, np.NaN, inplace = True)
beliefsNotNYU = notnyu.filter(cols, axis = 1)#.replace(-1, np.NaN, inplace = True)

#remove the not sures
beliefsNYU.replace(-1, np.NaN, inplace = True)
beliefsNotNYU.replace(-1, np.NaN, inplace = True)

beliefsNYUStats = aggStats(beliefsNYU)
beliefsNotNYUStats = aggStats(beliefsNotNYU)

totalData = pd.concat([nyu,notnyu])
beliefsTotal = pd.concat([beliefsNYU,beliefsNotNYU])

totalStats = aggStats(totalData)
beliefTotalStats = aggStats(beliefsTotal)

#combine regular stats with belief stats
nyustats = pd.concat([nyustats, beliefsNYUStats])
notNYUStats = pd.concat([notNYUStats, beliefsNotNYUStats])
totalStats = pd.concat([totalStats,beliefTotalStats])

print('\nNYU ', len(nyu.index),'\n',nyustats, '\n\nNon NYU', len(notnyu.index),'\n',notNYUStats, '\n\nTotal',len(totalData.index),'\n', totalStats)

#print(totalStats, "\n", beliefTotalStats)
#pd.concat([dataStats,beliefdataStats]).to_csv('2.csv')

#nyustats.to_csv('1.csv')
#notNYUStats.to_csv('2.csv')

#ax = nyustats.plot()
#notNYUStats.plot(ax=ax)

#plot.show()



#plot.plot(data['ifMandatoryCameraId'], data['ifMandatoryCameraId'].value_counts())
#plot.ylabel('some numbers')
#plot.show()
#freq = pd.DataFrame(data =data.ifMandatoryCameraId.value_counts().sort_index())
#print(freq)
#plot.plot([0,1,2,3],freq)
#plot.show