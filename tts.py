from gtts import gTTS
import os

mytext = 'E-Bike Nearby'

myobj = gTTS(text=mytext, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
