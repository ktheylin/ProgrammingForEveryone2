fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)
from_email = dict()
line_no = 0
for line in fhand:
	line_no = line_no + 1
	#print("This is line number", line_no)
	pieces = line.split()
    if pieces[0] != "From":
        continue
    else
        from = pieces[1]
	for word in pieces:
		if word not in words:
			words[word] = 1
		else:
			words[word] = words[word] + 1

print(words)