import requests
import datetime as dt

date = dt.datetime.now()
d_ate = date.date()
new_date = d_ate.strftime("%d/%m/%Y")
new_time = date.time().strftime("%H:%M:%S")

APP_ID = ""
APP_KEY =""
SHEETY_ENDPOINT = ""


WEIGHT = 47
HEIGHT = 171
AGE = 20

NUTRITIONIX_ENDPOINT =""

parameters = {
    "query":input("Tell me the exercises that you did:"),
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}
headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}

sheety_header ={
    "Authorization": "Bearer "
}
response = requests.post(url=NUTRITIONIX_ENDPOINT,json=parameters,headers=headers)
data = response.json()
exercise = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
print(exercise)
print(duration)
print(calories)

sheety_params = {
    "workout":{
        "date":new_date,
        "time":new_time,
        "exercise":exercise.title(),
        "duration":duration,
        "calories":calories
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT,json=sheety_params,headers=sheety_header)
print(sheety_response.text)


