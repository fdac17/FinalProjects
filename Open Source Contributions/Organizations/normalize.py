import re
lines = []
for filename in ['abrelsfo_labeled.txt']:
	with open(filename, 'r') as f:
		for line in f.readlines():
			line = line.strip(' ').strip('\n').split(':')
			if not line[2]:
				line[2] = '3'
			
			if line[0].endswith('.me') or line[0].endswith('.name'):
				line[2] = '3'
				
			if not re.match(r'.*\..*', line[0]):
				line[2] = '3'

			lines.append(line)

with open('combined.txt', 'w') as f:
	for line in lines:
		print(line)
		line = ':'.join(line)
		line += '\n'
		f.write(line)
