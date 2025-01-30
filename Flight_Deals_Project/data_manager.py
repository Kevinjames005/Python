import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/8500eebd04cf8978c668a6bedade384d/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = SHEETY_API_ENDPOINT

    def get_sheety_details(self):
        sheety_response = requests.get(url=self.sheety_endpoint)
        sheety_data = sheety_response.json()
        print(sheety_data)
