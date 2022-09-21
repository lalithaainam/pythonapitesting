import requests
header_data = {'t1': 'first_header', 't2': 'second_header'}
response = requests.get('https://httpbin.org/get', headers=header_data)
print(response.text)
