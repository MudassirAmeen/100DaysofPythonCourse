# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)


# All of the above work can also be done by Pandas

# import pandas
# data = pandas.read_csv("weather-data.csv")

# There are many many methods and parameters of Pandas.
# Convert to list 
# temperatures = data["temp"].to_list()

# Get avergae temperature

# Method 1
# sum = sum(temperatures)
# length = len(temperatures)
# avg_temp = sum / length

# Method 2
# avg_temp = data["temp"].mean()
# print(avg_temp)

# Get maximum value 

# Method 1
# for temp in temperatures:
#     max = 0
#     if temp > max:
#         max = temp

# Method 2
# max = data["temp"].max()
# print(max)


# Get the row
# row = data[data.temp == data["temp"].max()]

# F = row.temp * 9/5 + 32

# print(row, F)



import pandas
data = pandas.read_csv("squral_park.csv")


# row = data["Primary Fur Color"].to_list()
Gray = data["Primary Fur Color"].value_counts()["Gray"]
Cinnamon = data["Primary Fur Color"].value_counts()["Cinnamon"]
Black = data["Primary Fur Color"].value_counts()["Black"]
dictionary = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[Gray, Cinnamon, Black]
}
ex_dict = pandas.DataFrame(dictionary)
ex_dict.to_csv("new_data.csv")
