import requests
from datetime import *
import smtplib


MY_LAT = 37.353627
MY_LONG = 126.747786

def is_iss_overhead():
  

response = requests.get(url="https://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data['iss_position']["latitude"])
iss_longitude = float(data['iss_position']["longitude"])

if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
  return True
  
def is_night():
  parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  time_now = datetime.now().hour
  
  if time_now >= sunset or time_now <= sunrise:
    return True
  
  
if is_iss_overhead