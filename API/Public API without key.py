import requests
import json

URL = [
    'https://catfact.ninja/breeds',
    'https://catfact.ninja/fact',
    'https://catfact.ninja/facts',
    'https://randomuser.me/api/'
]

resp = requests.get(url=URL[3])
print(json.dumps(resp.json(),indent=4))
