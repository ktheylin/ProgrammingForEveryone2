
def compute_pay(hours,rate):
    if hours > 40:
        reg_pay = 40 * rate
        overtime_pay = (hours % 40) * (rate * 1.5)
        total_pay = reg_pay + overtime_pay
    else:
        total_pay = hours * rate
        
    return(total_pay)
        

hours = -1
rate = -1

while hours == -1:
    try:
        hours = input("Enter hours worked: ")
        hours = float(hours)
    except:
        print("Entry was not numeric, please enter a numeric value")
        hours = -1
        continue

while rate == -1:
    try:
        rate = input("Enter hourly rate: ")
        rate = float(rate)
    except:
        print("Entry was not numeric, please enter a numeric value")
        rate = -1
        continue

pay = compute_pay(hours, rate)
print(pay)