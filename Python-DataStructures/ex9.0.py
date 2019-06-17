fname = input('Enter a filename: ')
if len(fname) < 1: fname = 'clown.txt'

fhand = open(fname)

word_count = dict()
line_no = 0

for line in fhand:
	line = line.rstrip()
	words = line.split()
	for word in words:
		word_count[word] = word_count.get(word,0) + 1
		
			
count = -1
theword = None

for key, value in word_count.items():
	if value > count:
		count = value
		theword = key

print(theword, count)