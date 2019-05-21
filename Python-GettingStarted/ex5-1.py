count = 0
total = 0

while True :
    sval = input('Enter a number or done to quit: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + fval

print ("Count =", count, "Total =", total, "Average =", total/count)
