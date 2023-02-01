# with open("./pd/weather_data.csv", encoding='cp949') as data_file:
#   print(data_file.read())

# import csv
# with open("./pd/weather_data.csv", encoding='cp949') as data_file:
#   data = csv.reader(data_file)
#   for i in zip(data):
#     print(i)

import pandas as pd

data = pd.read_csv('./pd/weather_data.csv')
print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].tolist()
# print(temp_list)

# print(data.condition)

