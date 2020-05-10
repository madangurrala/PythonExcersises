import json

input= '''
{
    "name" : "Madan",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 456 7890"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(input)
#info is a dictionary. If the data was a list of JSON objects then it would be a list of dictionaries
print('Name:', info['name'])
print('Hide:', info['email']['hide'] )
