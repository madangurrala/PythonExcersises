fname = input("Enter File name:")
try:
    file = open(fname)
except:
    print('Enter correct file name', fname)
    quit()

words = list()

for line in file:
    ewordList = line.rstrip().split()
    for word in ewordList:
        if word not in words:
            words.append(word)

words.sort()
print(words)
