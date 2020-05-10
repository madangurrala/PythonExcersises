fName = input('Enter the file name')

try:
    fContent = open(fName)
except:
    print('Please enter correct filename', fName)
    quit()

count = 0
total = 0
average = 0

for line in fContent:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    index = line.find(':')
    value = float(line[index+1:].strip())
    total += value
    count += 1
    print(line, value, total, count)

average = total/count

print('Average spam confidence:',average)
