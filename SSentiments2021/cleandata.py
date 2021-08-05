# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Clean up data from survey')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input datafile in csv format')
parser.add_argument('ofile', type=argparse.FileType('a'), nargs='?', default= "none", help='output datafile in csv format')

args = parser.parse_args()
#ifile = args.file

infile = args.ifile.name
if infile.endswith('.csv'):
    data = pd.read_csv(args.ifile.name)
    
    data.drop([0,1], inplace = True, axis = 0) #drop the first two rows
    
    #after filtering get a list of emails and corresponding responseids and then drop the emails
    emails = data.filter(['ResponseId','Email'], axis = 1)
    emails.to_csv(infile[:-4]+'_emails'+infile[-4:])
    data = data[data.DataQuality != '0']
    data = data[data.DataQuality != '25']
    pd.to_numeric(data.Progress)
    data = data[pd.to_numeric(data.Progress) > 43]
    #print (data.columns)
    
    
    cols = ['Demo 7_1_TEXT','Demo 7_2_TEXT','Demo 7_3_TEXT']
    data['Demo 7_1_TEXT'] = data[cols].fillna('').sum(axis=1)
    # you have to yse fillna or else the NaN will turn whatever you added it to, to also NaN
    data['Z2'] = data['Z2'].str.replace('Other', '') + data['Z2_4_TEXT'].fillna('').map(str)
    data['L2'] = data['L2'].str.replace('Other', '') + data['L2_4_TEXT'].fillna('').map(str)
    data['Z6'] = data['Z6'].str.replace('Other', '') + data['Z6_17_TEXT'].fillna('').map(str)
    data['L3'] = data['L3'].str.replace('Other', '') + data['L3_17_TEXT'].fillna('').map(str)
    data['E7'] = data['E7'].str.replace('Other', '') + data['E7_17_TEXT'].fillna('').map(str)
    
    data.drop(['Status','DistributionChannel','UserLanguage', 'Referer', 'RecipientAvgTimeToRespond',
               'Demo 1', 'Demo 2', 'Demo 7_2_TEXT','Demo 7_3_TEXT',
               'Z2_4_TEXT', 'L2_4_TEXT', 'Z6_17_TEXT','L3_17_TEXT'],inplace = True, axis = 1)
    data.drop([c for c in data.columns if c.startswith('Q_') or c.startswith('Email') or c.startswith('Consent') or ("Date" in c)],inplace = True, axis = 1)
    
    data = data.rename(columns={"Demo 5": "University", "Demo 6": "Age", "Demo 7_1_TEXT": "Referer",
                                "Z2": "VidConSoftwareUsed", "L2":"LMSUsed", "E3":"ProctorUsed", 
                                "Z3_1":"ifMandatoryCamera", "Z3_2": "ifLecturesRecorded",
                                "Z6":"beliefsVidCon", "Z7":"beliefsDataSentVidCon", "L3":"beliefsLMS", "L4":"beliefsDataSentLMS","E7": "beliefsProctor", "E8":"beliefsDataSentProctor",
                                "Z4_1":"ifWantRemote","Z4_2":"ifWantCameraOn","Z4_3":"ifWantRecording"})
    
    if args.ofile.name.endswith('.csv'):
        #data.to_csv(args.ofile.name)
        data.to_csv(args.ofile.name, mode = 'a')
    else:
        data.to_csv(infile[:-4]+'_clean'+infile[-4:])  # filename_clean.csv
        #data.to_csv(infile[:-4]+'_clean'+infile[-4:], mode = 'a')
else:
    print('File not supported')
    
args.ofile.close()
args.ifile.close()