import requests
from config import *

user_params = {
  "token":TOKEN,
  "username":USERNAME,
  "agreeTermsOfService":"yes",
  "notMinor":"yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)