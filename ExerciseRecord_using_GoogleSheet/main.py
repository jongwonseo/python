from config import *
import requests

exercise_text = input("Tell me which exercises you did: ")

parameters = {
  "query":exercise_text,
  "gender":GENDER,
  "weight_kg":WEIGHT_KG,
  "height_cm":HEIGHT_CM,
  "age":AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)