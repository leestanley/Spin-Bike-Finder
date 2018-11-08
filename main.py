import requests
import json
import numpy as np
from gtts import gTTS


userdata = {"device": {"mobileType": "ios", "uid": ":“123E6567-E89B-12D3-A456-426655440000"}, "grantType": "device"}
data = requests.post("https://web.spin.pm/api/v1/auth_tokens", json=userdata)

jsonload = data.json()
jsonload = json.dumps(jsonload)
jsonload = jsonload.split('"')
jwttoken = jsonload[3]

jsonget = requests.get("https://web.spin.pm/api/v3/vehicles?lng=-117.2329987&lat=32.8777024&distance=&mode=", headers={'Authorization': 'Bearer ' + jwttoken})
jsonloadget = jsonget.json()

#print(json.dumps(jsonloadget, indent=4, sort_keys=True))

jsonarray = json.dumps(jsonloadget).split("{")
ebikes = []
for i in jsonarray:
    if("ebike" in i):
        ebikes.append(i)

# print(jsonarray)


print(ebikes, len(ebikes))
# while True:
#     for i in ebikes:
