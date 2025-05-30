# # Weather Dataframes and Series with Pandas

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_fah = monday_temp * 9/5 + 32
# print(monday_temp_fah)

# Create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
