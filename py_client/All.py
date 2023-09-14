import requests

request_type=input('Ener your request method eg post,get,put,delete > ')
request_type=request_type.lower()
if request_type == 'get':
  endpoint= input('Enter your endpoint > ')
  get_response = requests.get(endpoint)
  print(get_response.json()) 
  print(f'status code : {get_response.status_code}')
elif request_type == 'post':
    endpoint= input('Enter your endpoint > ')
    name = input('enter your name > ')
    data={
       'name':name
    }
    get_response = requests.post(endpoint, json=data)
    print(get_response.json()) 
    print(f'status code : {get_response.status_code}')
elif request_type == 'put':
    endpoint= input('Enter your endpoint > ')
    name = input('update your name > ')
    data={
       'name':name
    }
    get_response = requests.put(endpoint, json=data)
    print(get_response.json()) 
    print(f'status code : {get_response.status_code}')
elif request_type == 'patch':
    endpoint= input('Enter your endpoint > ')
    name = input('update your name > ')
    data={
       'name':name
    }
    get_response = requests.patch(endpoint, json=data)
    print(get_response.json()) 
    print(f'status code : {get_response.status_code}')
elif request_type == 'delete':
    endpoint= input('Enter your endpoint > ')
    get_response = requests.delete(endpoint)
    print(f'status code : {get_response.status_code,get_response.status_code==204}')
else:
    print('request_type is invalid')    