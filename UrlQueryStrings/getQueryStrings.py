# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:46:34 2021

@author: SemicolonExpected
"""

import argparse
#import pandas as pd
import sys
import json

def splitUrls(urls):
    domains = {}
    for i in range(len(urls)):
        urlpair = urls[i].split('?')
        #split the querystring
        referers = {}
        if len(urlpair) > 1:
            if urlpair[1] != '':
                refpairs = urlpair[1].split('&')
                for j in range(len(refpairs)):
                    if refpairs[j] != '':
                        refpair = refpairs[j].split('=')
                        if len(refpair) > 1:
                            referers[refpair[0]] = refpair[1]
    
        if urlpair[0] not in domains:
            domains[urlpair[0]] = [referers]
        else:
            if referers not in domains[urlpair[0]]:
                domains[urlpair[0]].append(referers)
    return domains
    
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
    
#print(urls[0])
#obj structure
#   url =>
#       {rid => referral string}
# list of urls, and a dict of all their referalids to referal strings
    
#alternately all the same url will map to a list of all (rid, referalstring) pairs
    

#urlpair = urls[101617].split('?')
#print(urlpair)
domains = splitUrls(urls)


out_file = open("spliturls.json", "w")
json.dump(domains, out_file, indent = 4)
#keys = list(domains)
#print(domains[keys[100]])
