import requests
import json
userdata = {"device": {"mobileType": "ios", "uid": ":“123E4567-E89B-12D3-A456-426655440000"}, "grantType": "device"}
response = requests.post("https://web.spin.pm/api/v1/auth_tokens", json=userdata)

# print(response)
print json.dumps(response, indent=4)
