import sys
import requests
import json
import datetime
import pymongo

quidditch = "16943627"
literal_cancer = "16943627"
clown_fiesta = "25519348"
overwatch = "22929552"
officers = "16582942"

url = 'https://api.groupme.com/v3/groups/24005147/messages?token=ccd839e00aae013598855f61481f1a55'

#initialize database instance
client = pymongo.MongoClient(host="da1.eecs.utk.edu")
db = client['kye2']
coll = db['kye2_test']

#make the get request
response = requests.get(url)
print(response.encoding)
print(response)
text = response.text
str_response = response.content.decode('utf-8')
if response.ok:
	r = json.loads(text)
	#print(r['response']['messages'][0]['created_at'].encode('utf8'))
	#get time of message and convert to more readable date time format
	print(datetime.datetime.fromtimestamp(r['response']['messages'][0]['created_at']).month)
	r1 = {}
	r1['text'] = r['response']['messages'][0]['text']
	r1['uid'] = r['response']['messages'][0]['sender_id']
	r1['created_at'] = r['response']['messages'][0]['created_at']
	coll.update(r1, r1, upsert=True)

	#sys.stdout.buffer.write(r['response'])
	#sys.stdout.buffer.write(r)

client.close()
print("Connection to client closed")
