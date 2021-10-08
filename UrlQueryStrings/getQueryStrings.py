# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:46:34 2021

@author: SemicolonExpected
"""

import argparse
#import pandas as pd
import sys

parser = argparse.ArgumentParser(description='Gets the Query Strings from list of urls')
parser.add_argument('--noheader', dest = 'ifheader', action='store_false')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input list of urls in txt file without header')

args = parser.parse_args()

infile = args.ifile.name

try:
    file1 = open(infile, 'r')
    urls = file1.readlines()
except:
    print('Input file not supported')
    sys.exit(1)
    
print(urls[0])
