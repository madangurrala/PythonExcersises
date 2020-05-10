fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

file = open(fname)
count = 0
for line in file:
    if line.startswith('From') and 'From:' not in line :
        sLine = line.split()
        print(sLine[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
