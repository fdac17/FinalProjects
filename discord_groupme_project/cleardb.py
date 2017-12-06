import pymongo
client = pymongo.MongoClient(host="da1.eecs.utk.edu")
db = client['kye2']
coll = db['quidditch']
print("entries: " + str(coll.count()))
coll.delete_many({})
print("entries: " + str(coll.count()))

coll = db['literal_cancer']
print("entries: " + str(coll.count()))
coll.delete_many({})
print("entries: " + str(coll.count()))

coll = db['clown_fiesta']
print("entries: " + str(coll.count()))
coll.delete_many({})
print("entries: " + str(coll.count()))

coll = db['officers']
print("entries: " + str(coll.count()))
coll.delete_many({})
print("entries: " + str(coll.count()))

coll = db['overwatch']
print("entries: " + str(coll.count()))
coll.delete_many({})
print("entries: " + str(coll.count()))

