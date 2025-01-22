import requests
from twilio.rest import Client

API_KEY = ""
MY_LAT = "44.40726"
MY_LONG = "8.9338624"
weather_id = None
account_sid = ''
auth_token = ''

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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      messaging_service_sid='',
      body="It's going to rain take an Umbrella",
      from_="senders_phone_no",
      to='receivers_phone_no'
    )
    print(message.status)

