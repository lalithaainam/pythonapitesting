import requests
import json
import jsonpath
import openpyxl
from datadriven import library


def test_add_multiple_students():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/ainam/Desktop/python/addnewjson.txt', 'r')
    request_json = json.loads(f.read())

    obj = library.Common('filepath', 'sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, request_json, keylist)
        response = requests.post(api_url, updated_json_request)
        print(response.text)



