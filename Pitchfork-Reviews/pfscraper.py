import requests as req
import json
import sys
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

import genres

count = 0

def writeToFile(data):
    with open("reviews.json", 'a') as f:
        f.write(json.dumps(data, indent=4, separators=(',', ': ')))
        f.write(',')
        
def testQuery(key):
    table = dynamodb.Table("pitchfork_reviews")
    response = table.scan(
        FilterExpression=Attr('albumReleaseYear').eq(2005)
    )
    items = response["Items"]
    print(items)
    
def keyInTable(key):
    table = dynamodb.Table("pitchfork_reviews")
    response = table.get_item(
        Key={
            'artistNameAlbumName': key
        }
    )
    
    if ("Item" in response):
        return True
        
    else:
        return False
        
def writeToDynamodb(reviewInfo):
    table = dynamodb.Table("pitchfork_reviews")
    # print(table.creation_date_time)
    table.put_item(
        Item=reviewInfo
    )
        
def cleanReview(data):
    global count
    count += 1
    if (not count % 100):
        print(count)
        
    try:
        reviewInfo = {}
        reviewInfo["artistNameAlbumName"] = data["results"][0]["tombstone"]["albums"][0]["album"]["artists"][0]["display_name"] + ' - ' + data["results"][0]["tombstone"]["albums"][0]["album"]["display_name"]
        
        if (not keyInTable(reviewInfo["artistNameAlbumName"])):
            reviewInfo["artistName"] = data["results"][0]["tombstone"]["albums"][0]["album"]["artists"][0]["display_name"]
            reviewInfo["albumName"] = data["results"][0]["tombstone"]["albums"][0]["album"]["display_name"]
            reviewInfo["genre"] = data["results"][0]["genres"][0]["display_name"]
            reviewInfo["albumReleaseYear"] = data["results"][0]["tombstone"]["albums"][0]["album"]["release_year"]
            
            reviewInfo["url"] = data["results"][0]["url"]
            reviewInfo["authorName"] = data["results"][0]["authors"][0]["name"]
            reviewInfo["publishDate"] = data["results"][0]["pub_date"]
            reviewInfo["title"] = data["results"][0]["title"]
            reviewInfo["rating"] = data["results"][0]["tombstone"]["albums"][0]["rating"]["display_rating"]
            reviewInfo["body"] = data["results"][0]["body"]["en"]
            # print(json.dumps(reviewInfo, indent=4, separators=(',', ': ')))
            
            writeToDynamodb(reviewInfo)
            
        # else:
        #     print(reviewInfo["artistNameAlbumName"])
    
    except IndexError:
        print("!!----------!!")
        print(json.dumps(data, indent=4, separators=(',', ': ')))

def getReview(reviewLink):
    url = "https://pitchfork.com/api/v2" + reviewLink
    res = req.get(url)
    if (res.ok):
        data = json.loads(res.text)
        # rating = data["results"][0]["tombstone"]["albums"][0]["rating"]["rating"]
        # print(rating)
        # writeToFile(data)
        cleanReview(data)
        

def getReviews(artistLink):
    url = "https://pitchfork.com/api/v2/entities" + artistLink
    res = req.get(url)
    if (res.ok):
        data = json.loads(res.text)
        count = len(data["content"]["albumreviews"]["items"])
        # print(count)
        if count > 0:
            for i in range(0, count):
                # print(artistLink)
                reviewLink = data["content"]["albumreviews"]["items"][i]["url"]
                # print(reviewLink)
                getReview(reviewLink)

def getArtistLinks(genre, count):
    # print(count)
    for i in range(0, count):
        url = "https://pitchfork.com/api/v2/search/?sort=name%20asc&types=musicgroups&status=published&hierarchy=genres%2F" + genre + "&size=1&start=" + str(i)
        res = req.get(url)
        if (res.ok):
            data = json.loads(res.text)
            # print(json.dumps(data, indent=4, separators=(',', ': ')))
            artistLink = data["results"]["list"][0]["url"]
            # print(artistLink)
            getReviews(artistLink)

def getHtml():
    # with open("reviews.json", 'a') as f:
    #     f.write('[')
    
    for genre in  genres.genres:
        url = "https://pitchfork.com/api/v2/search/?sort=name%20asc&types=musicgroups&status=published&hierarchy=genres%2F" + genre + "&size=1&start=0"
        res = req.get(url)
        if (res.ok):
            data = json.loads(res.text)
            # print(json.dumps(data, indent=4, separators=(',', ': ')))
            # print(data["count"])
            getArtistLinks(genre, data["count"])
            
        else:
            print("error getting html")
            
    # with open("reviews.json", 'a') as f:
    #     f.write('done]')
            
getHtml()
# testQuery()
    