fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)
from_count = dict()
line_no = 0
for line in fhand:
	line = line.strip()
	if len(line) != 0:
		pieces = line.split()
	if pieces[0] != "From":
		continue
	else:
		sender = pieces[1]
		from_count[sender] = from_count.get(sender,0) + 1
user = ""
count = 0
for key, value in from_count.items():
	if value > count:
		count = value
		user = key

print(user, count)