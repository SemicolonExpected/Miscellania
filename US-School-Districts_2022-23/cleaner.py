# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:13:35 2024

@author: semic
"""

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

import argparse
import pandas as pd
import sys
import csv
import re


parser = argparse.ArgumentParser()
parser.add_argument('ifile', type=argparse.FileType('r'), help='input csv file with header')

args = parser.parse_args()
infile = args.ifile.name

try: 
    data = pd.read_csv(infile)
    print(data.iloc[:1])
    
except:
    sys.exit("File not found")