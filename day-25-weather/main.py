# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# import csv
import pandas

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     counter = 0
#     for row in data:
#         if counter != 0:
#             temperatures.append(int(row[1]))
#         counter += 1
#     print(temperatures)

# file = pandas.read_csv("weather_data.csv")
# print(file)
# temp_list = file["temp"].to_list()
# temperature_sum = 0
# for temperature in temp_list:
#     temperature_sum += temperature

# avg_temp = temperature_sum / len(temp_list)
# or the easiest way
# avg_temp2 = sum(temp_list) / len(temp_list)
# or yet
# print(file["temp"].mean())
# print(avg_temp)
# print(avg_temp2)
# max value in the series of values
# print(f"Max temp = {file['temp'].max()}")
# to get the entire row where day == Monday
# print(file[file.day == "Monday"])
# to get the row where temperature hit its highest
# print(file[file.temp == file.temp.max()])

# monday = file[file.day == "Monday"]
# monday_in_fahrenheit = (int(monday.temp) * 9 / 5) + 32
# print(monday_in_fahrenheit)

# create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
data_from_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_grey_count = len(data_from_file[data_from_file.PrimaryFurColor == "Gray"])
color_red_count = len(data_from_file[data_from_file.PrimaryFurColor == "Cinnamon"])
color_black_count = len(data_from_file[data_from_file.PrimaryFurColor == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_grey_count, color_red_count, color_black_count]
}
data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("squirrel_count.csv")
