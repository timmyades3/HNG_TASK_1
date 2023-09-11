import requests


endpoint = "http://localhost:8000/api/tim/"

data={
  # 'title' : 'hello world my old friend',
  # 'price' : 129.99
  'name':'manictim'

}
get_response = requests.put(endpoint , json = data)

print(get_response.json())


  