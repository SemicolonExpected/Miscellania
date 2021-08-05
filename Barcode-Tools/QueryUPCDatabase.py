# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:02:02 2021

@author: SemicolonExpected
"""

import requests
#import pandas as pd
from bs4 import BeautifulSoup
#import csv

class QueryUPCDatabase:
    def __init__(self, upc=""):
        self.upc = upc.zfill(13)
        self.brand = "NA"
        self.image = "NA"
        self.name = "NA"
        self.description = "NA"
        self.get_item(self.upc)

    '''
    Gets a new item populating the member variables with new information
    '''
    def get_item(self, upc):
        self.upc = upc.zfill(13)
        self.brand = "NA"
        self.image = "NA"
        self.name = "NA"
        self.description = "NA"
        if upc != "":
            response = requests.get("https://barcodesdatabase.org/barcode/"+upc.zfill(13)+"+++")
            #print(response.text)
            soup = BeautifulSoup(response.text, 'lxml')
            tables = [
                [
                    [td.get_text(strip=True) for td in tr.find_all('td')]
                    for tr in table.find_all('tr')
                ]
                for table in soup.find_all('table')
            ]

            if tables:
                tables = tables[0]

                '''
                This part is specific to the International Barcode Database layout
                accessed 27 March 2021

                Test whether the img src ends up in the Product image tuple.
                If not then layout has changed and this block up to the next comment block
                too needs to be changed
                '''
                self.brand = tables[1][1]
                self.name = tables[2][1]
                self.description = tables[4][1]
                '''
                end of the assignment block
                '''

                self.image = [
                    [img['src'] for img in table.find_all('img')]
                    for table in soup.find_all('table')
                    ][0]
                self.image = self.image[0] if self.image else self.image

    #def get_item_img:

#QUD = QueryUPCDatabase()

#url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
#response = requests.get(url)
#response.text # Access the HTML with the text property
