# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:16:00 2024

@author: semicolonexpected
"""

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

import argparse
import pandas as pd
import sys
import json
import re

def getdistrictWebsites():
    temp = 0
    
headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81   Safari/537.36"

#starting page https://en.wikipedia.org/wiki/Lists_of_school_districts_in_the_United_States

headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81   Safari/537.36"

try:
    response = requests.get("https://en.wikipedia.org/wiki/Lists_of_school_districts_in_the_United_States", headers=headers)
except:
    print("Wikipedia: Lists_of_school_districts_in_the_United_States would not connect")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    #get all the states
    stateLinks = ["".join(["https://en.wikipedia.org",link]) for link in [link.get('href') for link in soup.find_all('a')] if link is not None and "List_of_school_districts" in link]
    
    #open csv file here
    
    
    for stateLink in stateLinks:
        try: 
            response = requests.get(stateLink, headers=headers)
        except:
            print(stateLink, " cannot be reached")
        if response.status_code == 200:
            #print (stateLink)
            soup = BeautifulSoup(response.text, 'lxml')
            #check if link has a table
            tables = soup.find_all('table',class_ ="wikitable")
            if len(tables) > 0:
                for table in tables:
                    print(stateLink)
            else:
                print("no table")
            
            #format into csv file
else:
    print("Wikipedia: Lists_of_school_districts_in_the_United_States responded with ", response.status_code)