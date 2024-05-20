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
    data = pd.read_csv(infile, dtype=str, keep_default_na=False)
    
    #remove redundant rows (note we need to keep FIPST and LEAID to look it up on the database)
    data = data[(data['OPERATIONAL_SCHOOLS'] != '0')]
    
    data['MSTREET1'] = data.MSTREET1 + data.MSTREET2 + data.MSTREET3 #+ " " + data.LCITY + "," + data.STATENAME + " " + data.LZIP.map(str) + "-" + data.LZIP4.map(str)
    data['LZIP'] = data.LZIP.map(str) + "-" + data.LZIP4.map(str)
    data['LSTREET1'] = data.LSTREET1 + data.LSTREET2 + data.LSTREET3 #+ " " + data.LCITY + "," + data.STATENAME + " " + data.LZIP.map(str) + "-" + data.LZIP4.map(str)
    data['SY_STATUS'] = data.SY_STATUS_TEXT
    data['LEA_TYPE'] = data.LEA_TYPE_TEXT
    data['IGOFFERED'] = "'" + data.GSLO + "-" + data.GSHI
    
    data = data.drop(columns=['MSTREET2', 'MSTREET3', 'LSTREET2', 'LSTREET3', "LZIP4", "SY_STATUS_TEXT", "UPDATED_STATUS",  "UPDATED_STATUS_TEXT", "CHARTER_LEA", "LEA_TYPE_TEXT", "OUT_OF_STATE_FLAG", "G_PK_OFFERED", "G_KG_OFFERED", "G_1_OFFERED", "G_2_OFFERED", "G_3_OFFERED", "G_4_OFFERED", "G_5_OFFERED", "G_6_OFFERED", "G_7_OFFERED", "G_8_OFFERED", "G_9_OFFERED", "G_10_OFFERED", "G_11_OFFERED", "G_12_OFFERED", "G_13_OFFERED", "G_UG_OFFERED", "G_AE_OFFERED"])
    data = data.rename(columns={'MSTREET1': 'Mailing_Address', 'LSTREET1': 'Loc_Address', 'LZIP': 'Zipcode', 'IGOFFERED' : 'Grades'})
    #remove rows with 0 operational schools
    
    data.to_csv('data_clean.csv', index=False)
    #print(data.iloc[:1])
    
except:
    sys.exit("File not found")