hours = -1
rate = -1

while hours == -1:
    try:
        hours = input("Enter Hours: ")
        hours = float(hours)
    except:
        print("Please enter a numberic value for hours")
        hours = -1

while rate == -1:
    try:
        rate = input("Enter Rate: ")
        rate = float(rate)
    except:
        print("Please enter a numberic value for rate")
        rate = -1

pay = hours * rate
print("\nPay:", pay)