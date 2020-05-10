hours = input('Enter number of hours')
pay = input('Enter rate per hour')
hrs = float(hours)
payf = float(pay)

if hrs > 40:
    extraHrs = hrs - 40
    extraPay = extraHrs * (payf * 1.5)
    grosspay = (hrs-extraHrs) * payf + extraPay
else:
    grosspay = hrs * payf

print(grosspay)
