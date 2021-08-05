# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 01:54:05 2021

@author: SemicolonExpected
"""

import csv
import argparse
from QueryUPCDatabase import QueryUPCDatabase

parser = argparse.ArgumentParser()
parser.add_argument('upc_file')
parser.add_argument('output_file')
args = parser.parse_args()

with open(args.upc_file) as f:
    upcs = f.readlines()

upcs = [x.strip() for x in upcs]

with open(args.output_file, "a") as outfile:
    writer = csv.writer(outfile)
    for upc in upcs:
        QUD = QueryUPCDatabase(upc)
        writer.writerow([upc, QUD.brand, QUD.name, QUD.image])
        print(upc, " brand:", QUD.brand, " Product Name:", QUD.name, " image:", QUD.image)

#print(requests.get("https://barcodesdatabase.org/barcode/0074312017513").text)
#print(content)
#QUD = QueryUPCDatabase("0016500554356")
#print ("image:", QUD.image)
        