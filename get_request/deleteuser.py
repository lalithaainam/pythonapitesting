import requests

# api url
url = "https://reqres.in/api/users/2"
# deleting
response = requests.delete(url)
# print(response)
# fetch response code
print(response.status_code)
# validating status code
assert response.status_code == 204
