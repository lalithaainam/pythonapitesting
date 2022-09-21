import jsonpath
import json
import requests
import pytest

# api url
url = "https://reqres.in/api/users"


# a = 100


# @pytest.mark.skipif(a > 10, reason="condition is not satisfied")
@pytest.fixture(scope='module')
def start_execution():
    global file
    file = open('C:\\Users\\ainam\\Desktop\\python\\createnewuser.txt', 'r')


@pytest.mark.smoke
def test_create_new_user(start_execution):
    # read input json file
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201


@pytest.mark.sanity
def test_create_other_user(start_execution):
    # read input json file
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
