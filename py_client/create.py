import requests

endpoint = "https://hng-task-1-2xlb.onrender.com/api/"

data = {
    'username':'tim',
    'email':'tim@gmail.com',
    'password1':'dimeji2005',
    'password2':'dimeji2005',
}

get_response = requests.post(endpoint, json=data )

print(get_response.json())


  