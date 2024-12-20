import csv
# with open("weather_data.csv") as File:
#     data = File.readlines()
#
# new_data = []
# for dat in data:
#     new_data.append(dat.strip("\n"))
# print(new_data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temp = row[1]
        temperatures.append(temp)
temperatures.remove("temp")

temperatures_final = []
for temp in temperatures:
    temps = int(temp)
    temperatures_final.append(temps)
print(temperatures_final)
