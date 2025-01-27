import requests
import datetime as dt

date = dt.datetime.now()
d_ate = date.date()
new_date = d_ate.strftime("%d/%m/%Y")


APP_ID = ""
APP_KEY =""
SHEETY_ENDPOINT = ""


WEIGHT = 
HEIGHT = 
AGE = 

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

response = requests.post(url=NUTRITIONIX_ENDPOINT,json=parameters,headers=headers)
data = response.json()
exercise = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]


sheety_params = {
    "workouts":{
        "Date":new_date,
        "Time":date.time(),
        "Exercise":exercise,
        "Duration":duration,
        "Calories":calories
    }
}


#
sheety_response = requests.post(url=SHEETY_ENDPOINT,json=sheety_params)
print(sheety_response.text)
