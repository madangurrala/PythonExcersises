import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Madan</name>
    <phone type="intl">
        +1 123 456 7890
    </phone>
    <email hide="yes"/>
</person>'''

#tree object
tree = ET.fromstring(data)
print('Name:', tree.find('name').text )
print('Attr:', tree.find('email').get('hide'))


input = '''
<data>
    <users>
        <user x="3">
            <id>01</id>
            <name>Madan</name>
        </user>
        <user x="5">
            <id>02</id>
            <name>Brent</name>
        </user>
    </users>
</data>
'''

xmldata = ET.fromstring(input)

#fidall returns list
datalist = xmldata.findall('users/user')
print('Users count:', len(datalist))
for person in datalist:
    print('Id:', person.find('id').text)
    print('Name:', person.find('name').text)
