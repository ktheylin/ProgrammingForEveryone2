fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)
hour_count = dict()
line_no = 0
for line in fhand:
	line = line.strip()
	if len(line) != 0:
		pieces = line.split()
	if pieces[0] != "From":
		continue
	else:
		time = pieces[5]
		pieces = time.split(":")
		hour = pieces[0]
		#print(hour)
		hour_count[hour] = hour_count.get(hour,0) + 1
#print(hour_count)

tmp = list()

for key, value in hour_count.items():
	#print(key, value)
	tmp_dict = (key,value)
	tmp.append(tmp_dict)

tmp = sorted(tmp)

for key, value in tmp :
	print(key, value)