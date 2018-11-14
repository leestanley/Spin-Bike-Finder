import requests
import json
import numpy as np
#from gtts import gTTS
import os
#import time
from geopy.distance import geodesic

lng = -117.2329987
lat = 32.8777024


userdata = {"device": {"mobileType": "ios", "uid": ":“123E6568-E89B-12D3-A456-426655440000"}, "grantType": "device"}
data = requests.post("https://web.spin.pm/api/v1/auth_tokens", json=userdata)
print(data)
jsonload = data.json()
jsonload = json.dumps(jsonload)
jsonload = jsonload.split('"')
jwttoken = jsonload[3]

jsonget = requests.get("https://web.spin.pm/api/v3/vehicles?lng=-117.2329987&lat=32.8777024&distance=&mode=", headers={'Authorization': 'Bearer ' + jwttoken})
jsonloadget = jsonget.json()

jsonarray = json.dumps(jsonloadget).split("{")
ebikes = []
regbikes = []
for i in jsonarray:
    if("ebike" in i):
        ebikes.append(i)
    elif("bicycle" in i):
        regbikes.append(i)
splitray = ebikes[0].split(" ")
print(splitray)
finalray = []
for i in splitray:
    if "." in i:
        j = i.replace(",", "")
        finalray.append(float(j))
finalray.append(32.123232)
finalray.append(-120.23232)
print(finalray)

tuplefinalray = []
for i in np.arange(0, len(finalray), 2):
    tuplefinalray.append([finalray[i], finalray[i + 1]])

print(len(ebikes))
print(tuple(map(tuple, tuplefinalray)))


def voice():
    if(len(ebikes) == 1):
        # mytext = str(len(ebikes)) + 'E-Bikes Nearby and'
        # ortext = str(len(regbikes)) + "Bicycles Nearby"
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/1.m4a")
    elif(len(ebikes) == 2):
        # mytext = str(len(ebikes)) + 'E-Bike Nearby'
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/2.m4a")
    elif(len(ebikes) == 3):
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/3.m4a")
    elif(len(ebikes) == 4):
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/4.m4a")
    elif(len(ebikes) == 5):
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/5.m4a")
    elif(len(ebikes) > 5):
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/nearby.m4a")
    else:
        os.system("C:/Users/Stanley/Desktop/Spin-Bike-Finder/haojin/none.mp3")


#print(geodesic(base, cleveland_oh).miles)

voice()

# mytext = 'No E-Bikes Nearby'
# while True:
#     voice()
#     time.sleep(300)
# myobj = gTTS(text=mytext, slow=False)
# myobj.save("owo.mp3")
# #os.system("owo.mp3")
# time.sleep(2.5)
# myobjs = gTTS(text=ortext, slow=False)
# myobjs.save("uwu.mp3")
# #os.system("uwu.mp3")
