name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = dict()
semail = None
ecount = None
for line in handle:
    if line.startswith('From') and 'From:' not in line :
        sLine = line.split()
        emails[sLine[1]] = emails.get(sLine[1], 0) + 1

for email,count in emails.items():
    if ecount is None or count > ecount:
        semail = email
        ecount = count

print(semail, ecount)
