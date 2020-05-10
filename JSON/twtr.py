import urllib.request, urllib.parse, urllib.error
import json
import ssl
from twurl import augment

#Ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'madan_gurrala', 'count': '0'})
print(url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
headers = dict(connection.getheaders())
js = json.loads(data)
print(json.dumps(js, indent = 3))
print('========================')
print(headers)
