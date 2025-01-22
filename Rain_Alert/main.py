import requests

API_KEY = ""
MY_LAT = "20.593683"
MY_LONG = "78.962883"
weather_id = None

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]
for weather in weather_list:
    weather_id = weather["weather"][0]["id"]
    if int(weather_id) < 800:
        break
if weather_id < 800:
    print("bring an umberlla")
