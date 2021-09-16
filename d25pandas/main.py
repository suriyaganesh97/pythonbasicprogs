# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])
# temp_list = data["temp"].to_list()
#
# avg = sum(temp_list)/len(temp_list)
# print(avg)


# high_day = data[data.temp == data["temp"].max()]
# print(high_day.day)

monday_data = data[data.day == "Monday"]
print(monday_data.temp + 274)