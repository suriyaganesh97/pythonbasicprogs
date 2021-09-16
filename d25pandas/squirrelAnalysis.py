

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

new_data = data["Primary Fur Color"].value_counts().reset_index()
new_data.columns = ['colour', 'count']
print(new_data)
new_data.to_csv("squirrel_color.csv")