fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'words.txt'
fhand = open(fname)
words = dict()
line_no = 0
for line in fhand:
	line_no = line_no + 1
	print("This is line number", line_no)
	pieces = line.split()
	for word in pieces:
		if word not in words:
			words[word] = 1
		else:
			words[word] = words[word] + 1

print(words)