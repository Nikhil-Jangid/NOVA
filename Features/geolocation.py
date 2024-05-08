import requests
import json

def city():
    response = requests.get('http://ip-api.com/json')
    data = json.loads(response.text)
    return data['city']

#print("City:", city())
