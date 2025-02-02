#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import requests

cities =['Paris', 'Frankfurt', 'Tokyo', 'Hong Kong', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Dublin']

sheety_files = DataManager(cities)
# excel_dict = sheety_files.get_sheety_details()
# print(excel_dict)

# sheety_files.get_iatacode()
# # print(iata_code)
iata_code_list = []
endpoint = f"https://test.api.amadeus.com/v1/reference-data/locations"
iata_header = {
        "Authorization":f"Bearer ipFrJbQCxYKDa51DT5LDamZwEEUO"
}

parameters = {
    "subType":"CITY",
    "keyword":cities[0]
}
iata_code = requests.get(url=endpoint,headers=iata_header,params=parameters)
# iata_code_list.append(iata_code.json()["data"])
print(iata_code.json()["data"])



