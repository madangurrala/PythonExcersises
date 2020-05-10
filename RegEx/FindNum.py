import re

fileName = input("Enter file name:")
try:
    if len(fileName) < 1 : fileName = 'regex_sum_386449.txt'
    fileHandler = open(fileName)
except:
    print('Incorrect File Name', fileName)
    quit()

numbers = list()
for line in fileHandler:
    number = re.findall('[0-9]+', line)
    for num in number:
        numbers.append(int(num))

print(sum(numbers))
