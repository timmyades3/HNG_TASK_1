import requests

endpoint = "http://localhost:8000/api/"
data = {
  'name':"timmy"
}
get_response = requests.get(endpoint,params=data )

print(get_response.json()) 