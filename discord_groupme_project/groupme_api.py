import requests
import json
import sys
import datetime
import pymongo

token = "ccd839e00aae013598855f61481f1a55"
quidditch = "24005147"
literal_cancer = "16943627"
clown_fiesta = "25519348"
overwatch = "22929552"
officers = "16582942"

msg_limit = 100

#initialize mongodb
client = pymongo.MongoClient(host="da1.eecs.utk.edu")
db = client['kye2']
#coll = db['groupme_data']

#data a response data structure
def insert_data(r):
#	print("entries: " + str(len(r['response']['messages'])))
	for m in r['response']['messages']:
		r1 = {}
		r1['text'] = m['text']
		r1['uid'] = m['sender_id']
		r1['id'] = m['id']
		r1['created_at'] = m['created_at']
		#print(r1['created_at'])
		coll.update(r1, r1, upsert=True)

#given the group_id return the group's messages for the month of November
#@param[in] group_id is a string with the groupid integer
def get_group(group_id):
	url = "https://api.groupme.com/v3/groups/" + group_id + "/messages?limit=" + str(msg_limit) + "&token="+token
	response = requests.get(url)
	text = response.text
	r = json.loads(text)
	#print(json.dumps(r['response']['messages'], indent=4, sort_keys=True))
	last_id = r['response']['messages'][msg_limit-1]['id']
	#print(last_id)
	insert_data(r)
	
	#test code
	'''url = "https://api.groupme.com/v3/groups/" + group_id + "/messages?limit=" + str(msg_limit) + "&token="+token + "&before_id=" + str(last_id)
	response = requests.get(url)
	text = response.text
	r = json.loads(text)
	#print(json.dumps(r['response']['messages'], indent=4, sort_keys=True))
	print(json.dumps(r['response']['messages'][msg_limit-1]['text']))'''
	#end test code

	#main loop
	while True:
		#test if message was posted before November
		last_date = datetime.datetime.fromtimestamp(r['response']['messages'][msg_limit-1]['created_at'])
		#print(datetime.datetime.fromtimestamp(r['response']['messages'][msg_limit-1]['created_at']))
		#print(last_date.month)
		if last_date.month < 11:
			#if so break the loop
			break;

		url = "https://api.groupme.com/v3/groups/" + group_id + "/messages?limit=" + str(msg_limit) + "&token="+token + "&before_id=" + str(last_id)
		response = requests.get(url)
		text = response.text
		r = json.loads(text)
		last_id = r['response']['messages'][msg_limit-1]['id']
		insert_data(r)
		
coll = db['quidditch']
get_group(quidditch)
print("collection has: " + str(coll.count()) + " entries")

coll = db['literal_cancer']
get_group(literal_cancer)
print("collection has: " + str(coll.count()) + " entries")

coll = db['clown_fiesta']
get_group(clown_fiesta)
print("collection has: " + str(coll.count()) + " entries")

coll = db['officers']
get_group(officers)
print("collection has: " + str(coll.count()) + " entries")

coll = db['overwatch']
get_group(overwatch)
print("collection has: " + str(coll.count()) + " entries")

client.close()
