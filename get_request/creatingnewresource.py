import json
import requests
import jsonpath

# api url
url = "https://reqres.in/api/users"
# read input json file
file = open('C:\\Users\\ainam\\Desktop\\python\\createnewuser.txt', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
# print(request_json)
# make post requests to json input body
response = requests.post(url, request_json)
print(response.content)
# validating response code
assert response.status_code == 201
# fetch header from response
print(response.headers.get('Content-Type'))
# parse response to json format
response_json = json.loads(response.text)
print(response_json)
# pick id using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
