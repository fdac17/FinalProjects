import operator

es = {}
with open('emails.txt') as f:
	for line in f.readlines():
		line = line.strip('\n').strip(' ').lower()
		if '@' in line:
			email = line.split('@')[1]
			if email in es:
				es[email] += 1
			else:
				es[email] = 1
ess = sorted(es.items(), key=operator.itemgetter(1))

for key, val in ess:
	print('{:>15}: {}'.format(key, val))
