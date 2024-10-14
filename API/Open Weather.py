import requests
import json

API_KEY = ""
CITY = ""
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
resp = requests.get(URL)
try:
    with open("data.json","w") as f:
        f.write(str(resp.json()))
        #json.dump(resp.json(),f,indent=4)
except Exception as e:
    with open("data.json","w") as f:
        f.write(str(e))
        #json.dump(e, f, indent=4)
