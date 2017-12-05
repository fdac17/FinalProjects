# Ty Vaughan
# CS 545 - Fall 2017
# Final Project

# This program obtains users from StackAPI.

from stackapi import StackAPI, StackAPIError
from datetime import datetime
import requests as req
from bs4 import BeautifulSoup
import json

import time
import unicodedata
import os.path

ClientID = 11052
ClientSecret = 'BULQoUExD)pGc0SDom0tjg(('
Key = 'iwV*aJ1Ac6jGaDJ5UxlF7A(('

# This function retrieves questions.
def GatherQuestionData(SITE):
    # Fetch questions that have a coding language as a tag
    languages = ['python', 'c', 'c++', 'java', 'javascript', 'r', 'objective-c', 'php', 'sql', 'ruby']
    question_results = {}

    # The dates for roughly the entire 9 nine years StackOverflow has existed.
    dates = [
        1508111137,
        1476489600,
        1444867200,
        1413331200,
        1381795200,
        1350259200
    ]

    for l in languages:
        for d in range(len(dates)-2,-1,-1):
            try:
                questions = SITE.fetch('questions', fromdate=dates[d+1], todate=dates[d], tagged=l, sort='votes')
                #questions = SITE.fetch('questions', tagged=l, sort='votes')
                key = l + '_' + str(dates[d])
                print('key {}'.format(key))
                question_results[key] = questions
            except StackAPIError as e:
                print("   Error URL: {}".format(e.url))
                print("   Error Code: {}".format(e.code))
                print("   Error Error: {}".format(e.error))
                print("   Error Message: {}".format(e.message))
    
    dict_str = json.dumps(question_results)
    dict_json = json.loads(dict_str)
    fname = 'questiondata_' + str(int(time.time()))

    f = open(fname,'w')
    json.dump(dict_json, f)
    f.close()
    return


def GatherUserInfo(datafile):
    # Open the file to read questions from.
    fname = open(datafile,'r')
    data = json.load(fname)

    # Open the file to access already interpreted users.
    if(not os.path.isfile('userprofiles.txt')):
        f = open('userprofiles.txt', 'w+')
        f.close()

    # Obtain all existing user profiles.
    Users = []
    f = open('userprofiles.txt','r')
    for line in f.readlines():
        info = line.rstrip().split(';')
        Users.append(int(info[0]))
    f.close()

    # Open file for writing user profiles.
    f = open('userprofiles.txt', 'a+')

    # Append new users to the user profiles file.
    for qset_attr, qset_val in data.iteritems():
        for q_attr, q_val in qset_val.iteritems():
            if(q_attr == 'items'):
                for val in q_val:
                    val = json.dumps(val)
                    json_obj = json.loads(val)

                    # Iterate through each of the question attributes.
                    for attr, val in json_obj.iteritems():
                        if( isinstance(val, unicode)):
                            unicodedata.normalize('NFKD', val).encode('ascii','ignore')

                        # Obtain the user information
                        if(attr == 'owner'):

                            date_init = json_obj['creation_date']
                            date_end = json_obj['last_activity_date']

                            owner = json.dumps(val)
                            json_owner = json.loads(owner)

                            #print json_owner.keys()
                            #exit(0)

                            # Iterate through each of the questions' owner attributes
                            #for o_attr, o_val in json_owner.iteritems():
                            #    print('{} = {}'.format(o_attr,o_val))
                            if('user_id' in json_owner.keys() and \
                                'link' in json_owner.keys() and  \
                                'display_name' in json_owner.keys()):

                                user_id = json_owner['user_id']
                                link = json_owner['link']
                                display = json_owner['display_name']

                                # Convert unicode to ascii
                                if( isinstance(user_id, unicode)):
                                    unicodedata.normalize('NFKD', user_id).encode('ascii','ignore')
                                if( isinstance(link, unicode)):
                                    unicodedata.normalize('NFKD', link).encode('ascii','ignore')
                                if( isinstance(display, unicode)):
                                    unicodedata.normalize('NFKD', display).encode('ascii','ignore')

                                if(user_id not in Users):
                                    try:
                                        f.write('{};{};{};{};{}\n'.format(user_id,link,display,date_init,date_end))
                                    except UnicodeEncodeError as e:
                                        print e
    return

# This function gather the user location
def GatherUserLocations(SITE):
    # Open the file to access already interpreted users.
    if(not os.path.isfile('userprofiles.txt')):
        f = open('userprofiles.txt', 'w+')
        f.close()

    # Obtain all existing user profiles.
    Users_info = {}
    f = open('userprofiles.txt','r')
    for line in f.readlines():
        info = line.rstrip().split(';')
        Users_info[int(info[0])] = line.rstrip()
    f.close()

    # Open the file to access users whose location we have.
    if(not os.path.isfile('userlocations.txt')):
        f = open('userlocations.txt', 'w+')
        f.close()

    # Obtain all existing users whose location we have.
    Users_locs = []
    f = open('userlocations.txt','r')
    for line in f.readlines():
        info = line.rstrip().split(';')
        Users_locs.append(int(info[0]))
    f.close()

    # Open user locations file for writing.
    f = open('userlocations.txt','a+')
    count = 0
    maxCount = len(Users_info.keys()) - len(Users_locs)
    ids = []

    # Go through all users that we have info for.
    for user, userVal in Users_info.items():

        # Ensure that the user hasn't bee searched yet.
        if user not in Users_locs:
            count += 1


            # Append to list if don't have max size.
            if(len(ids) < 3 and maxCount - count != 0):
                ids.append(user)

            # Query for users if we do.
            else:
                try:
                    questions = SITE.fetch('users', ids=ids)
                    #questions = SITE.fetch('questions', tagged=l, sort='votes')
                    for user in questions['items']:
                        if('location' in user.keys()):
                            user_id = user['user_id']
                            account_id = user['account_id']
                            location = user['location']
                            unicodedata.normalize('NFKD', location).encode('ascii','ignore')
                            try:
                                #print('{};{};{}'.format(user_id, account_id, location))
                                if(user_id not in Users_locs and account_id not in Users_locs):
                                    f.write('{};{};{}\n'.format(user_id, account_id, location))
                                    f.flush()
                                    Users_locs.append(user_id)
                                    Users_locs.append(account_id)
                            except UnicodeEncodeError as e:
                                print(e)
                except StackAPIError as e:
                    print("   Error URL: {}".format(e.url))
                    print("   Error Code: {}".format(e.code))
                    print("   Error Error: {}".format(e.error))
                    print("   Error Message: {}".format(e.message))
                ids = []
    f.close()
    return

def GatherUserLocations2():
    # Open the file to access already interpreted users.
    if(not os.path.isfile('userprofiles.txt')):
        f = open('userprofiles.txt', 'w+')
        f.close()

    # Obtain all existing user profiles.
    Users_info = {}
    f = open('userprofiles.txt','r')
    for line in f.readlines():
        info = line.rstrip().split(';')
        Users_info[int(info[0])] = info[1]
    f.close()

    # Open the file to access users whose location we have.
    if(not os.path.isfile('user_locations.txt')):
        f = open('user_locations.txt', 'w+')
        f.close()

    # Obtain all existing users whose location we have.
    Users_locs = []
    f = open('user_locations.txt','r')
    for line in f.readlines():
        info = line.rstrip().split(';')
        Users_locs.append(int(info[0]))
    f.close()

    # Open user locations file for writing.
    f = open('user_locations.txt','a+')

    count = 0
    max_count = len(Users_info.keys()) - len(Users_locs)

    # Get the locations for all users
    for user, url in Users_info.items():

        if(user not in Users_locs):

            location = ''
            email = ''
            count += 1

            # Obtain the returned stackoverflow profile page.
            ret = req.get(url)
            data = ret.text
            soup = BeautifulSoup(data,'html.parser')

            # Obtain the email info
            bio = soup.find('div', {'class': 'bio'})
            if(bio != None):
                para = bio.findAll('p', {})
                if(para != None):
                    for p in para:
                        text = p.getText()
                        if('email:' in text):
                            t = text.strip().split(' ')
                            email = t[1]
                            break

            # Obtain the location info
            lists = soup.findAll('div', {'class': 'user-links'})
            for _list in lists:
                li = _list.findAll('li', {})
                for element in li:
                    loc = element.getText().strip()
                    if('Your' not in loc and 'Member' not in loc and 'profile' not in loc and \
                        '.' not in loc and 'Last' not in loc):
                        location = loc
                        break
                
                # Exit this loop if the location was found.
                if(location != ''):
                        break

            # Write the user information to userlocations.txt
            output = str(user) + ';;' + location
            if(email != ''):
                output += ';;' + email
            output += '\n'

            # Provide output
            try:
                f.write(output)
            except UnicodeEncodeError as e:
                print(e)
                print('Could not process user: ' + str(user))
            if(count % 100 == 0):
                print('Finished {:6d} out of {:6d}'.format(count,max_count))

            # Throttle the search.
            time.sleep(5)
            
    print('Finished {:6d} out of {:6d}'.format(count,max_count))


if __name__ == '__main__':
    GatherQuestions = False
    GatherUserInfo = False
    GatherUserLocs = True


    #resp = requests.get('https://stackexchange.com/oauth/dialog?client_id=11052&scope=private_info&redirect_uri=https://stackexchange.com/oauth/login_success/')
    #print(vars(resp))

    # Initialize StackAPI to StackOverflow
    try:
        SITE = None
        #SITE = StackAPI('stackoverflow')
        #SITE._api_key = None

        # Set the query parameters.
        #SITE.page_size = 100   # 100 is the max size per query -> 10 daily queries
        #SITE.max_pages = 1     # Each page is at least one query
    except StackAPIError as e:
        print("   Error URL: {}".format(e.url))
        print("   Error Code: {}".format(e.code))
        print("   Error Error: {}".format(e.error))
        print("   Error Message: {}".format(e.message))

    # Obtain 5000 questions pertaining to the specified multiple languages.
    if(GatherQuestions):
        GatherQuestionData(SITE)

    # Obtain which users posted the questsions 
    if(GatherUserInfo):
        GatherUserInfo('questiondata.txt')

    # Obtain the location of the users that posted questions.
    if(GatherUserLocs):
        #GatherUserLocations(SITE)
        GatherUserLocations2()
