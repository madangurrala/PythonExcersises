def computepay(hours, pay):
    if hours > 40:
        extraHrs = hours - 40
        extraPay = extraHrs * (pay * 1.5)
        grosspay = (hours-extraHrs) * pay + extraPay
        return grosspay
    else:
        grosspay = hours * pay
        return grosspay

hoursStr = input('Enter number of hours')
payStr = input('Enter rate per hour')
hours = float(hoursStr)
pay = float(payStr)

print("Pay",computepay(hours, pay))
