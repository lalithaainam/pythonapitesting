import requests
import json
import jsonpath
import pytest


@pytest.mark.smoke
def test_fetch_user_details():
    # api url
    url = "https://reqres.in/api/users?page=2"
    # sending get request
    response = requests.get(url)
    print(response.content)
    # parse response to json format
    json_response = json.loads(response.text)
    print(json_response)
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print(first_name[0])
