import requests

data = {'value': 42}
#response = requests.post('http://<raspberry-pi-ip>:8000/api/data', json=data)
response = requests.post('http://192.168.195.190:80/api/data', json=data)

print(response.json())