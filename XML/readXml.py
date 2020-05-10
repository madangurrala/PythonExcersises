import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SLL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_386453.xml'
fileHandler = urllib.request.urlopen(url, context=ctx).read().decode()

xmlTree = ET.fromstring(fileHandler)
dataList = xmlTree.findall('.//count')
numbers = list()
for element in dataList:
    numbers.append(int(element.text))

print(sum(numbers))
