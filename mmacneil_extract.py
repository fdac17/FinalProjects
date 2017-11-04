import pymongo, json, sys


client = pymongo.MongoClient (host="da1")
db = client ['NPM_packages']
id = "mmacneil"

coll = db [ 'npms_' + id]

has = set ()
for r in coll.find():
  nMnt = 0;
  if 'maintainers' in r ['collected']['metadata']:
    nMnt = len(r ['collected']['metadata']['maintainers'])
  nDev = 0;
  if 'devDependencies' in r ['collected']['metadata']:
    nDev = len(r ['collected']['metadata']['devDependencies'])
  nR = 0;
  if 'releases' in r ['collected']['metadata']:
    for rl in r ['collected']['metadata']['releases']:
      nR =+ rl ['count']
  nDn = 0
  if 'npm' in r['collected']:
    for dn in r['collected']['npm']['downloads']:
      nDn =+ dn ['count']
  
  data = r['collected']['metadata']['name'];
  if 'date' in r['collected']['metadata']:
    data += ';' + r['collected']['metadata']['date']
  else:
    data += ';'
  if 'scope' in r['collected']['metadata']:
    data += ';' + r['collected']['metadata']['scope']
  else:
    data += ';'
  if 'npm' in r['collected']:
    data += ';' + str(r['collected']['npm']['starsCount']) +';'+ str(r['collected']['npm']['dependentsCount'])
  else:
    data += ';;'
  data += ';' + \
     str(r['score']['final']) +';'+ str(r['score']['detail']['quality'])+';'+ str(r['score']['detail']['popularity'])+';'+ str(r['score']['detail']['maintenance']) +';'+\
     str(r['evaluation']['quality']['health'])+';'+  str(r['evaluation']['quality']['branding'])+';'+  str(r['evaluation']['quality']['tests'])+';'+  str(r['evaluation']['quality']['carefulness'])+';'+\
     str(r['evaluation']['popularity']['downloadsCount'])+';'+  str(r['evaluation']['popularity']['downloadsAcceleration'])+';'+\
     str(r['evaluation']['popularity']['communityInterest'])+';'+  str(r['evaluation']['popularity']['dependentsCount'])+';'+\
     str(r['evaluation']['maintenance']['releasesFrequency'])+';'+  str(r['evaluation']['maintenance']['issuesDistribution'])+';'+\
     str(r['evaluation']['maintenance']['openIssues'])+';'+  str(r['evaluation']['maintenance']['commitsFrequency']) +';'+\
     str(nMnt) +';'+ str(nDev) +';'+ str(nR) +';'+ str(nDn)
  if 'source' in r['collected']:
    data += ';' +  str(r['collected']['source']['files']['testsSize']) +';'+ str(r['collected']['source']['files']['readmeSize'])
  else:
    data += ';;'
  if  'hasTestScript' in  r['collected']['metadata']:
    data += ';' + str(r['collected']['metadata']['hasTestScript'])
  else:
    data += ';'
  print (data)




