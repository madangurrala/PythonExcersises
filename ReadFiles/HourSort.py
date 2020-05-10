name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
hoursList = list()
for line in handle:
    if line.startswith('From') and 'From:' not in line :
        sLine = line.split()
        time = sLine[5].split(':')
        hours[time[0]] = hours.get(time[0], 0)+1

hoursList = sorted([(hour, count) for hour, count in hours.items()])

for hour, count in hoursList:
    print(hour, count)
