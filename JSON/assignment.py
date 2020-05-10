import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_386454.json'
data = urllib.request.urlopen(url, context=ctx).read().decode()
jsonData = json.loads(data)
numbers = list()
#print(json.dumps(jsonData, indent=2))
for cmt in jsonData['comments']:
    numbers.append(int(cmt['count']))

print(sum(numbers))
