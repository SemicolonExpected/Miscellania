# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:46:34 2021

@author: SemicolonExpected
"""

import argparse
import pandas as pd
import sys
import json

def splitUrls(urls, ifFilter = False, ifEmptyStrings = True):
    domains = {}
    ignorerefs = []
    if ifFilter is True:
        ignorerefs = ['dclid','gclid', 'gclsrc']
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
                            if refpair[0] not in ignorerefs:
                                if ifEmptyStrings is True or (ifEmptyStrings is False and refpair[1] != ""):
                                    referers[refpair[0]] = refpair[1].strip()

        urlpair[0] = urlpair[0].strip()
        if urlpair[0] not in domains:
            if referers != {}:
                domains[urlpair[0]] = [referers]
            else:
                domains[urlpair[0]] = []
        else:
            if referers != {}:
                domains[urlpair[0]].append(referers)
    return domains

def aggregateReferers(urldict):
    for url in urldict:
        if len(urldict[url]) > 1:
            #combine dictionaries by key
            agg = pd.DataFrame(urldict[url]).to_dict(orient='list')
            for key in agg:
                agg[key] = list(set(agg[key]))
            urldict[url] = agg

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
    
domains = splitUrls(urls, args.iffilter)
domainsNoEmpty = splitUrls(urls, args.iffilter, False)

aggregateReferers(domains)

#print(len(list(domains.keys())))

out_file = open("spliturlsAggregated.json", "w")
json.dump(domains, out_file, indent = 4)
out_file.close()

'''
# uncomment out to print to json

out_file = open("spliturls.json", "w")
json.dump(domains, out_file, indent = 4)
out_file.close()

out_file = open("spliturls_noempty.json", "w")
json.dump(domainsNoEmpty, out_file, indent = 4)
out_file.close()
'''
#keys = list(domains)
#print(domains[keys[100]])
