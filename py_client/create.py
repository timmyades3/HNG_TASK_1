import requests

endpoint = "http://localhost:8000/api/"

data = {
    'name':'tim'}

get_response = requests.post(endpoint, json=data )

print(get_response.json())


  