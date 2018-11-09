import requests
import json
import numpy as np
from gtts import gTTS
import os


lng = -117.2329987
lat = 32.8777024


userdata = {"device": {"mobileType": "ios", "uid": ":“123E6568-E89B-12D3-A456-426655440000"}, "grantType": "device"}
data = requests.post("https://web.spin.pm/api/v1/auth_tokens", json=userdata)

jsonload = data.json()
jsonload = json.dumps(jsonload)
jsonload = jsonload.split('"')
jwttoken = jsonload[3]

jsonget = requests.get("https://web.spin.pm/api/v3/vehicles?lng=-117.2329987&lat=32.8777024&distance=&mode=", headers={'Authorization': 'Bearer ' + jwttoken})
jsonloadget = jsonget.json()

jsonarray = json.dumps(jsonloadget).split("{")
ebikes = []
regbikes = []
print(jsonarray)
for i in jsonarray:
    if("ebike" in i):
        ebikes.append(i)
    elif("bike" in i):
        regbikes.append(i)

#print(ebikes, len(ebikes))
splitray = ebikes[0].split(" ")
print(regbikes)

# x = splitray
# x = map(str, x)
# x = list(x)
# print(x)
# y = []
# for i in splitray:
#     i.replace
#     y.append(i)
# print(y)

# while True:
#     for i in ebikes:
#         splitray


if(len(ebikes) > 1):
    mytext = str(len(ebikes)) + 'E-Bikes Nearby'
elif(len(ebikes) == 1):
    mytext = str(len(ebikes)) + 'E-Bike Nearby'
else:
    mytext = 'No E-Bikes Nearby'

myobj = gTTS(text=mytext, slow=False)
myobj.save("owo.mp3")
os.system("owo.mp3")
