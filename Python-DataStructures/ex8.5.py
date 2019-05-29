fname = input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)

count = 0

for line in fhand:
    if not line.startswith("From "): 
        continue
    pieces = line.split()
    count = count + 1
    print(pieces[1])

print("There were", count, "lines in the file with From as the first word")