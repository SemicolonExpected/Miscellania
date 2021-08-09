# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:47:01 2021

@author: SemicolonExpected
"""

#df.to_csv('my_csv.csv', mode='a', header=False)

import argparse
import pandas as pd
import re
import glob, os


parser = argparse.ArgumentParser(description='Clean up data from survey')
parser.add_argument('path', help='input datafile in csv format')
parser.add_argument('ofile', type=argparse.FileType('a'), nargs='?', default= "none", help='output datafile in csv format')
parser.add_argument('--append', '-a', dest = 'ifappend', action='store_true')

args = parser.parse_args()

filepath = args.path

if filepath.endswith("/") is False and filepath.endswith("\\") is False:
    filepath = filepath+"/"

data = [pd.read_csv(filepath+file) for file in os.listdir(filepath) if file.endswith("_clean.csv")]
combineddata = pd.concat(data, ignore_index=True)

combineddata.drop("Unnamed: 0", inplace = True, axis = 1)
combineddata.drop_duplicates(subset=['ResponseId'], inplace = True)

if args.ofile.name == "none":
    if args.ifappend is True:
        combineddata.to_csv(filepath + 'cleanedData.csv', mode='a', header=False)
    else:
        combineddata.to_csv(filepath + 'cleanedData.csv')
elif args.ofile.name.endswith('.csv'):
    if args.ifappend is True:
        combineddata.to_csv(filepath + args.ofile.name, mode='a', header=False)
    else:
        combineddata.to_csv(filepath + args.ofile.name)
else:
    if args.ifappend is True:
        combineddata.to_csv(filepath + 'cleanedData.csv', mode='a', header=False)
    else:
        combineddata.to_csv(filepath + 'cleanedData.csv')
    print("File not supported, stored in cleanedData.csv")

[os.remove(filepath+file) for file in os.listdir(filepath) if file.endswith("_clean.csv")]