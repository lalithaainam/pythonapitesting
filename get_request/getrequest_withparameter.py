import requests
param = {'name': 'lali', 'email': 'lalitha28@gmail.com', 'number': '+1-909-357-8670'}
response = requests.get('https://httpbin.org/get', params=param)
print(response.text)
