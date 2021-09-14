import requests
import base64
import json

## grant type: Resource Owner Password Credentials
## request your sandbox credentials via the contact form in the "Getting Started" section
client_id = "XXXXXXX"   # replace with actual client id
client_secret = "YYYYYYYYYYYYYY" # replace with actual client secret
grant_type = "password"
username = "xxxxxx@xxxxxxx.xxx"  # replace with actual username
password = "zzzzzzzz"   # replace with actual password

auth_token = base64.urlsafe_b64encode(
    "{id}:{secret}".format(id=client_id, secret=client_secret).encode(
        "utf-8"
    )
)

auth_header = "Basic {auth_token}".format(
        auth_token=auth_token.decode("utf-8")
    )

url = "https://sandbox.elationemr.com/api/2.0/oauth2/token/"
response = requests.post(url,
                     data={"grant_type": "password",
                           "username": username,
                           "password": password},
                     headers={'Authorization': auth_header})

print(response.status_code)
response_data = json.loads(response.content)
print(json.dumps(response_data, indent=2))

access_token = response_data["access_token"]