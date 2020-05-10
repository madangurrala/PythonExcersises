import urllib.request, urllib.parse, urllib.error
import ssl
import json

#ignore ssl error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    serviceURL = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceURL = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Address:')
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceURL + urllib.parse.urlencode(parms)
    print('Retrieving URL', url)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    jsData = json.loads(data)
    #print(json.dumps(jsData, indent=3))
    for components in jsData['results']:
        print(components['place_id'])
