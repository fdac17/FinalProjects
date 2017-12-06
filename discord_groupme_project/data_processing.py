import pymongo
from datetime import datetime
import time

groups = ['literal_cancer', 'clown_fiesta', 'officers', 'overwatch']
group_names = {'literal_cancer':'Anime', 'clown_fiesta':'League of Legends', 'officers':'Officers', 'overwatch':'Overwatch'}

client = pymongo.MongoClient('da1.eecs.utk.edu')
db = client['kye2']

#function to grab data from a certain range
#@param[in] date_start is a datetime object denoting the start of the range
def get_data_range(date_start, date_end, db_name):
	coll = db[db_name]
	#test code
	#print(coll.find({'created_at': {'$gte':int(datetime(2017, 10, 31, 15, 45, 2).strftime('%s'))}}))
	#print(time.strptime('2017-10-31 15:45:02', '%y-%m-%d %H:%M:%S').strftime('%s'))
	print(datetime(2017, 10, 31, 15, 45, 2).strftime('%s'))
	#the magic line that grabs the entries from the database between the two dates and throws it into a list
	dates = list(coll.find( {'created_at': {'$gte': int(date_start.strftime('%s')), '$lt':int(date_end.strftime('%s'))}}))
	#user feedback prints date range and entry count
	print(str(len(dates)) + " entries.")
	print("From: " + str(datetime.fromtimestamp(dates[0]['created_at'])) + " To: " + str(datetime.fromtimestamp(dates[len(dates)-1]['created_at'])))
	return dates
	
#@param[in] data is the list of entries from the date range
def group_by_day(data):
	days = {}
	for d in data:
		#debug code
		#print(int(datetime.fromtimestamp(d['created_at']).strftime('%d')))
		day = int(datetime.fromtimestamp(d['created_at']).strftime('%d'))
		#print(day)
		if day in days:
			days[day].append(d)
		else:
			days[day] = []
			days[day].append(d)
	return days

#@param[in] data is the list of entries from the date range
def group_by_hour(data):
	days = {}
	for d in data:
		#debug code
		#print(int(datetime.fromtimestamp(d['created_at']).strftime('%d')))
		day = int(datetime.fromtimestamp(d['created_at']).strftime('%H'))
		#print(day)
		if day in days:
			days[day].append(d)
		else:
			days[day] = []
			days[day].append(d)
	return days

#start = datetime(2017, 11, 1, 0, 0, 0)
#end = datetime(2017, 11, 30, 23,59, 59)
#data = get_data_range(start, end, groups[0])
#print(group_by_hour(data).keys())
