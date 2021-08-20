# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import argparse
import pandas as pd
import re
import sys

parser = argparse.ArgumentParser(description='Clean up data from survey')
parser.add_argument('ifile', type=argparse.FileType('r'), help='input datafile in csv format')
#parser.add_argument('ofile', type=argparse.FileType('a'), nargs='?', default= "none", help='output datafile in csv format')

args = parser.parse_args()
#ifile = args.file

infile = args.ifile.name
try:
    data = pd.read_csv(args.ifile.name)

except:
    print('Input file not supported')
    sys.exit(1)
    
data.drop([0,1], inplace = True, axis = 0) #drop the first two rows

#Drop bad data
data = data[data.DataQuality != '0']
data = data[data.DataQuality != '25']
pd.to_numeric(data.Progress)
data = data[pd.to_numeric(data.Progress) > 43]
#print (data.columns)

#after filtering get a list of emails and corresponding responseids and then drop the emails
emails = data.filter(['ResponseId','Email'], axis = 1)
emails.to_csv(infile[:-4]+'_emails'+infile[-4:])

#Combine columns with "Other" together with the text data
cols = ['Demo 7_1_TEXT','Demo 7_2_TEXT','Demo 7_3_TEXT']
data['Demo 7_1_TEXT'] = data[cols].fillna('').sum(axis=1)
#Clean up all the variations of NYU
data['Demo 5'] = data['Demo 5'].str.replace('^Tandon$', 'NYU Tandon', flags=re.I)
data['Demo 5'] = data['Demo 5'].str.replace('nyu', 'NYU', flags=re.I)
data['Demo 5'] = data['Demo 5'].str.replace('New York University', 'NYU', flags=re.I)

# you have to yse fillna or else the NaN will turn whatever you added it to, to also NaN
data['Z2'] = data['Z2'].str.replace('Other', '') + data['Z2_4_TEXT'].fillna('').map(str)
data['L2'] = data['L2'].str.replace('Other', '') + data['L2_4_TEXT'].fillna('').map(str)
data['E3'] = data['E3'].str.replace('Other', '') + data['E3_4_TEXT'].fillna('').map(str)
data['Z6'] = data['Z6'].str.replace('Other', '') + data['Z6_17_TEXT'].fillna('').map(str)
data['L3'] = data['L3'].str.replace('Other', '') + data['L3_17_TEXT'].fillna('').map(str)
data['E7'] = data['E7'].str.replace('Other', '') + data['E7_17_TEXT'].fillna('').map(str)

#Drop the rest of the unessicary fields
data.drop(['DataQuality','Status','DistributionChannel','UserLanguage', 'Referer', 'RecipientAvgTimeToRespond',
           'Demo 1', 'Demo 2', 'Demo 7_2_TEXT','Demo 7_3_TEXT',
           'Z2_4_TEXT', 'L2_4_TEXT', 'E3_4_TEXT', 'Z6_17_TEXT','L3_17_TEXT','E7_17_TEXT'],inplace = True, axis = 1)
data.drop([c for c in data.columns if c.startswith('Q_') or c.startswith('Email') or c.startswith('Consent') or ("Date" in c)],inplace = True, axis = 1)

data = data.rename(columns={"Demo 3": "degreePersuing", "Demo 4": "yearInProgram", "Demo 5": "University", "Demo 6": "Age", "Demo 7_1_TEXT": "Referer",
                            "Z1": "ifZoomUsed", "L1": "ifLMSUsed", "E2": "ifProctorUsed",
                            "Z2": "VidConSoftwareUsed", "L2":"LMSUsed", "E3":"ProctorUsed", 
                            "Z3_1":"ifMandatoryCamera", "Z3_2": "ifLecturesRecorded",
                            "Z6":"beliefsVidCon", "Z7":"beliefsDataSentVidCon", 
                            "L3":"beliefsLMS", "L4":"beliefsDataSentLMS","E7": "beliefsProctor", "E8":"beliefsDataSentProctor",
                            "Z4_1":"ifWantRemote","Z4_2":"ifWantCameraOn","Z4_3":"ifWantRecording",
                            "E4_1":"ifComfortableProctor","E4_2":"ifPreferProctor","E4_3":"ifBelieveFairProctor", "E4_4":"ifBelieveEffectiveProctor",
                            "L5":"ifLMSHelped",
                            "Z5": "Qual_Zoom", "E1": "Qual_Exam", "E6": "Qual_Proctor"})
#Turn likerts into numeric values
temp = [0 if i == 'None of my classes' else 1 if i == 'Some of my classes' else 2 if i == 'Most of my classes' else 3 if i == 'All of my classes' else -100 for i in data['ifMandatoryCamera'] ]
data.insert(13, 'ifMandatoryCameraId', temp)
temp = [0 if i == 'None of my classes' else 1 if i == 'Some of my classes' else 2 if i == 'Most of my classes' else 3 if i == 'All of my classes' else -100 for i in data['ifLecturesRecorded'] ]
data.insert(15, 'ifLecturesRecordedId', temp)

temp = [2 if i == 'Yes. All of it' else 1 if i == 'Yes. Some of it' else 2 if i == 'No' else -1 if i == "I\'m not sure" else -100 for i in data['beliefsDataSentVidCon'] ]
data.insert(22, 'beliefsDataSentVidConId', temp)
temp = [2 if i == 'Yes. All of it' else 1 if i == 'Yes. Some of it' else 2 if i == 'No' else -1 if i == "I\'m not sure" else -100 for i in data['beliefsDataSentLMS'] ]
data.insert(27, 'beliefsDataSentLMSId', temp)
temp = [2 if i == 'Yes. All of it' else 1 if i == 'Yes. Some of it' else 2 if i == 'No' else -1 if i == "I\'m not sure" else -100 for i in data['beliefsDataSentProctor'] ]
data.insert(39, 'beliefsDataSentProctorId', temp)

temp = [-2 if i == 'Definitely No' else -1 if i == 'No' else 0 if i == 'Might or Might Not' else 1 if i == 'Yes' else 2 if i == 'Definitely Yes' else -100 for i in data['ifWantRemote'] ]
data.insert(17, 'ifWantRemoteId', temp)
temp = [-2 if i == 'Definitely No' else -1 if i == 'No' else 0 if i == 'Might or Might Not' else 1 if i == 'Yes' else 2 if i == 'Definitely Yes' else -100 for i in data['ifWantCameraOn'] ]
data.insert(19, 'ifWantCameraOnId', temp)
temp = [-2 if i == 'Definitely No' else -1 if i == 'No' else 0 if i == 'Might or Might Not' else 1 if i == 'Yes' else 2 if i == 'Definitely Yes' else -100 for i in data['ifWantRecording'] ]
data.insert(21, 'ifWantRecordingId', temp)

temp = [-2 if i == 'Definitely not' else -1 if i == 'Probably not' else 0 if i == 'Might or might Not' else 1 if i == 'Probably yes' else 2 if i == 'Definitely yes' else -100 for i in data['ifBelieveEffectiveProctor'] ]
data.insert(40, 'ifBelieveEffectiveProctorId', temp)
temp = [-2 if i == 'Definitely not' else -1 if i == 'Probably not' else 0 if i == 'Might or might Not' else 1 if i == 'Probably yes' else 2 if i == 'Definitely yes' else -100 for i in data['ifBelieveFairProctor'] ]
data.insert(39, 'ifBelieveFairProctorId', temp)
temp = [-2 if i == 'Definitely not' else -1 if i == 'Probably not' else 0 if i == 'Might or might Not' else 1 if i == 'Probably yes' else 2 if i == 'Definitely yes' else -100 for i in data['ifPreferProctor'] ]
data.insert(38, 'ifPreferProctorId', temp)
temp = [-2 if i == 'Definitely not' else -1 if i == 'Probably not' else 0 if i == 'Might or might Not' else 1 if i == 'Probably yes' else 2 if i == 'Definitely yes' else -100 for i in data['ifComfortableProctor'] ]
data.insert(40, 'ifComfortableProctorId', temp)

temp = [-2 if i == 'LMS greatly hindered my learning' else -1 if i == 'LMS hindered my learning' else 0 if i == 'LMS made no difference' else 1 if i == 'LMS aided my learning' else 2 if i == 'LMS greatly aided my learning' else -100 for i in data['ifLMSHelped'] ]
data.insert(33, 'ifLMSHelpedId', temp)

data.insert(24, 'beliefsVidConId', data['beliefsVidCon'])
data.insert(30, 'beliefsLMSId', data['beliefsLMS'])
data.insert(48, 'beliefsProctorId', data['beliefsProctor'])

cols = ['beliefsVidConId','beliefsLMSId','beliefsProctorId']
for col in cols:
    data[col] = data[col].str.replace('Video/ Audio Recordings', '1')
    data[col] = data[col].str.replace('IP Address' , '2')
    data[col] = data[col].str.replace('Hardware and System Specifications \(eg operating system, type of device, internet service provider, installed peripherals such as monitors or keyboards, etc\)', '3')
    data[col] = data[col].str.replace('Browser Specifications', '5')
    data[col] = data[col].str.replace('Open Applications or Browser Tabs','6')
    data[col] = data[col].str.replace('Installed Browser Plugins','7')
    data[col] = data[col].str.replace('Personal Files/ Documents', '8')
    data[col] = data[col].str.replace('Keystrokes/ Mouse Activity', '9')
    data[col] = data[col].str.replace('Facial Movements', '10')
    data[col] = data[col].str.replace('Sensitive Information \(information that may result in harm or discrimination eg race, health information, political beliefs, etc\)', '11')
    data[col] = data[col].str.replace('Behavioral Information \(information about how you use the software eg. how much time you spend on the software, what features you use, etc\)', '12')
    data[col] = data[col].str.replace('Personal Information \(information that can be used to identify you eg. phone number, address, employer, SSN. For the purposes of this survey your name and email address are not considered personal information\)', '13')
    data[col] = data[col].str.replace('I\'m not sure', '-1')

cols = [c for c in data.columns if c.startswith('if') and c.endswith('Id')]
data[cols]=data[cols].apply(pd.to_numeric)

columns = pd.DataFrame(data = data.columns)
#print(data['beliefsVidConId'])

data.to_csv(infile[:-4]+'_clean'+infile[-4:])  # filename_clean.csv
    
#args.ofile.close()
args.ifile.close()