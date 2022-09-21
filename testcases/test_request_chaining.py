import json
import requests
import jsonpath


def test_add_new_student():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/ainam/Desktop/python/addstudent.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(api_url, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_get_details():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(api_url)
    print(response.text)