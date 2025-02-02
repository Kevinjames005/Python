import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/8500eebd04cf8978c668a6bedade384d/flightDeals/prices"
AMADEUS_URL = "https://test.api.amadeus.com/v1"
prameters_amadeus_header = {
    "Content_Type":"application/x-www-form-urlencoded"
}
data_amadeus = {
    "grant_type": "client_credentials",
    "client_id": "eAE77ZRVR4lKZtpFBZRuQZBhZ4otunVq",  # Replace with your actual client_id
    "client_secret": "5GEeLf6YFULbaOpO"  # Replace with your actual client_secret
}
AMADEUS_ACCESS_TOKEN = "ipFrJbQCxYKDa51DT5LDamZwEEUO"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,cities):
        self.sheety_endpoint = SHEETY_API_ENDPOINT
        self.cities_list = cities

    def get_sheety_details(self):
        sheety_response = requests.get(url=self.sheety_endpoint)
        sheety_data = sheety_response.json()
        return sheety_data

    def get_token(self):
        amadeus_token = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=prameters_amadeus_header,data=data_amadeus)
        return amadeus_token

    def get_iatacode(self):
        iata_code_list = []
        endpoint = f"{AMADEUS_URL}/reference-data/locations"
        iata_header = {
            "Authorization":f"Bearer {AMADEUS_ACCESS_TOKEN}"
        }
        for i in range(len(self.cities_list)-1):
            parameters = {
                "subType":"CITY",
                "keyword":self.cities_list[i]
            }
            iata_code = requests.get(url=endpoint,headers=iata_header,params=parameters)
            iata_code_list.append(iata_code.json()["data"][0]["iataCode"])
            print(iata_code.json()["data"][0]["iataCode"])


