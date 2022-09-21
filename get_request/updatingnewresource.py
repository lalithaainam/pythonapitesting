import json
import requests
import jsonpath

# api url
url = "https://reqres.in/api/users/2"
# read input json file
file = open('C:\\Users\\ainam\\Desktop\\python\\createnewuser.txt', 'r')
json_input = file.read()
request_json = json.loads(json_input)
# print(request_json)
# make put requests to json input body
response = requests.put(url, request_json)
# print(response.content)
# validating response code
assert response.status_code == 200
# parse response to json format
response_json = json.loads(response.text)
print(response_json)
# pick updatedat using json path
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
