import requests

# api url
url = "https://reqres.in/api/users?page=2"
# sending get request
response = requests.get(url)
print(response)
# display response content
# print(response.content)
# print(response.headers)
# validate status code
print(response.status_code)
assert response.status_code == 200
# fetch response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))
# fetch cookies
print(response.cookies)
# fetch encoding
print(response.encoding)
# fetch elapsed time
print(response.elapsed)


