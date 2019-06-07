fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'words.txt'
fhand = open(fname)
words = dict()
for line in fhand:
	pieces = line.split()
	for word in pieces:
		if word not in words:
			words[word] = 1
		else:
			words[word] = words[word] + 1

print(words)