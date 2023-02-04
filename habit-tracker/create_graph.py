from config import *
import requests

graph_config = {
  "id":GRAPH_ID,
  "name":"Cycling Graph",
  "unit":"km",
  "type":"float",
  "color":"ajisai"
}


response = requests.post(url=graph_endpoing, json=graph_config, headers=headers)
print(response.text)