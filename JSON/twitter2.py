import urllib.request, urllib.parse, urllib.error
import json
import ssl
import twurl

#Ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#This URL check the account user's friends
twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    account = input('Enter account name:')
    if (len(account) < 1) : break
    url = twurl.augment(twitter_url, {'screen_name': account, 'count': '10'})
    print('Retrieving URL:', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    #print(json.dumps(js, indent=4))

    for user in js['users']:
        print(user['screen_name'])
        s = user['status']['text']
        print('  ', s[:50])
