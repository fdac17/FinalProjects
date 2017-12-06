import requests
from github import Github
import json

g = Github("", "")
print(g.get_rate_limit())

with open("since.txt", "r") as f1:
	since = int(f1.read())
	print(since)
	with open("emails.txt", "a") as f2:
		try:
			for user in g.get_users(since=since):
				if user.email != None:
					f2.write(user.email + '\n')
					print(user.email)
		except:
			since += 5000
			f1.write(str(since))
