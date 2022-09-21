import requests
import json
import jsonpath


def test_add_new_data():
    app_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\ainam\\Desktop\\python\\request_json.txt", 'r')
    request_json = json.loads(f.read())
    response = requests.post(app_url, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open('C:\\Users\\ainam\\Desktop\\python\\techdetails.json.txt', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    f = open('C:\\Users\\ainam\\Desktop\\python\\address.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(add_api_url, request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)


