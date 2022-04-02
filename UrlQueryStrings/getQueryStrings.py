# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:46:34 2021

@author: SemicolonExpected
"""


import pandas as pd
from urllib.parse import urlparse

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
        if len(urldict[url]) == 1:
            if isinstance(urldict[url], list):
                urldict[url] = urldict[url][0]
        if len(urldict[url]) == 0:
            urldict[url] = {}

def aggregateDomains(urldict):
    aggurldict = {}
    for url in urldict:
        host = urlparse(url).scheme+"://"+urlparse(url).netloc
        if host in aggurldict:
            #add new entry
            aggurldict[host]["links"][url] = urldict[url]
        else:
            aggurldict[host] = {"links":{url: urldict[url]}}
        
    return aggurldict
        
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
