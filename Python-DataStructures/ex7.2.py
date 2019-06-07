fname = input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('File mbox-short.txt does not exsist')
    exit()

count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pieces = line.split(":")
    r_side=pieces[1]
    count = count +1
    total = total + float(r_side)
    
print("Average spam confidence:", total / count)

        