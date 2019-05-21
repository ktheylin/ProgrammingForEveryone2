score = -1

while score == -1:
    try:
        score = input("\nEnter score between 0.0 and 1.0: ")
        score = float(score)
    except:
        print ("\nEntered score is not numeric, please enter a score between 0.0 and 1.0")
        score = -1
        continue

    if score < 0.0 or score > 1.0:
        print ("\nThe score entered is not in the range between 0.0 and 1.0")
        score = -1

if score < 0.6:
    print ("F")
elif score <0.7:
    print ("D")
elif score <0.8:
    print ("C")
elif score <0.9:
    print ("B")
else:
    print ("A")
