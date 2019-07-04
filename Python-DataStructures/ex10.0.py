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
		
			
#print(word_count)

count = -1
theword = None
tmp = list()

for key, value in word_count.items():
	#print(key, value)
	flip_word_count = (value, key)
	tmp.append(flip_word_count)

tmp = sorted(tmp, reverse=True)
for value, key in tmp[:5] :
	print(key, value)
	