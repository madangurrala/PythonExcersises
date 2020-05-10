largestNum = -1
smallestNum = None

while True:
    number = input('Enter a Number')

    if number != 'done':
        try:
            intNum = int(number)
        except:
            print('Invalid input')

        if intNum > largestNum:
            largestNum = intNum

        if smallestNum is None:
            smallestNum = intNum

        elif intNum < smallestNum:
            smallestNum = intNum
    else:
        break

print('Maximum is', largestNum)
print('Minimum is', smallestNum)
