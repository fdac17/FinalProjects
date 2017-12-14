# Ty Vaughan
# CS 545 - Fall 2017
# Final Project

# This function parses the StackDump StackOverflow users file and writes users to 
# file for later reading.

from stackapi import StackAPI, StackAPIError
import xml.etree.ElementTree as ET
from datetime import datetime
import requests as req
from bs4 import BeautifulSoup
import json

import time
import unicodedata
import os

if __name__ == "__main__":

    # Change directory to the user dump file.
    os.chdir('../..')
    with open('Users.xml') as infile:

        # Open the file to access already interpreted users.
        if(not os.path.isfile('alluserprofiles.txt')):
            f = open('alluserprofiles.txt', 'w+')
            f.close()

        # Obtain all of the users that have already been processed
        Users_info = {}
        f = open('alluserprofiles.txt','r')
        for line in f.readlines():
            if(line.rstrip() != ''):
                info = line.rstrip().split(';;')
                Users_info[int(info[0])] = line.rstrip()
        f.close()

        # Re-open the user file for writing new profiles.
        f = open('alluserprofiles.txt','w+')

        # Obtain the user locations for all obtained user Ids
        cur = 0
        for line in infile:
            
            # Skip the metadata lines.
            if(cur > 2):

                try:
                    # Obtain the parsed user data.
                    root = ET.fromstring(line)

                    if('AccountId' in root.attrib.keys() and \
                        'Id' in root.attrib.keys() and \
                        'Location' in root.attrib.keys() and \
                        root.attrib['Id'] not in Users_info.keys()):
                        accountID = root.attrib['AccountId']
                        userID = root.attrib['Id']
                        location = root.attrib['Location']
                        
                        output = userID + ';;' + accountID + ';;' + location + '\n'
                        try:
                            f.write(output)
                            f.flush()
                        except UnicodeEncodeError as e:
                            print('Cannot process user: {}'.format(root.attrib['Id']))
                except:
                    print('Line not readable')

            if(cur%10000 == 0):
                print(cur)
            cur += 1