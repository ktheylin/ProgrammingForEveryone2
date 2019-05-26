try:
    fh = open("mbox-short.txt")
except:
    print('File mbox-short.txt does not exsist')
    exit()

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
        