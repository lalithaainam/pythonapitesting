import json
import requests
import jsonpath


def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(token_url, data)
    print(response.text)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer' + token_value[0]}
    api_url = "https://thetestingworldapi.com/api/studentsDetails/1104"
    response = requests.get(api_url, headers=auth)
    print(response.text)
