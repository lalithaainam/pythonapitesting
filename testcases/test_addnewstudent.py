import requests
import json
import jsonpath


def test_add_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\ainam\\Desktop\\python\\request.json.txt', 'r')
    json_request = json.loads(f.read())
    response = requests.post(api_url, json_request)
    print(response.text)


def test_update_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/3845068"
    f = open('C:\\Users\\ainam\\Desktop\\python\\request_json.txt', 'r')
    json_request = json.loads(f.read())
    response = requests.put(api_url, json_request)
    print(response.text)


def test_delete_student_date():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/3845068"
    response = requests.delete(api_url)
    print(response.text)


def test_get_student_date():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/3845068"
    response = requests.get(api_url)
    json_response = json.loads(response.text)  # or can write response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 3845068
