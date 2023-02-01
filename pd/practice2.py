import pandas as pd

path = './pd/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pd.read_csv(path)

grey_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict ={
  "Fur Color":["Gray", "Cinnamon", "Black"],
  "count": [grey_squirrels_count, Cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
