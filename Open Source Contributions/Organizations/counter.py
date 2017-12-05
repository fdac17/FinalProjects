
fname = "wvaugha2_labeled.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

m = 0 
y = 0
n = 0

mi = 0 
yi = 0
ni = 0

imp = []

for c in content:
	if int(c[-3]) > 1:
		imp.append(c)

for c in content:

	if c[-1:] == ('m' or '2'):
		m = m+1
	elif c[-1:] == ('y' or '1'):
		y =y +1
	else:
		n = n+1

print "May be: ", m/float(len(content)) * 100
print "Yes: ", y/float(len(content)) * 100
print "No: ", n/float(len(content)) * 100

for i in imp:
	if i[-1:] == ('m' or '2'):
		mi = mi+1
	elif i[-1:] == ('y' or '1'):
		yi =yi +1
	else:
		ni = ni+1
print "\n"
print "May be: ", mi/float(len(imp)) * 100
print "Yes: ", yi/float(len(imp)) * 100
print "No: ", ni/float(len(imp)) * 100
