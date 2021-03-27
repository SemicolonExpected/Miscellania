# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:02:02 2021

@author: SemicolonExpected
"""

import pycurl
from io import BytesIO

b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, 'http://www.semicolonexpected.com')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request 1:\n%s' % get_body.decode('utf8')) 

b_obj.truncate(0)

crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, 'https://www.barcodelookup.com/0016500554356')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request 2:\n%s' % get_body.decode('utf8')) 

