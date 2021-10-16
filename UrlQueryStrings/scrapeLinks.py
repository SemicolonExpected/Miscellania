# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:44:23 2021

@author: SemicolonExpected
"""
"""

curl "https://astrosnout.com/images/uploads/game1/10200/fortnite.png" ^
  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"94^\^", ^\^"Google Chrome^\^";v=^\^"94^\^", ^\^";Not A Brand^\^";v=^\^"99^\^"" ^
  -H "Referer: https://astrosnout.com/action/fortnite?utm_content=target2&gclid=EAIaIQobChMIvprwt93h8QIVxrpRCh1BRgQ1EAEYASAAEgJO9_D_BwE" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  --compressed
  
"""
# get list of links and referer (main site)
# use getquerystrings to split
# merge sites to referer

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

import argparse
import pandas as pd
import sys
import json
import re

    
def scrape(urls, ifFilter = False):
    
    ignore = ["facebook", "amazon"]
    
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81   Safari/537.36"
    
    #response = requests.get("http://www.stopfungustoenail.com", headers=headers)
    #soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    #responselinks = re.findall("(?P<url>https?://[^\s]+)", response.text)
    #for i in range(len(responselinks)):
    #    print(i, responselinks[i])

    #in future grab all the script and maybe see if can find urls in that
    #grab all the a tags and li tags
    for url in urls:
        try:
            response = requests.get(url, headers=headers)
        except:
            print(url, "would not connect")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
        else:
            print(url, " responded with ", response.status_code)
        
        #r = re.compile(r"(http://[^ ]+)")
        #r = re.compile(r"(http://[^ ]+)")
        #print( re.search("(?P<url>https?://[^\s]+)", response).group("url") )
        

    #grab anything http:// and anything js

    #if https:// or .js in text
    #{url: url affiliate: true/false, links: []}

    
    #url = ""
    #resp = requests.get(url, headers=headers)
    


parser = argparse.ArgumentParser(description='Gets the Query Strings from list of urls')
parser.add_argument('--filter', dest = 'iffilter', action='store_true')
parser.add_argument('--noheader', dest = 'ifheader', action='store_false')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input list of urls in txt file without header')

args = parser.parse_args()

infile = args.ifile.name
print(infile)
try:
    file = open(infile, 'r')
    urlObj = json.load(file)
except:
    print('Input file not supported')
    sys.exit(1)

urls = list(urlObj.keys())
scrape(urls, args.iffilter)
print(len(urls))



#if resp.status_code == 200 then get response text