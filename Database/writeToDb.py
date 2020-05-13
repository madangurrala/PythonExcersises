from urllib.request import Request, urlopen
import ssl
import sqlite3

#Ignore SLL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Database connection
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')
url = 'https://www.py4e.com/code3/mbox.txt'
try:
    req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    response = urlopen(req, context=ctx)
except:
    print('Can not open URL', url)
    quit()

for lines in response:
    line = lines.decode().strip()
    if line.startswith('From') and 'From:' not in line :
        email = line.split()
        pos = email[1].find('@')
        domain = email[1][pos+1:]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()
