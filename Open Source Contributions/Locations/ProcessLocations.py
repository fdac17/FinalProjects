# Ty Vaughan
# CS 545 - Fall 2017
# Final Project

# This file reads in and finds the locations of users in the file output provided by GatherSOData.py

# Types of location formats to be used:
# 1. Country
# 2. City, Country (Country is full name or abbreviation) -> 2 possibilities
# 3. City, State (State is full name or abbreviation) -> 2 possibilities
# 4. State, Country (State and Country can be either full name or abbreviation) -> 4 possibilities
# 5. City, State, Country (State and Country can be full name or abbreviation) -> 4 possibilities

# Outputs will be of the format:
# 1. location: the original location text 
# 2. country
# 3. city
# 4. state (for locations in the US)
# 5. gps latitude
# 6. gps longitude

import pycountry
import os
import string

# This function discovers locations that exists within the united states.
def getUSLocation(location):
    global US_States
    global US_States_Abbr
    global CountryCodes
    global Cities
    global States
    global GPS

    loc = location[0]
    for i in range(1,len(location)):
        loc += ',,' + location[i] 

    state_centers = [
        (32.7794, 86.8287),
        (64.0685, 152.2782),
        (34.2744, 111.6602),
        (34.8938, 92.4426),
        (37.1841, 119.4696),
        (38.9972, 105.5478),
        (41.6219, 72.7273),
        (38.9896, 75.5050),
        (38.9101, 77.0147),
        (28.6305, 82.4497),
        (32.6415, 83.4426),
        (20.2927, 156.3737),
        (44.3509, 114.6130),
        (40.0417, 89.1965),
        (39.8942, 86.2816),
        (42.0751, 93.4960),
        (38.4937, 98.3804),
        (37.5347, 85.3021),
        (31.0689, 91.9968),
        (45.3695, 69.2428),
        (39.0550, 76.7909),
        (42.2596, 71.8083),
        (44.3467, 85.4102),
        (46.2807, 94.3053),
        (32.7364, 89.6678),
        (38.3566, 92.4580),
        (47.0527, 109.6333),
        (41.5378, 99.7951),
        (39.3289, 116.6312),
        (43.6805, 71.5811),
        (40.1907, 74.6728),
        (34.4071, 106.1126),
        (42.9538, 75.5268),
        (35.5557, 79.3877),
        (47.4501, 100.4659),
        (40.2862, 82.7937),
        (35.5889, 97.4943),
        (43.9336, 120.5583),
        (40.8781, 77.7996),
        (41.6762, 71.5562),
        (33.9169, 80.8964),
        (44.4443, 100.2263),
        (35.8580, 86.3505),
        (31.4757, 99.3312),
        (39.3055, 111.6703),
        (44.0687, 72.6658),
        (37.5215, 78.8537),
        (47.3826, 120.4472),
        (38.6409, 80.6227),
        (44.6243, 89.9941),
        (42.9957, 107.5512)
    ]

    countryFound = False
    stateFound = False
    cityFound = False

    # Now that we have the segments of the location, first check if we have a country
    abbrevs = ['us', 'usa', 'united states']
    index1 = -1
    for a in abbrevs:
        for e in location:
            if(a == e):
                countryFound = True
                index1 = location.index(e)
                break
        if(countryFound):
            break

    # Now check if we have a state
    index3 = -1
    state = ''
    for i in range(len(US_States)):
        s = US_States[i]
        for e in location:
            if(s == e):
                stateFound = True
                index3 = location.index(e)
                if(index3 != index1):
                    state = US_States_Abbr[i]
                    break
        if(stateFound):
            break
    if(not stateFound):
        for s in US_States_Abbr:
            for e in location:
                if(s == e):
                    stateFound = True
                    index3 = location.index(e)
                    if(index3 != index1):
                        state = s
                        break
            if(stateFound):
                break

    # Now check if we have a city
    index2 = -1
    city = ()
    for i in range(len(Cities)):
        c = Cities[i]
        for e in location:
            if(city == e):
                index2 = location.index(c)
                if(index2 != index1 and index2 != index3 and CountryCodes[i] == 'us'):
                    if(stateFound):
                        if(state == States[i]):
                            cityFound = True
                            city = (i,c)
                            break
                    else:
                        state = States[i]
                        stateFound = True
                        cityFound = True
                        city = (i,c)
        if(cityFound):
            break

    if(countryFound and not stateFound and not cityFound):
        coords = (38.0000, -97.0000)
        return True, "{};{};;;{};{}".format(loc,'us', coords[0], coords[1])

    if(countryFound and stateFound and not cityFound):
        coords = state_centers[US_States_Abbr.index(state)]
        return True, "{};{};;{};{};{}".format(loc,'us',state,coords[0], coords[1])

    if(countryFound and stateFound and cityFound):
        coords = GPS[city[0]]
        return True, "{};{};{};{};{};{}".format(loc,'us',city[1],state,coords[0], coords[1])

    if(not countryFound and stateFound and not cityFound):
        coords = state_centers[US_States_Abbr.index(state)]
        return True, "{};{};;{};{};{}".format(loc,'us',state,coords[0], coords[1])

    if(not countryFound and stateFound and cityFound):
        coords = GPS[city[0]]
        return True, "{};{};{};{};{};{}".format(loc,'us',city[1],state,coords[0], coords[1])

    return False, ''

# This function discovers locations that exist outside of the united states.
def getLocation(location):
    global Countries
    global CountryCodes
    global Cities
    global States
    global GPS

    countryFound = False
    cityFound = False

    loc = location[0]
    for i in range(1,len(location)):
        loc += ',,' + location[i] 

    # Now that we have the segments of the location, first check if we have a country
    index1 = -1
    code = ''
    for c in Countries.keys():
        for e in location:
            if(c == e):
                countryFound = True
                index1 = location.index(c)
                code = Countries[c]
                break
        if(countryFound):
            break

    # Now check if we have a city
    index2 = -1
    city = ()
    for i in range(len(Cities)):
        c = Cities[i]
        for e in location:
            if(c == e):
                index2 = location.index(c)
                if(index2 != index1):
                    cityFound = True
                    city = (i,c,CountryCodes[i])
                    break
        if(cityFound):
            break

    # If we only found a country:
    if(countryFound and not cityFound):
        try:
            tmpi = CountryCodes.index(code)
            if(tmpi >= 0):
                coords = GPS[tmpi]
                return True, "{};{};;;{};{}".format(loc, code, coords[0], coords[1])
        except:
            return False, ''


    # If we only found a city:
    if(not countryFound and cityFound):
        try:
            index = city[0]
            c = city[1]
            country = ''

            # Get the country.
            for key,value in Countries.items():
                if(value == city[2]):
                    country = key
                    break

            # Get the coordinates.
            coords = GPS[index]
            return True, "{};{};{};;{};{}".format(loc, city[2], location[index2], coords[0], coords[1])
        except:
            return False, ''

    # If we found both:
    if(countryFound and cityFound and index1 != index2):
        try:
            if(city[2] == code):
                # Get the coordinates.
                coords = GPS[city[0]]
                return True, "{};{};{};;{};{}".format(loc, city[2], location[index2], coords[0], coords[1])
        except:
            return False, ''

    return False, ''


# This function takes in all user locations and tries to map them to GPS coordinates.
if __name__ == "__main__":
    ###############################################
    #
    #  Obtain all overhead information.
    #
    ###############################################

    US_States = []
    US_States_Abbr = []
    Countries = {}

    # GPS Data
    CountryCodes = []
    Cities = []
    States = []
    GPS = []

    # Obtain all users that should be analyzed.
    UserTimes = {}
    f = open('userprofiles.txt','r')
    for line in f.readlines():
        elements = line.rstrip().split(';')
        UserTimes[elements[0]] = elements[3]


    # Obtain all US States:
    f = open('states_abbr.txt','r')
    for line in f.readlines():
        line = line.rstrip()
        US_States_Abbr.append(line.lower())
    f.close()
    f = open('states.txt','r')
    for line in f.readlines():
        line = line.rstrip()
        US_States.append(line.lower())
    f.close()

    # Obtain all countries and their country codes
    for country in pycountry.countries:
        Countries[(country.name.lower()).encode('ascii', 'ignore')] = ((country.alpha_2).lower()).encode('ascii', 'ignore')

    # Obtain all cities, countries, and gps coordinates
    os.chdir('../..')
    f = open('worldcitiespop.txt','r')
    firstline = True
    for line in f.readlines():
        if(firstline == True):
            firstline = False
        else:
            elements = line.rstrip().split(',')
            CountryCodes.append(''.join(filter(lambda c: c in string.printable, elements[0].lower())))
            Cities.append(''.join(filter(lambda c: c in string.printable, elements[1].lower())))
            States.append(''.join(filter(lambda c: c in string.printable, elements[3].lower())))
            GPS.append((float(elements[5]),float(elements[6])))
    f.close()

    os.chdir('./CS545Project/wvaugha2')

    # Store all users based on their location.
    UserLocs = {}
    f = open('user_locations.txt','r')
    #f = open('alluserprofiles.txt','r')
    for line in f.readlines():
        line = line.rstrip()

        # Split into userID and location
        userElements = line.split(';;')
        if(len(userElements) > 1):
            userId = userElements[0]
            
            #location = userElements[2].strip()
            #time = ''

            location = userElements[1]
            time = UserTimes[userId]

            

            if(location != ''):
                if(location in UserLocs.keys()):
                    UserLocs[location].append((userId, time, location))
                else:
                    UserLocs[location] = [(userId, time, location)]



    ###############################################
    #
    #  Process all users and identify a location
    #
    ###############################################

    items = sorted(UserLocs.items())
    for key,value in items:

        location = []

        # Try to separate the line based on commas
        elements = key.split(',')
        if(len(elements) > 1):
            location = elements

        # Try to separate the line based on forward slashes
        elements = key.split('/')
        if(len(elements) > 1 and len(location) == 0):
            location = elements

        # Try to interpret single location
        if(key != '' and len(location) == 0):
            location = elements

        for i in range(len(location)):
            location[i] = ''.join(filter(lambda c: c in string.printable, location[i]))
            location[i] = location[i].strip().lower()

        # Obtain the GPS locations for each user.
        ret, place = getUSLocation(location)
        if(ret):
            for user in value:
                userId = user[0]
                time = user[1]
                print userId + ';' + time + ';' + place
        else:
            ret, place = getLocation(location)
            if(ret):
                for user in value:
                    userId = user[0]
                    time = user[1]
                    print userId + ';' + time + ';' + place



        