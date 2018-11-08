import requests
import json
userdata = {"device": {"mobileType": "ios", "uid": ":“123E5567-E89B-12D3-A456-426655440000"}, "grantType": "device"}
data = requests.post("https://web.spin.pm/api/v1/auth_tokens", json=userdata)

jsonload = data.json()
jsonload = json.dumps(jsonload)
# print(jsonload)
jsonload = jsonload.split('"')

jwttoken = jsonload[3]

jsonget = requests.get("https://web.spin.pm/api/v3/vehicles?lng=-117.2329987&lat=32.8777024&distance=&mode=", headers={'Authorization': 'Bearer ' + jwttoken})
jsonloadget = jsonget.json()
jsonloadget = json.dumps(jsonloadget)

print(jsonloadget)
