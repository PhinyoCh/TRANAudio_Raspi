import requests
url = 'http://192.168.1.9:5000/connection'
myobj = {'key': 'hello from raspi'}

x = requests.post(url, myobj)

# print the response text (the content of the requested file):

print(x.text)