from config import *
import requests
from datetime import datetime

graph_config = {
  'id': GRAPH_ID,
  'name':'Cycling Grap',
  'type':'float',
  'color':'ajisai'
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(datetime.now())
print(today.strftime("%Y%m%d"))

pixel_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": "9.74"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#   "quantity": "100"
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)