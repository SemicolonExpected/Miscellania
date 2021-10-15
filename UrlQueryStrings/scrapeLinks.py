# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:44:23 2021

@author: SemicolonExpected
"""
"""
# curl "https://fonts.gstatic.com/s/lato/v20/S6u8w4BMUTPHjxsAXC-q.woff2" ^
#  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"94^\^", ^\^"Google Chrome^\^";v=^\^"94^\^", ^\^";Not A Brand^\^";v=^\^"99^\^"" ^
#  -H "Referer: https://fonts.googleapis.com/" ^
#  -H "Origin: https://daniel.haxx.se" ^
#  -H "sec-ch-ua-mobile: ?0" ^
#  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36" ^
#  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
#  --compressed

curl "https://astrosnout.com/images/uploads/game1/10200/fortnite.png" ^
  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"94^\^", ^\^"Google Chrome^\^";v=^\^"94^\^", ^\^";Not A Brand^\^";v=^\^"99^\^"" ^
  -H "Referer: https://astrosnout.com/action/fortnite?utm_content=target2&gclid=EAIaIQobChMIvprwt93h8QIVxrpRCh1BRgQ1EAEYASAAEgJO9_D_BwE" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  --compressed
  
"""

import requests
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

import argparse
import pandas as pd
import sys
import json

    
def scrape():
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81   Safari/537.36"


parser = argparse.ArgumentParser(description='Gets the Query Strings from list of urls')
parser.add_argument('--filter', dest = 'iffilter', action='store_true')
parser.add_argument('--noheader', dest = 'ifheader', action='store_false')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input list of urls in txt file without header')

args = parser.parse_args()

infile = args.ifile.name

try:
    file = open(infile, 'r')
    urls = file.readlines()
except:
    print('Input file not supported')
    sys.exit(1)
    
    
#url = ""
#resp = requests.get(url, headers=headers)

#if resp.status_code == 200 then get response text