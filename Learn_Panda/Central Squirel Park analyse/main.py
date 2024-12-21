import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241221.csv")
black_fur = 0
gray_fur = 0
red_fur = 0
data_list = data["Primary Fur Color"].to_list()
for datas in data_list:
    if datas == "Black":
        black_fur +=1
    elif datas == "Gray":
        gray_fur += 1
    elif datas == "Cinnamon":
        red_fur += 1
Color_dict = {
    "Fur Color":["Gray" ,"Cinnamon" , "Black"],
    "Count":[gray_fur , red_fur , black_fur]
              }
fur_color_data = pandas.DataFrame(Color_dict)
print(fur_color_data)
fur_color_data.to_csv("fur_color.csv")




