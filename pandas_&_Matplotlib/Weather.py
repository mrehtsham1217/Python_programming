# with open("227 - weather-data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)
"""
import csv
with open("227 - weather-data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

    # print(row)
    """

import pandas as pd
# file = pd.read_csv("227 - weather-data.csv")
# # print(file['temp'])

# data_dict = file.to_dict()
# print(data_dict)
"""data = pd.read_csv("227 - weather-data.csv")
monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_ftemp = 9/5*(monday_temp) + 32
print(monday_ftemp)"""
"""
data_dict = {
    "marks": [20, 30, 40, 50],
    "student": ['A', 'B', 'C', 'D']
}
dataframe = pd.DataFrame(data_dict)
print(dataframe)
"""

# --------2nd Example----------
data = pd.read_csv("229 - 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrles = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrles = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrles = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrles)
print(black_squirrles)
print(red_squirrles)


data_dict = {
    'colors': ['Gray', 'Cinamon', 'Black'],
    'count_data': [gray_squirrles, red_squirrles, black_squirrles]
}
data = pd.DataFrame(data_dict)
print(data)
